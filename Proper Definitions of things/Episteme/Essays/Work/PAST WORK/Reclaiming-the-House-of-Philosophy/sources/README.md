# Local reading copies — provenance and limits

These files support question-directed reading of the two EPUBs supplied by the user. They are research context, not replacement authorities for the working definition.

## Original editions

| Reading copy | Supplied original | SHA-256 of original |
| --- | --- | --- |
| [Nietzsche — Beyond Good and Evil](Nietzsche-Beyond-Good-and-Evil-reading.md) | `C:/Users/Graphics/Desktop/General Downloads/Beyond Good and Evil Penguin Classics (Friedrich Nietzsche etc.) (z-library.sk, 1lib.sk, z-lib.sk).epub` | `9accbbecf11c661c34ad1461518a56993513796d5e73384af7421b8943fa9d53` |
| [Popper — The Myth of the Framework](Popper-Myth-of-the-Framework-reading.md) | `C:/Users/Graphics/Desktop/General Downloads/The Myth of the Framework (Karl Raimund Popper) (z-library.sk, 1lib.sk, z-lib.sk).epub` | `75328523613a62a7a331b3aba42540d7096ad0ba92d242678bcf16d85fa1f04a` |

The Nietzsche edition includes R. J. Hollingdale's translation and a Michael Tanner introduction. Editorial introduction and authorial text must not be conflated. The Popper volume includes an editor's afterword distinct from Popper's chapters and introduction.

## Extraction

[The local extraction script](../tools/extract_epub_reading_text.py) follows the EPUB package spine, converts its textual members to searchable Markdown, and records source-member boundaries. It does not edit the originals. The two copies contain 21 and 22 spine members respectively. These are text-based reading copies, not page-faithful facsimiles: use chapter/section/aphorism identifiers for durable attribution, with reading-copy line numbers only as navigation aids.

The original hashes were checked again during the integration audit and matched the extraction provenance. Citations in the main definition distinguish arguments adopted, arguments used only as diagnostic prompts, and points on which our account departs from the source.

No internet source was consulted in this cycle. No claim is made that every chapter of either book was read for this task: the investigations record the selected passages relevant to the author's questions.
