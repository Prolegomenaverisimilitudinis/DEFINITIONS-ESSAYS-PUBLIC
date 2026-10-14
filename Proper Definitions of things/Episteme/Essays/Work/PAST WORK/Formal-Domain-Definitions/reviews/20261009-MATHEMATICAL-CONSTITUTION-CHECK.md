# Mathematical constitution check of the actual candidate

9 October 2026. Reviewed the actual candidate `drafts/20261009-SEMANTIC-CONSTITUTION-CANDIDATE.md`, specifically §§8.5–8.6, 14, 15 and 19. No candidate or target edits. This review checks the bounded mathematical arguments and the scope of their correspondence claims; it does not certify the surrounding empirical source interpretations or an implemented realization environment.

## Outcome

No consequential mathematical error or correspondence overclaim found in the reviewed sections. The numerical wrong-criterion counterinterpretation is valid, the generated-versus-imported distinction is explicit, and the limitations attached to the preservation and gluing results survive the candidate's compression of the longer investigation.

## Checks actually performed

### Representation factorization and question equivalence — §8.5

Checked both directions of the stated result. If `q = q̄ ∘ p`, equality of retained representations forces equality of answers. If answers agree whenever retained representations agree, assigning `q̄(p(w)) = q(w)` gives a well-defined function on the image. Uniqueness on the image also follows, although the candidate does not need it. The image domain matters: existence of an extension to all of `X` is unnecessary and can require additional assumptions in degenerate cases. The candidate correctly states the domain as `p(W)`.

Strictly, composition uses the corestriction `p:W→p(W)` of the originally given map `p:W→X`. That customary implicit corestriction is harmless here; an explicit phrase could make the typing entirely literal, but it is not a consequential error.

The relation defined by equality of all answers in the intended question family is an equivalence relation. Representation adequacy requires that each fiber of `p` lie within one such equivalence class. Enlarging the question family refines that equivalence and can invalidate prior adequacy. Nothing in the candidate claims that the factorization theorem discovers the relevant questions, proves an algorithm exists, or decides empirical truth. Qualified or alternative-valued answers can be represented in an appropriate codomain as stated; a genuinely partial question would additionally need a totalized result representation or a restricted case domain, consistent with the stated premise that `q` is a function.

### Common-context pullback — §8.6

Checked the defined set and its universal property. Given a set `Z` with maps `a:Z→A`, `b:Z→B` satisfying `s_A∘a=s_B∘b`, the unique map to the stated set is `z↦(a(z),b(z))`. Its projections are the original maps. The construction enforces exactly the equality represented in `K`; it cannot recover omitted revision distinctions or validate judgments. The candidate explicitly makes both qualifications.

### Sorted equations and generated composites — §§14.2–14.3

Every displayed equation has the same sort on both sides. Variables are quantified at the right sorts, and the wording “where those variables occur” avoids inadvertently making an unrelated possibly empty sort part of an equation's quantification context. There are eight distinct equations: two assessment-subject laws, one package-request law, two package-part laws, two arbitrary-package common-subject laws, and one decision-grounds law.

The generated decision formulas are type-correct. Substitution of the grounds law followed by the request law yields the request invariant; substitution of grounds, package-part and assessment-subject yields the constituent invariant. Both hold for each finite revision depth. No equation commutes edits, asserts favorable results, or equates distinct revision requests. The signature admits terms of unbounded finite depth. The numerical successor-revision model supplies a concrete interpretation in which revision distinctions remain; the candidate does not infer an infinite successful execution from finite formation.

### Actual category, products and substitution — §14.4

The stated construction defines the standard sorted term category: finite sort contexts as objects, typed term tuples modulo the generated congruence as arrows, variable tuples as identities, substitution as composition. Associativity follows from substitution. The congruence makes composition independent of representatives. Concatenated contexts are products: projecting a tuple to each output context determines the unique combined tuple. The empty context is terminal through the empty tuple. The candidate omits the latter routine detail but its category description does not contradict it.

Carriers and lawful primitive functions determine evaluation of all terms and hence a product-preserving interpretation in sets. The functorial composition equation is valid. The text's restriction to pure immutable information prevents illicit inference that Cartesian copying is a law for physical resources or observation events.

### Wrong-criterion counterinterpretation and imported packages — §14.5

The counterinterpretation can be made explicit with `A_i=Q×{pass,fail}`, subject projections, `P={(q,a_1,a_2):subject_1(a_1)=q=subject_2(a_2)}`, and `D=P×V`. In the intended model, assessors compare the respective quantities; in the defective model, the first assessor duplicates the second comparison. In both models, `package(q)` is formed from the chosen pair of assessors, package accessors are projections, and `decide(p)` retains `p` with the verdict determined by the two judgments. Every displayed equation holds in both models, but the revised request `(mass=12,space=8,limits=10)` receives different verdicts.

Reading “keep every interface ... unchanged” must mean unchanged types, access/subject structure and grounds, not unchanged output values of the package constructor while altering its assessor. The next sentences already specify that generated packages use the assessors, so the countermodel is coherent. For maximal literal clarity, “keep the types, projections and subject binding unchanged, forming packages with the newly interpreted assessor” would remove this minor possible misreading. No substantive correction is needed.

The candidate explicitly separates generated packages from arbitrary imports with a common subject. Therefore it does not assert that every package inhabitant carries accurate or authentic assessments. This is essential: package coherence alone imposes no judgment-validity relation on arbitrary carrier values.

### Preservation through composites — §14.6

The displayed primitive-preservation equation is precisely the sorted homomorphism condition. Structural induction establishes its extension to every generated term, including zero-ary primitives where present. Preservation of all primitive interpretations is a premise, not a result inferred from sharing labels or types. The limitation concerning noninjective maps is necessary and present: homomorphisms can collapse revisions or verdicts. The question-sensitive adequacy reference appropriately identifies an additional requirement when those distinctions affect use.

### Feature assignments, gluing and global constraints — §14.7

For a set of feature indices, products over subsets with coordinate restrictions define a presheaf on the subsets. For covers by union, matching local assignments glue uniquely by coordinate. Empty subset/empty cover gives the unique empty tuple, so the edge case is also correct. Equivalently this is an elementary sheaf on the discrete topology of the feature set; the candidate's “actual gluing property, of the kind formalized by sheaf theory” is justified without claiming that every domain structure is a sheaf.

The proof establishes gluing for unrestricted product assignments. It does not establish gluing for an arbitrary subfamily defined by a global constraint. The parity witness is appropriate: all binary pair projections can be identical while the permitted triples differ. The candidate explicitly asks for the local/global constraint account rather than inferring admissibility from raw gluing.

### Passage to operability and summary — §§15 and 19

The positive operability claim is conditional on supported defining forms, constituted primitive meanings, available powers and faithful evaluation. It does not claim that abstract functorial evaluation proves a physical implementation, external observation, empirical assessment, or liveness guarantee. The state correspondence notation supplies a forward simulation obligation and explicitly separates converse capability obligations. It is labelled an obligation, not a universal theorem.

Section 19 retains the relevant scope limitations: pure total immutable algebra; separately warranted primitive meanings and external interpretation; separately established coverings and global obligations; no universal realizing environment. Its evidence-level distinctions agree with the actual mathematical achievements in the reviewed sections.

## Review boundary

The result is a check of bounded correctness and claim calibration. It does not certify that the whole goal is complete merely because these mathematical passages are sound. In particular, the semantic reconstruction of psychological, narrative and instructional sources remains the primary investigator's separate responsibility.
