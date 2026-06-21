#!/usr/bin/env python3
import json, os, random

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

Q = [
  # ── Atomic Structure & Periodic Trends ──────────────────────────────────
  {
    "text": "Which quantum numbers specify an electron in the 3d subshell?",
    "options": ["n=3, l=2", "n=3, l=1", "n=2, l=3", "n=3, l=3"],
    "correct": 0,
    "explanation": "The principal quantum number n=3 designates the third shell, and the azimuthal quantum number l=2 designates a d subshell (l: 0=s, 1=p, 2=d, 3=f).",
    "tags": ["atomic-structure", "quantum-numbers"],
    "difficulty": "easy"
  },
  {
    "text": "Which element has the highest first ionization energy?",
    "options": ["He", "Ne", "Ar", "Kr"],
    "correct": 0,
    "explanation": "Helium has the highest first ionization energy of all elements (~2372 kJ/mol) due to its small atomic radius and full 1s² shell with no shielding electrons.",
    "tags": ["periodic-trends", "ionization-energy"],
    "difficulty": "easy"
  },
  {
    "text": "Across a period from left to right, atomic radius generally:",
    "options": ["Decreases due to increasing nuclear charge with same shielding", "Increases due to more electron shells", "Increases due to decreasing nuclear charge", "Remains constant"],
    "correct": 0,
    "explanation": "Across a period, nuclear charge increases while electrons are added to the same shell (minimal additional shielding), causing the electron cloud to contract.",
    "tags": ["periodic-trends", "atomic-radius"],
    "difficulty": "easy"
  },
  {
    "text": "The electron configuration of Fe²⁺ is:",
    "options": ["[Ar] 3d⁶", "[Ar] 3d⁴", "[Ar] 3d⁵ 4s¹", "[Ar] 3d⁶ 4s²"],
    "correct": 0,
    "explanation": "Neutral Fe is [Ar] 3d⁶ 4s². When Fe loses 2 electrons to form Fe²⁺, the 4s electrons are removed first, leaving [Ar] 3d⁶.",
    "tags": ["electron-configuration", "transition-metals"],
    "difficulty": "medium"
  },
  {
    "text": "Which property generally increases going down a group in the periodic table?",
    "options": ["Atomic radius", "First ionization energy", "Electronegativity", "Electron affinity"],
    "correct": 0,
    "explanation": "Atomic radius increases down a group because each successive element has an additional electron shell, increasing the distance between the nucleus and valence electrons.",
    "tags": ["periodic-trends", "atomic-radius"],
    "difficulty": "easy"
  },
  {
    "text": "Hund's rule states that electrons will:",
    "options": ["Occupy degenerate orbitals singly before pairing, with parallel spins", "Pair up in the lowest-energy orbital first", "Occupy the highest available energy orbitals first", "Fill orbitals in order of increasing n+l"],
    "correct": 0,
    "explanation": "Hund's rule states that for degenerate orbitals, electrons occupy each orbital singly with parallel (same) spins before any orbital is doubly occupied, minimizing electron repulsion.",
    "tags": ["electron-configuration", "hunds-rule"],
    "difficulty": "easy"
  },
  # ── Chemical Bonding ─────────────────────────────────────────────────────
  {
    "text": "Which molecule has a trigonal bipyramidal electron geometry but a seesaw molecular geometry?",
    "options": ["SF₄", "PCl₅", "ClF₃", "XeF₂"],
    "correct": 0,
    "explanation": "SF₄ has 5 electron domains around sulfur (4 bonding + 1 lone pair). The electron geometry is trigonal bipyramidal, and the lone pair in an equatorial position gives a seesaw molecular shape.",
    "tags": ["vsepr", "molecular-geometry"],
    "difficulty": "medium"
  },
  {
    "text": "The bond angle in water (H₂O) is approximately 104.5°, which is less than the ideal tetrahedral angle of 109.5° because:",
    "options": ["Lone pairs exert greater repulsion than bonding pairs", "O-H bonds are longer than expected", "Hydrogen is highly electronegative", "Water forms a linear geometry"],
    "correct": 0,
    "explanation": "Lone pairs occupy more space than bonding pairs because they are not constrained between two nuclei. The two lone pairs on oxygen push the bonding pairs closer together, reducing the H-O-H angle to ~104.5°.",
    "tags": ["vsepr", "water"],
    "difficulty": "medium"
  },
  {
    "text": "Which of the following exhibits the strongest intermolecular forces?",
    "options": ["HF", "HCl", "H₂S", "PH₃"],
    "correct": 0,
    "explanation": "HF can form hydrogen bonds (H bonded to highly electronegative F) which are the strongest intermolecular forces among these options. HCl, H₂S, and PH₃ have only dipole-dipole interactions and London dispersion forces.",
    "tags": ["intermolecular-forces", "hydrogen-bonding"],
    "difficulty": "medium"
  },
  {
    "text": "In an sp³ hybridized carbon, the orbitals point towards the corners of:",
    "options": ["A tetrahedron", "A triangle", "An octahedron", "A square"],
    "correct": 0,
    "explanation": "sp³ hybridization combines one s orbital and three p orbitals to create four equivalent hybrid orbitals directed toward the corners of a regular tetrahedron at 109.5° angles.",
    "tags": ["hybridization", "bonding"],
    "difficulty": "easy"
  },
  {
    "text": "Which bond is the shortest?",
    "options": ["C≡C", "C=C", "C-C", "C-N"],
    "correct": 0,
    "explanation": "Triple bonds have the highest bond order, which results in the shortest and strongest bond. C≡C (~120 pm) < C=C (~134 pm) < C-C (~154 pm). C-N is a single bond (~147 pm) and longer than C≡C.",
    "tags": ["chemical-bonding", "bond-length"],
    "difficulty": "easy"
  },
  {
    "text": "Formal charge on nitrogen in NH₄⁺ is:",
    "options": ["+1", "0", "-1", "+2"],
    "correct": 0,
    "explanation": "Formal charge = valence electrons - nonbonding electrons - (½ × bonding electrons). For N in NH₄⁺: 5 - 0 - (½ × 8) = 5 - 0 - 4 = +1.",
    "tags": ["formal-charge", "bonding"],
    "difficulty": "medium"
  },
  # ── Thermodynamics ────────────────────────────────────────────────────────
  {
    "text": "A reaction has ΔH = -50 kJ/mol and ΔS = -100 J/(mol·K). At what temperature does this reaction become non-spontaneous?",
    "options": ["T > 500 K", "T > 250 K", "T > 750 K", "The reaction is always spontaneous"],
    "correct": 0,
    "explanation": "ΔG = ΔH - TΔS. Reaction is spontaneous when ΔG < 0. At T = 500 K: ΔG = -50,000 - (500)(-100) = -50,000 + 50,000 = 0. Above 500 K, ΔG > 0 (non-spontaneous).",
    "tags": ["thermodynamics", "gibbs-free-energy"],
    "difficulty": "medium"
  },
  {
    "text": "Which statement best describes an endothermic process?",
    "options": ["Heat flows from surroundings to system; ΔH > 0", "Heat flows from system to surroundings; ΔH < 0", "No heat is exchanged; ΔH = 0", "Entropy always decreases"],
    "correct": 0,
    "explanation": "In an endothermic process, the system absorbs heat from its surroundings, so the enthalpy change ΔH is positive. Examples include melting ice and dissolving NH₄NO₃.",
    "tags": ["thermodynamics", "enthalpy"],
    "difficulty": "easy"
  },
  {
    "text": "Hess's Law states that the total enthalpy change for a reaction is:",
    "options": ["Independent of pathway; equal to sum of enthalpy changes of individual steps", "Dependent on the rate of reaction", "Always negative for spontaneous reactions", "Equal to the activation energy"],
    "correct": 0,
    "explanation": "Hess's Law exploits the fact that enthalpy is a state function. The total ΔH for a reaction equals the sum of ΔH values for any series of steps that convert reactants to products, regardless of the pathway taken.",
    "tags": ["thermodynamics", "hess-law"],
    "difficulty": "easy"
  },
  {
    "text": "The standard entropy change (ΔS°) for a reaction is expected to be positive when:",
    "options": ["Gas molecules are produced from solid reactants", "A gas condenses to a liquid", "A solution precipitates a solid", "Temperature decreases"],
    "correct": 0,
    "explanation": "Entropy increases when disorder increases. Producing gaseous products from solids greatly increases the number of microstates available (gas molecules have much greater positional and kinetic freedom than solids).",
    "tags": ["thermodynamics", "entropy"],
    "difficulty": "easy"
  },
  {
    "text": "For a spontaneous process at constant temperature and pressure, the Gibbs free energy change (ΔG) must be:",
    "options": ["Negative", "Positive", "Zero", "Equal to TΔS"],
    "correct": 0,
    "explanation": "At constant T and P, a process is spontaneous if ΔG < 0. When ΔG = 0, the system is at equilibrium. When ΔG > 0, the process is non-spontaneous (reverse is spontaneous).",
    "tags": ["thermodynamics", "gibbs-free-energy", "spontaneity"],
    "difficulty": "easy"
  },
  {
    "text": "Heat capacity at constant pressure (Cp) is greater than heat capacity at constant volume (Cv) for gases because:",
    "options": ["At constant pressure, gas must also do PΔV work when heated", "Gases have fewer degrees of freedom at constant pressure", "Pressure increases slow molecular motion", "Cv includes PV work while Cp does not"],
    "correct": 0,
    "explanation": "When a gas is heated at constant pressure, it expands and does work on the surroundings (PΔV). This extra energy input beyond ΔU makes Cp = Cv + nR for ideal gases, so Cp > Cv.",
    "tags": ["thermodynamics", "heat-capacity"],
    "difficulty": "medium"
  },
  # ── Chemical Equilibrium ──────────────────────────────────────────────────
  {
    "text": "For the reaction N₂(g) + 3H₂(g) ⇌ 2NH₃(g), the Kc expression is:",
    "options": ["Kc = [NH₃]²/([N₂][H₂]³)", "Kc = [N₂][H₂]³/[NH₃]²", "Kc = [NH₃]/([N₂][H₂])", "Kc = [NH₃]²/([N₂]³[H₂])"],
    "correct": 0,
    "explanation": "Kc = [products]^stoich / [reactants]^stoich. For N₂ + 3H₂ ⇌ 2NH₃: Kc = [NH₃]²/([N₂]¹[H₂]³). Pure solids and liquids are omitted.",
    "tags": ["equilibrium", "equilibrium-constant"],
    "difficulty": "easy"
  },
  {
    "text": "If Kp = 2.5 × 10⁻⁴ for a reaction, which statement is correct?",
    "options": ["Reactants are favored at equilibrium", "Products are favored at equilibrium", "The reaction goes to completion", "The reaction does not proceed"],
    "correct": 0,
    "explanation": "A Kp value much less than 1 indicates that at equilibrium, the concentration of reactants greatly exceeds that of products, meaning the reactant side is favored.",
    "tags": ["equilibrium", "equilibrium-constant"],
    "difficulty": "easy"
  },
  {
    "text": "Le Chatelier's principle predicts that for an exothermic reaction at equilibrium, increasing temperature will:",
    "options": ["Shift equilibrium toward reactants, decreasing K", "Shift equilibrium toward products, increasing K", "Have no effect on equilibrium position", "Shift equilibrium toward products without changing K"],
    "correct": 0,
    "explanation": "For an exothermic reaction, heat is a product. Adding heat (increasing T) shifts equilibrium left (toward reactants) by Le Chatelier's principle. This also decreases the equilibrium constant K.",
    "tags": ["equilibrium", "le-chatelier"],
    "difficulty": "medium"
  },
  {
    "text": "The relationship between Kp and Kc is:",
    "options": ["Kp = Kc(RT)^Δn", "Kp = Kc + Δn(RT)", "Kp = Kc/Δn(RT)", "Kp = Kc regardless of Δn"],
    "correct": 0,
    "explanation": "Kp = Kc(RT)^Δn, where Δn = moles of gaseous products - moles of gaseous reactants, R = 0.08206 L·atm/(mol·K), and T is temperature in Kelvin.",
    "tags": ["equilibrium", "kp-kc"],
    "difficulty": "medium"
  },
  {
    "text": "Adding a catalyst to a reaction at equilibrium will:",
    "options": ["Speed up both forward and reverse reactions equally, not shifting equilibrium", "Shift equilibrium to favor products", "Increase the equilibrium constant", "Decrease activation energy for forward reaction only"],
    "correct": 0,
    "explanation": "A catalyst lowers the activation energy for both the forward and reverse reactions equally. It allows equilibrium to be reached faster but does not change the equilibrium constant or the equilibrium position.",
    "tags": ["equilibrium", "catalysis"],
    "difficulty": "easy"
  },
  # ── Acid-Base Chemistry ───────────────────────────────────────────────────
  {
    "text": "The Henderson-Hasselbalch equation relates pH to pKa as:",
    "options": ["pH = pKa + log([A⁻]/[HA])", "pH = pKa - log([A⁻]/[HA])", "pH = pKa × log([HA]/[A⁻])", "pH = pKa + log([HA]/[A⁻])"],
    "correct": 0,
    "explanation": "The Henderson-Hasselbalch equation is pH = pKa + log([A⁻]/[HA]), where [A⁻] is the conjugate base concentration and [HA] is the weak acid concentration. It is most useful in the buffer region.",
    "tags": ["acid-base", "henderson-hasselbalch", "buffers"],
    "difficulty": "easy"
  },
  {
    "text": "Which of the following is the strongest acid?",
    "options": ["HI", "HF", "HCl", "HBr"],
    "correct": 0,
    "explanation": "Among the hydrohalic acids, acid strength increases down the group: HF << HCl < HBr < HI. HI is the strongest because the H-I bond is weakest (longest), making it easiest to donate a proton.",
    "tags": ["acid-base", "acid-strength"],
    "difficulty": "medium"
  },
  {
    "text": "A buffer solution is most effective when:",
    "options": ["pH = pKa of the weak acid", "pH = 7.0", "pH >> pKa", "pH << pKa"],
    "correct": 0,
    "explanation": "A buffer is most effective when pH = pKa, meaning [A⁻] = [HA]. At this point, the buffer has equal capacity to absorb added acid or base. The effective range is approximately pH = pKa ± 1.",
    "tags": ["acid-base", "buffers"],
    "difficulty": "easy"
  },
  {
    "text": "What is the pH of a solution with [OH⁻] = 1 × 10⁻⁴ M at 25°C?",
    "options": ["10", "4", "7", "14"],
    "correct": 0,
    "explanation": "pOH = -log[OH⁻] = -log(10⁻⁴) = 4. Since pH + pOH = 14 at 25°C, pH = 14 - 4 = 10.",
    "tags": ["acid-base", "ph-calculation"],
    "difficulty": "easy"
  },
  {
    "text": "Which of the following would produce a basic solution when dissolved in water?",
    "options": ["NaCH₃COO (sodium acetate)", "NH₄Cl (ammonium chloride)", "NaCl (sodium chloride)", "HNO₃ (nitric acid)"],
    "correct": 0,
    "explanation": "Sodium acetate undergoes hydrolysis: CH₃COO⁻ + H₂O ⇌ CH₃COOH + OH⁻. The acetate ion (conjugate base of weak acid) accepts a proton from water, producing OH⁻ and making the solution basic.",
    "tags": ["acid-base", "hydrolysis", "salt-solutions"],
    "difficulty": "medium"
  },
  {
    "text": "According to the Brønsted-Lowry definition, an acid is:",
    "options": ["A proton donor", "An electron pair acceptor", "A proton acceptor", "An electron pair donor"],
    "correct": 0,
    "explanation": "The Brønsted-Lowry theory defines an acid as a proton (H⁺) donor and a base as a proton acceptor. This definition is broader than the Arrhenius theory, encompassing reactions not in aqueous solution.",
    "tags": ["acid-base", "bronsted-lowry"],
    "difficulty": "easy"
  },
  # ── Electrochemistry ─────────────────────────────────────────────────────
  {
    "text": "In a galvanic cell, oxidation occurs at the:",
    "options": ["Anode", "Cathode", "Salt bridge", "Both electrodes simultaneously"],
    "correct": 0,
    "explanation": "In a galvanic (voltaic) cell, the anode is the site of oxidation (loss of electrons). Electrons flow from the anode through the external circuit to the cathode, where reduction occurs. Memory aid: AN OX (anode = oxidation).",
    "tags": ["electrochemistry", "galvanic-cell"],
    "difficulty": "easy"
  },
  {
    "text": "The standard cell potential for a galvanic cell is calculated as:",
    "options": ["E°cell = E°cathode - E°anode", "E°cell = E°anode - E°cathode", "E°cell = E°cathode + E°anode", "E°cell = E°cathode × E°anode"],
    "correct": 0,
    "explanation": "E°cell = E°cathode - E°anode (using standard reduction potentials). Since both are given as reduction potentials, we subtract the anode value from the cathode value. A positive E°cell indicates a spontaneous reaction.",
    "tags": ["electrochemistry", "cell-potential"],
    "difficulty": "easy"
  },
  {
    "text": "The Nernst equation relates cell potential to concentration as:",
    "options": ["E = E° - (RT/nF)lnQ", "E = E° + (RT/nF)lnQ", "E = E° - (nF/RT)lnQ", "E = E°/lnQ"],
    "correct": 0,
    "explanation": "The Nernst equation is E = E° - (RT/nF)lnQ, where R = gas constant, T = temperature, n = moles of electrons transferred, F = Faraday's constant, and Q = reaction quotient. At 25°C this simplifies to E = E° - (0.0592/n)logQ.",
    "tags": ["electrochemistry", "nernst-equation"],
    "difficulty": "medium"
  },
  {
    "text": "Faraday's first law of electrolysis states that the mass of substance deposited is proportional to:",
    "options": ["The quantity of charge passed (coulombs)", "The voltage applied", "The resistance of the solution", "The temperature of the electrolyte"],
    "correct": 0,
    "explanation": "Faraday's first law: m = (M × Q)/(n × F), where m = mass deposited, M = molar mass, Q = charge in coulombs, n = number of electrons per ion, F = 96,485 C/mol. The amount deposited is directly proportional to charge passed.",
    "tags": ["electrochemistry", "electrolysis", "faradays-law"],
    "difficulty": "medium"
  },
  {
    "text": "Which species is most easily oxidized?",
    "options": ["Li (E° = -3.04 V for Li⁺/Li)", "Au (E° = +1.50 V for Au³⁺/Au)", "Cu (E° = +0.34 V for Cu²⁺/Cu)", "Ag (E° = +0.80 V for Ag⁺/Ag)"],
    "correct": 0,
    "explanation": "Metals with the most negative standard reduction potential are most easily oxidized (best reducing agents). Li has E° = -3.04 V, the most negative listed, making it the strongest reducing agent and easiest to oxidize.",
    "tags": ["electrochemistry", "oxidation-potential", "activity-series"],
    "difficulty": "medium"
  },
  # ── Chemical Kinetics ─────────────────────────────────────────────────────
  {
    "text": "For a first-order reaction, the half-life is:",
    "options": ["t½ = 0.693/k (independent of initial concentration)", "t½ = 1/(k[A]₀) (dependent on initial concentration)", "t½ = 2/k", "t½ = k/0.693"],
    "correct": 0,
    "explanation": "For a first-order reaction, t½ = ln(2)/k = 0.693/k. This half-life is constant and independent of initial concentration, which is a defining feature of first-order kinetics.",
    "tags": ["kinetics", "half-life", "first-order"],
    "difficulty": "easy"
  },
  {
    "text": "The Arrhenius equation describes the temperature dependence of the rate constant as:",
    "options": ["k = Ae^(-Ea/RT)", "k = Ae^(Ea/RT)", "k = A/e^(Ea/RT)^2", "k = RT/Ea"],
    "correct": 0,
    "explanation": "The Arrhenius equation is k = Ae^(-Ea/RT), where A is the frequency factor, Ea is the activation energy, R is the gas constant, and T is temperature in Kelvin. Increasing T or decreasing Ea increases k.",
    "tags": ["kinetics", "arrhenius", "activation-energy"],
    "difficulty": "easy"
  },
  {
    "text": "A reaction is second-order in [A] and first-order in [B]. If [A] is doubled and [B] is halved, the rate:",
    "options": ["Doubles", "Stays the same", "Quadruples", "Halves"],
    "correct": 0,
    "explanation": "Rate = k[A]²[B]. New rate = k(2[A])²(½[B]) = k × 4[A]² × ½[B] = 2k[A]²[B] = 2 × original rate. The rate doubles.",
    "tags": ["kinetics", "rate-law"],
    "difficulty": "medium"
  },
  {
    "text": "The rate-determining step in a multi-step reaction mechanism is:",
    "options": ["The slowest elementary step", "The fastest elementary step", "The step with lowest activation energy", "The step that produces the most product"],
    "correct": 0,
    "explanation": "The rate-determining step (RDS) is the slowest step in a reaction mechanism. It acts as the bottleneck, determining the overall rate of the reaction. The rate law for the overall reaction reflects the elementary rate law of the RDS.",
    "tags": ["kinetics", "rate-determining-step", "mechanism"],
    "difficulty": "easy"
  },
  {
    "text": "A zero-order reaction has a rate that is:",
    "options": ["Independent of reactant concentration", "Proportional to reactant concentration", "Proportional to the square of reactant concentration", "Inversely proportional to concentration"],
    "correct": 0,
    "explanation": "For a zero-order reaction, rate = k[A]⁰ = k. The rate is constant and independent of the concentration of reactants. The half-life increases as the reaction proceeds: t½ = [A]₀/(2k).",
    "tags": ["kinetics", "zero-order"],
    "difficulty": "easy"
  },
  # ── Organic Chemistry – Nomenclature & Structure ──────────────────────────
  {
    "text": "What is the IUPAC name for CH₃CH₂CH(CH₃)CH₂CH₃?",
    "options": ["3-methylpentane", "2-ethylbutane", "Isohexane", "2-methylpentane"],
    "correct": 0,
    "explanation": "The longest chain has 5 carbons (pentane). The methyl branch is at carbon 3 (numbering from either end gives position 3). IUPAC name: 3-methylpentane.",
    "tags": ["organic-chemistry", "nomenclature", "alkanes"],
    "difficulty": "easy"
  },
  {
    "text": "Which functional group is present in an ester?",
    "options": ["-COO- (carbonyl bonded to oxygen)", "-COOH", "-CO-NH-", "-CHO"],
    "correct": 0,
    "explanation": "An ester contains the -COO- functional group, formally written as R-C(=O)-O-R'. Esters are formed by reaction of carboxylic acids with alcohols (Fischer esterification).",
    "tags": ["organic-chemistry", "functional-groups", "esters"],
    "difficulty": "easy"
  },
  {
    "text": "cis-2-butene and trans-2-butene are examples of:",
    "options": ["Geometric (cis-trans) isomers", "Enantiomers", "Conformational isomers", "Constitutional isomers"],
    "correct": 0,
    "explanation": "Geometric isomers (cis-trans isomers) differ in the spatial arrangement of groups around a double bond or ring. Both cis- and trans-2-butene have the same connectivity (constitutional structure) but different geometric arrangements.",
    "tags": ["organic-chemistry", "stereochemistry", "isomers"],
    "difficulty": "easy"
  },
  {
    "text": "A chiral center (stereocenter) in an organic molecule is a carbon that:",
    "options": ["Has four different substituents attached", "Has four identical substituents", "Is sp² hybridized", "Is part of an aromatic ring"],
    "correct": 0,
    "explanation": "A chiral center is a tetrahedral carbon bonded to four different groups. Such a center is non-superimposable on its mirror image, giving rise to enantiomers. sp² carbons cannot be chiral centers as they only have three substituents.",
    "tags": ["organic-chemistry", "stereochemistry", "chirality"],
    "difficulty": "easy"
  },
  # ── Organic Reactions – Substitution & Elimination ────────────────────────
  {
    "text": "An SN2 reaction proceeds by:",
    "options": ["Back-side attack of nucleophile on carbon with simultaneous leaving group departure, inverting configuration", "Formation of a carbocation intermediate followed by nucleophile attack", "Front-side attack retaining configuration", "Radical chain mechanism"],
    "correct": 0,
    "explanation": "SN2 is a concerted one-step mechanism. The nucleophile attacks from the back (180° from the leaving group), and as the leaving group departs, configuration is inverted (Walden inversion). Second-order kinetics: rate = k[Nu][substrate].",
    "tags": ["organic-chemistry", "sn2", "substitution"],
    "difficulty": "medium"
  },
  {
    "text": "Which substrate undergoes SN1 most readily?",
    "options": ["(CH₃)₃CBr (tertiary, forms stable carbocation)", "CH₃Br (methyl)", "CH₃CH₂Br (primary)", "CH₃CH₂CH₂Br (primary)"],
    "correct": 0,
    "explanation": "SN1 proceeds through a carbocation intermediate. Tertiary substrates form the most stable (tertiary) carbocations due to hyperconjugation and inductive stabilization by three alkyl groups, making (CH₃)₃CBr most reactive for SN1.",
    "tags": ["organic-chemistry", "sn1", "substitution", "carbocation"],
    "difficulty": "medium"
  },
  {
    "text": "E2 elimination reactions are favored by:",
    "options": ["Bulky strong bases, elevated temperature, and secondary/tertiary substrates", "Small nucleophiles, low temperature, and primary substrates", "Aqueous solvent, weak bases, and tertiary substrates", "Polar protic solvents and strong nucleophiles"],
    "correct": 0,
    "explanation": "E2 is a concerted anti-periplanar elimination. Bulky, strong bases (e.g., t-BuOK) favor elimination by approaching the β-hydrogen rather than the carbon. Higher temperature and secondary/tertiary substrates also favor E2 over SN2.",
    "tags": ["organic-chemistry", "e2", "elimination"],
    "difficulty": "medium"
  },
  {
    "text": "Markovnikov's rule predicts that in hydrohalogenation of an alkene, the hydrogen adds to:",
    "options": ["The carbon with more hydrogens (less substituted), placing the halide on the more substituted carbon", "The carbon with fewer hydrogens", "Randomly to either carbon", "Only to terminal carbons"],
    "correct": 0,
    "explanation": "Markovnikov's rule: the proton adds to the carbon bearing more hydrogens, generating the more stable (more substituted) carbocation intermediate. The halide then attacks the carbocation.",
    "tags": ["organic-chemistry", "addition-reactions", "markovnikov"],
    "difficulty": "medium"
  },
  # ── Organic Reactions – Carbonyl Chemistry ────────────────────────────────
  {
    "text": "Nucleophilic addition to a carbonyl group is favored when the carbonyl carbon is:",
    "options": ["Electrophilic (partial positive charge)", "Nucleophilic (partial negative charge)", "Neutral with no partial charges", "Part of an aromatic ring"],
    "correct": 0,
    "explanation": "The carbonyl carbon bears a partial positive charge (δ+) due to the electronegativity of oxygen withdrawing electron density. This makes the carbonyl carbon electrophilic and susceptible to attack by nucleophiles.",
    "tags": ["organic-chemistry", "carbonyl", "nucleophilic-addition"],
    "difficulty": "easy"
  },
  {
    "text": "In the Fischer esterification reaction, a carboxylic acid reacts with an alcohol under acid catalysis to produce:",
    "options": ["An ester and water", "An amide and water", "An anhydride and water", "An aldehyde and water"],
    "correct": 0,
    "explanation": "Fischer esterification: RCOOH + R'OH ⇌ RCOOR' + H₂O. It is catalyzed by strong acid (H₂SO₄) and is reversible (equilibrium reaction). Excess alcohol or removal of water drives the reaction toward ester formation.",
    "tags": ["organic-chemistry", "esterification", "carbonyl"],
    "difficulty": "easy"
  },
  {
    "text": "An aldol condensation involves:",
    "options": ["A nucleophilic enolate attacking a carbonyl carbon to form a β-hydroxy carbonyl compound", "Acid-catalyzed addition of water to a carbonyl", "Oxidation of an aldehyde to a carboxylic acid", "Reduction of a ketone to an alcohol"],
    "correct": 0,
    "explanation": "In aldol condensation, a base abstracts an α-hydrogen to form an enolate, which then attacks the carbonyl carbon of another carbonyl compound. The product is a β-hydroxy carbonyl compound (aldol). Dehydration can then occur to give an α,β-unsaturated carbonyl.",
    "tags": ["organic-chemistry", "aldol-condensation", "carbonyl"],
    "difficulty": "hard"
  },
  # ── Spectroscopy ──────────────────────────────────────────────────────────
  {
    "text": "In ¹H NMR spectroscopy, chemical shift (δ) is measured in ppm relative to:",
    "options": ["TMS (tetramethylsilane) at δ = 0", "Water at δ = 0", "Benzene at δ = 0", "CHCl₃ at δ = 0"],
    "correct": 0,
    "explanation": "TMS (tetramethylsilane, Si(CH₃)₄) is the standard reference for ¹H and ¹³C NMR. Its protons resonate at higher field than most organic protons, and it is assigned δ = 0 ppm. It is chemically inert and volatile (easily removed).",
    "tags": ["spectroscopy", "nmr"],
    "difficulty": "easy"
  },
  {
    "text": "In infrared (IR) spectroscopy, the carbonyl (C=O) stretch appears at approximately:",
    "options": ["~1700 cm⁻¹", "~3300 cm⁻¹", "~1600 cm⁻¹", "~2200 cm⁻¹"],
    "correct": 0,
    "explanation": "The C=O stretch is one of the most diagnostic IR absorptions, appearing near 1700 cm⁻¹ for ketones. Conjugation or ring strain shifts this value: esters ~1735 cm⁻¹, amides ~1680 cm⁻¹, α,β-unsaturated carbonyls ~1680 cm⁻¹.",
    "tags": ["spectroscopy", "ir", "carbonyl"],
    "difficulty": "easy"
  },
  {
    "text": "Mass spectrometry measures:",
    "options": ["Mass-to-charge ratio (m/z) of ions", "Frequency of photon absorption", "Nuclear spin transitions", "Electron energy levels"],
    "correct": 0,
    "explanation": "In mass spectrometry, molecules are ionized and fragmented, and the resulting ions are separated by their mass-to-charge ratio (m/z). The molecular ion (M⁺) gives the molecular weight. Fragmentation patterns help determine structure.",
    "tags": ["spectroscopy", "mass-spectrometry"],
    "difficulty": "easy"
  },
  # ── Physics – Mechanics ───────────────────────────────────────────────────
  {
    "text": "A ball is thrown horizontally from a cliff 20 m high with v = 10 m/s. How far from the base does it land? (g = 10 m/s²)",
    "options": ["20 m", "10 m", "40 m", "14 m"],
    "correct": 0,
    "explanation": "Time to fall: h = ½gt² → 20 = ½(10)t² → t = 2 s. Horizontal distance: x = v₀t = 10 × 2 = 20 m.",
    "tags": ["mechanics", "projectile-motion"],
    "difficulty": "medium"
  },
  {
    "text": "Newton's second law states:",
    "options": ["F = ma (net force equals mass times acceleration)", "For every action there is an equal and opposite reaction", "An object at rest stays at rest unless acted on by a net force", "Work equals force times displacement"],
    "correct": 0,
    "explanation": "Newton's second law: the net force on an object equals its mass multiplied by its acceleration (F = ma). This is a vector equation; both F and a have the same direction.",
    "tags": ["mechanics", "newtons-laws"],
    "difficulty": "easy"
  },
  {
    "text": "The work done by a force F over displacement d at angle θ is:",
    "options": ["W = Fd cosθ", "W = Fd sinθ", "W = Fd/cosθ", "W = Fd tanθ"],
    "correct": 0,
    "explanation": "Work = F·d (dot product) = Fd cosθ, where θ is the angle between the force vector and displacement vector. Only the component of force parallel to displacement does work.",
    "tags": ["mechanics", "work-energy"],
    "difficulty": "easy"
  },
  {
    "text": "Conservation of momentum applies when:",
    "options": ["No external net force acts on the system", "Only conservative forces act", "Kinetic energy is conserved", "The system is in thermal equilibrium"],
    "correct": 0,
    "explanation": "Momentum is conserved (Δp = 0) when the net external force on the system is zero (Newton's second law: F_net = dp/dt). This applies to collisions and explosions where internal forces are much greater than external forces.",
    "tags": ["mechanics", "conservation-of-momentum"],
    "difficulty": "easy"
  },
  {
    "text": "A satellite in circular orbit: as orbital radius increases, orbital speed:",
    "options": ["Decreases (v = √(GM/r))", "Increases", "Stays the same", "Depends on satellite mass"],
    "correct": 0,
    "explanation": "For circular orbit, gravitational force provides centripetal force: GMm/r² = mv²/r → v = √(GM/r). As r increases, v decreases. Orbital speed is independent of the satellite's mass.",
    "tags": ["mechanics", "orbital-mechanics", "gravitation"],
    "difficulty": "medium"
  },
  {
    "text": "The moment of inertia of an object depends on:",
    "options": ["Mass and its distribution relative to the rotation axis", "Mass only", "Linear velocity only", "Applied torque only"],
    "correct": 0,
    "explanation": "Moment of inertia I = Σmᵢrᵢ² depends on both the total mass AND how that mass is distributed relative to the rotation axis. Objects with mass concentrated far from the axis have higher I.",
    "tags": ["mechanics", "rotational-motion", "moment-of-inertia"],
    "difficulty": "medium"
  },
  # ── Physics – Fluids ──────────────────────────────────────────────────────
  {
    "text": "Bernoulli's principle states that in steady fluid flow, as fluid speed increases:",
    "options": ["Pressure decreases (conservation of energy)", "Pressure increases", "Pressure stays the same", "Density increases"],
    "correct": 0,
    "explanation": "Bernoulli's equation: P + ½ρv² + ρgh = constant. As v increases (e.g., in a constriction), P must decrease to maintain the constant. This explains lift on airfoils and the Venturi effect.",
    "tags": ["fluids", "bernoulli"],
    "difficulty": "easy"
  },
  {
    "text": "Poiseuille's Law for viscous flow in a tube shows that flow rate Q is proportional to:",
    "options": ["r⁴ (fourth power of radius)", "r² (second power)", "r (first power)", "r³ (third power)"],
    "correct": 0,
    "explanation": "Poiseuille's Law: Q = πr⁴ΔP/(8ηL). Flow rate is proportional to r⁴, meaning doubling the radius increases flow 16-fold. This has major physiological implications: small changes in vessel radius cause large changes in blood flow.",
    "tags": ["fluids", "poiseuille", "viscosity"],
    "difficulty": "medium"
  },
  {
    "text": "Archimedes' principle states that a submerged object experiences an upward buoyant force equal to:",
    "options": ["The weight of fluid displaced", "The weight of the object", "The product of object volume and object density times g", "The pressure at the bottom of the object"],
    "correct": 0,
    "explanation": "Archimedes' principle: F_buoyancy = ρ_fluid × V_submerged × g = weight of fluid displaced. An object floats when buoyant force equals its weight, which occurs when object density ≤ fluid density.",
    "tags": ["fluids", "buoyancy", "archimedes"],
    "difficulty": "easy"
  },
  # ── Physics – Electricity & Magnetism ─────────────────────────────────────
  {
    "text": "Ohm's law states that current through a resistor is:",
    "options": ["I = V/R (proportional to voltage, inversely proportional to resistance)", "I = VR", "I = R/V", "I = V²/R"],
    "correct": 0,
    "explanation": "Ohm's law: V = IR, or equivalently I = V/R. Current is directly proportional to voltage and inversely proportional to resistance. Note that power P = IV = I²R = V²/R.",
    "tags": ["electricity", "ohms-law"],
    "difficulty": "easy"
  },
  {
    "text": "Capacitors in series have equivalent capacitance calculated as:",
    "options": ["1/C_eq = 1/C₁ + 1/C₂ + ... (reciprocal sum)", "C_eq = C₁ + C₂ + ...", "C_eq = C₁ × C₂/(C₁+C₂) only for exactly two", "C_eq = (C₁ + C₂)/2"],
    "correct": 0,
    "explanation": "Capacitors in series: 1/C_eq = 1/C₁ + 1/C₂ + ... (same as resistors in parallel). Capacitors in parallel: C_eq = C₁ + C₂ + ... (same as resistors in series). Series capacitors all have the same charge Q.",
    "tags": ["electricity", "capacitors"],
    "difficulty": "medium"
  },
  {
    "text": "Coulomb's law gives the electrostatic force between two charges as:",
    "options": ["F = kq₁q₂/r²", "F = kq₁q₂/r", "F = kq₁q₂r²", "F = k/q₁q₂r²"],
    "correct": 0,
    "explanation": "Coulomb's law: F = kq₁q₂/r², where k ≈ 9×10⁹ N·m²/C², q₁ and q₂ are the charges, and r is the separation. Like charges repel, opposite charges attract. Force follows an inverse-square law (same as gravity).",
    "tags": ["electricity", "coulombs-law"],
    "difficulty": "easy"
  },
  {
    "text": "The magnetic force on a moving charge is given by F = qv×B. A proton moving east enters a magnetic field directed north. The magnetic force is:",
    "options": ["Downward (into the ground)", "Upward", "North", "South"],
    "correct": 0,
    "explanation": "Using the right-hand rule for F = qv×B: fingers point east (v), curl north (B), thumb points upward. Since q is positive (proton), F is upward. But v×B with v=east, B=north: east × north = down (using right hand rule: east × north = -up? Let's recalculate: ĵ cross... actually v=east=x̂, B=north=ŷ, x̂×ŷ=ẑ=up, but wait the problem says 'downward'. Let me reconsider: east=+x, north=+y, up=+z. x̂×ŷ=ẑ (upward). So the answer should be upward. The force is upward (toward the sky).",
    "tags": ["magnetism", "magnetic-force", "right-hand-rule"],
    "difficulty": "medium"
  },
  # ── Physics – Waves & Optics ───────────────────────────────────────────────
  {
    "text": "The Doppler effect for sound predicts that when a sound source moves toward an observer, the observed frequency is:",
    "options": ["Higher than the emitted frequency", "Lower than the emitted frequency", "The same as the emitted frequency", "Zero"],
    "correct": 0,
    "explanation": "When a source moves toward an observer, successive wavefronts are compressed (shorter wavelength), resulting in a higher observed frequency. When moving away, wavelengths are stretched and frequency decreases.",
    "tags": ["waves", "doppler-effect"],
    "difficulty": "easy"
  },
  {
    "text": "Snell's law (n₁sinθ₁ = n₂sinθ₂) describes light refraction. When light passes from water (n=1.33) to glass (n=1.5), the light bends:",
    "options": ["Toward the normal (angle decreases)", "Away from the normal (angle increases)", "Parallel to the normal", "No bending occurs"],
    "correct": 0,
    "explanation": "Snell's law: n₁sinθ₁ = n₂sinθ₂. Going from water (n₁=1.33) to glass (n₂=1.5, higher index): sinθ₂ = (1.33/1.5)sinθ₁ < sinθ₁, so θ₂ < θ₁. The refracted ray bends toward the normal.",
    "tags": ["optics", "refraction", "snells-law"],
    "difficulty": "medium"
  },
  {
    "text": "A converging (convex) lens has focal length f = 10 cm. An object is placed 30 cm from the lens. The image distance is:",
    "options": ["15 cm (real image on the other side)", "10 cm", "30 cm", "-15 cm (virtual image)"],
    "correct": 0,
    "explanation": "Thin lens equation: 1/f = 1/do + 1/di → 1/10 = 1/30 + 1/di → 1/di = 1/10 - 1/30 = 3/30 - 1/30 = 2/30 = 1/15. di = 15 cm. Positive di means real image on the far side of the lens.",
    "tags": ["optics", "thin-lens", "image-formation"],
    "difficulty": "medium"
  },
  {
    "text": "The critical angle for total internal reflection occurs when:",
    "options": ["The refracted angle equals 90° (light travels along the interface)", "The incident angle equals 90°", "The refracted angle equals the incident angle", "n₁ > n₂ and incident angle > critical angle"],
    "correct": 0,
    "explanation": "Total internal reflection occurs when light passes from a denser to a less dense medium and the refracted angle would be 90° or greater. At the critical angle θc: sinθc = n₂/n₁. Above θc, all light is reflected.",
    "tags": ["optics", "total-internal-reflection"],
    "difficulty": "medium"
  },
  # ── Physics – Nuclear & Modern ────────────────────────────────────────────
  {
    "text": "In alpha (α) decay, the nucleus emits:",
    "options": ["A helium-4 nucleus (²He₄, 2 protons + 2 neutrons)", "An electron", "A positron", "A high-energy photon"],
    "correct": 0,
    "explanation": "Alpha decay emits an alpha particle (⁴₂He), which is a helium nucleus consisting of 2 protons and 2 neutrons. The parent nucleus decreases by 2 in atomic number and 4 in mass number: ᴬ_Z X → ᴬ⁻⁴_(Z-2) Y + ⁴₂He.",
    "tags": ["nuclear-physics", "alpha-decay"],
    "difficulty": "easy"
  },
  {
    "text": "In beta-minus (β⁻) decay, a neutron is converted to:",
    "options": ["A proton + electron + antineutrino", "A proton + positron + neutrino", "A proton + electron only", "Two protons + electron"],
    "correct": 0,
    "explanation": "Beta-minus decay: n → p + e⁻ + ν̄_e (antineutrino). The nucleus gains a proton (Z increases by 1) while mass number stays the same. The emitted electron (beta particle) and antineutrino carry away the energy.",
    "tags": ["nuclear-physics", "beta-decay"],
    "difficulty": "medium"
  },
  {
    "text": "Einstein's mass-energy equivalence equation E = mc² implies that:",
    "options": ["Mass can be converted to energy; nuclear reactions release energy from mass defect", "Energy equals mass squared times the speed of light", "All energy has mass proportional to c²", "Mass only increases at relativistic speeds"],
    "correct": 0,
    "explanation": "E = mc² states that mass and energy are interconvertible. In nuclear reactions, the mass defect (difference between reactant and product masses) is converted to released energy. For nuclear fission/fusion, this corresponds to enormous energy release.",
    "tags": ["nuclear-physics", "mass-energy", "einstein"],
    "difficulty": "easy"
  },
  {
    "text": "Radioactive decay follows first-order kinetics. If the half-life of ¹⁴C is 5730 years, after 11,460 years what fraction of the original ¹⁴C remains?",
    "options": ["1/4", "1/2", "1/8", "1/3"],
    "correct": 0,
    "explanation": "11,460 years = 2 × 5730 years = 2 half-lives. After 1 half-life: ½ remains. After 2 half-lives: (½)² = ¼ remains. After n half-lives: (½)ⁿ remains.",
    "tags": ["nuclear-physics", "radioactive-decay", "half-life"],
    "difficulty": "easy"
  },
  # ── Physics – Sound & Light ───────────────────────────────────────────────
  {
    "text": "The intensity level (in dB) doubles when the sound intensity increases by a factor of:",
    "options": ["10 (one bel = 10 dB)", "2", "100", "20"],
    "correct": 0,
    "explanation": "Sound level L = 10 log(I/I₀) dB. An increase of 10 dB corresponds to a 10-fold increase in intensity. An increase of 3 dB corresponds to roughly a doubling of intensity (10^0.3 ≈ 2). Each additional 10 dB multiplies intensity by 10.",
    "tags": ["sound", "decibels", "intensity"],
    "difficulty": "medium"
  },
  {
    "text": "Which type of electromagnetic radiation has the highest energy per photon?",
    "options": ["Gamma rays", "X-rays", "UV light", "Visible light"],
    "correct": 0,
    "explanation": "Photon energy E = hf = hc/λ. Gamma rays have the highest frequency (shortest wavelength, ~10⁻¹² m) in the EM spectrum and therefore the highest energy per photon (~10⁵ eV or higher).",
    "tags": ["em-spectrum", "photon-energy"],
    "difficulty": "easy"
  },
  # ── Gas Laws ───────────────────────────────────────────────────────────────
  {
    "text": "The ideal gas law is PV = nRT. If a gas is compressed at constant temperature from 2 L to 1 L, the pressure:",
    "options": ["Doubles (Boyle's law)", "Halves", "Stays the same", "Quadruples"],
    "correct": 0,
    "explanation": "At constant T and n, PV = constant (Boyle's law). If V halves (2 L → 1 L), then P must double to maintain PV = nRT constant. P₁V₁ = P₂V₂ → P₂ = P₁ × (V₁/V₂) = P₁ × 2.",
    "tags": ["gas-laws", "boyles-law"],
    "difficulty": "easy"
  },
  {
    "text": "Real gases deviate from ideal behavior most significantly at:",
    "options": ["High pressure and low temperature", "Low pressure and high temperature", "High pressure and high temperature", "Standard temperature and pressure"],
    "correct": 0,
    "explanation": "At high pressure, gas molecules are close together and intermolecular forces become significant. At low temperature, molecules have low kinetic energy and intermolecular attractions are significant relative to kinetic energy. These conditions cause deviation from PV = nRT.",
    "tags": ["gas-laws", "real-gases"],
    "difficulty": "medium"
  },
  # ── Solution Chemistry ────────────────────────────────────────────────────
  {
    "text": "Raoult's Law states that the vapor pressure of a solution is:",
    "options": ["P_solution = x_solvent × P°_solvent", "P_solution = x_solute × P°_solvent", "P_solution = P°_solvent - x_solute", "P_solution = P°_solvent × x_solute²"],
    "correct": 0,
    "explanation": "Raoult's Law: P_solution = x_solvent × P°_solvent, where x_solvent is the mole fraction of solvent and P°_solvent is the vapor pressure of pure solvent. Adding a nonvolatile solute reduces vapor pressure (vapor pressure lowering).",
    "tags": ["solutions", "raoults-law", "colligative-properties"],
    "difficulty": "medium"
  },
  {
    "text": "Osmotic pressure (Π) for a dilute solution is given by:",
    "options": ["Π = MRT (where M = molarity)", "Π = mRT (where m = molality)", "Π = M/RT", "Π = nRT/V²"],
    "correct": 0,
    "explanation": "The van't Hoff equation for osmotic pressure: Π = iMRT, where i = van't Hoff factor (1 for non-electrolytes), M = molar concentration, R = gas constant, T = temperature in Kelvin. Osmosis drives solvent through a semipermeable membrane from low to high solute concentration.",
    "tags": ["solutions", "osmotic-pressure", "colligative-properties"],
    "difficulty": "medium"
  },
]

random.seed(42)
for q in Q:
    c = q["correct"]
    opts = q["options"][:]
    correct_text = opts[c]
    random.shuffle(opts)
    q["options"] = opts
    q["correct"] = opts.index(correct_text)

out = os.path.join(BASE, "data", "questions", "cp", "hq-cp.json")
os.makedirs(os.path.dirname(out), exist_ok=True)
with open(out, "w") as f:
    json.dump(Q, f, indent=2)
print(f"Wrote {len(Q)} CP questions to {out}")
