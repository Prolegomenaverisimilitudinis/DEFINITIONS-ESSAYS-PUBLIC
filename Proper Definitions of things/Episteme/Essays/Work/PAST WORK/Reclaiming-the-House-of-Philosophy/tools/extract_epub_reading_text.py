"""Read local EPUBs into traceable, spine-ordered UTF-8 reading copies.

This is a document conversion utility, not an execution of EPUB content.
Original files are read-only. Each section records its archive member.
"""
import argparse
import hashlib
import json
import posixpath
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote
import xml.etree.ElementTree as ET
import zipfile

class Text(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []
        self.skip = 0

    def handle_starttag(self, tag, attrs):
        tag = tag.lower()
        if tag in ("script", "style", "svg"):
            self.skip += 1
        if self.skip:
            return
        if tag in ("p", "div", "section", "article", "blockquote", "li", "br",
                   "h1", "h2", "h3", "h4", "h5", "h6", "tr"):
            self.parts.append("\n")
        if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self.parts.append("### ")
        if tag == "li":
            self.parts.append("- ")

    def handle_endtag(self, tag):
        tag = tag.lower()
        if tag in ("script", "style", "svg") and self.skip:
            self.skip -= 1
            return
        if not self.skip and tag in ("p", "div", "section", "article", "blockquote",
                                    "li", "h1", "h2", "h3", "h4", "h5", "h6", "tr"):
            self.parts.append("\n")

    def handle_data(self, data):
        if not self.skip:
            self.parts.append(data)

    def result(self):
        return "\n\n".join(
            line for raw in "".join(self.parts).splitlines()
            if (line := " ".join(raw.split()))
        )

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--epub", required=True)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()
    src = Path(args.epub)
    dest = Path(args.output)
    with zipfile.ZipFile(src) as archive:
        container = ET.fromstring(archive.read("META-INF/container.xml"))
        rootfile = next(x.attrib["full-path"] for x in container.iter()
                        if x.tag.endswith("rootfile"))
        package = ET.fromstring(archive.read(rootfile))
        base = posixpath.dirname(rootfile)
        items = {}
        for x in package.iter():
            if x.tag.endswith("}item"):
                items[x.attrib["id"]] = x.attrib
        ordered = []
        for x in package.iter():
            if x.tag.endswith("}itemref"):
                item = items[x.attrib["idref"]]
                member = posixpath.normpath(posixpath.join(base, unquote(item["href"])))
                if member not in ordered:
                    ordered.append(member)
        # Retain notes/front matter not included in the linear reading spine.
        extras = []
        for item in items.values():
            if item.get("media-type") in ("application/xhtml+xml", "text/html"):
                member = posixpath.normpath(posixpath.join(base, unquote(item["href"])))
                if member not in ordered:
                    extras.append(member)
        meta = {key: [x.text for x in package.iter()
                      if x.tag == "{http://purl.org/dc/elements/1.1/}"+key]
                for key in ("title", "creator", "publisher", "date")}
        result = ["# Local EPUB reading copy",
                  "Source: "+str(src),
                  "SHA256: "+hashlib.sha256(src.read_bytes()).hexdigest(),
                  "Metadata: "+json.dumps(meta, ensure_ascii=False),
                  "Conversion: spine order; paragraphs normalized; source-member boundaries retained. "
                  "Front matter, editorial commentary and author text must be distinguished.",
                  "## Archive reading order",
                  "\n".join(f"- {i+1}. {m}" for i, m in enumerate(ordered))]
        for i, member in enumerate(ordered + extras):
            parsed = Text()
            parsed.feed(archive.read(member).decode("utf-8-sig"))
            section = "Spine" if i < len(ordered) else "Supplement"
            result += [f"## {section} member: {member}", parsed.result()]
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text("\n\n".join(result)+"\n", encoding="utf-8")
    print(json.dumps({"output":str(dest), "spine_members":len(ordered),
                      "supplement_members":len(extras), "metadata":meta},
                     ensure_ascii=True))

if __name__ == "__main__":
    main()
