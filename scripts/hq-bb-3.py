#!/usr/bin/env python3
import json, os, random

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

Q = [
  # ── Microbiology – Bacteria ───────────────────────────────────────────────
  {
    "text": "Which component of gram-positive bacteria is targeted by beta-lactam antibiotics?",
    "options": ["Peptidoglycan cross-linking (transpeptidase/PBP)", "The outer membrane lipopolysaccharide", "30S ribosomal subunit", "DNA gyrase"],
    "correct": 0,
    "explanation": "Beta-lactams (penicillin, amoxicillin, cephalosporins) inhibit penicillin-binding proteins (transpeptidases) that cross-link peptidoglycan strands. Gram-positive bacteria have a thick peptidoglycan layer and no outer membrane, making them highly susceptible. LPS is the target of polymyxins; 30S is targeted by aminoglycosides; DNA gyrase by fluoroquinolones.",
    "tags": ["microbiology", "bacteria", "antibiotics"],
    "difficulty": "medium"
  },
  {
    "text": "Gram staining distinguishes bacteria primarily based on differences in:",
    "options": ["Cell wall peptidoglycan thickness and presence/absence of an outer membrane", "The presence or absence of ribosomes", "Capsule composition", "Flagella arrangement"],
    "correct": 0,
    "explanation": "Gram-positive bacteria retain crystal violet (stain purple) due to their thick peptidoglycan layer; gram-negative bacteria lose it during decolorization because their thin peptidoglycan is sandwiched between inner and outer membranes, and counterstain pink with safranin. The outer membrane with LPS is unique to gram-negatives.",
    "tags": ["microbiology", "bacteria", "gram-stain"],
    "difficulty": "easy"
  },
  {
    "text": "Which process transfers genetic material directly through cell-to-cell contact via a pilus?",
    "options": ["Conjugation", "Transformation", "Transduction", "Sporulation"],
    "correct": 0,
    "explanation": "Conjugation requires physical contact between bacteria via the sex pilus (F-pilus), through which plasmid or chromosomal DNA is transferred. Transformation involves uptake of free DNA from the environment. Transduction uses bacteriophage as a vector. Sporulation is endospore formation, not gene transfer.",
    "tags": ["microbiology", "bacteria", "genetics", "conjugation"],
    "difficulty": "easy"
  },
  {
    "text": "A bacterium incorporates a fragment of donor DNA from the environment into its chromosome. This process is called:",
    "options": ["Transformation", "Transduction", "Conjugation", "Transposition"],
    "correct": 0,
    "explanation": "Transformation is the uptake and incorporation of exogenous DNA from the environment by competent bacteria (e.g., Streptococcus pneumoniae). This was first demonstrated by Griffith and the molecular basis identified by Avery et al. Transduction uses phage; conjugation uses pili; transposition moves genetic elements within/between chromosomes.",
    "tags": ["microbiology", "bacteria", "genetics", "transformation"],
    "difficulty": "easy"
  },
  {
    "text": "In generalized transduction, a bacteriophage accidentally packages:",
    "options": ["Random fragments of host bacterial DNA instead of phage DNA", "Only phage DNA from the host", "Plasmids that the bacterium carries", "RNA from the bacterial host"],
    "correct": 0,
    "explanation": "In generalized transduction, the phage accidentally packages random pieces of host chromosomal DNA during assembly. When the phage infects a new host, this donor DNA can recombine with the recipient's chromosome. In specialized transduction, only specific genes adjacent to the phage integration site are transferred.",
    "tags": ["microbiology", "bacteria", "genetics", "transduction"],
    "difficulty": "medium"
  },
  {
    "text": "Aminoglycoside antibiotics (e.g., gentamicin) kill bacteria primarily by:",
    "options": ["Binding the 30S ribosomal subunit, causing misreading of mRNA and defective protein synthesis", "Inhibiting RNA polymerase", "Disrupting the cell membrane", "Blocking folate synthesis"],
    "correct": 0,
    "explanation": "Aminoglycosides bind the 30S ribosomal subunit (specifically 16S rRNA), causing misreading of mRNA codons, which leads to incorporation of wrong amino acids and production of abnormal proteins that disrupt the cell membrane, causing bactericidal effects. Rifampin inhibits RNA polymerase; polymyxins disrupt membranes; sulfonamides block folate.",
    "tags": ["microbiology", "bacteria", "antibiotics", "aminoglycosides"],
    "difficulty": "medium"
  },
  {
    "text": "Fluoroquinolone antibiotics (e.g., ciprofloxacin) target:",
    "options": ["DNA gyrase (topoisomerase II) and topoisomerase IV, preventing DNA replication", "The 50S ribosomal subunit", "Cell wall synthesis", "Dihydrofolate reductase"],
    "correct": 0,
    "explanation": "Fluoroquinolones inhibit DNA gyrase (topoisomerase II) in gram-negative bacteria and topoisomerase IV in gram-positive bacteria. These enzymes relieve supercoiling ahead of the replication fork. Without them, DNA replication stalls and the bacteria cannot divide. This explains their bactericidal, broad-spectrum activity.",
    "tags": ["microbiology", "bacteria", "antibiotics", "fluoroquinolones"],
    "difficulty": "medium"
  },
  {
    "text": "Quorum sensing in bacteria allows population-density-dependent regulation of gene expression. Which molecule typically mediates this in gram-negative bacteria?",
    "options": ["N-acyl homoserine lactones (AHLs)", "Peptide pheromones", "cAMP", "Cyclic-di-GMP only"],
    "correct": 0,
    "explanation": "Gram-negative bacteria primarily use N-acyl homoserine lactones (AHLs) as autoinducers for quorum sensing. At high cell density, AHL accumulates and binds transcription factors to activate genes for biofilm formation, virulence factor production, and bioluminescence (Vibrio fischeri). Gram-positive bacteria typically use peptide pheromones.",
    "tags": ["microbiology", "bacteria", "quorum-sensing"],
    "difficulty": "hard"
  },
  {
    "text": "Endospores formed by Bacillus and Clostridium species are notable because they:",
    "options": ["Are dormant, heat-resistant structures that can survive boiling water for hours", "Actively replicate inside host cells", "Are destroyed by standard alcohol-based sanitizers", "Contain membrane-bound organelles"],
    "correct": 0,
    "explanation": "Bacterial endospores (formed by Bacillus and Clostridium) are metabolically dormant and extremely resistant to heat, UV radiation, chemicals, and desiccation. Autoclaving at 121°C for 15–20 minutes (not just boiling) is required to kill them. They lack membrane-bound organelles (prokaryotic). Alcohol sanitizers are ineffective against spores.",
    "tags": ["microbiology", "bacteria", "endospores"],
    "difficulty": "medium"
  },
  {
    "text": "Which bacterial structure protects against phagocytosis and is composed of polysaccharides in most pathogenic bacteria?",
    "options": ["Capsule", "Fimbriae", "Pili", "Peptidoglycan cell wall"],
    "correct": 0,
    "explanation": "The bacterial capsule (polysaccharide in most pathogens like S. pneumoniae, Haemophilus influenzae, N. meningitidis) inhibits phagocytosis by preventing opsonization and complement activation. Fimbriae and pili mediate adhesion to host cells. Peptidoglycan is structural. Encapsulated bacteria are more virulent; capsular vaccines are highly effective.",
    "tags": ["microbiology", "bacteria", "capsule", "virulence"],
    "difficulty": "medium"
  },
  {
    "text": "Tetracyclines work by binding the 30S ribosomal subunit to block:",
    "options": ["Aminoacyl-tRNA binding to the A site", "Peptide bond formation at the peptidyl transferase center", "Translocation of the ribosome along mRNA", "Release factor binding at the stop codon"],
    "correct": 0,
    "explanation": "Tetracyclines bind the 30S ribosomal subunit and block aminoacyl-tRNA from entering the A site, preventing elongation of the polypeptide chain. This is bacteriostatic. Chloramphenicol inhibits peptidyl transferase (50S); fusidic acid blocks translocation; no clinically used drug blocks release factor binding.",
    "tags": ["microbiology", "bacteria", "antibiotics", "tetracycline"],
    "difficulty": "hard"
  },
  {
    "text": "Rifampin treats tuberculosis by inhibiting:",
    "options": ["Bacterial RNA polymerase (beta subunit)", "Bacterial DNA polymerase III", "30S ribosomal subunit", "Cell wall synthesis"],
    "correct": 0,
    "explanation": "Rifampin (rifampicin) inhibits the beta subunit of bacterial DNA-dependent RNA polymerase, blocking transcription initiation. It is highly selective because mammalian RNA polymerases differ structurally. It is a key component of TB treatment and must be combined with other drugs (isoniazid, pyrazinamide, ethambutol) to prevent resistance.",
    "tags": ["microbiology", "bacteria", "antibiotics", "rifampin"],
    "difficulty": "medium"
  },
  # ── Microbiology – Viruses ─────────────────────────────────────────────────
  {
    "text": "According to the Baltimore classification, which class of virus uses reverse transcriptase to convert its RNA genome into DNA?",
    "options": ["Class VI retroviruses (ssRNA-RT)", "Class III dsRNA viruses", "Class IV positive-sense ssRNA viruses", "Class I dsDNA viruses"],
    "correct": 0,
    "explanation": "Baltimore Class VI retroviruses (e.g., HIV) have a positive-sense ssRNA genome that is reverse-transcribed into dsDNA by reverse transcriptase, then integrated into the host genome as a provirus. Class III (dsRNA), Class IV (positive ssRNA like hepatitis C), and Class I (dsDNA like herpesviruses) all use different replication strategies.",
    "tags": ["microbiology", "viruses", "baltimore", "retroviruses"],
    "difficulty": "medium"
  },
  {
    "text": "During the HIV replication cycle, which enzyme integrates the viral dsDNA into the host cell's chromosome?",
    "options": ["Integrase", "Reverse transcriptase", "Protease", "Neuraminidase"],
    "correct": 0,
    "explanation": "HIV integrase catalyzes the insertion of viral dsDNA (made by reverse transcriptase) into the host genome, creating a provirus. Reverse transcriptase makes dsDNA from RNA; protease cleaves viral polyproteins into functional proteins during viral maturation; neuraminidase is an influenza enzyme that releases virions from host cells.",
    "tags": ["microbiology", "viruses", "HIV", "integrase"],
    "difficulty": "medium"
  },
  {
    "text": "HIV protease inhibitors work by preventing:",
    "options": ["Cleavage of polyprotein precursors into functional viral proteins", "Reverse transcription of viral RNA", "Integration of viral DNA into the host genome", "Attachment of HIV to CD4+ T cells"],
    "correct": 0,
    "explanation": "HIV protease cleaves the Gag and Gag-Pol polyproteins into functional structural proteins (matrix, capsid, nucleocapsid) and enzymes (protease, reverse transcriptase, integrase). Without cleavage, immature, non-infectious virions are produced. Protease inhibitors (ritonavir, lopinavir) are key components of HAART.",
    "tags": ["microbiology", "viruses", "HIV", "protease-inhibitor"],
    "difficulty": "medium"
  },
  {
    "text": "In the bacteriophage lytic cycle, which event occurs that does NOT occur in the lysogenic cycle?",
    "options": ["Host cell lysis and release of new phage particles", "Phage DNA integration into the host chromosome", "Phage DNA replication within the host", "Expression of phage genes"],
    "correct": 0,
    "explanation": "The lytic cycle culminates in host cell lysis: phage DNA is replicated, phage proteins are made, new phages are assembled, and the cell bursts to release hundreds of phage particles. In the lysogenic cycle, phage DNA integrates as a prophage and replicates with the host chromosome without killing the cell. Integration is unique to lysogeny.",
    "tags": ["microbiology", "viruses", "bacteriophage", "lytic-lysogenic"],
    "difficulty": "easy"
  },
  {
    "text": "Prions cause disease by inducing the conversion of normal cellular prion protein (PrP^C) into:",
    "options": ["An abnormally folded, protease-resistant isoform (PrP^Sc) that accumulates in neurons", "A hyperphosphorylated form that activates apoptosis", "A truncated form that activates innate immunity", "A glycosylated form that mimics a viral capsid protein"],
    "correct": 0,
    "explanation": "Prions are misfolded proteins (PrP^Sc) that act as templates to convert normal PrP^C into the disease-causing isoform. PrP^Sc is protease-resistant, accumulates in the brain, and causes spongiform encephalopathy (Creutzfeldt-Jakob disease, scrapie, BSE). Prions contain no nucleic acid, making them unique infectious agents.",
    "tags": ["microbiology", "viruses", "prions"],
    "difficulty": "medium"
  },
  {
    "text": "The viral envelope is derived from:",
    "options": ["The host cell membrane acquired during budding", "The viral capsid protein alone", "De novo synthesis by viral enzymes", "The endoplasmic reticulum only"],
    "correct": 0,
    "explanation": "Enveloped viruses (HIV, influenza, herpes) acquire their lipid bilayer envelope from the host cell membrane (plasma membrane or ER/Golgi) as they bud out. Viral glycoproteins are embedded in this envelope and mediate attachment. Non-enveloped (naked) viruses (adenovirus, poliovirus) are released by cell lysis and have only a protein capsid.",
    "tags": ["microbiology", "viruses", "envelope"],
    "difficulty": "easy"
  },
  {
    "text": "Neuraminidase inhibitors (oseltamivir/Tamiflu) treat influenza by preventing:",
    "options": ["Progeny virions from being released from infected host cells", "Viral hemagglutinin from attaching to sialic acid receptors", "Viral RNA polymerase from replicating the genome", "Viral protein synthesis in host ribosomes"],
    "correct": 0,
    "explanation": "Influenza neuraminidase cleaves sialic acid on host cell surfaces to release budding virions. Oseltamivir inhibits neuraminidase, trapping new virions attached to the host cell surface and limiting infection spread. Hemagglutinin mediates initial attachment but is not the target of neuraminidase inhibitors.",
    "tags": ["microbiology", "viruses", "influenza", "neuraminidase"],
    "difficulty": "medium"
  },
  {
    "text": "Which feature distinguishes positive-sense ssRNA viruses from negative-sense ssRNA viruses?",
    "options": ["Positive-sense RNA can be directly translated by host ribosomes; negative-sense RNA must first be converted to positive-sense by viral RNA-dependent RNA polymerase", "Positive-sense viruses have DNA as an intermediate; negative-sense do not", "Positive-sense viruses always have an envelope; negative-sense do not", "Negative-sense RNA is translated directly; positive-sense requires processing"],
    "correct": 0,
    "explanation": "Positive-sense ssRNA (e.g., poliovirus, hepatitis C, coronaviruses) has the same sequence as mRNA and can be directly translated by host ribosomes upon cell entry. Negative-sense ssRNA (e.g., influenza, rabies, Ebola) is complementary to mRNA and must first be transcribed into positive-sense RNA by a virion-packaged RNA-dependent RNA polymerase.",
    "tags": ["microbiology", "viruses", "ssRNA", "baltimore"],
    "difficulty": "hard"
  },
  {
    "text": "A patient is found to have a retrovirus integrated into CD4+ T cells. Which drug class would interfere with the step where viral RNA is converted to DNA?",
    "options": ["Nucleoside/nucleotide reverse transcriptase inhibitors (NRTIs)", "Protease inhibitors", "Integrase strand transfer inhibitors (INSTIs)", "CCR5 antagonists"],
    "correct": 0,
    "explanation": "NRTIs (zidovudine/AZT, tenofovir) are nucleoside/nucleotide analogs that are incorporated by reverse transcriptase into the growing DNA chain and terminate elongation (chain terminators). This blocks conversion of viral RNA into dsDNA. Protease inhibitors block polyprotein cleavage; INSTIs block integration; CCR5 antagonists block co-receptor attachment.",
    "tags": ["microbiology", "viruses", "HIV", "NRTI"],
    "difficulty": "medium"
  },
  # ── Population Genetics ────────────────────────────────────────────────────
  {
    "text": "In a population at Hardy-Weinberg equilibrium, if the frequency of the recessive allele (q) is 0.3, what is the expected frequency of heterozygotes?",
    "options": ["0.42", "0.09", "0.49", "0.21"],
    "correct": 0,
    "explanation": "If q = 0.3, then p = 1 - 0.3 = 0.7. Heterozygote frequency = 2pq = 2(0.7)(0.3) = 0.42. Homozygous dominant = p² = 0.49; homozygous recessive = q² = 0.09. The HWE equation is p² + 2pq + q² = 1.",
    "tags": ["genetics", "population-genetics", "hardy-weinberg"],
    "difficulty": "medium"
  },
  {
    "text": "Hardy-Weinberg equilibrium requires which of the following conditions?",
    "options": ["Large population, random mating, no mutation, no gene flow, no natural selection", "Small population with geographic isolation", "High mutation rate with random mating", "Positive assortative mating with no drift"],
    "correct": 0,
    "explanation": "HWE is maintained only when all five conditions are met: (1) large population (no genetic drift), (2) random mating (no assortative mating), (3) no mutation, (4) no gene flow (isolated population), (5) no natural selection. Violation of any condition causes allele frequencies to change across generations.",
    "tags": ["genetics", "population-genetics", "hardy-weinberg"],
    "difficulty": "easy"
  },
  {
    "text": "A severe reduction in population size due to a catastrophic event, followed by recovery from a few survivors, is called the:",
    "options": ["Bottleneck effect", "Founder effect", "Gene flow", "Frequency-dependent selection"],
    "correct": 0,
    "explanation": "The bottleneck effect occurs when population size is dramatically reduced by a random catastrophic event (disease, earthquake), leading to reduced genetic diversity in survivors. The founder effect is similar but occurs when a small subgroup colonizes a new area. Both cause genetic drift but have different origins and sociological contexts.",
    "tags": ["genetics", "population-genetics", "bottleneck"],
    "difficulty": "easy"
  },
  {
    "text": "In directional selection, the population's trait distribution shifts because:",
    "options": ["One extreme phenotype has higher fitness, so alleles underlying it increase in frequency", "Both extreme phenotypes have higher fitness than the intermediate", "The intermediate phenotype has higher fitness than either extreme", "Allele frequencies change randomly with no fitness difference"],
    "correct": 0,
    "explanation": "Directional selection favors one extreme phenotype (e.g., darker moths in polluted environments), causing a shift in the mean trait value over generations. Disruptive selection favors both extremes (can lead to speciation). Stabilizing selection favors intermediates (e.g., birth weight). Genetic drift involves random, not fitness-driven, changes.",
    "tags": ["genetics", "population-genetics", "natural-selection"],
    "difficulty": "easy"
  },
  {
    "text": "If a recessive lethal allele has a frequency of 0.01, what fraction of the population carries it (is heterozygous), assuming HWE?",
    "options": ["~0.0198 (about 2%)", "~0.0001 (0.01%)", "~0.99 (99%)", "~0.01 (1%)"],
    "correct": 0,
    "explanation": "With q = 0.01, p ≈ 0.99, heterozygote frequency = 2pq = 2(0.99)(0.01) ≈ 0.0198, or ~2%. This illustrates why recessive lethal alleles are not quickly eliminated — most copies hide in heterozygous carriers. Homozygous recessive (affected) = q² = 0.0001 (only 1 in 10,000).",
    "tags": ["genetics", "population-genetics", "hardy-weinberg"],
    "difficulty": "hard"
  },
  {
    "text": "Genetic drift has the GREATEST effect on allele frequencies in:",
    "options": ["Small, isolated populations", "Large, outbred populations", "Populations under strong directional selection", "Populations with high gene flow from neighboring groups"],
    "correct": 0,
    "explanation": "Genetic drift (random changes in allele frequency) has greater impact in small populations because chance sampling errors are proportionally larger. In large populations, random fluctuations average out. Gene flow and strong selection override drift in large populations. Isolation prevents gene flow, compounding the effect.",
    "tags": ["genetics", "population-genetics", "genetic-drift"],
    "difficulty": "easy"
  },
  {
    "text": "Frequency-dependent selection maintains polymorphism when:",
    "options": ["Rare alleles have higher fitness than common alleles (negative frequency-dependence)", "Common alleles always have higher fitness regardless of frequency", "Fitness is constant regardless of allele frequency", "All alleles have equal fitness at any frequency"],
    "correct": 0,
    "explanation": "Negative frequency-dependent selection (e.g., MHC diversity, prey search image avoidance) gives rare alleles a fitness advantage — when they become common, their advantage diminishes. This self-correcting mechanism maintains multiple alleles at stable intermediate frequencies, contributing to polymorphism in natural populations.",
    "tags": ["genetics", "population-genetics", "frequency-dependent-selection"],
    "difficulty": "hard"
  },
  # ── Advanced Metabolism – Gluconeogenesis & Integration ────────────────────
  {
    "text": "During fasting, the liver performs gluconeogenesis. Which enzyme converts pyruvate to oxaloacetate as the first committed step?",
    "options": ["Pyruvate carboxylase", "Pyruvate kinase", "PEP carboxykinase (PEPCK)", "Fructose-1,6-bisphosphatase"],
    "correct": 0,
    "explanation": "Pyruvate carboxylase (mitochondrial, requires biotin and acetyl-CoA as allosteric activator) converts pyruvate + CO₂ + ATP → oxaloacetate. OAA is then converted by PEPCK to PEP. Pyruvate kinase runs the reverse reaction in glycolysis (PEP → pyruvate); fructose-1,6-bisphosphatase bypasses PFK-1; PEPCK acts after pyruvate carboxylase.",
    "tags": ["metabolism", "gluconeogenesis", "pyruvate-carboxylase"],
    "difficulty": "medium"
  },
  {
    "text": "The Cori cycle shuttles lactate from exercising muscle to the liver. In the liver, lactate is converted back to glucose via:",
    "options": ["Gluconeogenesis using lactate → pyruvate → OAA → PEP → glucose", "Glycogenolysis releasing glucose-1-phosphate", "Direct phosphorylation of lactate to glucose-6-phosphate", "Beta-oxidation to acetyl-CoA followed by gluconeogenesis"],
    "correct": 0,
    "explanation": "In the Cori cycle, lactate (produced by anaerobic glycolysis in muscle) is released into blood, taken up by the liver, and converted to pyruvate by lactate dehydrogenase, then to oxaloacetate by pyruvate carboxylase, through gluconeogenesis to glucose-6-phosphate and finally glucose. Mammals cannot perform net gluconeogenesis from acetyl-CoA.",
    "tags": ["metabolism", "gluconeogenesis", "cori-cycle"],
    "difficulty": "medium"
  },
  {
    "text": "Glucagon stimulates hepatic gluconeogenesis primarily by:",
    "options": ["Activating cAMP-PKA signaling, which phosphorylates and inactivates pyruvate kinase while inducing PEPCK expression", "Directly activating pyruvate carboxylase by binding to it", "Inhibiting fructose-2,6-bisphosphate production, relieving inhibition of fructose-1,6-bisphosphatase", "Both A and C are correct"],
    "correct": 3,
    "explanation": "Glucagon (via cAMP-PKA) has dual effects: (1) phosphorylates and inactivates pyruvate kinase (blocking glycolysis), and (2) activates phosphofructokinase-2 kinase domain to decrease fructose-2,6-bisphosphate, relieving inhibition of fructose-1,6-bisphosphatase and activating gluconeogenesis. Glucagon also induces PEPCK transcription. Both A and C are correct.",
    "tags": ["metabolism", "gluconeogenesis", "glucagon", "regulation"],
    "difficulty": "hard"
  },
  {
    "text": "Which metabolic state is characterized by the liver producing ketone bodies from fatty acid-derived acetyl-CoA?",
    "options": ["Prolonged fasting/starvation when oxaloacetate is depleted for gluconeogenesis", "Well-fed state with high insulin", "After a carbohydrate-rich meal", "During intense aerobic exercise with ample glucose"],
    "correct": 0,
    "explanation": "Ketone bodies (acetoacetate, beta-hydroxybutyrate, acetone) are produced in starvation when: (1) glucagon drives oxaloacetate toward gluconeogenesis, depleting it for the TCA cycle, and (2) fatty acid beta-oxidation generates excess acetyl-CoA that cannot enter TCA. Ketones are exported as fuel for brain and muscle. High insulin inhibits ketogenesis.",
    "tags": ["metabolism", "ketogenesis", "starvation"],
    "difficulty": "medium"
  },
  {
    "text": "The glucose-alanine cycle parallels the Cori cycle but uses alanine instead of lactate. What is the role of the liver in this cycle?",
    "options": ["Convert alanine to pyruvate (transamination), then use pyruvate for gluconeogenesis, releasing urea from the nitrogen", "Convert alanine directly to glucose without transamination", "Export alanine to the brain as a fuel source", "Use alanine to synthesize fatty acids"],
    "correct": 0,
    "explanation": "In the glucose-alanine cycle, muscle transaminases convert pyruvate + glutamate → alanine + alpha-ketoglutarate. Alanine is exported to the liver, where ALT converts it back to pyruvate (+ glutamate). Pyruvate enters gluconeogenesis; the amino group enters the urea cycle. This cycle transports both carbon (as glucose) and nitrogen (as urea) between muscle and liver.",
    "tags": ["metabolism", "gluconeogenesis", "alanine-cycle"],
    "difficulty": "hard"
  },
  # ── Pentose Phosphate Pathway & Others ────────────────────────────────────
  {
    "text": "The primary product of the oxidative phase of the pentose phosphate pathway that is critical for antioxidant defense is:",
    "options": ["NADPH", "NADH", "ATP", "Ribose-5-phosphate"],
    "correct": 0,
    "explanation": "The oxidative phase of the PPP converts glucose-6-phosphate to ribulose-5-phosphate and generates 2 NADPH per molecule. NADPH is essential for: (1) reducing oxidized glutathione (glutathione reductase), protecting RBCs from oxidative damage; (2) fatty acid synthesis; (3) cholesterol synthesis; (4) NADPH oxidase in immune cells. NADH fuels the ETC; ATP is from glycolysis/TCA.",
    "tags": ["metabolism", "pentose-phosphate-pathway", "NADPH"],
    "difficulty": "medium"
  },
  {
    "text": "G6PD deficiency causes hemolytic anemia triggered by certain foods (fava beans) and drugs (primaquine) because:",
    "options": ["Without G6PD, RBCs cannot generate NADPH to regenerate glutathione, leaving them vulnerable to oxidative damage", "RBCs cannot perform glycolysis without G6PD", "G6PD is required for hemoglobin synthesis", "Without G6PD, RBCs cannot synthesize ATP via the ETC"],
    "correct": 0,
    "explanation": "G6PD (glucose-6-phosphate dehydrogenase) catalyzes the first step of the PPP, producing NADPH. Mature RBCs lack mitochondria and depend entirely on the PPP for NADPH. Without NADPH, glutathione cannot be regenerated, H₂O₂ accumulates, hemoglobin oxidizes to methemoglobin, and Heinz bodies form — causing hemolysis. RBCs do perform glycolysis; G6PD is not in that pathway.",
    "tags": ["metabolism", "pentose-phosphate-pathway", "G6PD", "hemolytic-anemia"],
    "difficulty": "medium"
  },
  {
    "text": "Glycogen synthase adds glucose residues to a growing glycogen chain using which activated glucose precursor?",
    "options": ["UDP-glucose", "ADP-glucose", "Glucose-1-phosphate directly", "Glucose-6-phosphate directly"],
    "correct": 0,
    "explanation": "Glycogen synthase transfers glucose from UDP-glucose (uridine diphosphate glucose) to the non-reducing end of a growing glycogen chain via an alpha-1,4 glycosidic bond. The branching enzyme creates alpha-1,6 branches. ADP-glucose is used by plants/bacteria for starch/glycogen synthesis; animals use UDP-glucose.",
    "tags": ["metabolism", "glycogen", "glycogen-synthase"],
    "difficulty": "medium"
  },
  {
    "text": "HMG-CoA reductase is the rate-limiting enzyme of cholesterol synthesis. Statins work by:",
    "options": ["Competitively inhibiting HMG-CoA reductase, reducing conversion of HMG-CoA to mevalonate", "Blocking PCSK9 to upregulate LDL receptors", "Inhibiting cholesterol absorption in the intestine", "Activating ApoE-mediated cholesterol clearance"],
    "correct": 0,
    "explanation": "Statins (lovastatin, atorvastatin) are structural analogs of HMG-CoA that competitively inhibit HMG-CoA reductase, blocking the conversion of HMG-CoA → mevalonate (the committed, rate-limiting step). This reduces intracellular cholesterol, upregulates LDL receptors (secondary effect), and lowers plasma LDL. PCSK9 inhibitors are a different drug class.",
    "tags": ["metabolism", "cholesterol", "HMG-CoA-reductase", "statins"],
    "difficulty": "medium"
  },
  {
    "text": "Acetyl-CoA carboxylase (ACC) catalyzes the first committed step in fatty acid synthesis. Its product is:",
    "options": ["Malonyl-CoA", "Acetoacetyl-CoA", "Palmitoyl-CoA", "HMG-CoA"],
    "correct": 0,
    "explanation": "ACC uses biotin to carboxylate acetyl-CoA to malonyl-CoA using ATP and CO₂ (ACC: acetyl-CoA + CO₂ + ATP → malonyl-CoA + ADP + Pi). Malonyl-CoA is the 2-carbon donor for fatty acid elongation by FAS. Malonyl-CoA also inhibits carnitine acyltransferase I, preventing fatty acid import into mitochondria — preventing simultaneous synthesis and oxidation.",
    "tags": ["metabolism", "fatty-acid-synthesis", "ACC", "malonyl-CoA"],
    "difficulty": "medium"
  },
  # ── Muscle Physiology ──────────────────────────────────────────────────────
  {
    "text": "During skeletal muscle contraction, Ca²⁺ binds to which protein to allow myosin-actin interaction?",
    "options": ["Troponin C", "Tropomyosin", "Troponin I", "Titin"],
    "correct": 0,
    "explanation": "Ca²⁺ released from the sarcoplasmic reticulum binds troponin C (the Ca²⁺-binding subunit of the troponin complex). This causes a conformational change that moves tropomyosin away from myosin-binding sites on actin, allowing cross-bridge formation. Troponin I normally inhibits myosin binding; titin is a structural protein maintaining sarcomere elasticity.",
    "tags": ["physiology", "muscle", "excitation-contraction-coupling"],
    "difficulty": "medium"
  },
  {
    "text": "The I-band of a sarcomere contains:",
    "options": ["Only thin (actin) filaments with no myosin overlap", "Only thick (myosin) filaments", "Both actin and myosin filaments overlapping", "The M-line and thick filament tails only"],
    "correct": 0,
    "explanation": "The I-band (isotropic) consists of actin (thin) filaments from two adjacent sarcomeres with no myosin overlap, flanking the Z-lines. During contraction, I-bands shorten as thin filaments slide over thick filaments, reducing overlap. The A-band (anisotropic) contains the full length of myosin filaments; the H-zone is myosin only (no actin); the M-line anchors thick filaments.",
    "tags": ["physiology", "muscle", "sarcomere"],
    "difficulty": "medium"
  },
  {
    "text": "Rigor mortis occurs after death because:",
    "options": ["ATP depletion prevents myosin cross-bridges from detaching from actin, locking muscles in a contracted state", "Ca²⁺ floods into muscle cells and permanently activates troponin", "Glycogen depletion prevents new muscle contractions", "Acetylcholine accumulates at the NMJ causing persistent depolarization"],
    "correct": 0,
    "explanation": "Myosin detaches from actin only when ATP binds to myosin (completing the cross-bridge cycle). After death, ATP production ceases; existing ATP is consumed but new ATP cannot be made. Without ATP, myosin remains tightly bound to actin (rigor state). Rigor mortis resolves 24–48 hours post-mortem as proteolytic enzymes degrade the cross-bridges.",
    "tags": ["physiology", "muscle", "rigor-mortis"],
    "difficulty": "easy"
  },
  {
    "text": "Slow-twitch (Type I) muscle fibers differ from fast-twitch (Type II) fibers in that they:",
    "options": ["Are more fatigue-resistant, rely on oxidative phosphorylation, and contain more mitochondria and myoglobin", "Contract faster and generate more peak force", "Rely primarily on glycolysis for ATP", "Lack troponin and tropomyosin regulation"],
    "correct": 0,
    "explanation": "Type I (slow-twitch, red) fibers are fatigue-resistant, aerobic, rich in mitochondria and myoglobin (giving red color), and suited for endurance. Type II (fast-twitch, white) fibers contract faster with greater peak force but fatigue quickly, relying on glycolysis (Type IIb) or mixed metabolism (Type IIa). All skeletal muscle uses troponin/tropomyosin regulation.",
    "tags": ["physiology", "muscle", "fiber-types"],
    "difficulty": "easy"
  },
  {
    "text": "The sliding filament theory of muscle contraction states that during shortening:",
    "options": ["Actin and myosin filament lengths remain constant while the sarcomere shortens due to increased filament overlap", "Myosin filaments shorten by folding upon themselves", "Actin filaments shorten by depolymerizing at the Z-lines", "Both actin and myosin shorten proportionally"],
    "correct": 0,
    "explanation": "In the sliding filament model, neither actin (thin) nor myosin (thick) filaments change in length. Instead, myosin cross-bridges walk along actin, pulling thin filaments toward the center of the sarcomere (M-line), increasing overlap. The A-band width is constant; I-band and H-zone shorten. This was demonstrated by Huxley and Hanson using electron microscopy.",
    "tags": ["physiology", "muscle", "sliding-filament"],
    "difficulty": "easy"
  },
  # ── GI Physiology & Digestion ──────────────────────────────────────────────
  {
    "text": "Cholecystokinin (CCK) is secreted by I-cells in the duodenum in response to fats and proteins. Its primary functions are:",
    "options": ["Stimulate pancreatic enzyme secretion and gallbladder contraction", "Stimulate gastric acid secretion and increase stomach motility", "Inhibit pancreatic enzyme secretion and stimulate HCO₃⁻ release", "Stimulate gastric emptying and absorb fat-soluble vitamins"],
    "correct": 0,
    "explanation": "CCK is released in response to dietary fats and proteins entering the duodenum. It stimulates: (1) the pancreas to secrete digestive enzymes (lipase, protease, amylase) and (2) the gallbladder to contract and release bile. CCK also slows gastric emptying and inhibits gastric acid (via somatostatin). Secretin (not CCK) stimulates pancreatic bicarbonate.",
    "tags": ["physiology", "GI", "CCK", "hormones"],
    "difficulty": "medium"
  },
  {
    "text": "Bile salts facilitate fat digestion primarily by:",
    "options": ["Emulsifying fat globules into smaller droplets, increasing surface area for pancreatic lipase", "Directly hydrolyzing triglycerides into fatty acids and monoglycerides", "Activating pancreatic lipase by binding to it", "Transporting fatty acids across the intestinal epithelium"],
    "correct": 0,
    "explanation": "Bile salts are amphipathic (hydrophilic and hydrophobic regions) and act as detergents to emulsify dietary fats — breaking large fat globules into smaller droplets that dramatically increase surface area for pancreatic lipase action. They also form micelles to transport lipid digestion products to the brush border. Lipase itself hydrolyzes the bonds; colipase (not bile salts) activates lipase.",
    "tags": ["physiology", "GI", "bile-salts", "fat-digestion"],
    "difficulty": "easy"
  },
  {
    "text": "Secretin is released from S-cells of the duodenum in response to acidic chyme. Its primary effect is to:",
    "options": ["Stimulate pancreatic ductal cells to secrete bicarbonate-rich fluid, neutralizing acidic chyme", "Stimulate gastric acid secretion", "Stimulate gallbladder contraction", "Increase intestinal motility"],
    "correct": 0,
    "explanation": "Secretin is released when duodenal pH drops below 4.5 (acidic chyme from the stomach). It stimulates pancreatic ductal cells to secrete HCO₃⁻-rich fluid, neutralizing the acid. Secretin also inhibits gastric acid secretion and gastric motility. CCK (not secretin) stimulates gallbladder contraction and pancreatic enzyme secretion.",
    "tags": ["physiology", "GI", "secretin"],
    "difficulty": "easy"
  },
  {
    "text": "Dietary triglycerides are absorbed by intestinal enterocytes as:",
    "options": ["2-monoglycerides and free fatty acids, re-esterified in the ER into triglycerides packaged into chylomicrons", "Intact triglycerides transported across membranes by protein carriers", "Glycerol and free fatty acids transported separately via portal blood", "Fatty acids only, with glycerol excreted in feces"],
    "correct": 0,
    "explanation": "Pancreatic lipase cleaves triglycerides at sn-1 and sn-3 positions to yield 2-monoglycerides and free fatty acids. These enter enterocytes by diffusion/transport, are re-esterified in the smooth ER, packaged with apolipoprotein B-48 into chylomicrons, and secreted into lymph (lacteals). They bypass portal circulation. Very long-chain fatty acids may need transport proteins.",
    "tags": ["physiology", "GI", "lipid-absorption", "chylomicrons"],
    "difficulty": "medium"
  },
  {
    "text": "Fat-soluble vitamins (A, D, E, K) are absorbed similarly to dietary fats and travel from the intestine to circulation via:",
    "options": ["Chylomicrons through lymph, eventually entering the bloodstream via the thoracic duct", "Portal vein directly to the liver", "Binding to albumin in the intestinal lumen", "Active transport by sodium-glucose cotransporters"],
    "correct": 0,
    "explanation": "Fat-soluble vitamins are incorporated into micelles in the intestinal lumen, taken up by enterocytes, packaged into chylomicrons, and transported via the lymphatic system (lacteals → thoracic duct) to the bloodstream. They bypass first-pass hepatic metabolism. Water-soluble vitamins (B vitamins, vitamin C) are absorbed into the portal blood directly.",
    "tags": ["physiology", "GI", "fat-soluble-vitamins", "absorption"],
    "difficulty": "medium"
  },
  # ── Reproductive Biology & Development ────────────────────────────────────
  {
    "text": "Crossing over (chiasmata formation) during meiosis occurs specifically during:",
    "options": ["Prophase I (pachytene stage)", "Metaphase I", "Anaphase II", "Prophase II"],
    "correct": 0,
    "explanation": "Crossing over between non-sister chromatids of homologous chromosomes occurs during prophase I (specifically at the pachytene stage when synaptonemal complexes hold homologs together). This creates genetic recombination and new allele combinations. Anaphase I separates homologs; anaphase II separates sister chromatids. Crossing over does not occur in prophase II.",
    "tags": ["genetics", "meiosis", "crossing-over"],
    "difficulty": "medium"
  },
  {
    "text": "A key difference between meiosis I and meiosis II is that:",
    "options": ["Meiosis I separates homologous chromosomes; meiosis II separates sister chromatids", "Meiosis I separates sister chromatids; meiosis II separates homologs", "Both divisions separate sister chromatids", "Meiosis II is more similar to mitosis than meiosis I is"],
    "correct": 0,
    "explanation": "Meiosis I is the reductional division — homologous chromosomes (each consisting of 2 sister chromatids) separate, halving chromosome number. Meiosis II is the equational division — like mitosis, it separates sister chromatids. Starting with 2n (4 chromatids per homolog pair), after meiosis I: 2 cells each 1n (2 chromatids); after meiosis II: 4 haploid cells (1 chromatid each).",
    "tags": ["genetics", "meiosis"],
    "difficulty": "medium"
  },
  {
    "text": "In oogenesis, meiosis is arrested at which stage until fertilization?",
    "options": ["Metaphase II", "Prophase I (for primary oocytes)", "Anaphase I", "Telophase II"],
    "correct": 0,
    "explanation": "Primary oocytes are arrested in prophase I from fetal development until puberty. After LH surge, the primary oocyte completes meiosis I and arrests as a secondary oocyte at metaphase II. Meiosis II is completed only upon fertilization by a sperm. This means the egg released during ovulation is a secondary oocyte in metaphase II arrest.",
    "tags": ["genetics", "meiosis", "oogenesis"],
    "difficulty": "hard"
  },
  {
    "text": "The LH surge during the menstrual cycle triggers:",
    "options": ["Ovulation and completion of meiosis I by the primary oocyte", "Proliferation of the endometrium", "Decreased estrogen secretion", "Inhibition of FSH release from the pituitary"],
    "correct": 0,
    "explanation": "The midcycle LH surge (triggered by high estrogen at day ~14 via positive feedback) causes ovulation and stimulates the primary oocyte to complete meiosis I, forming the secondary oocyte and first polar body. The secondary oocyte is released and arrested at metaphase II. FSH also surges at this time but is less important for ovulation itself.",
    "tags": ["physiology", "reproductive", "LH-surge", "ovulation"],
    "difficulty": "medium"
  },
  {
    "text": "Human chorionic gonadotropin (hCG), the hormone detected by pregnancy tests, is produced by the:",
    "options": ["Syncytiotrophoblast of the developing placenta", "Corpus luteum", "Anterior pituitary", "Endometrium"],
    "correct": 0,
    "explanation": "hCG is produced by the syncytiotrophoblast (outer layer of the blastocyst/early placenta) after implantation. hCG mimics LH and maintains the corpus luteum, which continues producing progesterone to support the endometrium during the first trimester. Home pregnancy tests detect beta-hCG in urine. After ~10 weeks, the placenta takes over progesterone production.",
    "tags": ["physiology", "reproductive", "hCG", "pregnancy"],
    "difficulty": "easy"
  },
  {
    "text": "Sertoli cells in the testes perform which functions?",
    "options": ["Support spermatogenesis, form the blood-testis barrier, and secrete inhibin and androgen-binding protein", "Produce testosterone in response to LH", "Produce sperm cells by meiosis", "Produce FSH and LH under GnRH stimulation"],
    "correct": 0,
    "explanation": "Sertoli cells (nurse cells) line the seminiferous tubules and: (1) support spermatogenesis nutritionally; (2) form the blood-testis barrier (tight junctions) protecting developing sperm from immune attack; (3) secrete inhibin (feedback inhibits FSH) and androgen-binding protein (concentrates testosterone). Leydig cells (interstitial cells) produce testosterone in response to LH.",
    "tags": ["physiology", "reproductive", "sertoli-cells", "spermatogenesis"],
    "difficulty": "medium"
  },
  # ── Laboratory Techniques ─────────────────────────────────────────────────
  {
    "text": "The three steps of a standard PCR cycle are, in order:",
    "options": ["Denaturation (~95°C), annealing (~55°C), extension (~72°C)", "Annealing, denaturation, extension", "Extension (~72°C), denaturation (~95°C), annealing (~55°C)", "Denaturation, extension, annealing"],
    "correct": 0,
    "explanation": "PCR cycle: (1) Denaturation at ~95°C — heat separates dsDNA into ssDNA templates; (2) Annealing at ~50–65°C — primers bind (hybridize) to complementary sequences on template strands; (3) Extension at ~72°C — Taq polymerase synthesizes new DNA from each primer. After ~30 cycles, the target sequence is amplified ~10⁹-fold.",
    "tags": ["laboratory", "PCR"],
    "difficulty": "easy"
  },
  {
    "text": "RT-PCR differs from standard PCR in that it first uses:",
    "options": ["Reverse transcriptase to convert mRNA into cDNA before PCR amplification", "RNA polymerase to transcribe DNA into mRNA before amplification", "Heat-stable RNA polymerase instead of Taq", "A different annealing temperature for RNA templates"],
    "correct": 0,
    "explanation": "Reverse transcription PCR (RT-PCR) starts with RNA (e.g., mRNA or viral RNA). Reverse transcriptase (from retroviruses) synthesizes a complementary DNA (cDNA) strand from the RNA template. The cDNA (which lacks introns) is then used as template for standard PCR. RT-PCR is used to detect gene expression levels and RNA viruses (e.g., COVID-19 SARS-CoV-2 testing).",
    "tags": ["laboratory", "PCR", "RT-PCR"],
    "difficulty": "easy"
  },
  {
    "text": "In Southern blotting, the molecule being detected is:",
    "options": ["DNA", "RNA", "Protein", "Carbohydrate"],
    "correct": 0,
    "explanation": "Mnemonic: SNoW DRoP — Southern = DNA, Northern = RNA, Western = Protein. In Southern blotting: DNA is restriction-digested, size-separated by gel electrophoresis, transferred to a membrane, and hybridized with a labeled DNA probe. Northern blotting uses RNA. Western blotting uses antibody probes to detect proteins. Eastern blotting detects carbohydrates/lipids.",
    "tags": ["laboratory", "blotting", "southern-blot"],
    "difficulty": "easy"
  },
  {
    "text": "In an ELISA sandwich assay, the antigen is detected by:",
    "options": ["A capture antibody bound to a plate, antigen binding, then a detection antibody linked to an enzyme that produces a colorimetric signal", "Direct binding of antigen to enzyme-linked substrate", "An antigen-coated plate with patient serum added to detect antibodies", "PCR amplification of antigen followed by staining"],
    "correct": 0,
    "explanation": "Sandwich ELISA: (1) capture antibody coated on plate binds target antigen; (2) detection antibody (linked to enzyme, e.g., HRP) binds a different epitope on the same antigen; (3) enzyme substrate produces color proportional to antigen concentration. Indirect ELISA detects antibodies in patient serum. Sandwich ELISA is highly specific because two antibodies must bind the same antigen.",
    "tags": ["laboratory", "ELISA"],
    "difficulty": "medium"
  },
  {
    "text": "CRISPR-Cas9 genome editing requires which two components to cut DNA at a specific location?",
    "options": ["A single-guide RNA (sgRNA) complementary to the target sequence and the Cas9 nuclease", "Two restriction enzymes targeting the same sequence", "A zinc-finger nuclease and a template DNA", "Reverse transcriptase and a target-specific primer"],
    "correct": 0,
    "explanation": "CRISPR-Cas9 uses: (1) single-guide RNA (sgRNA) — a chimeric RNA that guides Cas9 to the target by Watson-Crick base pairing with a 20-nucleotide sequence adjacent to a PAM (protospacer adjacent motif, typically NGG); (2) Cas9 — endonuclease that creates a double-strand break. The cell then repairs via NHEJ (causing indels) or HDR (if a repair template is provided).",
    "tags": ["laboratory", "CRISPR", "gene-editing"],
    "difficulty": "medium"
  },
  {
    "text": "Sanger sequencing (chain termination method) uses fluorescently labeled dideoxynucleotides (ddNTPs) because they:",
    "options": ["Lack a 3'-OH group, terminating chain elongation when incorporated", "Block primer annealing at specific sequences", "Fluoresce only at specific temperatures", "Act as substrates for a different polymerase than Taq"],
    "correct": 0,
    "explanation": "ddNTPs (dideoxyribonucleotides) lack the 3'-OH group required for phosphodiester bond formation. When incorporated by DNA polymerase, chain elongation terminates. Each ddNTP (ddATP, ddCTP, ddGTP, ddTTP) is labeled with a different fluorophore. The resulting fragments are size-separated by capillary electrophoresis and detected by laser, reading the sequence from the fluorescence pattern.",
    "tags": ["laboratory", "sanger-sequencing"],
    "difficulty": "medium"
  },
  # ── Vitamins, Cofactors & Coenzymes ───────────────────────────────────────
  {
    "text": "Vitamin B1 (thiamine) in its active form (thiamine pyrophosphate, TPP) is a cofactor for which enzymes?",
    "options": ["Pyruvate dehydrogenase, alpha-ketoglutarate dehydrogenase, and transketolase", "Pyruvate carboxylase and acetyl-CoA carboxylase", "Amino acid transaminases (aminotransferases)", "Homocysteine methyltransferase"],
    "correct": 0,
    "explanation": "TPP (thiamine pyrophosphate) is required for: (1) pyruvate dehydrogenase (pyruvate → acetyl-CoA); (2) alpha-ketoglutarate dehydrogenase (TCA cycle); (3) transketolase (PPP, non-oxidative phase); (4) branched-chain ketoacid dehydrogenase. Thiamine deficiency (beriberi, Wernicke-Korsakoff) impairs these reactions, especially in high-energy-demand tissues. Biotin cofactors carboxylases; PLP cofactors transaminases.",
    "tags": ["vitamins", "thiamine", "TPP", "cofactors"],
    "difficulty": "hard"
  },
  {
    "text": "Vitamin B6 (pyridoxal phosphate, PLP) is the cofactor primarily involved in:",
    "options": ["Transamination reactions (amino acid metabolism) and decarboxylation of amino acids", "Fatty acid synthesis and carboxylation reactions", "One-carbon metabolism and methylation reactions", "Oxidation-reduction reactions in the ETC"],
    "correct": 0,
    "explanation": "PLP is the active form of vitamin B6 and is a cofactor for: (1) aminotransferases (transaminations — transfers amino groups from amino acids to alpha-keto acids); (2) amino acid decarboxylases (makes neurotransmitters: GABA, serotonin, dopamine, histamine); (3) glycogen phosphorylase. Deficiency causes peripheral neuropathy and sideroblastic anemia.",
    "tags": ["vitamins", "B6", "PLP", "transamination"],
    "difficulty": "medium"
  },
  {
    "text": "Vitamin B7 (biotin) functions as a cofactor for reactions involving:",
    "options": ["CO₂ transfer (carboxylation reactions)", "Hydrogen transfer (oxidation-reduction)", "Amino group transfer (transamination)", "Methyl group transfer"],
    "correct": 0,
    "explanation": "Biotin is the cofactor for carboxylases — enzymes that add CO₂ to substrates: (1) pyruvate carboxylase (pyruvate → OAA); (2) acetyl-CoA carboxylase (acetyl-CoA → malonyl-CoA); (3) propionyl-CoA carboxylase (propionyl-CoA → methylmalonyl-CoA). Avidin in raw egg whites binds biotin, preventing absorption. Deficiency causes dermatitis, alopecia, neurological symptoms.",
    "tags": ["vitamins", "biotin", "carboxylation"],
    "difficulty": "medium"
  },
  {
    "text": "Vitamin B12 (cobalamin) deficiency causes megaloblastic anemia AND neurological symptoms. The neurological symptoms arise because B12 is required for:",
    "options": ["Conversion of methylmalonyl-CoA to succinyl-CoA (critical for myelin synthesis) and regeneration of methionine from homocysteine", "Synthesis of heme for hemoglobin", "Production of NADH for the electron transport chain", "Fatty acid synthesis in neurons"],
    "correct": 0,
    "explanation": "B12 has two key roles: (1) Methylcobalamin cofactors methionine synthase (regenerates methionine from homocysteine, needed for myelin synthesis and DNA methylation); (2) Adenosylcobalamin cofactors methylmalonyl-CoA mutase (methylmalonyl-CoA → succinyl-CoA for TCA). Deficiency causes methylmalonic acid accumulation, disrupting myelin, causing subacute combined degeneration of the spinal cord. Folate deficiency also causes megaloblastic anemia but NOT neurological symptoms.",
    "tags": ["vitamins", "B12", "cobalamin", "neurological"],
    "difficulty": "hard"
  },
  {
    "text": "Vitamin K is required for the gamma-carboxylation of which clotting factors?",
    "options": ["Factors II (thrombin), VII, IX, X, and proteins C and S", "Factors I (fibrinogen), V, and VIII", "Von Willebrand factor and platelet GPIb", "Factor XIII (fibrin stabilizing factor)"],
    "correct": 0,
    "explanation": "Vitamin K (reduced form KH₂) is a cofactor for gamma-glutamyl carboxylase, which adds a carboxyl group to glutamate residues on clotting factors II, VII, IX, X (plus anticoagulant proteins C and S). This carboxylation allows Ca²⁺ binding and phospholipid membrane binding, essential for clotting. Warfarin inhibits vitamin K epoxide reductase, blocking regeneration of active vitamin K.",
    "tags": ["vitamins", "vitamin-K", "coagulation"],
    "difficulty": "medium"
  },
  {
    "text": "Vitamin D (1,25-dihydroxycholecalciferol, calcitriol) is activated by sequential hydroxylations in:",
    "options": ["The liver (25-hydroxylation) then the kidney (1-alpha-hydroxylation)", "The skin (25-hydroxylation) then the liver (1-alpha-hydroxylation)", "The kidney then the liver", "The intestine then the skin"],
    "correct": 0,
    "explanation": "Vitamin D3 (cholecalciferol) is made in the skin from 7-dehydrocholesterol via UV radiation. It is 25-hydroxylated in the liver to calcidiol (25-OH vitamin D3, the storage form measured in blood). Calcidiol is then 1-alpha-hydroxylated in the kidney by PTH-stimulated CYP27B1 to calcitriol (1,25-(OH)₂ D3), the active hormone that increases intestinal Ca²⁺ and phosphate absorption.",
    "tags": ["vitamins", "vitamin-D", "calcium-regulation"],
    "difficulty": "medium"
  },
]

random.seed(33)
for q in Q:
    c = q["correct"]
    opts = q["options"][:]
    correct_text = opts[c]
    random.shuffle(opts)
    q["options"] = opts
    q["correct"] = opts.index(correct_text)

out = os.path.join(BASE, "data", "questions", "bb", "hq-bb-3.json")
os.makedirs(os.path.dirname(out), exist_ok=True)
with open(out, "w") as f:
    json.dump(Q, f, indent=2)
print(f"Wrote {len(Q)} BB questions to {out}")
