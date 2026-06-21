#!/usr/bin/env python3
"""Write 300 high-quality Biology/Biochemistry questions to data/questions/bb/hq-bb.json"""
import json, os, random

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

Q = [
# ── AMINO ACIDS (35) ──────────────────────────────────────────────────────
{"text":"Which amino acid is the only one that lacks a chiral alpha carbon?",
 "options":["Glycine","Alanine","Serine","Proline"],"correct":0,
 "explanation":"Glycine has two H atoms on its alpha carbon (R = H), giving it two identical substituents and no chirality. Every other standard amino acid has four distinct groups at the alpha carbon and exists as the L-enantiomer in proteins.",
 "tags":["amino acids","chirality"],"difficulty":"easy"},

{"text":"At physiological pH (~7.4), which amino acid side chain is best positioned to donate or accept a proton and function as an acid-base catalyst?",
 "options":["Histidine","Lysine","Aspartate","Glutamine"],"correct":0,
 "explanation":"Histidine's imidazole side chain has pKa ≈ 6.0, closest to physiological pH of all standard amino acids. This lets it toggle between protonated and deprotonated forms under physiological conditions. Lysine (pKa ≈ 10.5) stays protonated; aspartate (pKa ≈ 3.9) stays deprotonated; glutamine has no ionizable side chain.",
 "tags":["amino acids","enzyme catalysis"],"difficulty":"medium"},

{"text":"Which amino acid side chain contains a thiol group (–SH) that can form disulfide bonds?",
 "options":["Cysteine","Serine","Threonine","Methionine"],"correct":0,
 "explanation":"Cysteine's thiol (–SH) group is oxidized to form disulfide bonds (–S–S–) with another cysteine, stabilizing tertiary/quaternary protein structure. Serine and threonine have –OH groups. Methionine contains a thioether (–S–CH3) that cannot form disulfide bonds.",
 "tags":["amino acids","protein structure"],"difficulty":"easy"},

{"text":"Why does proline disrupt alpha-helices?",
 "options":["Its side chain bonds to the backbone nitrogen, eliminating the N–H hydrogen bond donor","Its side chain is too large to fit in the helix","It carries a negative charge at physiological pH","It forms an extra covalent bond with adjacent residues"],
 "correct":0,
 "explanation":"Proline's nitrogen is locked in a pyrrolidine ring with its side chain, removing the backbone N–H needed for hydrogen bonding in a helix. This creates a rigid kink, making proline a 'helix breaker.' It can appear at the end of helices or in beta-turns.",
 "tags":["amino acids","protein structure"],"difficulty":"medium"},

{"text":"Proteins absorb strongly at 280 nm primarily because of which amino acids?",
 "options":["Tryptophan and tyrosine","Phenylalanine and alanine","Methionine and cysteine","Glycine and proline"],"correct":0,
 "explanation":"Tryptophan (indole ring) and tyrosine (phenol ring) absorb at 280 nm due to aromatic pi electrons. Tryptophan has the larger extinction coefficient. This is used to estimate protein concentration spectrophotometrically. Phenylalanine absorbs weakly at ~257 nm.",
 "tags":["amino acids","spectroscopy"],"difficulty":"medium"},

{"text":"Which amino acid is the direct precursor for catecholamine biosynthesis (dopamine, norepinephrine, epinephrine)?",
 "options":["Tyrosine","Tryptophan","Phenylalanine","Histidine"],"correct":0,
 "explanation":"Tyrosine → L-DOPA (tyrosine hydroxylase) → Dopamine → Norepinephrine → Epinephrine. Phenylalanine can be converted to tyrosine by phenylalanine hydroxylase, but tyrosine is the direct precursor. Tryptophan makes serotonin. Histidine makes histamine.",
 "tags":["amino acids","neurotransmitters"],"difficulty":"medium"},

{"text":"In eukaryotes, which amino acid is delivered by the initiator tRNA at the start codon AUG?",
 "options":["Methionine","Valine","Alanine","Leucine"],"correct":0,
 "explanation":"AUG codes for methionine and serves as the start codon in eukaryotes (the initiator tRNA is met-tRNAi). In prokaryotes, the initiator carries N-formyl-methionine (fMet). The initiating methionine is often cleaved post-translationally.",
 "tags":["amino acids","translation"],"difficulty":"easy"},

{"text":"A patient with phenylketonuria (PKU) lacks phenylalanine hydroxylase. Which metabolite accumulates and causes neurological damage?",
 "options":["Phenylalanine and its toxic byproducts (phenylpyruvate, phenyllactate)","Tyrosine","Tryptophan metabolites","Excess dopamine"],"correct":0,
 "explanation":"Without phenylalanine hydroxylase, phenylalanine cannot be converted to tyrosine and accumulates. It is shunted to phenylpyruvate, phenyllactate, and phenylacetate. These metabolites inhibit brain aromatic amino acid transport, impair myelination, and cause intellectual disability if untreated.",
 "tags":["amino acids","metabolic disorders"],"difficulty":"medium"},

{"text":"Glutamic acid (pI ≈ 3.2) carries what net charge at pH 7.4?",
 "options":["–1","0","+1","+2"],"correct":0,
 "explanation":"At pH 7.4, well above pI 3.2: the alpha-COOH (pKa ~2.1) and side-chain COOH (pKa ~4.1) are both deprotonated (–1 each), while the alpha-NH3+ (pKa ~9.5) is protonated (+1). Net = +1 – 1 – 1 = –1.",
 "tags":["amino acids","acid-base"],"difficulty":"medium"},

{"text":"Which of the following is a complete list of the nine essential amino acids?",
 "options":["His, Ile, Leu, Lys, Met, Phe, Thr, Trp, Val","Ala, Gly, Pro, Ser, Thr, Asn, Gln, Cys, Tyr","Arg, His, Lys, Asp, Glu, Asn, Gln, Ser, Thr","Phe, Tyr, Trp, Met, Cys, Gly, Pro, Val, Ala"],"correct":0,
 "explanation":"The nine essential amino acids (cannot be synthesized by humans) are Histidine, Isoleucine, Leucine, Lysine, Methionine, Phenylalanine, Threonine, Tryptophan, Valine. Mnemonic: PVT TIM HaLL. They must come from the diet.",
 "tags":["amino acids","nutrition"],"difficulty":"easy"},

{"text":"Glycine appears in regions of the Ramachandran plot that are forbidden for other amino acids because:",
 "options":["It lacks a side chain, minimizing steric clash at extreme phi/psi angles","It has the most hydrophobic side chain","It forms the most stable hydrogen bonds","Its pKa is farthest from physiological pH"],"correct":0,
 "explanation":"Without a side chain, glycine has minimal steric restriction and can adopt phi/psi combinations (including left-handed alpha-helix conformations) inaccessible to other amino acids. This flexibility is why glycine is common at tight turns and in collagen (Gly-X-Y). Proline, conversely, is the most restricted.",
 "tags":["amino acids","protein structure"],"difficulty":"hard"},

{"text":"Collagen requires hydroxyproline for stability. Which vitamin is essential for prolyl hydroxylase, and what disease results from its deficiency?",
 "options":["Vitamin C (ascorbic acid); scurvy","Vitamin D; rickets","Vitamin B12; pernicious anemia","Vitamin K; coagulopathy"],"correct":0,
 "explanation":"Prolyl hydroxylase requires ascorbate (vitamin C) as a cofactor to hydroxylate proline residues in collagen. Hydroxyproline forms extra hydrogen bonds in the collagen triple helix. Without vitamin C, hydroxylation fails, collagen is unstable, and patients develop scurvy: bleeding gums, poor wound healing, perifollicular hemorrhages.",
 "tags":["amino acids","collagen","vitamins"],"difficulty":"medium"},

{"text":"GABA (gamma-aminobutyric acid) is synthesized from which amino acid by glutamate decarboxylase?",
 "options":["Glutamate","Aspartate","Tryptophan","Tyrosine"],"correct":0,
 "explanation":"Glutamate decarboxylase (requires PLP/vitamin B6) converts glutamate → GABA by removing the carboxyl group. GABA is the principal inhibitory neurotransmitter in the CNS. Disruption of GABA signaling is linked to anxiety disorders, epilepsy, and the mechanism of benzodiazepines and barbiturates.",
 "tags":["amino acids","neurotransmitters"],"difficulty":"medium"},

{"text":"The branched-chain amino acids (BCAAs) are:",
 "options":["Leucine, isoleucine, valine","Lysine, arginine, histidine","Phenylalanine, tyrosine, tryptophan","Serine, threonine, cysteine"],"correct":0,
 "explanation":"BCAAs (Leu, Ile, Val) have branched aliphatic side chains and are metabolized primarily in skeletal muscle (not liver), making them important for muscle protein synthesis and energy during exercise. All three are essential amino acids.",
 "tags":["amino acids","metabolism"],"difficulty":"easy"},

{"text":"Which amino acid pair contains sulfur in their side chains?",
 "options":["Cysteine and methionine","Serine and threonine","Aspartate and glutamate","Asparagine and glutamine"],"correct":0,
 "explanation":"Cysteine (thiol –SH) and methionine (thioether –S–CH3) are the two standard sulfur-containing amino acids. Cysteine's sulfur forms disulfide bonds; methionine's sulfur is used in methyl group transfer reactions (as SAM, S-adenosylmethionine).",
 "tags":["amino acids"],"difficulty":"easy"},

{"text":"Serine and threonine are common targets for phosphorylation. Which type of kinase performs this modification?",
 "options":["Serine/threonine kinase","Tyrosine kinase","Lipid kinase","RNA kinase"],"correct":0,
 "explanation":"Serine/threonine kinases (e.g., PKA, PKC, CDKs) phosphorylate the hydroxyl groups of serine and threonine. Tyrosine kinases (e.g., receptor tyrosine kinases, Src) phosphorylate tyrosine. Phosphorylation on any of these three residues is a key regulatory mechanism in signal transduction.",
 "tags":["amino acids","signal transduction","phosphorylation"],"difficulty":"easy"},

{"text":"An amino acid has pI = 9.7. This is most characteristic of which amino acid?",
 "options":["Lysine","Glutamate","Glycine","Tryptophan"],"correct":0,
 "explanation":"Lysine (pI ≈ 9.7) has a positively charged epsilon-amino group (pKa ≈ 10.5) in addition to the alpha-amino group. Basic amino acids (Arg, Lys, His) have pI > 7.4 because they carry extra positive charges. Glutamate (pI ≈ 3.2) is acidic; glycine (pI ≈ 6.0) is near neutral.",
 "tags":["amino acids","acid-base"],"difficulty":"medium"},

{"text":"N-linked glycosylation is added to which amino acid residue in the ER?",
 "options":["Asparagine","Serine","Threonine","Lysine"],"correct":0,
 "explanation":"N-linked glycosylation occurs on asparagine residues in the consensus sequence Asn-X-Ser/Thr (where X ≠ Pro) in the ER, as oligosaccharyltransferase adds a pre-assembled oligosaccharide. O-linked glycosylation occurs on serine and threonine in the Golgi. N-linked glycosylation is important for protein folding, stability, and cell-surface recognition.",
 "tags":["amino acids","glycosylation","post-translational modification"],"difficulty":"medium"},

{"text":"Tryptophan is the precursor for which neurotransmitter and hormone?",
 "options":["Serotonin and melatonin","Dopamine and norepinephrine","GABA and glycine","Acetylcholine and histamine"],"correct":0,
 "explanation":"Tryptophan → 5-hydroxytryptophan (tryptophan hydroxylase) → Serotonin (5-HT) by aromatic amino acid decarboxylase. Serotonin → N-acetylserotonin → Melatonin (in pineal gland). Melatonin regulates circadian rhythms. Serotonin deficiency is associated with depression; SSRI antidepressants increase synaptic serotonin.",
 "tags":["amino acids","neurotransmitters"],"difficulty":"medium"},

{"text":"Which amino acids are most commonly found at the active sites of serine proteases (e.g., chymotrypsin, trypsin)?",
 "options":["Serine, histidine, and aspartate (the catalytic triad)","Lysine, arginine, and glutamate","Cysteine, histidine, and asparagine","Glycine, alanine, and valine"],"correct":0,
 "explanation":"Serine proteases use a catalytic triad: Ser (nucleophile), His (general base/acid), and Asp (orients and stabilizes His). Asp hydrogen bonds to His, lowering its pKa so it can abstract a proton from Ser, making Ser a better nucleophile. This triad is a classic example of convergent evolution, found in unrelated serine proteases.",
 "tags":["amino acids","enzyme catalysis","proteases"],"difficulty":"hard"},

{"text":"The epsilon-amino group of lysine participates in which important post-translational reaction in collagen?",
 "options":["Cross-linking by lysyl oxidase to form aldehyde-derived crosslinks","Phosphorylation by receptor tyrosine kinases","Glycosylation to form N-linked oligosaccharides","Hydroxylation by prolyl hydroxylase"],"correct":0,
 "explanation":"Lysyl oxidase (requires copper) oxidatively deaminates lysine/hydroxylysine epsilon-amino groups to aldehydes, which then condense with adjacent lysine residues to form covalent crosslinks. These crosslinks are essential for the tensile strength of collagen fibers. Defects occur in Menkes disease (copper deficiency) and lathyrism.",
 "tags":["amino acids","collagen","post-translational modification"],"difficulty":"hard"},

{"text":"Which amino acid is a precursor for heme biosynthesis?",
 "options":["Glycine","Histidine","Methionine","Lysine"],"correct":0,
 "explanation":"Heme biosynthesis begins with glycine + succinyl-CoA (from TCA cycle) → delta-aminolevulinic acid (ALA), catalyzed by ALA synthase (rate-limiting step, requires PLP). Eight glycine residues contribute to heme. Glycine's simplicity (no side chain, small) makes it ubiquitous in metabolic biosynthesis pathways.",
 "tags":["amino acids","heme synthesis","metabolism"],"difficulty":"hard"},

{"text":"The pKa of an amino acid side chain can shift in a protein environment. The active site serine of a serine protease has a lower pKa than free serine because:",
 "options":["The neighboring histidine abstracts its proton, effectively lowering its pKa and increasing its nucleophilicity","The protein core is more acidic than solution","The serine forms an extra disulfide bond","Nearby ionic residues completely neutralize the serine"],"correct":0,
 "explanation":"In the catalytic triad, histidine acts as a general base, abstracting the proton from serine's hydroxyl. This lowers the effective pKa of serine (from ~13 to near 7), making it a much stronger nucleophile. The aspartate stabilizes the protonated histidine, completing the charge relay system.",
 "tags":["amino acids","enzyme catalysis"],"difficulty":"hard"},

{"text":"Which statement about D-amino acids in biology is correct?",
 "options":["D-amino acids are found in bacterial peptidoglycan cell walls but not in typical mammalian proteins","D-amino acids are the normal configuration in all proteins","D-amino acids are found in all collagen molecules","D-amino acids are toxic to all organisms"],"correct":0,
 "explanation":"Most proteins contain exclusively L-amino acids. However, D-amino acids appear in bacterial peptidoglycan (D-Ala, D-Glu), conferring resistance to most proteases. Some antibiotics (vancomycin, penicillin) exploit this by targeting D-amino acid-containing structures. Small amounts of D-amino acids also exist in the mammalian brain (D-serine as a co-agonist of NMDA receptors).",
 "tags":["amino acids","microbiology"],"difficulty":"medium"},

{"text":"Arginine is the most basic standard amino acid. Which functional group in its side chain accounts for this?",
 "options":["Guanidinium group (pKa ~12.5)","Imidazole ring (pKa ~6)","Epsilon-amino group (pKa ~10.5)","Secondary amine in a ring"],"correct":0,
 "explanation":"Arginine's side chain contains a guanidinium group (–NH–C(=NH)–NH2), which is positively charged at essentially all physiological and experimental pH values (pKa ~12.5). This makes arginine the most basic amino acid. It participates in the urea cycle and forms salt bridges/electrostatic interactions with negatively charged residues and DNA phosphates.",
 "tags":["amino acids","acid-base"],"difficulty":"medium"},

{"text":"Which amino acid is least likely to be found in a transmembrane helix of an integral membrane protein?",
 "options":["Lysine","Leucine","Valine","Isoleucine"],"correct":0,
 "explanation":"Transmembrane helices span the hydrophobic lipid bilayer and require predominantly hydrophobic residues (Leu, Val, Ile, Ala, Phe, Met). Lysine is positively charged and highly hydrophilic; burying it in the membrane bilayer is thermodynamically unfavorable. Charged residues found in transmembrane segments are usually involved in ion channel gating or proton transfer.",
 "tags":["amino acids","membrane proteins"],"difficulty":"medium"},

{"text":"Histidine, lysine, and arginine are basic amino acids. At physiological pH (7.4), which of these carries a net charge of approximately zero (uncharged side chain)?",
 "options":["Histidine (pKa ~6.0, mostly deprotonated at pH 7.4)","Lysine (pKa ~10.5)","Arginine (pKa ~12.5)","None; all three are fully protonated at pH 7.4"],"correct":0,
 "explanation":"At pH 7.4, histidine's imidazole (pKa ~6.0) is mostly deprotonated (neutral), since pH > pKa. By Henderson-Hasselbalch, at pH 7.4: ratio = 10^(7.4–6.0) = 25:1 unprotonated:protonated. Lysine and arginine have pKa values far above 7.4 and remain fully protonated (positively charged) at physiological pH.",
 "tags":["amino acids","acid-base"],"difficulty":"hard"},

{"text":"Which amino acid provides the nitrogen atoms used in urea cycle reactions?",
 "options":["Aspartate and ammonia (via carbamoyl phosphate)","Glutamine and alanine","Glycine and serine","Histidine and arginine"],"correct":0,
 "explanation":"The urea cycle incorporates two nitrogen atoms into urea: one from ammonia (as carbamoyl phosphate, made from NH4+ + CO2) and one from aspartate (which donates its amino group via argininosuccinate). Glutamine transports amino nitrogen from peripheral tissues to the liver as NH4+ and as aspartate precursors.",
 "tags":["amino acids","urea cycle","nitrogen metabolism"],"difficulty":"hard"},

{"text":"A peptide bond is formed by:",
 "options":["Condensation of the alpha-carboxyl group of one amino acid with the alpha-amino group of the next, releasing water","Oxidation of two adjacent amino acid side chains","Phosphorylation of the alpha-amino group","Reduction of a disulfide bond between two cysteines"],"correct":0,
 "explanation":"Peptide bond formation is a condensation (dehydration) reaction: the alpha-COOH of one amino acid reacts with the alpha-NH2 of the next, releasing H2O and forming an amide bond (–CO–NH–). This occurs at the ribosome during translation. The peptide bond has partial double bond character due to resonance, making it planar and restricting rotation.",
 "tags":["amino acids","protein structure"],"difficulty":"easy"},

{"text":"Selenocysteine is sometimes called the 21st amino acid. It is encoded by which codon?",
 "options":["UGA (normally a stop codon, recoded in context)","AUG","UAA","CGG"],"correct":0,
 "explanation":"Selenocysteine is incorporated at UGA codons when a special stem-loop structure (SECIS element) is present in the mRNA 3' UTR. Normally UGA is a stop codon, but SECIS causes the ribosome to insert selenocysteine instead. Selenoproteins include thioredoxin reductase and glutathione peroxidase. Dietary selenium is essential for their synthesis.",
 "tags":["amino acids","translation","molecular biology"],"difficulty":"hard"},

{"text":"Which pair of amino acids is important for forming salt bridges in proteins?",
 "options":["Aspartate/glutamate (negative) with lysine/arginine/histidine (positive)","Glycine and alanine","Leucine and valine","Serine and threonine"],"correct":0,
 "explanation":"Salt bridges form between oppositely charged side chains: anionic residues (Asp pKa ~3.9, Glu pKa ~4.1) pair with cationic residues (Lys pKa ~10.5, Arg pKa ~12.5, His pKa ~6.0). Salt bridges contribute to protein stability, especially in thermophilic proteins, and to protein-protein and protein-DNA interactions.",
 "tags":["amino acids","protein structure"],"difficulty":"medium"},

# ── PROTEIN STRUCTURE & FUNCTION (30) ────────────────────────────────────
{"text":"Which level of protein structure is maintained by hydrogen bonds between backbone carbonyl and amide groups?",
 "options":["Secondary structure (alpha-helices and beta-sheets)","Primary structure","Tertiary structure","Quaternary structure"],"correct":0,
 "explanation":"Secondary structure (alpha-helices, beta-sheets, turns) is stabilized by H-bonds between backbone C=O and N–H groups, not side chains. Primary structure is the amino acid sequence (covalent). Tertiary structure involves side chain interactions. Quaternary structure involves interactions between subunits.",
 "tags":["protein structure"],"difficulty":"easy"},

{"text":"In an alpha-helix, each residue forms a hydrogen bond with the residue how many positions later?",
 "options":["4 positions (i+4)","2 positions (i+2)","3 positions (i+3)","7 positions (i+7)"],"correct":0,
 "explanation":"In an alpha-helix, the N–H of residue i hydrogen bonds to the C=O of residue i+4. The helix has 3.6 residues per turn and a rise of 1.5 Å per residue (5.4 Å per turn). This geometry and the i→i+4 hydrogen bonding pattern define the alpha-helix.",
 "tags":["protein structure","alpha-helix"],"difficulty":"medium"},

{"text":"The dominant thermodynamic driving force for protein folding in aqueous solution is:",
 "options":["The hydrophobic effect — burying nonpolar side chains away from water","Maximizing the number of hydrogen bonds","Formation of disulfide bonds","Maximizing ionic interactions"],"correct":0,
 "explanation":"The hydrophobic effect drives folding: exposing nonpolar residues to water is entropically costly (water forms ordered cage around them). Burying them in the protein core releases water, increasing entropy. This is the dominant force, though hydrogen bonds, electrostatic interactions, and van der Waals forces also contribute.",
 "tags":["protein structure","folding","thermodynamics"],"difficulty":"medium"},

{"text":"Hemoglobin (alpha2beta2) exhibits cooperative O2 binding. This means:",
 "options":["Binding of O2 to one subunit increases O2 affinity in remaining subunits","O2 binds to only one subunit at a time","All four subunits bind O2 simultaneously with equal affinity","Cooperativity decreases O2 binding at high PO2"],"correct":0,
 "explanation":"Hemoglobin's cooperative binding produces a sigmoidal O2 saturation curve. O2 binding to one heme group causes a conformational change from T-state (tense, low affinity) to R-state (relaxed, high affinity), increasing affinity of the remaining hemes. This allows efficient O2 loading in lungs (high PO2) and unloading in tissues (low PO2).",
 "tags":["protein structure","hemoglobin","cooperativity"],"difficulty":"medium"},

{"text":"The Bohr effect describes how hemoglobin O2 affinity changes with:",
 "options":["Decreasing pH and increasing CO2 (lower affinity, promotes O2 release to tissues)","Increasing pH and decreasing CO2","2,3-BPG binding to the T-state","Temperature changes only"],"correct":0,
 "explanation":"CO2 from metabolizing tissues lowers blood pH (H2CO3 formation) and also carbamylates hemoglobin. Both H+ and CO2 stabilize the T-state (lower O2 affinity), promoting O2 unloading. In lungs, CO2 is expelled and pH rises, shifting to R-state for O2 loading. This is an exquisite physiological adaptation.",
 "tags":["protein structure","hemoglobin","Bohr effect"],"difficulty":"medium"},

{"text":"2,3-bisphosphoglycerate (2,3-BPG) binds to hemoglobin and:",
 "options":["Stabilizes the T-state, decreasing O2 affinity and shifting the curve rightward","Increases O2 affinity (left shift)","Has no effect on O2 binding","Is produced only in the lungs"],"correct":0,
 "explanation":"2,3-BPG binds in the central cavity of deoxyhemoglobin (T-state), stabilizing it and decreasing O2 affinity (right shift of the O2-dissociation curve). High altitude → hypoxia → increased 2,3-BPG → more efficient O2 unloading. Fetal hemoglobin (HbF, gamma subunits) has lower affinity for 2,3-BPG, giving it higher O2 affinity to extract O2 from maternal blood.",
 "tags":["protein structure","hemoglobin","2,3-BPG"],"difficulty":"medium"},

{"text":"SDS-PAGE separates proteins primarily based on:",
 "options":["Molecular weight","Isoelectric point","Hydrophobicity","Ligand-binding affinity"],"correct":0,
 "explanation":"SDS (sodium dodecyl sulfate) denatures proteins and coats them with negative charge proportional to their size. When run through an acrylamide gel under electric field, all proteins migrate based on size alone (smaller migrates faster). The resulting bands can be stained to reveal molecular weight distribution.",
 "tags":["protein structure","lab techniques"],"difficulty":"easy"},

{"text":"Which statement about enzyme active sites is correct?",
 "options":["Active sites are small pockets or clefts that are complementary in shape and charge to the substrate","Active sites are randomly distributed on the protein surface","Active sites only function when the substrate is in excess","Active sites are always composed of hydrophobic residues only"],"correct":0,
 "explanation":"Enzyme active sites are specific three-dimensional pockets with precise geometries, charge distributions, and hydrophobic/hydrophilic properties complementary to the transition state (and substrate). They are formed by residues from different parts of the primary sequence that come together in the folded protein. The induced fit model proposes that substrates cause conformational changes to optimize complementarity.",
 "tags":["protein structure","enzyme function"],"difficulty":"easy"},

{"text":"Chaperone proteins (e.g., Hsp70, GroEL) assist in protein folding by:",
 "options":["Preventing premature/incorrect aggregation by transiently binding exposed hydrophobic regions","Catalyzing disulfide bond formation","Directly specifying the final folded structure","Degrading misfolded proteins exclusively"],"correct":0,
 "explanation":"Molecular chaperones bind to exposed hydrophobic regions of nascent or unfolded polypeptides, preventing aggregation and providing a protected environment for folding. ATP hydrolysis drives cycles of binding and release, giving the protein repeated chances to fold correctly. Chaperones do not specify the final folded structure — that information is in the primary sequence (Anfinsen's principle).",
 "tags":["protein structure","chaperones","folding"],"difficulty":"medium"},

{"text":"The proteasome degrades proteins that are tagged with:",
 "options":["Ubiquitin chains (polyubiquitination)","Phosphate groups","Glycosyl groups","Acetyl groups"],"correct":0,
 "explanation":"The ubiquitin-proteasome system (UPS) marks proteins for degradation: ubiquitin ligases attach ubiquitin chains (usually K48-linked polyubiquitin) to target proteins. The 26S proteasome recognizes polyubiquitin, unfolds the protein, and degrades it into short peptides. This is the main pathway for regulated protein degradation in eukaryotes.",
 "tags":["protein structure","ubiquitin-proteasome","protein degradation"],"difficulty":"medium"},

{"text":"Which immunoglobulin class is most abundant in serum and crosses the placenta?",
 "options":["IgG","IgM","IgA","IgE"],"correct":0,
 "explanation":"IgG is the most abundant immunoglobulin (~80% of serum Ig) and the only class that crosses the placenta (via FcRn receptors), providing passive immunity to the fetus and newborn for the first months of life. IgM is produced first in an immune response (pentamer, good at complement activation). IgA is the main Ig in mucosal secretions. IgE mediates allergic responses and anti-parasite immunity.",
 "tags":["protein structure","immunology"],"difficulty":"medium"},

{"text":"Beta-lactam antibiotics (penicillins, cephalosporins) work by:",
 "options":["Irreversibly inhibiting transpeptidase (PBP) enzymes that crosslink peptidoglycan in bacterial cell walls","Inhibiting the bacterial 50S ribosomal subunit","Disrupting bacterial cell membranes","Blocking dihydrofolate reductase"],"correct":0,
 "explanation":"Beta-lactam antibiotics mimic the D-Ala-D-Ala terminus of peptidoglycan precursors and covalently acylate penicillin-binding proteins (PBPs = transpeptidases), blocking crosslinking of peptidoglycan strands. This weakens the cell wall, causing lysis. Bacteria acquire resistance via beta-lactamases (hydrolyze the beta-lactam ring) or altered PBPs (MRSA).",
 "tags":["protein structure","antibiotics","microbiology"],"difficulty":"medium"},

{"text":"Collagen is unusually stable because of its unique triple helix structure. What amino acid is essential at every third position in collagen?",
 "options":["Glycine","Proline","Alanine","Hydroxyproline"],"correct":0,
 "explanation":"Collagen has the repeating sequence Gly-X-Y, where Gly at every third position is absolutely required. The triple helix packs three chains tightly, and only glycine (the smallest amino acid, R = H) can fit in the central space of the triple helix without steric clash. Mutations substituting even one Gly cause osteogenesis imperfecta.",
 "tags":["protein structure","collagen"],"difficulty":"medium"},

{"text":"Sickle cell anemia results from which mutation in hemoglobin?",
 "options":["Val→Glu substitution at position 6 of the beta-globin chain (HbS: glutamic acid replaced by valine)","A deletion in the alpha-globin gene","Phosphorylation of histidine in the active site","Incorrect disulfide bond formation"],"correct":0,
 "explanation":"HbS has a single nucleotide change (GAG→GTG) causing substitution of hydrophilic Glu with hydrophobic Val at position 6 of beta-globin. In the deoxy (T) state, this Val fits into a hydrophobic pocket on an adjacent beta-chain, causing polymerization. These long fibers distort RBCs into sickle shapes, causing hemolysis, vaso-occlusion, and pain crises. HbS provides heterozygote protection against malaria.",
 "tags":["protein structure","hemoglobin","genetic disease"],"difficulty":"medium"},

{"text":"Antibody diversity is primarily generated by which mechanism?",
 "options":["V(D)J recombination — somatic recombination of variable, diversity, and joining gene segments","Point mutations in germ cells","Alternative splicing only","Copy number variation in the germ line"],"correct":0,
 "explanation":"V(D)J recombination randomly joins one V, D, and J segment (heavy chain) or V and J segments (light chain) in developing B cells, creating enormous receptor diversity (~10^11 combinations). Additional diversity comes from junctional imprecision (P and N nucleotide addition) and somatic hypermutation (after antigen exposure). This process underlies the ability to recognize virtually any antigen.",
 "tags":["protein structure","immunology","molecular biology"],"difficulty":"hard"},

# ── ENZYME KINETICS AND REGULATION (30) ──────────────────────────────────
{"text":"The Michaelis constant (Km) reflects:",
 "options":["Substrate concentration at which v = Vmax/2; inversely related to enzyme-substrate affinity","Maximum reaction velocity","The concentration of product that inhibits the enzyme","The number of active sites per enzyme molecule"],"correct":0,
 "explanation":"Km is the substrate concentration at half-maximal velocity. Low Km → enzyme reaches half-saturation at low [S] → high affinity. High Km → enzyme needs more substrate to half-saturate → low affinity. Numerically, Km ≈ (k-1 + k2)/k1 for simple Michaelis-Menten kinetics.",
 "tags":["enzyme kinetics"],"difficulty":"easy"},

{"text":"A competitive inhibitor increases apparent Km but leaves Vmax unchanged because:",
 "options":["High substrate concentrations can displace the competitive inhibitor from the active site","The inhibitor binds irreversibly, so more enzyme must be synthesized","The inhibitor activates an alternative active site","The inhibitor changes the protein's secondary structure"],"correct":0,
 "explanation":"Competitive inhibitors bind reversibly to the active site. At high [S], substrate outcompetes the inhibitor, so Vmax (the rate when enzyme is fully saturated with substrate) is unchanged. However, more substrate is needed to achieve half-saturation in the presence of inhibitor, so apparent Km increases.",
 "tags":["enzyme kinetics","competitive inhibition"],"difficulty":"medium"},

{"text":"An inhibitor decreases Vmax but leaves Km unchanged. This is consistent with:",
 "options":["Pure noncompetitive inhibition","Competitive inhibition","Uncompetitive inhibition","Substrate inhibition"],"correct":0,
 "explanation":"Pure noncompetitive inhibitors bind equally well to free enzyme and enzyme-substrate complex (at a site other than active site), reducing the total functional enzyme population. Km is unchanged (substrate still binds normally), but Vmax decreases proportionally with inhibitor concentration. On a Lineweaver-Burk plot, lines have different y-intercepts but the same x-intercept.",
 "tags":["enzyme kinetics","noncompetitive inhibition"],"difficulty":"medium"},

{"text":"An uncompetitive inhibitor binds only to the enzyme-substrate complex. On a Lineweaver-Burk plot, uncompetitive inhibition produces:",
 "options":["Parallel lines (same slope, different intercepts)","Lines intersecting at the x-axis","Lines intersecting at the y-axis","No change in the graph"],"correct":0,
 "explanation":"Uncompetitive inhibitors bind ES complex, decreasing apparent Km and Vmax by the same factor (alpha'). On a double-reciprocal plot, the uninhibited and inhibited lines are parallel (same slope = Km/Vmax, since both change by the same factor). Both the x-intercept (–1/Km) and y-intercept (1/Vmax) shift left/up by the same factor.",
 "tags":["enzyme kinetics","uncompetitive inhibition"],"difficulty":"hard"},

{"text":"Organophosphate compounds (e.g., nerve agents) are dangerous because they:",
 "options":["Irreversibly phosphorylate the active-site serine of acetylcholinesterase, preventing ACh breakdown","Competitively inhibit nicotinic acetylcholine receptors","Block voltage-gated sodium channels in motor neurons","Activate adenylyl cyclase, flooding cells with cAMP"],"correct":0,
 "explanation":"Organophosphates covalently phosphorylate the catalytic serine of acetylcholinesterase (AChE) at the neuromuscular junction. Without AChE, acetylcholine accumulates, causing continuous muscle stimulation (SLUDGE symptoms: salivation, lacrimation, urination, defecation, GI distress, emesis). Treatment includes atropine (muscarinic antagonist) and pralidoxime (reactivates AChE if given early).",
 "tags":["enzyme kinetics","irreversible inhibition","neuroscience"],"difficulty":"hard"},

{"text":"Allosteric regulation differs from competitive inhibition in that:",
 "options":["Allosteric effectors bind to sites distinct from the active site and cause conformational changes; competitive inhibitors bind at the active site","Both mechanisms bind at the active site","Allosteric effectors only inhibit, never activate","Competitive inhibitors permanently modify enzyme structure"],"correct":0,
 "explanation":"Allosteric regulation involves binding of an effector to a regulatory (allosteric) site, causing conformational changes that alter active site geometry/affinity. Allosteric effectors can be activators or inhibitors and are not structurally similar to the substrate. Competitive inhibitors are typically substrate analogs that directly compete at the active site.",
 "tags":["enzyme regulation","allosterism"],"difficulty":"medium"},

{"text":"Feedback inhibition in the isoleucine biosynthetic pathway involves isoleucine inhibiting:",
 "options":["Threonine deaminase (first committed step)","The last enzyme in the pathway","All enzymes simultaneously","Only the export of isoleucine from the cell"],"correct":0,
 "explanation":"Classic feedback (product) inhibition: isoleucine (end product) allosterically inhibits threonine deaminase, the first committed step. This prevents overproduction by shutting down the pathway when sufficient product exists. Inhibiting the first committed step is more efficient than inhibiting later enzymes.",
 "tags":["enzyme regulation","feedback inhibition"],"difficulty":"medium"},

{"text":"Protein kinase A (PKA) is activated by which second messenger?",
 "options":["cAMP (cyclic AMP)","IP3","Diacylglycerol (DAG)","Ca2+"],"correct":0,
 "explanation":"PKA is a tetrameric enzyme with two catalytic (C) and two regulatory (R) subunits. cAMP binds R subunits, causing dissociation and releasing active C subunits. cAMP is made by adenylyl cyclase in response to GPCR activation (e.g., beta-adrenergic receptors). PKA phosphorylates many targets including glycogen phosphorylase kinase and CREB.",
 "tags":["enzyme regulation","signal transduction","cAMP"],"difficulty":"medium"},

{"text":"Michaelis-Menten kinetics break down when an enzyme has multiple subunits with cooperative substrate binding. This behavior is better described by:",
 "options":["The Hill equation (sigmoidal binding curve)","The Lineweaver-Burk equation","Competitive inhibition kinetics","First-order rate kinetics"],"correct":0,
 "explanation":"Cooperative enzymes (like hemoglobin for O2, or regulatory enzymes like PFK-1) show sigmoidal v vs. [S] curves. The Hill coefficient (n) quantifies cooperativity: n>1 = positive cooperativity, n<1 = negative, n=1 = hyperbolic (Michaelis-Menten). The Hill equation: v = Vmax[S]^n / (K0.5^n + [S]^n).",
 "tags":["enzyme kinetics","cooperativity","Hill equation"],"difficulty":"hard"},

{"text":"Hexokinase (in muscle) and glucokinase (hexokinase IV, in liver) both phosphorylate glucose, but differ in that:",
 "options":["Glucokinase has a high Km for glucose and is not inhibited by G6P; hexokinase has low Km and is inhibited by G6P","Both have the same Km but glucokinase is allosterically activated","Hexokinase only works at high glucose concentrations","Glucokinase requires NAD+ as a cofactor"],"correct":0,
 "explanation":"Glucokinase (hexokinase IV) has high Km (~10 mM, near portal vein glucose), is not inhibited by G6P, and shows sigmoidal kinetics (cooperative). This makes glucokinase a glucose sensor: it acts as a low-affinity glucose phosphorylator in the liver when blood glucose is high. Muscle hexokinase has low Km (~0.1 mM), is inhibited by G6P, and saturates at normal glucose levels.",
 "tags":["enzyme regulation","glycolysis","hexokinase"],"difficulty":"hard"},

{"text":"The kcat/Km ratio (catalytic efficiency) is important because:",
 "options":["It reflects how efficiently an enzyme converts substrate to product at low [S], approaching the diffusion limit","It equals the maximum velocity","It measures enzyme concentration","It is used to calculate the equilibrium constant"],"correct":0,
 "explanation":"kcat/Km is the second-order rate constant for the reaction E + S → E + P at low [S]. The theoretical maximum is the diffusion limit (~10^8–10^9 M-1s-1). 'Catalytically perfect' enzymes (like carbonic anhydrase, triose phosphate isomerase) approach this limit. kcat/Km is used to compare catalytic efficiencies of different enzymes or compare the same enzyme with different substrates.",
 "tags":["enzyme kinetics","catalytic efficiency"],"difficulty":"hard"},

{"text":"Zymogen activation is best exemplified by:",
 "options":["Trypsinogen is cleaved to trypsin by enteropeptidase in the small intestine","Hexokinase is phosphorylated to activate it","DNA polymerase requires RNA primer to initiate","Hemoglobin binds O2 cooperatively"],"correct":0,
 "explanation":"Zymogens (proenzymes) are inactive precursors activated by proteolytic cleavage. Trypsinogen → trypsin (by enteropeptidase/enterokinase); trypsin then activates other zymogens (chymotrypsinogen, proelastase, procarboxypeptidases). This irreversible mechanism prevents premature activation in the pancreas. Premature activation causes pancreatitis.",
 "tags":["enzyme regulation","zymogens","digestion"],"difficulty":"medium"},

# ── CARBOHYDRATE METABOLISM (40) ──────────────────────────────────────────
{"text":"Which enzyme catalyzes the rate-limiting committed step of glycolysis?",
 "options":["Phosphofructokinase-1 (PFK-1)","Hexokinase","Pyruvate kinase","Aldolase"],"correct":0,
 "explanation":"PFK-1 catalyzes fructose-6-phosphate → fructose-1,6-bisphosphate (using ATP). This is the first committed, irreversible step of glycolysis and its major regulatory point. PFK-1 is activated by AMP/ADP/F-2,6-BP and inhibited by ATP/citrate/glucagon. Hexokinase is also regulated but not the committed rate-limiting step.",
 "tags":["glycolysis","enzyme regulation"],"difficulty":"easy"},

{"text":"Net ATP yield from glycolysis (glucose → 2 pyruvate) is:",
 "options":["2 ATP","4 ATP","6 ATP","36–38 ATP"],"correct":0,
 "explanation":"Glycolysis: 4 ATP produced (steps 7 and 10, substrate-level phosphorylation) minus 2 ATP consumed (hexokinase and PFK-1) = net 2 ATP. Also produces 2 NADH. The 36-38 ATP figure includes downstream oxidative phosphorylation from the full aerobic catabolism of glucose.",
 "tags":["glycolysis","bioenergetics"],"difficulty":"easy"},

{"text":"Which glycolytic enzyme catalyzes the only oxidation-reduction step in glycolysis?",
 "options":["Glyceraldehyde-3-phosphate dehydrogenase (G3PDH)","Phosphoglycerate mutase","Enolase","Phosphoglycerate kinase"],"correct":0,
 "explanation":"G3PDH oxidizes glyceraldehyde-3-phosphate to 1,3-bisphosphoglycerate, reducing NAD+ to NADH. This is the only redox step in glycolysis. The high-energy thioester intermediate is captured as 1,3-BPG, which then drives ATP synthesis at phosphoglycerate kinase (substrate-level phosphorylation).",
 "tags":["glycolysis","redox reactions"],"difficulty":"medium"},

{"text":"Under anaerobic conditions, NADH generated in glycolysis is reoxidized by:",
 "options":["Lactate dehydrogenase (pyruvate → lactate), regenerating NAD+ to sustain glycolysis","The electron transport chain","Pyruvate dehydrogenase complex","Malate-aspartate shuttle"],"correct":0,
 "explanation":"Without O2, the ETC cannot reoxidize NADH. Lactate dehydrogenase (LDH) transfers the electrons from NADH to pyruvate, forming lactate and regenerating NAD+. This NAD+ is essential for continued glycolysis. In yeast, pyruvate decarboxylase and alcohol dehydrogenase regenerate NAD+ via ethanol fermentation.",
 "tags":["glycolysis","anaerobic metabolism"],"difficulty":"medium"},

{"text":"Pyruvate dehydrogenase complex (PDC) is inhibited by all of the following EXCEPT:",
 "options":["AMP (which activates PDC)","Acetyl-CoA (product)","NADH (product)","PDC kinase activated by high ATP/ADP ratio"],"correct":0,
 "explanation":"PDC is inhibited by its products (acetyl-CoA and NADH) and by PDC kinase when ATP/ADP and NADH/NAD+ ratios are high (energy surplus). PDC is activated by PDC phosphatase (activated by insulin and Ca2+), by AMP, by CoA, and by NAD+. High AMP signals low energy and would activate PDC to produce more acetyl-CoA.",
 "tags":["pyruvate dehydrogenase","enzyme regulation"],"difficulty":"hard"},

{"text":"How many CO2 molecules are released per turn of the TCA cycle?",
 "options":["2","1","3","4"],"correct":0,
 "explanation":"Two CO2 are released per TCA cycle turn: one at isocitrate dehydrogenase (isocitrate → alpha-ketoglutarate) and one at alpha-ketoglutarate dehydrogenase (alpha-KG → succinyl-CoA). These are the two oxidative decarboxylation steps of the TCA cycle. The 2-carbon acetyl group entering from acetyl-CoA is fully oxidized over multiple turns.",
 "tags":["TCA cycle","carbon balance"],"difficulty":"medium"},

{"text":"The energetic yield of one NADH oxidized by the ETC is approximately:",
 "options":["2.5 ATP","1.5 ATP","3 ATP","4 ATP"],"correct":0,
 "explanation":"Modern measurements (using P/O ratios from chemiosmosis) give ~2.5 ATP per NADH (pumps 10 H+ across inner mitochondrial membrane; ATP synthase needs ~4 H+ per ATP → 10/4 = 2.5 ATP). FADH2 yields ~1.5 ATP (pumps 6 H+). Older textbooks cited 3 ATP (NADH) and 2 ATP (FADH2), but 2.5 and 1.5 are now accepted values.",
 "tags":["electron transport chain","ATP yield"],"difficulty":"medium"},

{"text":"Which complex of the ETC does NOT pump protons across the inner mitochondrial membrane?",
 "options":["Complex II (succinate dehydrogenase)","Complex I (NADH dehydrogenase)","Complex III (cytochrome bc1)","Complex IV (cytochrome c oxidase)"],"correct":0,
 "explanation":"Complexes I, III, and IV pump protons from matrix to intermembrane space, generating the proton motive force. Complex II (succinate dehydrogenase) accepts electrons from FADH2 and passes them to ubiquinone (CoQ) but does NOT translocate protons. This is why FADH2 yields less ATP than NADH.",
 "tags":["electron transport chain"],"difficulty":"medium"},

{"text":"Rotenone, a pesticide, blocks which complex of the ETC?",
 "options":["Complex I (NADH:ubiquinone oxidoreductase)","Complex II","Complex III","Complex IV"],"correct":0,
 "explanation":"Rotenone is a specific inhibitor of Complex I (blocks electron transfer from Fe-S center to ubiquinone). Inhibiting Complex I prevents NADH oxidation, halting the ETC. It is also used experimentally to model Parkinson's disease (dopaminergic neurons are especially sensitive to Complex I inhibition).",
 "tags":["electron transport chain","toxicology"],"difficulty":"hard"},

{"text":"Uncoupling proteins (UCPs, e.g., thermogenin/UCP1 in brown fat) affect oxidative phosphorylation by:",
 "options":["Allowing protons to flow back across the inner mitochondrial membrane without producing ATP, generating heat instead","Activating ATP synthase to produce more ATP per proton","Inhibiting electron flow at Complex III","Increasing proton gradient without generating heat"],"correct":0,
 "explanation":"UCPs dissipate the proton gradient (uncouple ETC from ATP synthesis) by providing an alternative proton leak pathway. Instead of driving ATP synthase, the energy is released as heat — thermogenesis. UCP1 in brown adipose tissue is especially important in newborns and hibernating animals for non-shivering thermogenesis.",
 "tags":["oxidative phosphorylation","thermogenesis","uncoupling"],"difficulty":"medium"},

{"text":"The unique enzymes of gluconeogenesis that bypass glycolytic irreversible steps are:",
 "options":["Pyruvate carboxylase, PEPCK, fructose-1,6-bisphosphatase, glucose-6-phosphatase","Hexokinase, PFK-1, pyruvate kinase","Glycogen synthase and glycogen phosphorylase","Aldolase and enolase"],"correct":0,
 "explanation":"Three irreversible glycolytic steps are bypassed: (1) Pyruvate kinase step bypassed by pyruvate carboxylase (pyruvate→OAA) + PEPCK (OAA→PEP); (2) PFK-1 step bypassed by fructose-1,6-bisphosphatase; (3) Hexokinase step bypassed by glucose-6-phosphatase. Glucose-6-phosphatase is only in liver/kidney, explaining why only those organs can release glucose to blood.",
 "tags":["gluconeogenesis"],"difficulty":"medium"},

{"text":"Insulin promotes which of the following metabolic effects in hepatocytes?",
 "options":["Glycolysis, glycogen synthesis, fatty acid synthesis; inhibits gluconeogenesis","Glycogenolysis, gluconeogenesis, fatty acid oxidation","Ketone body production and glucose output","Protein catabolism and urea synthesis"],"correct":0,
 "explanation":"Insulin (secreted by beta cells in response to high glucose) promotes anabolic pathways: activates PFK-2 (increases F-2,6-BP → activates PFK-1 → glycolysis), glycogen synthase (glycogen synthesis), acetyl-CoA carboxylase (fatty acid synthesis), and inhibits PEPCK and glucose-6-phosphatase (gluconeogenesis). Net effect: lower blood glucose.",
 "tags":["carbohydrate metabolism","hormones","insulin"],"difficulty":"medium"},

{"text":"The pentose phosphate pathway (hexose monophosphate shunt) is particularly important in red blood cells because it:",
 "options":["Produces NADPH to maintain glutathione (GSH) reduced, protecting against oxidative hemolysis","Provides the primary ATP source for red blood cells","Is the only source of ribose for nucleotide synthesis in RBCs","Generates acetyl-CoA for fatty acid synthesis in RBCs"],"correct":0,
 "explanation":"RBCs lack mitochondria and nuclei (no TCA, no ETC, no nucleotide synthesis). The pentose phosphate pathway produces NADPH, which reduces glutathione (GSSG → GSH) via glutathione reductase. Reduced GSH protects hemoglobin from oxidative damage. G6PD deficiency impairs this pathway → oxidative hemolysis with oxidative stressors (certain drugs, fava beans).",
 "tags":["pentose phosphate pathway","red blood cells","G6PD"],"difficulty":"medium"},

{"text":"Glycogen synthase is activated by:",
 "options":["Dephosphorylation (by phosphatase, stimulated by insulin) and allosterically by glucose-6-phosphate","Phosphorylation by PKA","Glucagon via cAMP","Epinephrine in skeletal muscle"],"correct":0,
 "explanation":"Glycogen synthase is active when dephosphorylated (insulin activates PP1 via inhibiting GSK-3). G6P allosterically activates glycogen synthase — high intracellular glucose signals available precursor. Glucagon and epinephrine activate PKA → phosphorylates glycogen synthase → INACTIVATES it (and activates phosphorylase). This reciprocal regulation is a key metabolic switch.",
 "tags":["glycogen metabolism","enzyme regulation","insulin"],"difficulty":"hard"},

{"text":"In the Cori cycle, skeletal muscle sends which metabolite to the liver during intense exercise?",
 "options":["Lactate","Glucose","Pyruvate","Fatty acids"],"correct":0,
 "explanation":"During intense anaerobic exercise, skeletal muscle converts glucose to lactate (anaerobic glycolysis) to regenerate NAD+ for continued glycolysis. Lactate is exported to the blood, taken up by the liver, converted to pyruvate and then glucose via gluconeogenesis. This glucose returns to muscle — the Cori cycle. Alanine (from muscle amino acid catabolism) participates in the glucose-alanine cycle.",
 "tags":["Cori cycle","glucose-lactate cycle"],"difficulty":"easy"},

{"text":"Fructose-1,6-bisphosphatase (FBPase-1) is inhibited by which metabolite?",
 "options":["AMP and fructose-2,6-bisphosphate","ATP and citrate","Glucose-6-phosphate","Acetyl-CoA"],"correct":0,
 "explanation":"FBPase-1 (the gluconeogenesis enzyme) is inhibited by AMP (low energy signal) and fructose-2,6-bisphosphate (F-2,6-BP, high glycolytic signal). F-2,6-BP is produced by PFK-2 and is a powerful inhibitor of FBPase-1 while simultaneously activating PFK-1. This reciprocal regulation ensures glycolysis and gluconeogenesis don't run simultaneously at high rates.",
 "tags":["gluconeogenesis","enzyme regulation"],"difficulty":"hard"},

{"text":"Pyruvate carboxylase, an enzyme in gluconeogenesis, is activated by:",
 "options":["Acetyl-CoA","AMP","Glucose-6-phosphate","NADH"],"correct":0,
 "explanation":"Pyruvate carboxylase (PC) requires biotin (vitamin B7) and is allosterically activated by acetyl-CoA. High acetyl-CoA (from beta-oxidation during fasting) signals excess fuel and need for oxaloacetate replenishment for both the TCA cycle and gluconeogenesis. Acetyl-CoA cannot be converted back to pyruvate/glucose directly, so PC channels pyruvate into OAA.",
 "tags":["gluconeogenesis","pyruvate carboxylase","enzyme regulation"],"difficulty":"hard"},

{"text":"Galactosemia is caused by deficiency of galactose-1-phosphate uridyltransferase, which converts:",
 "options":["Galactose-1-phosphate + UDP-glucose → glucose-1-phosphate + UDP-galactose","Galactose to glucose directly","UDP-galactose to UDP-glucose","Lactose to glucose and galactose"],"correct":0,
 "explanation":"In galactose metabolism: galactose → galactose-1-phosphate (galactokinase) → glucose-1-phosphate (galactose-1-phosphate uridyltransferase). Deficiency causes accumulation of galactose-1-phosphate, which is toxic to liver, brain, and kidneys. Newborn screening detects this enzyme deficiency. Treatment is elimination of galactose (lactose) from the diet.",
 "tags":["carbohydrate metabolism","metabolic disorders","galactose"],"difficulty":"hard"},

{"text":"Which metabolic process generates the majority of the NADH used by the ETC during aerobic glucose catabolism?",
 "options":["The TCA cycle (most NADH) plus pyruvate dehydrogenase","Glycolysis exclusively","Beta-oxidation","The pentose phosphate pathway"],"correct":0,
 "explanation":"Of the 10 NADH produced per glucose in complete aerobic catabolism: glycolysis produces 2 NADH (cytoplasmic); pyruvate dehydrogenase produces 2 NADH; the TCA cycle produces 6 NADH (3 per turn × 2 turns). Additionally 2 FADH2 come from TCA. The TCA cycle + PDC provide 8 of 10 NADH, making them the dominant source for the ETC.",
 "tags":["TCA cycle","NADH","bioenergetics"],"difficulty":"medium"},

{"text":"Type 1 diabetes results from autoimmune destruction of pancreatic beta cells. Without insulin, which metabolic pathway is inappropriately active in adipose tissue?",
 "options":["Lipolysis (HSL activated by glucagon/epinephrine, not inhibited by insulin)","Lipogenesis (fatty acid synthesis)","Glycogen synthesis","Glucose uptake via GLUT4"],"correct":0,
 "explanation":"Insulin normally suppresses hormone-sensitive lipase (HSL) in adipocytes. Without insulin, HSL is active → releases free fatty acids → liver converts to ketone bodies → ketoacidosis. Insulin also promotes GLUT4 insertion into adipocyte membranes for glucose uptake; without insulin, glucose uptake is impaired. This explains the metabolic crisis in untreated T1DM.",
 "tags":["lipid metabolism","hormones","diabetes"],"difficulty":"medium"},

# ── LIPID METABOLISM (20) ─────────────────────────────────────────────────
{"text":"Which enzyme is the rate-limiting step of fatty acid synthesis, and how is it regulated?",
 "options":["Acetyl-CoA carboxylase (ACC); activated by citrate, inhibited by palmitoyl-CoA and glucagon-induced phosphorylation","Fatty acid synthase; regulated by product inhibition only","HMG-CoA reductase; inhibited by statins","Malonyl-CoA decarboxylase; activated by glucagon"],"correct":0,
 "explanation":"ACC carboxylates acetyl-CoA to malonyl-CoA (requires biotin). It is allosterically activated by citrate (excess acetyl-CoA signal) and inhibited by palmitoyl-CoA (feedback) and by phosphorylation (AMPK or PKA, activated by fasting/glucagon). Malonyl-CoA also inhibits carnitine palmitoyltransferase-1 (CPT-1), preventing concurrent fatty acid oxidation.",
 "tags":["fatty acid synthesis","enzyme regulation"],"difficulty":"medium"},

{"text":"The transport of long-chain fatty acids into the mitochondrial matrix requires:",
 "options":["Carnitine shuttle (carnitine palmitoyltransferase-1 on outer membrane, CPT-2 on inner membrane)","Simple diffusion across the inner membrane","VLDL particle transport","The GLUT family of transporters"],"correct":0,
 "explanation":"Long-chain fatty acyl-CoA cannot cross the inner mitochondrial membrane directly. Acyl-CoA is converted to acylcarnitine by CPT-1 (rate-limiting step of beta-oxidation; inhibited by malonyl-CoA). Acylcarnitine crosses via a translocase; CPT-2 on the inner membrane regenerates acyl-CoA in the matrix for beta-oxidation.",
 "tags":["fatty acid oxidation","carnitine"],"difficulty":"medium"},

{"text":"The net ATP yield from complete oxidation of one molecule of palmitate (C16:0) is approximately:",
 "options":["106–108 ATP","2 ATP","38 ATP","15 ATP"],"correct":0,
 "explanation":"Palmitoyl-CoA → 7 cycles of beta-oxidation: 7 FADH2 (×1.5=10.5 ATP) + 7 NADH (×2.5=17.5 ATP) + 8 acetyl-CoA (×10 ATP each = 80 ATP) = 108 ATP. Subtract 2 ATP for activation (palmitoyl-CoA synthesis). Net ≈ 106 ATP. This is ~3× the yield from glycolysis + TCA for glucose, reflecting fats' higher energy density.",
 "tags":["beta-oxidation","bioenergetics"],"difficulty":"hard"},

{"text":"Odd-chain fatty acid beta-oxidation produces propionyl-CoA, which is converted to succinyl-CoA by which enzymes and cofactors?",
 "options":["Propionyl-CoA carboxylase (biotin) → methylmalonyl-CoA mutase (vitamin B12) → succinyl-CoA","Propionyl-CoA dehydrogenase → acetyl-CoA directly","Fatty acid synthase in reverse","Thiolase cleavage to two acetyl-CoA"],"correct":0,
 "explanation":"Odd-chain fatty acid catabolism: beta-oxidation proceeds normally until 3-carbon propionyl-CoA (instead of 2-carbon acetyl-CoA). Propionyl-CoA carboxylase (biotin) → D-methylmalonyl-CoA → L-methylmalonyl-CoA → succinyl-CoA (methylmalonyl-CoA mutase, requires B12). Succinyl-CoA enters TCA cycle. Methylmalonic acidemia results from B12/mutase deficiency.",
 "tags":["beta-oxidation","odd-chain fatty acids","vitamin B12"],"difficulty":"hard"},

{"text":"HMG-CoA reductase catalyzes the committed, rate-limiting step of cholesterol synthesis. Statins treat hypercholesterolemia by:",
 "options":["Competitively inhibiting HMG-CoA reductase, reducing hepatic cholesterol synthesis and upregulating LDL receptors","Activating VLDL secretion from the liver","Blocking bile acid reabsorption in the intestine","Increasing LDL oxidation in macrophages"],"correct":0,
 "explanation":"Statins (e.g., atorvastatin) are structural analogs of HMG-CoA that competitively inhibit HMG-CoA reductase. Reduced intrahepatic cholesterol triggers upregulation of hepatic LDL receptors → more LDL cleared from blood. This is the primary mechanism by which statins lower LDL-C and reduce cardiovascular risk.",
 "tags":["cholesterol synthesis","pharmacology"],"difficulty":"medium"},

{"text":"In diabetic ketoacidosis (DKA), ketone bodies accumulate because:",
 "options":["Excess acetyl-CoA from beta-oxidation cannot enter the TCA cycle (depleted OAA), so it is channeled to ketogenesis","Cells cannot oxidize glucose, so they burn fat instead (oversimplified: technically OAA depletion is key)","Ketone body utilization is blocked in peripheral tissues","Insulin blocks beta-oxidation, diverting all acetyl-CoA to ketones"],"correct":0,
 "explanation":"In DKA (untreated T1DM), lack of insulin → lipolysis → excess fatty acids → beta-oxidation in liver → acetyl-CoA accumulates. OAA is depleted (used for gluconeogenesis, reducing TCA capacity). Excess acetyl-CoA → HMG-CoA → ketone bodies (acetoacetate, beta-hydroxybutyrate). Paradoxically, brain eventually uses ketones as fuel during prolonged starvation. Acetone gives the characteristic fruity breath.",
 "tags":["ketone bodies","diabetes","lipid metabolism"],"difficulty":"hard"},

{"text":"Adipose triglyceride lipase (ATGL) and hormone-sensitive lipase (HSL) are key lipolytic enzymes. Which hormone activates these during fasting?",
 "options":["Glucagon (and epinephrine) via cAMP-PKA cascade","Insulin via PI3K pathway","Leptin directly activating HSL","Cortisol via nuclear receptors only"],"correct":0,
 "explanation":"Glucagon and epinephrine activate adenylyl cyclase → cAMP → PKA → phosphorylates HSL (activating it) and perilipin (allowing access to lipid droplet). ATGL is also activated. Free fatty acids + glycerol are released. Insulin inhibits PKA effects and activates phosphodiesterase (breaks down cAMP), suppressing lipolysis. This is how insulin promotes fat storage and glucagon/epinephrine promote fat mobilization.",
 "tags":["lipolysis","hormones","signal transduction"],"difficulty":"medium"},

{"text":"Eicosanoids (prostaglandins, thromboxanes, leukotrienes) are derived from which fatty acid?",
 "options":["Arachidonic acid (C20:4, omega-6)","Linoleic acid (C18:2, omega-6)","Alpha-linolenic acid (C18:3, omega-3)","Palmitic acid (C16:0)"],"correct":0,
 "explanation":"Arachidonic acid (AA, 20:4, omega-6), released from membrane phospholipids by phospholipase A2, is the major precursor for eicosanoids. COX (cyclooxygenase) converts AA to prostaglandins/thromboxanes; 5-LOX converts AA to leukotrienes. NSAIDs (aspirin, ibuprofen) inhibit COX. Omega-3 fatty acids (EPA, DHA) compete with AA and produce less inflammatory eicosanoids.",
 "tags":["lipid metabolism","eicosanoids","inflammation"],"difficulty":"medium"},

# ── MOLECULAR BIOLOGY: DNA/RNA/REPLICATION (25) ───────────────────────────
{"text":"Which strand of the double-stranded DNA serves as the template for RNA polymerase?",
 "options":["Template strand (antisense strand, read 3'→5' by RNA polymerase, producing RNA 5'→3')","Coding strand (non-template strand, same sequence as mRNA)","Either strand is equally used","The strand with the promoter sequence"],
 "correct":0,
 "explanation":"RNA polymerase reads the template (antisense) strand 3'→5' and synthesizes RNA 5'→3'. The resulting mRNA has the same sequence as the non-template (coding/sense) strand, except U replaces T. The coding strand is also called the sense strand or non-template strand.",
 "tags":["transcription","molecular biology"],"difficulty":"easy"},

{"text":"Which DNA repair mechanism corrects single-base mismatches and small insertions/deletions that escape proofreading during replication?",
 "options":["Mismatch repair (MMR)","Nucleotide excision repair (NER)","Base excision repair (BER)","Non-homologous end joining (NHEJ)"],"correct":0,
 "explanation":"MMR detects and corrects replication errors: MSH2/MSH6 recognize mismatches, MLH1/PMS2 coordinate excision and resynthesis. MMR deficiency (Lynch syndrome/HNPCC) causes microsatellite instability and predisposes to colorectal cancer. NER handles bulky lesions (UV damage). BER handles single oxidized/deaminated bases. NHEJ joins double-strand breaks.",
 "tags":["DNA repair","mismatch repair","molecular biology"],"difficulty":"medium"},

{"text":"Telomeres are maintained in stem cells and cancer cells by which enzyme?",
 "options":["Telomerase (an RNA-dependent DNA polymerase with its own RNA template)","DNA polymerase delta","Topoisomerase II","Primase"],"correct":0,
 "explanation":"Telomeres shorten with each replication (end replication problem). Telomerase is a reverse transcriptase (TERT) with an RNA component (TERC) that serves as the template to extend telomeric repeats (TTAGGG) de novo. Active in stem cells, germ cells, and ~85-90% of cancer cells (allowing immortalization). Absence in somatic cells contributes to cellular senescence.",
 "tags":["DNA replication","telomeres","cancer biology"],"difficulty":"medium"},

{"text":"Which statement about DNA helicase during replication is correct?",
 "options":["Helicase unwinds the double helix by breaking hydrogen bonds between base pairs, creating a replication fork","Helicase synthesizes RNA primers at origins of replication","Helicase ligates Okazaki fragments together","Helicase removes supercoils introduced by replication"],"correct":0,
 "explanation":"DNA helicase (DnaB in prokaryotes; MCM complex in eukaryotes) translocates along DNA, using ATP hydrolysis to break hydrogen bonds between complementary base pairs, unwinding the double helix at the replication fork. Single-strand binding proteins (SSBPs) stabilize the separated strands. Topoisomerases resolve the supercoiling generated ahead of the fork.",
 "tags":["DNA replication","helicase"],"difficulty":"easy"},

{"text":"The RNA primer used to initiate DNA replication is synthesized by:",
 "options":["Primase (a type of RNA polymerase)","DNA polymerase I (for removal)","DNA ligase","Helicase"],"correct":0,
 "explanation":"DNA polymerases cannot initiate a new strand de novo — they can only extend a pre-existing 3'-OH. Primase synthesizes a short (~5-10 nt) RNA primer, providing the 3'-OH for DNA polymerase to extend. In eukaryotes, DNA pol alpha-primase complex lays down the primer. After replication, the RNA primer is removed (RNase H/FEN1) and replaced with DNA by pol delta/epsilon.",
 "tags":["DNA replication","primase"],"difficulty":"easy"},

{"text":"Eukaryotic pre-mRNA processing includes all of the following EXCEPT:",
 "options":["Removal of tRNA introns by spliceosomes (tRNA introns are removed by endonuclease/ligase, not the spliceosome)","5' capping with 7-methylguanosine","3' polyadenylation","Removal of introns by the spliceosome"],"correct":0,
 "explanation":"Pre-mRNA processing: 5' cap (m7G added co-transcriptionally), 3' poly-A tail (added after cleavage at polyadenylation signal AAUAAA), and splicing by the spliceosome (snRNPs U1, U2, U4, U5, U6). tRNA introns are spliced by a different mechanism (tRNA splicing endonuclease + tRNA ligase). The spliceosome is for pre-mRNA, not tRNA.",
 "tags":["RNA processing","splicing","molecular biology"],"difficulty":"hard"},

{"text":"Which RNA polymerase in eukaryotes transcribes mRNA precursors (pre-mRNA)?",
 "options":["RNA polymerase II","RNA polymerase I","RNA polymerase III","Primase"],"correct":0,
 "explanation":"Eukaryotes have three nuclear RNA polymerases: Pol I makes 28S, 18S, 5.8S rRNA (in nucleolus); Pol II makes mRNA, snRNA, miRNA precursors; Pol III makes 5S rRNA, tRNA, and other small RNAs. Alpha-amanitin (from death cap mushroom) selectively inhibits Pol II at low doses. Pol II requires general transcription factors (TFIID, etc.) and mediator complex.",
 "tags":["transcription","RNA polymerase"],"difficulty":"easy"},

{"text":"During translation, the A site, P site, and E site of the ribosome perform which functions?",
 "options":["A site: aminoacyl-tRNA entry; P site: peptidyl-tRNA (growing chain); E site: exit of deacylated tRNA","A site: exits the ribosome; P site: entry of new aminoacyl-tRNA; E site: elongation","All three sites participate equally in peptide bond formation","A site: polyadenylation; P site: processing; E site: export"],"correct":0,
 "explanation":"Ribosome sites: Aminoacyl site (A) — incoming aminoacyl-tRNA decodes mRNA codon; Peptidyl site (P) — carries growing polypeptide chain (peptidyl-tRNA); Exit site (E) — holds deacylated tRNA before release. Peptide bond formation: peptidyl transferase (23S/28S rRNA ribozyme) transfers the polypeptide from P-site tRNA to A-site aminoacyl-tRNA.",
 "tags":["translation","ribosome"],"difficulty":"medium"},

{"text":"Aminoacyl-tRNA synthetases perform which critical function in translation?",
 "options":["Charge tRNAs with their correct amino acid, ensuring the genetic code is accurately interpreted","Decode the mRNA codon directly","Catalyze peptide bond formation","Release the polypeptide from the ribosome"],"correct":0,
 "explanation":"Each of the 20 aminoacyl-tRNA synthetases recognizes a specific amino acid and its cognate tRNA(s), charging the tRNA (forming aminoacyl-tRNA) in a two-step reaction (amino acid + ATP → aminoacyl-AMP + PPi; then transfer to tRNA 3'-OH). These enzymes are the true 'adaptors' of the genetic code — their fidelity determines translation accuracy.",
 "tags":["translation","aminoacyl-tRNA synthetase","genetic code"],"difficulty":"medium"},

{"text":"Stop codons (UAA, UAG, UGA) do not have corresponding tRNAs. Instead, translation terminates when:",
 "options":["Release factors (eRF1, eRF3) recognize stop codons and trigger peptidyl-tRNA hydrolysis","The ribosome falls off the mRNA spontaneously","A ribonuclease cleaves the mRNA","The 5' cap is removed, stalling the ribosome"],"correct":0,
 "explanation":"When a stop codon enters the A site, no aminoacyl-tRNA can decode it. Instead, eukaryotic release factors eRF1 (recognizes all three stop codons) and eRF3 (GTPase) bind the A site. eRF1 triggers peptidyl transferase to hydrolyze the ester bond linking the polypeptide to the P-site tRNA, releasing the polypeptide. Then the ribosome disassembles.",
 "tags":["translation","termination","release factors"],"difficulty":"medium"},

# ── GENETICS (25) ─────────────────────────────────────────────────────────
{"text":"In a monohybrid cross of two heterozygous individuals (Aa × Aa), the expected phenotype ratio is:",
 "options":["3 dominant : 1 recessive","1:1:1:1","1:2:1","All dominant"],"correct":0,
 "explanation":"Aa × Aa → 1/4 AA : 2/4 Aa : 1/4 aa (genotype 1:2:1). For a dominant trait, AA and Aa both express the dominant phenotype, giving 3/4 dominant : 1/4 recessive phenotype ratio. This is Mendel's law of segregation.",
 "tags":["genetics","Mendelian genetics"],"difficulty":"easy"},

{"text":"The probability that a child inherits an autosomal recessive disease when both parents are carriers (Aa × Aa) is:",
 "options":["1/4","1/2","1","3/4"],"correct":0,
 "explanation":"Carrier × carrier cross: 1/4 AA, 2/4 Aa, 1/4 aa. Only aa individuals are affected (1/4 probability). This is the basis of recessive disease genetics. With cystic fibrosis, for example, if both parents carry one CFTR mutation, each child has a 25% chance of having CF.",
 "tags":["genetics","autosomal recessive"],"difficulty":"easy"},

{"text":"Duchenne muscular dystrophy (DMD) is X-linked recessive. An unaffected carrier mother (XᴬXᵃ) and unaffected father (XᴬY) have children. What fraction of ALL children is expected to be affected?",
 "options":["1/4","1/2","1/8","All daughters"],"correct":0,
 "explanation":"Mother's gametes: 1/2 Xᴬ, 1/2 Xᵃ. Father's gametes: 1/2 Xᴬ, 1/2 Y. Possible outcomes: 1/4 XᴬXᴬ (unaffected daughter), 1/4 XᴬXᵃ (carrier daughter), 1/4 XᴬY (unaffected son), 1/4 XᵃY (affected son). Only 1/4 children are affected (all affected are male). 1/2 of sons are affected, but 1/4 of ALL children.",
 "tags":["genetics","X-linked recessive"],"difficulty":"medium"},

{"text":"Chromosomal non-disjunction during meiosis I in a female results in:",
 "options":["One secondary oocyte with both homologous chromosomes, one with neither","One secondary oocyte with an extra chromatid","Normal gametes with an extra chromosome","Two identical oocytes"],"correct":0,
 "explanation":"Meiosis I non-disjunction: homologous chromosomes fail to separate → one cell receives both chromosomes of a pair, the other receives neither. After meiosis II: two gametes have n+1 chromosomes (disomy), two have n-1 (nullisomy). Fertilization with normal sperm → trisomy (e.g., trisomy 21 Down syndrome) or monosomy. Meiosis II non-disjunction produces sister chromatid separation failure.",
 "tags":["genetics","non-disjunction","meiosis"],"difficulty":"medium"},

{"text":"Down syndrome (trisomy 21) most commonly arises from:",
 "options":["Maternal non-disjunction during meiosis I (frequency increases with maternal age)","Paternal non-disjunction","Translocation (Robertsonian) in ~4% of cases","De novo point mutation in the DYRK1A gene"],"correct":0,
 "explanation":"~95% of Down syndrome cases are standard trisomy 21 from maternal non-disjunction during meiosis I (rarely meiosis II). Risk increases dramatically with maternal age (from ~1/1500 at age 20 to ~1/30 at age 45). About 4% are Robertsonian translocations (chromosome 21 fused to chromosome 14); these have a higher recurrence risk. ~1% are mosaics.",
 "tags":["genetics","chromosomal abnormalities","Down syndrome"],"difficulty":"medium"},

{"text":"Turner syndrome (45,X) results from:",
 "options":["Monosomy X (missing one sex chromosome), most commonly from paternal non-disjunction","Trisomy X","Klinefelter syndrome (47,XXY)","Loss of an autosome"],"correct":0,
 "explanation":"Turner syndrome: 45,X (missing one sex chromosome). Features: short stature, webbed neck, shield chest, gonadal dysgenesis (streak ovaries, primary amenorrhea), coarctation of the aorta. Most commonly arises from paternal non-disjunction (losing the Y or X from the sperm). Despite having only one X, Barr body is absent (normal: females have one Barr body per extra X above 2 total).",
 "tags":["genetics","chromosomal abnormalities","Turner syndrome"],"difficulty":"medium"},

{"text":"Genomic imprinting means that:",
 "options":["Some genes are expressed from only one parental allele (maternal or paternal), determined by differential methylation","All genes from the father are expressed over maternal genes","Imprinted genes are deleted in the other parent","Only mitochondrial genes are imprinted"],"correct":0,
 "explanation":"Imprinted genes have parent-of-origin-specific expression determined by epigenetic marks (DNA methylation, histone modification) established in the germ line. IGF2 (insulin-like growth factor 2) is expressed from the paternal allele; H19 from the maternal. Prader-Willi syndrome (loss of paternal 15q11-q13) and Angelman syndrome (loss of maternal 15q11-q13) are classic imprinting disorders affecting the same chromosomal region.",
 "tags":["genetics","imprinting","epigenetics"],"difficulty":"hard"},

{"text":"What is the significance of Mendel's law of independent assortment?",
 "options":["Alleles of different genes on different chromosomes are inherited independently of one another","All alleles of a single gene are inherited together","Dominant alleles are always inherited over recessive alleles","Alleles are always inherited in the same combination as the parent"],"correct":0,
 "explanation":"Independent assortment (Mendel's second law): alleles at different loci (on different chromosomes or far apart on the same chromosome) are distributed to gametes independently. This is the basis for dihybrid crosses producing 9:3:3:1 ratios. Genes linked on the same chromosome violate this law unless separated by recombination.",
 "tags":["genetics","Mendel's laws","independent assortment"],"difficulty":"easy"},

{"text":"A female with X-linked red-green colorblindness (XᵃXᵃ) has children with a normal male (XᴬY). What fraction of their daughters will have colorblindness?",
 "options":["0 (all daughters are carriers, none are colorblind)","1/4","All daughters are colorblind","1/2"],"correct":0,
 "explanation":"Mother: XᵃXᵃ (affected). Father: XᴬY. All daughters receive Xᵃ from mother and Xᴬ from father → all daughters are XᴬXᵃ (carriers, not affected). All sons receive Xᵃ from mother and Y from father → all sons are XᵃY (affected). 0 daughters are colorblind in this cross.",
 "tags":["genetics","X-linked","colorblindness"],"difficulty":"medium"},

{"text":"Genetic linkage means that genes on the same chromosome:",
 "options":["Tend to be inherited together; recombination frequency between them reflects map distance (1 cM = 1% recombination)","Cannot recombine under any circumstances","Are always co-expressed in the same cell","Have identical allele frequencies in a population"],"correct":0,
 "explanation":"Linked genes violate independent assortment. Recombination (crossing over during meiosis I) creates new combinations (recombinant gametes). Recombination frequency is used to construct genetic maps: 1 centimorgan (cM) = 1% recombination frequency ≈ 1 Mb (roughly). Genes <50 cM apart are linked; genes >50 cM apart (or on different chromosomes) assort independently.",
 "tags":["genetics","genetic linkage","recombination"],"difficulty":"medium"},

# ── CELL BIOLOGY (25) ─────────────────────────────────────────────────────
{"text":"Which type of membrane transport allows Na+ to move from high concentration (outside) to low concentration (inside) the cell?",
 "options":["Facilitated diffusion via ion channels (passive)","Primary active transport","Secondary active transport","Endocytosis"],"correct":0,
 "explanation":"Na+ has high extracellular (~145 mM) and low intracellular (~12 mM) concentration, creating a large inward driving force. Na+ flows down its concentration AND electrical gradient (inside negative) via ion channels (facilitated diffusion) — no energy required. The Na+/K+ ATPase maintains this gradient using ATP (primary active transport).",
 "tags":["cell biology","membrane transport"],"difficulty":"easy"},

{"text":"The Na+/K+ ATPase pumps per cycle:",
 "options":["3 Na+ out and 2 K+ in, hydrolyzing 1 ATP","2 Na+ out and 3 K+ in","Equal amounts of Na+ and K+ in opposite directions","Only Na+ out, no K+ movement"],"correct":0,
 "explanation":"Na+/K+ ATPase (P-type ATPase) per cycle: 3 Na+ exported out + 2 K+ imported in + 1 ATP hydrolyzed. Net charge movement: 3(+) out and 2(+) in = net 1(+) charge out → electrogenic (contributes slightly to negative resting membrane potential). This pump accounts for ~20-30% of basal ATP consumption in cells.",
 "tags":["cell biology","Na/K ATPase"],"difficulty":"easy"},

{"text":"Tight junctions between epithelial cells primarily function to:",
 "options":["Create a paracellular seal that prevents movement of solutes between cells, maintaining epithelial polarity","Provide mechanical adhesion between cells","Facilitate rapid communication between adjacent cells","Anchor the cytoskeleton to the ECM"],"correct":0,
 "explanation":"Tight junctions (zonula occludens, made of claudins, occludins, ZO proteins) seal adjacent epithelial cells, preventing paracellular diffusion of ions and molecules. They also maintain membrane polarity by preventing lateral diffusion of membrane proteins between apical and basolateral domains. The 'fence' and 'gate' functions. Desmosomes provide mechanical strength; gap junctions allow communication; integrins anchor to ECM.",
 "tags":["cell biology","cell junctions","epithelium"],"difficulty":"medium"},

{"text":"The endosome-lysosome pathway processes materials taken up by endocytosis. Which enzyme activates lysosomal hydrolases by making the lumen acidic?",
 "options":["V-type H+ ATPase (vacuolar proton pump)","Na+/K+ ATPase","Carbonic anhydrase","Cytochrome c oxidase"],"correct":0,
 "explanation":"Lysosomes maintain pH ~4.5–5.0 through V-type H+ ATPase (uses ATP to pump H+ into the lumen). This acidic environment is required for the activity of ~50+ lysosomal hydrolases (proteases, lipases, nucleases, glycosidases). Chloroquine/hydroxychloroquine work by raising lysosomal pH, disrupting pathogen degradation.",
 "tags":["cell biology","lysosomes","vesicle trafficking"],"difficulty":"medium"},

{"text":"Receptor tyrosine kinases (RTKs) transmit signals by:",
 "options":["Ligand binding causes dimerization and autophosphorylation of tyrosine residues, creating docking sites for SH2 domain-containing signaling proteins","Ligand binding activates associated trimeric G proteins","Ligand-receptor complex translocates to the nucleus to act as transcription factor","Ligand stimulates adenylyl cyclase directly"],"correct":0,
 "explanation":"RTK signaling: ligand (e.g., EGF, PDGF, insulin) binds extracellular domain → RTK dimerizes → trans-autophosphorylation of tyrosine residues in the intracellular domain → phosphotyrosines serve as docking sites for SH2-domain proteins (Grb2, PI3K, PLC-gamma, Shp2) → activate downstream cascades (Ras-MAPK, PI3K-Akt, PLC-PKC). Mutated/amplified RTKs are oncogenes in cancer.",
 "tags":["cell biology","signal transduction","RTK"],"difficulty":"hard"},

{"text":"G-protein coupled receptors (GPCRs) signal through trimeric G proteins. In the inactive state, the G protein:",
 "options":["Has GDP bound to the alpha subunit and the alpha-beta-gamma trimer is intact","Has GTP bound to the alpha subunit and is dissociated","Is free of any nucleotide","Is constitutively active"],"correct":0,
 "explanation":"Inactive GPCR: trimeric G protein (alpha-beta-gamma) has GDP bound to alpha subunit. Ligand binds GPCR → conformational change → GPCR acts as GEF, causing GDP-GTP exchange in alpha subunit → alpha-GTP dissociates from beta-gamma → each activates downstream effectors (adenylyl cyclase for Gs, PLC for Gq, adenylyl cyclase inhibition for Gi). GTPase activity of alpha subunit returns to inactive GDP state.",
 "tags":["cell biology","GPCR","signal transduction"],"difficulty":"medium"},

{"text":"The cell cycle checkpoint at the G1/S boundary (restriction point) monitors:",
 "options":["DNA integrity and sufficient cell size/growth factors before committing to DNA replication","DNA replication completion and accurate chromosome alignment","Spindle assembly and chromosome attachment to kinetochores","Sister chromatid cohesion before anaphase"],"correct":0,
 "explanation":"The G1/S checkpoint (restriction point in mammals) is the key decision point for cell division. Rb (retinoblastoma protein) inhibits E2F transcription factors (needed for S-phase entry). When growth factor signaling drives cyclin D/CDK4,6 activity → phosphorylates Rb → releases E2F → S-phase entry. DNA damage activates p53 → p21 → inhibits CDK4,6/cyclin D → cell cycle arrest.",
 "tags":["cell biology","cell cycle","checkpoints"],"difficulty":"hard"},

{"text":"Mitosis produces daughter cells that are:",
 "options":["Genetically identical to the parent cell (diploid cells producing two diploid daughters)","Haploid with half the genetic material","Cells with random chromosome number","Cells that have undergone meiotic recombination"],"correct":0,
 "explanation":"Mitosis is cell division for growth, repair, and asexual reproduction. It produces two genetically identical daughter cells, each with the same chromosome number as the parent cell (2n → 2n in diploid organisms). Meiosis, by contrast, produces four haploid (n) cells with genetic variation from recombination and independent assortment, for sexual reproduction.",
 "tags":["cell biology","mitosis","cell division"],"difficulty":"easy"},

{"text":"During the S phase of interphase:",
 "options":["DNA is replicated (each chromosome is duplicated to form two sister chromatids joined at the centromere)","The cell prepares for division by synthesizing cyclins","Sister chromatids separate to opposite poles","Chromosomes condense and the spindle forms"],"correct":0,
 "explanation":"S (synthesis) phase: all chromosomal DNA is replicated semiconservatively, producing identical sister chromatids joined at the centromere by cohesin. DNA content doubles from 2C to 4C. After S: G2 phase (growth and preparation) → M phase (mitosis: prophase, prometaphase, metaphase, anaphase, telophase, cytokinesis).",
 "tags":["cell biology","cell cycle","DNA replication"],"difficulty":"easy"},

{"text":"The unfolded protein response (UPR) is triggered by:",
 "options":["Accumulation of misfolded proteins in the ER lumen, which activates sensors (IRE1, PERK, ATF6)","Misfolded proteins in the cytoplasm","Ribosome stalling during translation","Depletion of ER Ca2+ stores only"],"correct":0,
 "explanation":"ER stress: misfolded proteins accumulate in the ER → BiP (Hsp70 chaperone) is titrated away from UPR sensors IRE1, PERK, ATF6 → sensors activate → UPR responses: increased chaperone synthesis, reduced global translation, ERAD (ER-associated degradation). If UPR cannot resolve ER stress, apoptosis ensues (via CHOP transcription factor). UPR is implicated in diabetes, neurodegeneration, and cancer.",
 "tags":["cell biology","ER stress","unfolded protein response"],"difficulty":"hard"},

# ── PHYSIOLOGY (25) ────────────────────────────────────────────────────────
{"text":"The resting membrane potential of a neuron (~–70 mV) is primarily maintained by:",
 "options":["High intracellular K+ and leak channels; Na+/K+ ATPase maintains ion gradients","High intracellular Na+ and voltage-gated Na+ channels","Equal concentrations of all ions inside and outside","Chloride pumps actively removing Cl-"],"correct":0,
 "explanation":"The resting membrane potential is set mainly by K+ permeability (K+ leak channels) and the K+ electrochemical equilibrium (Nernst potential for K+ ≈ –90 mV). Selective permeability to K+ and impermeability to Na+ (at rest) creates the negative interior. Na+/K+ ATPase maintains the gradients over time but contributes little directly to the resting potential (~–3 mV from electrogenic pumping).",
 "tags":["neuroscience","membrane potential"],"difficulty":"medium"},

{"text":"An action potential is propagated along an axon because:",
 "options":["Depolarization at one node spreads current that depolarizes adjacent membrane, triggering sodium channel opening in the next segment","Neurotransmitter release propagates the signal","Gap junctions directly connect adjacent axon segments","Calcium influx triggers membrane depolarization sequentially"],"correct":0,
 "explanation":"Local circuit currents flow from the depolarized region (inside positive) to adjacent resting regions (inside negative). This depolarizes the adjacent membrane to threshold, triggering opening of voltage-gated Na+ channels and a new action potential. In myelinated axons (Schwann cells/oligodendrocytes), APs jump between nodes of Ranvier (saltatory conduction), greatly increasing speed.",
 "tags":["neuroscience","action potential","axon conduction"],"difficulty":"medium"},

{"text":"The Frank-Starling mechanism describes which cardiac property?",
 "options":["Stroke volume increases with increased preload (end-diastolic volume), due to increased myocardial fiber stretch and force generation","Heart rate is inversely proportional to stroke volume","The heart rate increases with increased arterial pressure","Cardiac output is fixed regardless of venous return"],"correct":0,
 "explanation":"Frank-Starling law: within limits, stroke volume is proportional to EDV (preload). Greater ventricular filling → more myofibril overlap → more forceful contraction (Starling mechanism). This is why both ventricles pump equal volumes over time. Increased afterload (SVR) at constant contractility decreases stroke volume. Heart failure reduces the Frank-Starling curve.",
 "tags":["cardiovascular physiology","Frank-Starling"],"difficulty":"medium"},

{"text":"Pulmonary surfactant, produced by type II pneumocytes, reduces surface tension in alveoli. Without it (as in neonatal respiratory distress syndrome):",
 "options":["Alveoli collapse (atelectasis) because surface tension increases as alveoli shrink, creating positive feedback of collapse","Alveoli over-inflate because pressure is increased","Surfactant removal increases O2 diffusion","Alveolar macrophages become hyperactive"],"correct":0,
 "explanation":"By Laplace's law, P = 2T/r; smaller alveoli would collapse unless surface tension (T) decreases as radius decreases. Surfactant (DPPC, dipalmitoylphosphatidylcholine) reduces T proportionally with radius, stabilizing small alveoli. Without surfactant (prematurity, RDS): high T in small alveoli → collapse → atelectasis → hypoxia. Treated with exogenous surfactant and CPAP.",
 "tags":["respiratory physiology","surfactant","lung mechanics"],"difficulty":"medium"},

{"text":"Which statement about glomerular filtration is correct?",
 "options":["GFR is determined by net filtration pressure = (Pcap – Pbowman) – oncotic pressure; GFR ≈ 120 mL/min","GFR is primarily regulated by hormones acting on tubular cells","Only small molecules < 1 kDa are filtered","The filtration barrier has no size selectivity"],"correct":0,
 "explanation":"GFR is driven by the net balance of Starling forces across the glomerular capillary: hydraulic pressure in capillary (Pgc, ~50 mmHg) minus Bowman's capsule pressure (~15 mmHg) minus plasma oncotic pressure (~30 mmHg) = ~5 mmHg net filtration. Normal GFR ≈ 120-125 mL/min. Regulated by afferent (dilates → increases GFR) and efferent (constricts → increases GFR) arteriolar tone.",
 "tags":["renal physiology","GFR","filtration"],"difficulty":"medium"},

{"text":"Aldosterone increases sodium reabsorption by acting on which segment of the nephron?",
 "options":["Principal cells of the collecting duct (and late distal tubule), increasing ENaC and Na+/K+ ATPase expression","Proximal tubule (majority of Na+ reabsorption)","Thick ascending limb via NKCC2","Loop of Henle via ADH-sensitive channels"],"correct":0,
 "explanation":"Aldosterone (from adrenal cortex, stimulated by angiotensin II, high K+) acts on principal cells in the collecting duct: binds cytosolic MR receptor → increases transcription of ENaC (epithelial Na+ channel) and Na+/K+ ATPase. Net: Na+ reabsorption, K+ secretion, water follows Na+. Spironolactone is an aldosterone receptor antagonist (K+-sparing diuretic).",
 "tags":["renal physiology","aldosterone","RAAS"],"difficulty":"medium"},

{"text":"Parathyroid hormone (PTH) is released in response to hypocalcemia. Its effects include all of the following EXCEPT:",
 "options":["Decreasing bone resorption (PTH increases bone resorption via osteoclast activation)","Increasing renal Ca2+ reabsorption","Increasing renal phosphate excretion","Activating renal 1-alpha-hydroxylase to produce calcitriol (active vitamin D)"],"correct":0,
 "explanation":"PTH actions on calcium homeostasis: (1) bone: stimulates osteoclast activity → Ca2+ and phosphate release from bone; (2) kidney: increases Ca2+ reabsorption in DCT, increases phosphate excretion, activates 1-alpha-hydroxylase → calcitriol production; (3) gut: indirectly increases Ca2+ absorption via calcitriol. PTH increases serum Ca2+, so answer A is false — PTH INCREASES bone resorption.",
 "tags":["endocrine physiology","PTH","calcium homeostasis"],"difficulty":"medium"},

{"text":"The oxyhemoglobin dissociation curve shifts to the RIGHT (decreased O2 affinity) with:",
 "options":["Increased temperature, increased pCO2, decreased pH, increased 2,3-BPG (Bohr effect)","Decreased temperature, decreased pCO2, increased pH","Fetal hemoglobin (HbF)","Carbon monoxide poisoning"],"correct":0,
 "explanation":"Right shift (decreased O2 affinity, more O2 delivery to tissues): increased T (fever/exercise), increased pCO2 (exercising tissues), decreased pH (Bohr effect), increased 2,3-BPG (altitude, anemia). Left shift (increased O2 affinity): decreased T, alkalosis, decreased 2,3-BPG, CO poisoning (CO shifts curve left AND occupies binding sites), HbF (lower 2,3-BPG affinity).",
 "tags":["respiratory physiology","hemoglobin","O2 dissociation curve"],"difficulty":"medium"},

{"text":"During exercise, increased CO2 and H+ in working muscles cause:",
 "options":["Right shift of oxyhemoglobin dissociation curve → increased O2 unloading to working muscles","Hemoglobin to bind more O2 (left shift)","Vasoconstriction in working muscles","Decreased cardiac output to spare oxygen"],"correct":0,
 "explanation":"This is the Bohr effect in action: CO2 from aerobic metabolism lowers muscle pH → hemoglobin's O2 affinity decreases (right shift) → more O2 released at a given PO2 → increased O2 delivery to the active tissue. Simultaneously, increased CO2 stimulates respiration (peripheral and central chemoreceptors), increasing ventilation and O2 delivery.",
 "tags":["respiratory physiology","Bohr effect","exercise physiology"],"difficulty":"medium"},

{"text":"The thyroid hormones T3 and T4 are synthesized from which amino acid?",
 "options":["Tyrosine (iodinated by thyroid peroxidase)","Tryptophan","Histidine","Phenylalanine"],"correct":0,
 "explanation":"Thyroid hormone synthesis: tyrosine residues in thyroglobulin are iodinated by thyroid peroxidase (TPO) → monoiodotyrosine (MIT) and diiodotyrosine (DIT) → coupling: DIT + DIT → T4 (thyroxine); DIT + MIT → T3 (triiodothyronine). T3 is the more potent form; T4 is converted to T3 in peripheral tissues by deiodinase. TPO is inhibited by propylthiouracil (PTU) and methimazole.",
 "tags":["endocrine physiology","thyroid hormones"],"difficulty":"medium"},
]

# shuffle correct answer positions for variety
import random; random.seed(42)
for q in Q:
    c = q["correct"]
    opts = q["options"][:]
    correct_text = opts[c]
    random.shuffle(opts)
    q["options"] = opts
    q["correct"] = opts.index(correct_text)

out = os.path.join(BASE, "data", "questions", "bb", "hq-bb.json")
with open(out, "w") as f:
    json.dump(Q, f, indent=2)
print(f"Wrote {len(Q)} BB questions to {out}")
