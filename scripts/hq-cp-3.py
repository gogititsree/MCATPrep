#!/usr/bin/env python3
import json, os, random

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

Q = [
  # ── Stereochemistry Advanced ───────────────────────────────────────────────
  {
    "text": "According to Cahn-Ingold-Prelog (CIP) rules, a chiral center is assigned R configuration when:",
    "options": ["The remaining three groups (after placing lowest priority group away from viewer) rotate clockwise from highest to lowest priority", "The three groups rotate counterclockwise from highest to lowest priority", "The molecule has a positive specific rotation", "The molecule cannot be superimposed on its mirror image"],
    "correct": 0,
    "explanation": "CIP rules: assign priorities 1–4 based on atomic number (highest = 1). Place the lowest priority group (4) away from viewer. If groups 1→2→3 rotate clockwise, the center is R (rectus). If counterclockwise, it is S (sinister). Specific rotation (+ or −) is an experimental measurement unrelated to R/S designation. Non-superimposability defines chirality, not R/S.",
    "tags": ["organic-chemistry", "stereochemistry", "CIP", "RS-configuration"],
    "difficulty": "medium"
  },
  {
    "text": "A meso compound is achiral despite having multiple stereocenters because:",
    "options": ["It has an internal plane of symmetry that makes the molecule superimposable on its mirror image", "All stereocenters have the same R/S configuration", "It is a racemic mixture", "The stereocenters cancel optical activity by rotating light in opposite directions"],
    "correct": 0,
    "explanation": "A meso compound has two (or more) stereocenters with an internal plane of symmetry — one half of the molecule is the mirror image of the other. The molecule is superimposable on its mirror image, making it achiral and optically inactive. meso-tartaric acid (2R,3S-tartaric acid) is the classic example. A racemic mixture is a 50:50 mixture of two enantiomers, not a single compound.",
    "tags": ["organic-chemistry", "stereochemistry", "meso"],
    "difficulty": "medium"
  },
  {
    "text": "The E/Z nomenclature for alkene geometry is based on:",
    "options": ["CIP priority of substituents on each carbon of the double bond — Z (zusammen/together) when higher-priority groups are on the same side", "Whether the compound rotates plane-polarized light clockwise (E) or counterclockwise (Z)", "The number of carbons on each side of the double bond", "Whether the double bond is cis or trans based on hydrogen positions"],
    "correct": 0,
    "explanation": "E/Z uses CIP priorities: assign priority (1 or 2) to each substituent on each doubly bonded carbon by atomic number. Z (zusammen, 'together') = higher priority groups on same side; E (entgegen, 'opposite') = higher priority groups on opposite sides. E/Z is more general than cis/trans because it works even when there are no hydrogen atoms on the double bond carbons.",
    "tags": ["organic-chemistry", "stereochemistry", "EZ-nomenclature"],
    "difficulty": "medium"
  },
  {
    "text": "Which statement correctly describes enantiomers vs diastereomers?",
    "options": ["Enantiomers are non-superimposable mirror images with opposite configurations at ALL stereocenters; diastereomers differ at SOME but not all stereocenters", "Enantiomers differ at one stereocenter; diastereomers differ at all stereocenters", "Enantiomers always rotate light; diastereomers are always optically inactive", "Enantiomers can be separated by achiral chromatography; diastereomers cannot"],
    "correct": 0,
    "explanation": "Enantiomers: mirror images with opposite (R vs S) configurations at EVERY stereocenter — they have identical physical properties except optical rotation (equal and opposite). Diastereomers: stereoisomers that are NOT mirror images — they differ at some but not all stereocenters. Diastereomers have different physical properties (MP, BP, solubility) and can be separated by ordinary chromatography. Enantiomers require chiral stationary phases for separation.",
    "tags": ["organic-chemistry", "stereochemistry", "enantiomers", "diastereomers"],
    "difficulty": "medium"
  },
  {
    "text": "SN2 reactions proceed with inversion of configuration at the chiral center because:",
    "options": ["The nucleophile attacks from the backside (180° from the leaving group), displacing it and inverting the geometry like an umbrella turning inside-out (Walden inversion)", "The reaction goes through a planar carbocation intermediate that allows attack from both faces", "The leaving group departs before the nucleophile attacks, allowing free rotation", "SN2 reactions actually retain configuration — SN1 causes inversion"],
    "correct": 0,
    "explanation": "In SN2 (bimolecular nucleophilic substitution), the nucleophile attacks the electrophilic carbon from the back (anti to the leaving group) in a single concerted step. The three remaining substituents 'flip' like an umbrella turning inside-out (Walden inversion), giving 100% inversion of configuration (R→S or S→R). SN1 gives a racemic mixture (carbocation intermediate allows attack from both faces).",
    "tags": ["organic-chemistry", "stereochemistry", "SN2", "walden-inversion"],
    "difficulty": "medium"
  },
  {
    "text": "A racemic mixture contains equal amounts of two enantiomers. It is optically inactive because:",
    "options": ["The equal and opposite rotations of each enantiomer cancel out, giving net zero rotation of plane-polarized light", "Neither enantiomer can rotate plane-polarized light individually", "Racemic mixtures have a plane of symmetry within a single molecule", "The two enantiomers interconvert rapidly at room temperature"],
    "correct": 0,
    "explanation": "Each pure enantiomer rotates plane-polarized light equally but in opposite directions (+x° and −x°). In a 50:50 racemic mixture, the two rotations cancel, giving net 0° rotation. This is external compensation (vs internal compensation in meso compounds). Racemic mixtures can be resolved into enantiomers using chiral reagents, enzymes, or chiral chromatography.",
    "tags": ["organic-chemistry", "stereochemistry", "racemic-mixture"],
    "difficulty": "easy"
  },
  # ── Carbonyl Advanced ─────────────────────────────────────────────────────
  {
    "text": "In the Michael addition, a nucleophile adds to an alpha,beta-unsaturated carbonyl at the:",
    "options": ["Beta carbon (conjugate/1,4-addition), not the carbonyl carbon (1,2-addition)", "Carbonyl carbon (1,2-addition)", "Alpha carbon after enolization", "Carbonyl oxygen"],
    "correct": 0,
    "explanation": "In Michael (conjugate) addition, a soft nucleophile (enolate, malonate, amine) attacks the beta carbon of an alpha,beta-unsaturated carbonyl compound (enone, enoate). This is 1,4-addition because the nucleophile adds at position 4 relative to the oxygen. Hard nucleophiles (organolithium) prefer 1,2-addition at the carbonyl carbon. The product is a 1,4-dicarbonyl after workup.",
    "tags": ["organic-chemistry", "carbonyl", "michael-addition"],
    "difficulty": "medium"
  },
  {
    "text": "The Diels-Alder reaction requires a diene in which conformation?",
    "options": ["s-cis conformation (both double bonds on same side of the single bond)", "s-trans conformation", "A cumulated diene (allene)", "Any conformation — the reaction is conformationally flexible"],
    "correct": 0,
    "explanation": "The Diels-Alder is a [4+2] cycloaddition between a diene and a dienophile (electron-poor alkene). The diene must adopt the s-cis conformation so both ends can overlap with the dienophile's pi system simultaneously. s-trans dienes (locked in trans conformation) cannot react. Electron-withdrawing groups on the dienophile activate it; electron-donating groups on the diene activate it.",
    "tags": ["organic-chemistry", "carbonyl", "diels-alder"],
    "difficulty": "medium"
  },
  {
    "text": "The Robinson annulation combines a Michael addition followed by an intramolecular aldol condensation to form:",
    "options": ["A six-membered ring containing an enone (cyclohexenone)", "A five-membered ring lactam", "A beta-lactam ring", "A simple acyclic 1,5-dicarbonyl"],
    "correct": 0,
    "explanation": "The Robinson annulation (developed by Robert Robinson) uses an enone (Michael acceptor) and a ketone (Michael donor). Step 1: Michael addition forms a 1,5-dicarbonyl. Step 2: intramolecular aldol condensation closes the ring and dehydrates to form a six-membered alpha,beta-unsaturated ketone (cyclohex-2-enone). It is a key method for building ring systems in steroid synthesis.",
    "tags": ["organic-chemistry", "carbonyl", "robinson-annulation"],
    "difficulty": "hard"
  },
  {
    "text": "Alpha-halogenation of a ketone under acidic conditions is regioselective because:",
    "options": ["Acid catalysis gives a slow enol formation step that determines which alpha carbon is halogenated (kinetic enol selectivity)", "Halogen attacks the more substituted alpha carbon regardless of enol formation", "Under acidic conditions, only the carbonyl is halogenated", "Alpha-halogenation does not occur under acidic conditions"],
    "correct": 0,
    "explanation": "Under acidic conditions, enol formation is slow (rate-determining); each molecule of halogen reacts with one enol molecule before re-equilibration. The more substituted (thermodynamically more stable but kinetically slower to form) enol reacts preferentially to give monohalogenation at the more substituted position. Under basic conditions, carbanion (enolate) forms rapidly and multiple halogenations occur (haloform reaction).",
    "tags": ["organic-chemistry", "carbonyl", "halogenation"],
    "difficulty": "hard"
  },
  # ── Carbohydrates ─────────────────────────────────────────────────────────
  {
    "text": "In the Fischer projection of D-glucose, the D designation refers to:",
    "options": ["The configuration of the hydroxyl group at the highest-numbered chiral center (C5) being on the right, same as D-glyceraldehyde", "The molecule rotating plane-polarized light to the right (+)", "The molecule being found in the dextrorotatory form in nature", "The presence of more than four hydroxyl groups"],
    "correct": 0,
    "explanation": "D/L nomenclature for sugars is based on the configuration at the highest-numbered chiral carbon (C5 for hexoses) relative to D-glyceraldehyde. D-sugars have the hydroxyl group on the RIGHT at that carbon in the Fischer projection. D does NOT mean dextrorotatory — D-fructose is levorotatory (−). Most naturally occurring sugars are D-sugars.",
    "tags": ["organic-chemistry", "carbohydrates", "DL-nomenclature"],
    "difficulty": "medium"
  },
  {
    "text": "The anomeric carbon of a cyclic monosaccharide is the carbon that:",
    "options": ["Was the carbonyl carbon (C1 in aldoses) and becomes chiral upon ring closure, creating alpha and beta anomers", "Is connected to two hydroxyl groups", "Is attached to the ring oxygen and has a free hydroxyl", "Bears the primary hydroxyl (-CH₂OH) group"],
    "correct": 0,
    "explanation": "When glucose undergoes ring closure (intramolecular hemiacetal formation between C1 aldehyde and C5 hydroxyl), C1 becomes a new chiral center called the anomeric carbon. Alpha anomer: hydroxyl at anomeric carbon is AXIAL (same side as C6 in Haworth) / trans to CH₂OH; beta anomer: hydroxyl is EQUATORIAL / cis to CH₂OH in Haworth. Beta-D-glucose (equatorial -OH) is more stable and predominates at equilibrium (64%).",
    "tags": ["organic-chemistry", "carbohydrates", "anomeric-carbon", "anomers"],
    "difficulty": "medium"
  },
  {
    "text": "Mutarotation of glucose refers to the spontaneous change in:",
    "options": ["Optical rotation as alpha and beta anomers interconvert in solution through the open-chain form", "The D to L configuration at C5", "The ring size from pyranose to furanose", "The reducing end to a non-reducing end"],
    "correct": 0,
    "explanation": "Mutarotation: alpha-D-glucose ([α]D = +112°) and beta-D-glucose ([α]D = +18.7°) interconvert in aqueous solution through the open-chain (aldehyde) form, reaching an equilibrium mixture with [α]D = +52.7°. This equilibration is catalyzed by acid, base, or enzymes (mutarotase). Glucose is therefore a reducing sugar because its aldehyde (in the open form) can reduce Fehling's or Tollens' reagent.",
    "tags": ["organic-chemistry", "carbohydrates", "mutarotation"],
    "difficulty": "medium"
  },
  {
    "text": "Sucrose is a non-reducing sugar because:",
    "options": ["Its glycosidic bond links the anomeric carbons of both glucose and fructose (C1-C2 linkage), so neither has a free hemiacetal", "Sucrose cannot be hydrolyzed by water", "Sucrose lacks hydroxyl groups", "Sucrose is a polysaccharide"],
    "correct": 0,
    "explanation": "Sucrose (glucose + fructose) is formed by a glycosidic bond between C1 of glucose and C2 of fructose — both anomeric carbons are involved. This means no free hemiacetal/hemiketal (anomeric -OH) is available to open into an aldehyde/ketone form, so sucrose cannot reduce oxidizing agents (non-reducing). Maltose and lactose have free anomeric carbons and are reducing sugars.",
    "tags": ["organic-chemistry", "carbohydrates", "sucrose", "reducing-sugar"],
    "difficulty": "medium"
  },
  {
    "text": "The glycosidic bond in cellulose (beta-1,4 linkage) makes it indigestible to humans because:",
    "options": ["Humans lack beta-glucosidase (cellulase) to hydrolyze beta-1,4 glycosidic bonds; alpha-1,4 bonds (starch, glycogen) are hydrolyzed by amylase", "Cellulose is cross-linked with lignin, making it chemically inert", "Cellulose forms insoluble crystals that cannot enter the digestive tract", "Cellulose monomers are L-glucose, which cannot be transported"],
    "correct": 0,
    "explanation": "Cellulose has beta-1,4 glycosidic bonds between glucose units. Humans produce only alpha-glucosidases (salivary/pancreatic amylase) that cleave alpha-1,4 bonds. The beta-1,4 orientation makes cellulose a structural polymer (hydrogen bonds between chains create strong fibers). Ruminants harbor microbes that produce cellulase. Starch (alpha-1,4 with alpha-1,6 branches) is fully digestible.",
    "tags": ["organic-chemistry", "carbohydrates", "cellulose", "glycosidic-bond"],
    "difficulty": "easy"
  },
  # ── Amino Acids & Peptides ────────────────────────────────────────────────
  {
    "text": "At physiological pH (7.4), most amino acids exist as zwitterions. What is a zwitterion?",
    "options": ["A molecule with both a positive charge (protonated amine, -NH₃⁺) and a negative charge (deprotonated carboxyl, -COO⁻) but overall neutral", "A molecule with two negative charges", "A dipeptide with an ionized N-terminus only", "An amino acid dissolved in basic solution"],
    "correct": 0,
    "explanation": "A zwitterion (German: 'double ion') has both a positive charge (protonated amino group, -NH₃⁺, pKa ~9) and a negative charge (deprotonated carboxyl group, -COO⁻, pKa ~2), with net charge of zero. At physiological pH (7.4), both ionizable groups are in their charged forms because pH is between the two pKas. The isoelectric point (pI) is the pH at which net charge = 0.",
    "tags": ["biochemistry", "amino-acids", "zwitterion"],
    "difficulty": "easy"
  },
  {
    "text": "The isoelectric point (pI) of an amino acid with only alpha-amino and alpha-carboxyl groups (pKa1 = 2.0, pKa2 = 9.0) is:",
    "options": ["5.5 (average of the two pKas)", "2.0", "9.0", "7.0"],
    "correct": 0,
    "explanation": "For a simple amino acid (only two ionizable groups), pI = (pKa1 + pKa2)/2 = (2.0 + 9.0)/2 = 5.5. At pH 5.5, the molecule is electrically neutral (equal amounts of +1 and 0 charge forms, or strictly at the maximum zwitterion form). For acidic amino acids (Asp, Glu), pI = average of the two lowest pKas; for basic amino acids (Lys, Arg, His), pI = average of the two highest pKas.",
    "tags": ["biochemistry", "amino-acids", "isoelectric-point"],
    "difficulty": "medium"
  },
  {
    "text": "Edman degradation sequentially removes and identifies amino acids from the:",
    "options": ["N-terminus (free alpha-amino group) using phenyl isothiocyanate (PITC)", "C-terminus using carboxypeptidase", "Any position using trypsin cleavage", "Internal positions using cyanogen bromide (CNBr)"],
    "correct": 0,
    "explanation": "Edman degradation: PITC reacts with the free N-terminal alpha-amino group under mild alkaline conditions. Acid treatment cyclizes and releases the N-terminal amino acid as a PTH-amino acid without hydrolyzing the rest of the peptide, which can undergo another round. This allows sequential readout from the N-terminus. CNBr cleaves after methionine residues (internal); carboxypeptidases remove from C-terminus.",
    "tags": ["biochemistry", "amino-acids", "peptides", "edman-degradation"],
    "difficulty": "medium"
  },
  {
    "text": "Cyanogen bromide (CNBr) cleaves peptides specifically after:",
    "options": ["Methionine residues (at the C-side of Met)", "Lysine and arginine residues", "Tryptophan residues", "Aspartate residues"],
    "correct": 0,
    "explanation": "CNBr reacts specifically with the sulfur of methionine residues, converting Met into homoserine lactone and cleaving the peptide bond on the C-terminal side of the methionine. This is used to generate specific peptide fragments for sequencing. Trypsin cleaves after Lys and Arg; chymotrypsin after Phe, Trp, Tyr; V8 protease after Asp and Glu; pepsin less specifically.",
    "tags": ["biochemistry", "amino-acids", "peptide-sequencing", "CNBr"],
    "difficulty": "hard"
  },
  {
    "text": "The peptide bond between amino acids is formed by a condensation reaction and has which property due to resonance?",
    "options": ["Partial double-bond character, making the C-N bond rigid and planar (trans configuration preferred)", "Full single-bond character allowing free rotation", "Full double-bond character with no rotation at all", "Negative charge localized on nitrogen"],
    "correct": 0,
    "explanation": "The peptide bond (CO-NH) has resonance between C=O/C-N and C-O⁻/C=N⁺ forms, giving the C-N bond approximately 40% double-bond character. This makes the peptide bond rigid and planar (~0° or 180°, usually trans to minimize steric clashes between R groups). Rotation is only free at phi (Cα-N) and psi (Cα-C) angles — the basis for the Ramachandran plot.",
    "tags": ["biochemistry", "peptide-bond", "protein-structure"],
    "difficulty": "medium"
  },
  # ── Coordination Compounds ────────────────────────────────────────────────
  {
    "text": "In crystal field theory, the d-orbital splitting energy (Δ) in an octahedral complex is influenced by the spectrochemical series. Which ligand causes the LARGEST splitting?",
    "options": ["CN⁻ (cyanide), a strong-field ligand", "I⁻ (iodide), a weak-field ligand", "H₂O (water), a moderate-field ligand", "F⁻ (fluoride), a weak-field ligand"],
    "correct": 0,
    "explanation": "The spectrochemical series ranks ligands by their ability to split d-orbital energies: I⁻ < Br⁻ < Cl⁻ < F⁻ < OH⁻ < H₂O < py < NH₃ < en < NO₂⁻ < CN⁻ < CO. Strong-field ligands (CN⁻, CO) cause large Δ, leading to low-spin complexes. Weak-field ligands (halides) cause small Δ, leading to high-spin complexes. The color of complexes arises from d-d transitions absorbing complementary wavelengths.",
    "tags": ["general-chemistry", "coordination-chemistry", "crystal-field", "spectrochemical-series"],
    "difficulty": "medium"
  },
  {
    "text": "A coordination compound is paramagnetic if it has:",
    "options": ["Unpaired d-electrons", "All d-electrons paired", "Only s and p electrons", "A full d-subshell (d¹⁰)"],
    "correct": 0,
    "explanation": "Paramagnetic compounds have unpaired electrons and are attracted to magnetic fields. In transition metal complexes, unpaired d-electrons determine paramagnetism. High-spin complexes (weak-field ligands, small Δ) have more unpaired electrons (following Hund's rule for filling). Low-spin complexes (strong-field ligands, large Δ) have electrons paired in lower energy d-orbitals. d⁰ and d¹⁰ complexes are diamagnetic.",
    "tags": ["general-chemistry", "coordination-chemistry", "paramagnetism"],
    "difficulty": "medium"
  },
  {
    "text": "EDTA (ethylenediaminetetraacetic acid) is a hexadentate ligand. Polydentate (chelate) ligands form more stable complexes than monodentate ligands primarily because:",
    "options": ["The chelate effect: releasing multiple water molecules upon binding increases entropy (ΔS > 0), making complex formation more thermodynamically favorable", "Polydentate ligands have higher charge and stronger electrostatic attraction", "Chelates form stronger individual metal-ligand bonds", "Entropy decreases upon chelation, stabilizing the complex by enthalpy alone"],
    "correct": 0,
    "explanation": "The chelate effect: when a polydentate ligand replaces multiple monodentate ligands, the number of free particles in solution increases (e.g., EDTA replaces 6 water molecules, releasing 5 more particles net per EDTA). This large positive entropy change (ΔS > 0) makes ΔG = ΔH - TΔS more negative, stabilizing chelate complexes despite similar bond enthalpies. EDTA is used clinically for heavy metal poisoning (chelation therapy).",
    "tags": ["general-chemistry", "coordination-chemistry", "chelate-effect", "EDTA"],
    "difficulty": "hard"
  },
  {
    "text": "The color of transition metal complexes arises because:",
    "options": ["Electrons in split d-orbitals absorb visible light of the complementary color when promoted to higher d-orbitals", "Transition metals emit light via fluorescence", "The ligands absorb UV light and emit visible light", "d-electrons absorb infrared radiation"],
    "correct": 0,
    "explanation": "The crystal field splitting (Δ) in transition metal complexes corresponds to energies of visible light photons. When an electron absorbs a photon and is promoted from lower (t₂g) to upper (eg) d-orbitals, the complementary color is transmitted/reflected. For example, Cu²⁺(aq) absorbs red/orange light (Δ ≈ 2.1 eV) and appears blue. Larger Δ absorbs at shorter wavelengths (blue shift → appears red/orange).",
    "tags": ["general-chemistry", "coordination-chemistry", "color"],
    "difficulty": "medium"
  },
  # ── Colligative Properties & Phase Diagrams ───────────────────────────────
  {
    "text": "A 0.1 mol/kg solution of NaCl has a van't Hoff factor (i) of approximately 2. Its freezing point depression compared to a 0.1 mol/kg glucose solution is:",
    "options": ["Twice as large (NaCl solution freezes 2× lower)", "The same (molality determines ΔTf, not ions)", "Half as large", "Four times as large"],
    "correct": 0,
    "explanation": "ΔTf = i × Kf × m. For glucose (i = 1): ΔTf = 1 × 1.86 × 0.1 = 0.186°C. For NaCl (i ≈ 2, dissociates into Na⁺ and Cl⁻): ΔTf = 2 × 1.86 × 0.1 = 0.372°C. The NaCl solution has approximately twice the freezing point depression because it produces twice as many solute particles per formula unit. Colligative properties depend on particle count, not identity.",
    "tags": ["general-chemistry", "colligative-properties", "freezing-point-depression"],
    "difficulty": "medium"
  },
  {
    "text": "The triple point on a phase diagram represents:",
    "options": ["The unique temperature and pressure at which solid, liquid, and gas phases coexist in equilibrium", "The temperature above which a gas cannot be liquefied regardless of pressure", "The point at which solid and liquid densities become equal", "The normal boiling point at 1 atm"],
    "correct": 0,
    "explanation": "The triple point is the unique combination of temperature and pressure where all three phases (solid, liquid, gas) coexist simultaneously in equilibrium. For water, the triple point is 273.16 K (0.01°C) and 611.73 Pa (0.006 atm). Above the critical point (critical temperature and pressure), the liquid-gas distinction disappears and a supercritical fluid forms. Normal boiling point is at 1 atm on the liquid-gas boundary.",
    "tags": ["general-chemistry", "phase-diagram", "triple-point"],
    "difficulty": "easy"
  },
  {
    "text": "A solution's osmotic pressure (π) is given by π = iMRT. For a 0.2 M NaCl solution at 37°C (310 K), using R = 0.0821 L·atm/(mol·K) and i = 2, the osmotic pressure is approximately:",
    "options": ["~10.2 atm", "~5.1 atm", "~20.4 atm", "~2.5 atm"],
    "correct": 0,
    "explanation": "π = iMRT = 2 × 0.2 mol/L × 0.0821 L·atm/(mol·K) × 310 K = 2 × 0.2 × 25.45 = 2 × 5.09 ≈ 10.2 atm. This is close to the osmotic pressure of physiological saline (0.9% NaCl ≈ 0.154 M NaCl, giving ~7.6 atm). High osmotic pressure is why saline solutions must be carefully matched to biological fluids to prevent cell lysis or crenation.",
    "tags": ["general-chemistry", "colligative-properties", "osmotic-pressure"],
    "difficulty": "hard"
  },
  {
    "text": "Vapor pressure lowering by a nonvolatile solute is described by Raoult's law: P_solution = X_solvent × P°_solvent. Adding a solute:",
    "options": ["Decreases the vapor pressure proportionally to the mole fraction of solute", "Increases the vapor pressure by adding more molecules to the gas phase", "Has no effect on vapor pressure if the solute is nonvolatile", "Decreases vapor pressure only if the solute-solvent interactions are stronger than solvent-solvent interactions"],
    "correct": 0,
    "explanation": "Raoult's law states that vapor pressure is proportional to the mole fraction of solvent. Since Xsolvent = 1 − Xsolute, adding solute decreases Xsolvent and lowers vapor pressure. The decrease is ΔP = X_solute × P°. This is a purely statistical/entropic effect (fewer solvent molecules at the surface) for ideal solutions — solute-solvent interaction strength affects ideality but the lowering still occurs.",
    "tags": ["general-chemistry", "colligative-properties", "raoults-law"],
    "difficulty": "medium"
  },
  # ── Rotational Dynamics ───────────────────────────────────────────────────
  {
    "text": "A torque of 10 N·m is applied to a wheel with moment of inertia I = 2 kg·m². The angular acceleration is:",
    "options": ["5 rad/s²", "20 rad/s²", "0.2 rad/s²", "10 rad/s²"],
    "correct": 0,
    "explanation": "Newton's second law for rotation: τ = Iα, so α = τ/I = 10 N·m / 2 kg·m² = 5 rad/s². This is the rotational analog of F = ma. The moment of inertia I depends on mass distribution about the axis (not just total mass). Greater I means greater resistance to angular acceleration for the same torque.",
    "tags": ["physics", "rotational-dynamics", "torque", "angular-acceleration"],
    "difficulty": "easy"
  },
  {
    "text": "Conservation of angular momentum explains why a spinning skater speeds up when pulling their arms in, because:",
    "options": ["L = Iω is conserved; reducing I (smaller radius of gyration) must increase ω to keep L constant", "Reducing arm radius reduces friction, allowing faster rotation", "Pulling arms in increases the torque applied by leg muscles", "Total kinetic energy is conserved as translational energy converts to rotational energy"],
    "correct": 0,
    "explanation": "Angular momentum L = Iω is conserved when no external torque acts. When the skater pulls arms inward, the moment of inertia I decreases (mass is closer to the rotation axis). Since L = Iω must remain constant, ω (angular velocity) increases proportionally. Rotational kinetic energy (½Iω²) actually INCREASES because internal muscular work is done pulling arms in.",
    "tags": ["physics", "rotational-dynamics", "angular-momentum", "conservation"],
    "difficulty": "medium"
  },
  {
    "text": "A solid cylinder (I = ½MR²) and a hollow cylinder (I = MR²) start from rest and roll without slipping down an identical incline. Which reaches the bottom first?",
    "options": ["The solid cylinder — it has a smaller moment of inertia relative to its mass, so more energy goes to translational motion", "The hollow cylinder — it has more rotational energy stored", "They arrive simultaneously since both have the same mass M and radius R", "The hollow cylinder — it rolls more efficiently"],
    "correct": 0,
    "explanation": "Total KE at bottom = ½Mv² + ½Iω². For rolling without slipping, ω = v/R. Solid cylinder: KE = ½Mv² + ½(½MR²)(v/R)² = ½Mv² + ¼Mv² = ¾Mv². Hollow: KE = ½Mv² + ½(MR²)(v/R)² = Mv². Setting mgh = KE: solid gets v = √(4gh/3), hollow gets v = √(gh). Solid has higher translational speed and arrives first. Objects with more mass near the rim (larger I/MR² ratio) roll slower.",
    "tags": ["physics", "rotational-dynamics", "rolling", "moment-of-inertia"],
    "difficulty": "hard"
  },
  {
    "text": "The rotational kinetic energy of a spinning disk with I = 0.5 kg·m² and ω = 4 rad/s is:",
    "options": ["4 J", "8 J", "2 J", "1 J"],
    "correct": 0,
    "explanation": "Rotational KE = ½Iω² = ½ × 0.5 kg·m² × (4 rad/s)² = ½ × 0.5 × 16 = 4 J. Compare with translational KE = ½mv². If this disk were also translating at speed v_cm, the total KE would be the sum of both terms. For a rolling object, both terms contribute to total mechanical energy.",
    "tags": ["physics", "rotational-dynamics", "rotational-kinetic-energy"],
    "difficulty": "medium"
  },
  {
    "text": "The parallel axis theorem states that I_parallel = I_cm + Md². This is useful for calculating the moment of inertia about an axis:",
    "options": ["Parallel to the center-of-mass axis but displaced by distance d", "Perpendicular to the center-of-mass axis", "Only for hollow objects", "About any arbitrary axis with no restriction"],
    "correct": 0,
    "explanation": "The parallel axis theorem: to find I about any axis parallel to an axis through the center of mass, add Md² to I_cm (where d is the perpendicular distance between axes, M is total mass). Example: I of a rod about one end = I_cm + M(L/2)² = (1/12)ML² + (1/4)ML² = (1/3)ML². The axis must be parallel to the CM axis — the perpendicular axis theorem applies to perpendicular axes.",
    "tags": ["physics", "rotational-dynamics", "parallel-axis-theorem"],
    "difficulty": "medium"
  },
  # ── Fluid Dynamics Advanced ───────────────────────────────────────────────
  {
    "text": "A fluid flows through a pipe that narrows from radius R to R/2. By the continuity equation, the speed in the narrow section compared to the wide section is:",
    "options": ["4 times faster (v₂ = 4v₁)", "2 times faster", "The same speed", "16 times faster"],
    "correct": 0,
    "explanation": "Continuity equation for incompressible fluid: A₁v₁ = A₂v₂. Area A = πR². If radius decreases from R to R/2: A₂ = π(R/2)² = πR²/4 = A₁/4. So v₂ = A₁v₁/A₂ = 4v₁. The fluid speeds up 4-fold. By Bernoulli's principle, this increased speed corresponds to decreased pressure in the narrow section (Venturi effect).",
    "tags": ["physics", "fluid-dynamics", "continuity-equation"],
    "difficulty": "medium"
  },
  {
    "text": "Bernoulli's principle relates pressure and velocity in a flowing fluid. In an airplane wing (greater speed over top surface), the pressure:",
    "options": ["Is lower over the top surface (high speed = low pressure), creating a net upward lift force", "Is higher over the top surface due to faster-moving air pushing down", "Is equal on both surfaces since the fluid is air", "Is determined only by the wing's weight"],
    "correct": 0,
    "explanation": "Bernoulli's equation: P + ½ρv² + ρgh = constant along a streamline. Air flows faster over the curved top surface of a wing. By Bernoulli, higher v → lower P. So pressure above the wing < pressure below → net upward force (lift). This is one component of lift; Newton's third law (air deflected downward) also contributes. The Venturi tube and carburetor work by the same principle.",
    "tags": ["physics", "fluid-dynamics", "bernoulli", "lift"],
    "difficulty": "easy"
  },
  {
    "text": "Stokes' law gives the drag force on a sphere moving slowly through a viscous fluid: F = 6πηrv. This force increases proportionally with:",
    "options": ["Fluid viscosity (η), sphere radius (r), and sphere velocity (v)", "Sphere radius squared and velocity squared", "Fluid density and velocity only", "Sphere mass and gravity"],
    "correct": 0,
    "explanation": "Stokes' law: F_drag = 6πηrv, valid for slow (laminar, low Reynolds number) flow. Drag increases linearly with viscosity η (thicker fluid resists more), radius r (larger sphere has more surface area), and velocity v. At terminal velocity, drag equals gravitational force (mg): 6πηrv_t = (4/3)πr³(ρ_particle − ρ_fluid)g, so v_t = 2r²(Δρ)g/(9η). This is the basis for viscometry and sedimentation rate.",
    "tags": ["physics", "fluid-dynamics", "stokes-law", "viscosity"],
    "difficulty": "medium"
  },
  {
    "text": "Surface tension causes water to rise in a thin capillary tube (capillary action). The height to which water rises is:",
    "options": ["Greater in thinner tubes (h ∝ 1/r), because higher surface-area-to-volume ratio allows surface tension to lift more water per unit volume", "Greater in wider tubes", "Independent of tube radius", "Greater for non-polar liquids"],
    "correct": 0,
    "explanation": "Capillary rise height h = 2γcosθ/(ρgr), where γ = surface tension, θ = contact angle, ρ = fluid density, g = gravity, r = tube radius. Since h ∝ 1/r, water rises higher in narrower tubes. This occurs because cohesion (water-water surface tension) and adhesion (water-glass) combine. Water wets glass (θ < 90°); mercury doesn't (θ > 90°, so it is depressed in glass capillaries).",
    "tags": ["physics", "fluid-dynamics", "surface-tension", "capillary-action"],
    "difficulty": "medium"
  },
  # ── Thermodynamics Applications ────────────────────────────────────────────
  {
    "text": "In an adiabatic process, by definition:",
    "options": ["No heat is exchanged with the surroundings (q = 0), so ΔU = w", "No work is done (w = 0), so ΔU = q", "Both q = 0 and w = 0", "Temperature remains constant"],
    "correct": 0,
    "explanation": "Adiabatic: no heat exchange (q = 0). First law: ΔU = q + w → ΔU = w. If the gas expands adiabatically (w < 0 by convention when system does work), internal energy decreases and temperature falls. Isothermal = constant T (q ≠ 0). Isochoric = constant V (w = 0, ΔU = q). Isobaric = constant P. Adiabatic processes are faster than isothermal because no heat equilibration occurs.",
    "tags": ["physics", "thermodynamics", "adiabatic"],
    "difficulty": "easy"
  },
  {
    "text": "On a PV diagram, the work done BY the gas during expansion equals:",
    "options": ["The area under the PV curve (∫P dV)", "The change in internal energy (ΔU)", "The area to the LEFT of the PV curve", "PΔT (change in temperature times pressure)"],
    "correct": 0,
    "explanation": "Work done by the gas: w = ∫P dV = area under the P-V curve. For expansion (ΔV > 0), work is positive (system does work on surroundings). For compression (ΔV < 0), work is negative (surroundings do work on system). For a cyclic process, net work = area enclosed by the cycle. ΔU = q − w (if w = work done BY gas); for isothermal ideal gas expansion, ΔU = 0 and q = w.",
    "tags": ["physics", "thermodynamics", "PV-diagram", "work"],
    "difficulty": "medium"
  },
  {
    "text": "The efficiency of a Carnot heat engine operating between temperatures T_H (hot) and T_C (cold) is:",
    "options": ["e = 1 − T_C/T_H (using absolute/Kelvin temperatures)", "e = 1 − T_H/T_C", "e = (T_H − T_C)/T_C", "e = T_H/(T_H + T_C)"],
    "correct": 0,
    "explanation": "The Carnot efficiency e = 1 − T_C/T_H represents the maximum possible efficiency of any heat engine operating between two temperatures (must be in Kelvin). No real engine can exceed Carnot efficiency. Example: engine between 400 K and 300 K has max efficiency = 1 − 300/400 = 25%. Increasing T_H or decreasing T_C improves efficiency. Real engines are less efficient due to irreversibilities (friction, heat losses).",
    "tags": ["physics", "thermodynamics", "carnot", "heat-engine"],
    "difficulty": "medium"
  },
  {
    "text": "For an isothermal expansion of an ideal gas, ΔU = 0 because:",
    "options": ["Internal energy of an ideal gas depends only on temperature (T is constant), so ΔU = 0 regardless of volume change", "Work done and heat absorbed are both zero", "Ideal gas molecules do not interact, so expansion requires no energy", "Pressure and volume changes cancel exactly"],
    "correct": 0,
    "explanation": "For an ideal gas, internal energy U depends only on temperature (kinetic energy of molecules). In isothermal conditions (constant T), ΔU = 0 regardless of pressure or volume changes. By the first law: 0 = q + w → q = −w. For isothermal expansion, the gas does work (w < 0 by convention where w = work done ON gas), so q > 0 (heat is absorbed from surroundings to maintain T). Real gases have ΔU ≠ 0 in isothermal expansion due to intermolecular forces.",
    "tags": ["physics", "thermodynamics", "ideal-gas", "isothermal"],
    "difficulty": "medium"
  },
  {
    "text": "Entropy increases in a spontaneous irreversible process because:",
    "options": ["The total entropy of the universe (system + surroundings) increases; the second law of thermodynamics states ΔS_universe ≥ 0", "Heat always flows from cold to hot in irreversible processes", "Free energy always increases in irreversible processes", "Internal energy always increases in irreversible processes"],
    "correct": 0,
    "explanation": "The second law of thermodynamics: in any spontaneous process, total entropy of the universe increases (ΔS_universe = ΔS_system + ΔS_surroundings ≥ 0). Reversible processes have ΔS_universe = 0; irreversible spontaneous processes have ΔS_universe > 0. Gibbs free energy ΔG = ΔH − TΔS measures spontaneity at constant T and P (ΔG < 0 for spontaneous processes), combining system entropy change with enthalpy.",
    "tags": ["physics", "thermodynamics", "entropy", "second-law"],
    "difficulty": "easy"
  },
  # ── Electricity Advanced ───────────────────────────────────────────────────
  {
    "text": "A capacitor with capacitance C is charged to voltage V. The energy stored in the capacitor is:",
    "options": ["U = ½CV²", "U = CV²", "U = CV", "U = ½CV"],
    "correct": 0,
    "explanation": "The energy stored in a capacitor is U = ½CV² = ½Q²/C = ½QV (all equivalent). Derivation: as charge builds up, the work done against the increasing voltage is dW = V dq = (q/C)dq; integrating from 0 to Q gives W = Q²/(2C) = ½CV². The factor of ½ arises because voltage starts at 0 and increases linearly to V as charge accumulates. This energy is stored in the electric field between the plates.",
    "tags": ["physics", "electricity", "capacitor", "energy"],
    "difficulty": "easy"
  },
  {
    "text": "Inserting a dielectric material between capacitor plates (at constant charge Q):",
    "options": ["Increases capacitance by factor κ (dielectric constant) and decreases voltage by factor κ, leaving Q unchanged but reducing stored energy", "Decreases capacitance and increases voltage", "Has no effect on capacitance", "Increases both capacitance and voltage proportionally"],
    "correct": 0,
    "explanation": "A dielectric (κ > 1) between capacitor plates increases capacitance: C' = κC. With fixed Q: V' = Q/C' = Q/(κC) = V/κ (voltage decreases). Energy U' = Q²/(2C') = Q²/(2κC) = U/κ (stored energy decreases — the dielectric is pulled in, doing work on the capacitor). At constant voltage (battery connected): Q increases, C increases, and stored energy U = ½CV² increases as energy comes from the battery.",
    "tags": ["physics", "electricity", "capacitor", "dielectric"],
    "difficulty": "hard"
  },
  {
    "text": "In an RC circuit, the time constant τ = RC determines that the capacitor charges to approximately 63% of its final voltage after:",
    "options": ["One time constant (t = τ = RC)", "Half the time constant", "Two time constants", "The time constant squared"],
    "correct": 0,
    "explanation": "In an RC charging circuit, V(t) = V₀(1 − e^(−t/RC)). At t = τ = RC: V = V₀(1 − e⁻¹) = V₀(1 − 0.368) ≈ 0.632V₀ (≈63%). After 5τ, the capacitor is 99.3% charged (practically fully charged). The time constant τ = RC is larger for large capacitance (stores more charge) or large resistance (limits current flow). Same τ applies to discharge: V(t) = V₀e^(−t/RC).",
    "tags": ["physics", "electricity", "RC-circuit", "time-constant"],
    "difficulty": "medium"
  },
  {
    "text": "Lenz's law states that the induced EMF and current in a conductor oppose the change in magnetic flux that caused them. This is because:",
    "options": ["Conservation of energy requires the induced current to create a magnetic field opposing the change, preventing perpetual motion", "Magnetic fields always repel each other", "Electrons prefer to move opposite to the direction of the external field", "Ohm's law requires opposing currents"],
    "correct": 0,
    "explanation": "Lenz's law (a consequence of Faraday's law and energy conservation): if increasing flux induced a current that enhanced the flux further, a positive feedback loop would create energy from nothing. Instead, the induced current creates a magnetic field opposing the change in flux (if flux increases, induced B opposes it; if flux decreases, induced B supports it). This is why electromagnetic braking works and why AC transformers have energy losses.",
    "tags": ["physics", "electricity", "lenz-law", "electromagnetic-induction"],
    "difficulty": "medium"
  },
  {
    "text": "Electric power dissipated in a resistor can be expressed as P = I²R = V²/R = IV. If the voltage across a 100-Ω resistor is 10 V, the power dissipated is:",
    "options": ["1 W", "10 W", "1000 W", "0.1 W"],
    "correct": 0,
    "explanation": "P = V²/R = (10 V)²/100 Ω = 100/100 = 1 W. Alternatively: I = V/R = 10/100 = 0.1 A; P = IV = 0.1 × 10 = 1 W; or P = I²R = (0.1)² × 100 = 1 W. All three forms give the same answer. The power is dissipated as heat in the resistor (Joule heating). High-power resistors require heat sinks to prevent overheating.",
    "tags": ["physics", "electricity", "power", "resistor"],
    "difficulty": "easy"
  },
]

random.seed(11)
for q in Q:
    c = q["correct"]
    opts = q["options"][:]
    correct_text = opts[c]
    random.shuffle(opts)
    q["options"] = opts
    q["correct"] = opts.index(correct_text)

out = os.path.join(BASE, "data", "questions", "cp", "hq-cp-3.json")
os.makedirs(os.path.dirname(out), exist_ok=True)
with open(out, "w") as f:
    json.dump(Q, f, indent=2)
print(f"Wrote {len(Q)} CP questions to {out}")
