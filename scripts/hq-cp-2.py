#!/usr/bin/env python3
import json, os, random

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

Q = [
  # ── Stoichiometry & Solutions ──────────────────────────────────────────
  {
    "text": "In the reaction 2H₂ + O₂ → 2H₂O, 4 moles of H₂ react with 1 mole of O₂. What is the limiting reagent?",
    "options": ["O₂", "H₂", "H₂O", "Neither — both are consumed equally"],
    "correct": 0,
    "explanation": "The stoichiometric ratio requires 2 mol H₂ per 1 mol O₂. With 4 mol H₂ and 1 mol O₂, H₂:O₂ = 4:1 but the required ratio is 2:1, so H₂ is in excess. O₂ is the limiting reagent.",
    "tags": ["stoichiometry", "limiting-reagent"],
    "difficulty": "easy"
  },
  {
    "text": "The empirical formula of a compound is CH₂O and its molecular weight is 180 g/mol. Its molecular formula is:",
    "options": ["C₆H₁₂O₆", "C₃H₆O₃", "C₂H₄O₂", "CH₂O"],
    "correct": 0,
    "explanation": "Empirical formula CH₂O has mass = 12+2+16 = 30 g/mol. 180/30 = 6. Molecular formula = (CH₂O)₆ = C₆H₁₂O₆, which is glucose.",
    "tags": ["stoichiometry", "molecular-formula"],
    "difficulty": "easy"
  },
  {
    "text": "To prepare 500 mL of a 0.2 M NaCl solution from a 2.0 M stock, how much stock solution is needed?",
    "options": ["50 mL", "100 mL", "25 mL", "200 mL"],
    "correct": 0,
    "explanation": "M₁V₁ = M₂V₂: (2.0)(V₁) = (0.2)(500) → V₁ = 50 mL. Add 50 mL stock and dilute to 500 mL total.",
    "tags": ["solutions", "dilution"],
    "difficulty": "easy"
  },
  {
    "text": "Percent composition of oxygen in glucose (C₆H₁₂O₆, MW = 180 g/mol) is:",
    "options": ["53.3%", "40.0%", "26.7%", "6.7%"],
    "correct": 0,
    "explanation": "6 oxygen atoms × 16 g/mol = 96 g/mol. (96/180) × 100 = 53.3%.",
    "tags": ["stoichiometry", "percent-composition"],
    "difficulty": "easy"
  },
  {
    "text": "Molality (m) differs from molarity (M) in that molality is defined as:",
    "options": ["Moles of solute per kilogram of solvent", "Moles of solute per liter of solution", "Moles of solute per mole of solution", "Grams of solute per liter of solution"],
    "correct": 0,
    "explanation": "Molality = moles solute / kg solvent. Unlike molarity, molality doesn't change with temperature because mass is temperature-independent. Molality is used for colligative property calculations.",
    "tags": ["solutions", "molality"],
    "difficulty": "easy"
  },
  {
    "text": "A 1.0 m NaCl solution causes approximately what freezing point depression? (Kf water = 1.86°C/m)",
    "options": ["3.72°C", "1.86°C", "0.93°C", "5.58°C"],
    "correct": 0,
    "explanation": "ΔTf = i × Kf × m. NaCl dissociates into 2 ions (i ≈ 2). ΔTf = 2 × 1.86 × 1.0 = 3.72°C.",
    "tags": ["solutions", "colligative-properties", "freezing-point-depression"],
    "difficulty": "medium"
  },
  # ── Organic: Alcohols, Aldehydes, Ketones ────────────────────────────────
  {
    "text": "Oxidation of a primary alcohol with PCC produces:",
    "options": ["An aldehyde (reaction stops at aldehyde stage)", "A carboxylic acid", "A ketone", "An ether"],
    "correct": 0,
    "explanation": "PCC (pyridinium chlorochromate) is a mild oxidant that converts primary alcohols to aldehydes without further oxidation to carboxylic acids. Strong oxidants (KMnO₄, K₂Cr₂O₇) fully oxidize primary alcohols to carboxylic acids.",
    "tags": ["organic-chemistry", "alcohol-oxidation", "pcc"],
    "difficulty": "medium"
  },
  {
    "text": "A ketone differs from an aldehyde in that the carbonyl carbon in a ketone is bonded to:",
    "options": ["Two carbon substituents (no C-H bond at the carbonyl)", "At least one hydrogen", "An oxygen and a nitrogen", "Two oxygen atoms"],
    "correct": 0,
    "explanation": "Ketone: R-CO-R' (two carbon groups flanking the carbonyl). Aldehyde: R-CHO (one carbon group and one hydrogen at the carbonyl). This structural difference makes ketones more resistant to oxidation than aldehydes.",
    "tags": ["organic-chemistry", "ketones", "aldehydes"],
    "difficulty": "easy"
  },
  {
    "text": "An acetal forms when an aldehyde reacts with:",
    "options": ["Two equivalents of alcohol under acid catalysis with loss of water", "One equivalent of alcohol under base catalysis", "An amine and an alcohol", "Water under acid catalysis"],
    "correct": 0,
    "explanation": "Acetal formation: RCHO + 2R'OH ⇌ RCH(OR')₂ + H₂O (acid-catalyzed, reversible). First step gives hemiacetal; second step replaces -OH with -OR'. Acetals are used as carbonyl protecting groups.",
    "tags": ["organic-chemistry", "acetal"],
    "difficulty": "medium"
  },
  {
    "text": "The Wittig reaction converts a carbonyl compound to:",
    "options": ["An alkene (C=C), replacing C=O", "An alcohol", "An ester", "An epoxide"],
    "correct": 0,
    "explanation": "Wittig reaction: carbonyl (C=O) + phosphorus ylide (Ph₃P=CHR) → alkene (C=C) + triphenylphosphine oxide (Ph₃P=O). This reaction creates alkenes of defined geometry and is valuable in organic synthesis.",
    "tags": ["organic-chemistry", "wittig-reaction"],
    "difficulty": "hard"
  },
  {
    "text": "Secondary alcohols are oxidized by chromic acid to give:",
    "options": ["Ketones", "Aldehydes", "Carboxylic acids", "Primary alcohols"],
    "correct": 0,
    "explanation": "Oxidation of a secondary alcohol (R-CHOH-R') gives a ketone (R-CO-R') by removal of H₂. Ketones cannot be further oxidized under typical conditions because the carbonyl carbon has no H-C bond to oxidize.",
    "tags": ["organic-chemistry", "alcohol-oxidation"],
    "difficulty": "easy"
  },
  # ── Organic: Carboxylic Acids & Derivatives ────────────────────────────────
  {
    "text": "Which carboxylic acid derivative is most reactive toward nucleophilic acyl substitution?",
    "options": ["Acyl chloride (acid chloride)", "Ester", "Amide", "Carboxylic acid itself"],
    "correct": 0,
    "explanation": "Reactivity order: acid chlorides > anhydrides > esters > carboxylic acids >> amides. Acid chlorides are most reactive because Cl⁻ is an excellent leaving group and provides minimal resonance stabilization. Amides are least reactive due to strong N lone-pair donation into C=O.",
    "tags": ["organic-chemistry", "acyl-substitution"],
    "difficulty": "medium"
  },
  {
    "text": "Saponification is the base-catalyzed hydrolysis of an ester to produce:",
    "options": ["A carboxylate salt and an alcohol", "A carboxylic acid and an alcohol", "An amide and water", "An anhydride"],
    "correct": 0,
    "explanation": "Saponification: R-COO-R' + NaOH → R-COO⁻Na⁺ + R'OH. The base drives the reaction to completion by forming the resonance-stabilized carboxylate ion. This is the basis of soap-making from triglycerides.",
    "tags": ["organic-chemistry", "saponification"],
    "difficulty": "easy"
  },
  {
    "text": "The Claisen condensation between two ester molecules produces:",
    "options": ["A β-keto ester (after loss of alkoxide)", "An aldehyde", "A secondary alcohol", "A dicarboxylic acid"],
    "correct": 0,
    "explanation": "In the Claisen condensation, an ester enolate attacks the carbonyl of another ester. The alkoxide leaves, yielding a β-keto ester. This is mechanistically analogous to the aldol condensation (enolate + carbonyl electrophile) but uses esters instead of aldehydes/ketones.",
    "tags": ["organic-chemistry", "claisen-condensation"],
    "difficulty": "hard"
  },
  {
    "text": "Carboxylic acids are more acidic than alcohols because:",
    "options": ["The carboxylate anion is stabilized by resonance delocalization over both oxygens", "The O-H bond in carboxylic acids is longer", "Carboxylic acids have higher molecular weight", "Only inductive effects make them more acidic"],
    "correct": 0,
    "explanation": "Carboxylate anion (-COO⁻) has the negative charge delocalized over two equivalent oxygens via resonance. Alkoxide ions (-O⁻) have no resonance stabilization. Greater stabilization of conjugate base → stronger acid. Electron-withdrawing groups nearby further increase acidity by induction.",
    "tags": ["organic-chemistry", "acidity", "carboxylic-acids"],
    "difficulty": "medium"
  },
  # ── Organic: Amines & Aromatic Chemistry ─────────────────────────────────
  {
    "text": "Which amine is the most basic?",
    "options": ["Diethylamine (alkyl groups donate electrons by induction)", "Aniline (lone pair delocalized into aromatic ring)", "Acetamide (lone pair delocalized into C=O)", "Pyrrole (lone pair is part of the aromatic π system)"],
    "correct": 0,
    "explanation": "Basicity requires an available nitrogen lone pair. Diethylamine (pKaH ~11) has two alkyl groups donating electron density. Aniline (pKaH ~5) has lone pair partially delocalized into the benzene ring. Amides (pKaH ~0) and pyrrole are nearly non-basic for the same reason.",
    "tags": ["organic-chemistry", "amines", "basicity"],
    "difficulty": "medium"
  },
  {
    "text": "Electron-donating groups (like -OH) on benzene direct electrophilic substitution to which positions?",
    "options": ["Ortho and para positions", "Meta position only", "All positions equally", "Ipso position only"],
    "correct": 0,
    "explanation": "EDGs like -OH and -NH₂ stabilize the Wheland intermediate (carbocation) at ortho/para positions by resonance. They activate the ring and direct to ortho/para. EWGs like -NO₂ destabilize carbocation at ortho/para but not meta, directing to meta.",
    "tags": ["organic-chemistry", "eas", "directing-effects"],
    "difficulty": "medium"
  },
  {
    "text": "Benzene's extraordinary stability (aromatic stabilization) arises from:",
    "options": ["6 π electrons delocalized in a cyclic conjugated system (4n+2, n=1, Hückel's rule)", "Three isolated double bonds", "Six sp³ carbons", "Resonance between two Kekulé structures only"],
    "correct": 0,
    "explanation": "Hückel's rule: cyclic, planar, fully conjugated systems with 4n+2 π electrons are aromatic. Benzene (n=1, 6 π electrons) has complete delocalization over all 6 carbons, giving 36 kcal/mol stabilization energy compared to a hypothetical cyclohexatriene with isolated double bonds.",
    "tags": ["organic-chemistry", "aromaticity", "huckel"],
    "difficulty": "medium"
  },
  {
    "text": "Nucleophilic aromatic substitution (NAS) requires the aromatic ring to be:",
    "options": ["Electron-poor, with EWGs at ortho/para to the leaving group", "Electron-rich with EDGs activating the ring", "Unsubstituted for maximum reactivity", "Protonated (in acid solution)"],
    "correct": 0,
    "explanation": "NAS proceeds through a Meisenheimer complex (anionic σ-complex). EWGs at ortho/para to the leaving group stabilize this intermediate by delocalizing the negative charge onto their electronegative atoms. 2,4-Dinitrochlorobenzene readily undergoes NAS; chlorobenzene does not.",
    "tags": ["organic-chemistry", "nas"],
    "difficulty": "hard"
  },
  # ── Separation & Purification ───────────────────────────────────────────
  {
    "text": "In TLC using silica gel, a compound with a high Rf value is:",
    "options": ["Relatively nonpolar (higher affinity for mobile phase than polar stationary phase)", "Highly polar and retained by silica", "High molecular weight", "Charged at the pH of the mobile phase"],
    "correct": 0,
    "explanation": "Rf = distance compound moves / distance solvent front moves. On polar silica gel, nonpolar compounds interact weakly with the stationary phase and move far with the mobile phase (high Rf). Polar compounds interact strongly with silica and barely move (low Rf).",
    "tags": ["separation", "tlc"],
    "difficulty": "easy"
  },
  {
    "text": "In gel filtration (size-exclusion) chromatography, larger proteins elute:",
    "options": ["First (excluded from pores, travel only through void volume)", "Last (enter pores and take longer path)", "At the same time as small proteins", "Only with high ionic strength buffer"],
    "correct": 0,
    "explanation": "Gel filtration: porous beads exclude large molecules that cannot fit into the pores. Large molecules travel through the interstitial (void) volume and elute first. Small molecules enter the pores, travel a longer effective path, and elute later. This is the inverse of most chromatographic methods.",
    "tags": ["separation", "size-exclusion-chromatography"],
    "difficulty": "medium"
  },
  {
    "text": "When extracting benzoic acid (pKa 4.2) from an ether solution using aqueous NaHCO₃ (pKa of H₂CO₃ ≈ 6.4), benzoic acid:",
    "options": ["Deprotonates to benzoate and moves to aqueous layer", "Remains in ether (too nonpolar for water)", "Decomposes in base", "Requires NaOH, not NaHCO₃"],
    "correct": 0,
    "explanation": "NaHCO₃ is basic enough to deprotonate carboxylic acids (pKa ~4-5) because pKa of H₂CO₃ > pKa of benzoic acid. Benzoate anion is charged and water-soluble, moving to the aqueous layer. Neutral compounds remain in the organic phase. NaHCO₃ does NOT deprotonate phenols (pKa ~10).",
    "tags": ["separation", "extraction", "acid-base"],
    "difficulty": "medium"
  },
  {
    "text": "Gas chromatography (GC) separates volatile compounds primarily based on:",
    "options": ["Differential volatility and interaction with the stationary phase", "Molecular weight alone", "Charge and polarity in an aqueous mobile phase", "Affinity for specific antibodies"],
    "correct": 0,
    "explanation": "GC carries vaporized analytes through a column with an inert carrier gas (mobile phase). Separation depends on boiling point (volatility) and interaction with the stationary phase liquid/solid coating. Lower boiling or more volatile compounds elute first.",
    "tags": ["separation", "gas-chromatography"],
    "difficulty": "easy"
  },
  # ── Thermodynamics Advanced ────────────────────────────────────────────────
  {
    "text": "A Carnot engine operates between 800 K (hot) and 400 K (cold). Its maximum efficiency is:",
    "options": ["50%", "25%", "75%", "100%"],
    "correct": 0,
    "explanation": "Carnot efficiency = 1 - Tc/Th = 1 - 400/800 = 0.50 = 50%. This is the theoretical maximum; no real engine can exceed it for these temperatures.",
    "tags": ["thermodynamics", "carnot"],
    "difficulty": "medium"
  },
  {
    "text": "State functions like enthalpy (H), entropy (S), and Gibbs free energy (G) have what property for cyclic processes?",
    "options": ["ΔX = 0 (they return to their initial value)", "They increase monotonically", "They depend on path taken", "They are undefined for cyclic processes"],
    "correct": 0,
    "explanation": "State functions depend only on the current state, not on the path. For any process that returns to the initial state (cyclic), ΔH = ΔS = ΔG = ΔU = 0. Heat (q) and work (w) are path functions and need not be zero in a cycle.",
    "tags": ["thermodynamics", "state-functions"],
    "difficulty": "medium"
  },
  {
    "text": "Boiling point elevation ΔTb for a 1.0 m sucrose solution (i=1) in water (Kb = 0.512°C/m) is:",
    "options": ["0.512°C", "1.86°C", "1.024°C", "0.256°C"],
    "correct": 0,
    "explanation": "ΔTb = i × Kb × m = 1 × 0.512 × 1.0 = 0.512°C. So the solution boils at 100.512°C instead of 100°C. For electrolytes, use i = number of ions (e.g., NaCl has i ≈ 2, so ΔTb would be doubled).",
    "tags": ["thermodynamics", "colligative-properties"],
    "difficulty": "easy"
  },
  {
    "text": "The Van't Hoff factor (i) for MgCl₂ fully dissociated in solution is:",
    "options": ["3 (Mg²⁺ + 2 Cl⁻ = 3 particles)", "2", "1", "4"],
    "correct": 0,
    "explanation": "MgCl₂ → Mg²⁺ + 2Cl⁻, producing 3 ions per formula unit. i = 3 for complete dissociation. In reality, ion pairing reduces i slightly below 3, but for MCAT purposes i = 3 is used. This triples the colligative effect compared to a non-electrolyte.",
    "tags": ["solutions", "vant-hoff-factor"],
    "difficulty": "easy"
  },
  # ── Electrochemistry ─────────────────────────────────────────────────────
  {
    "text": "To balance MnO₄⁻ → Mn²⁺ in acidic solution as a half-reaction, what is added?",
    "options": ["8H⁺ and 5e⁻ on the left, 4H₂O on the right", "4H₂O on the left and 8OH⁻ on the right", "5e⁻ only on the left", "4H₂O and 8H⁺ on the right"],
    "correct": 0,
    "explanation": "Balance O: add 4H₂O right. Balance H: add 8H⁺ left. Balance charge: left = -1+8 = +7; right = +2; add 5e⁻ to left: +7-5 = +2. Result: MnO₄⁻ + 8H⁺ + 5e⁻ → Mn²⁺ + 4H₂O.",
    "tags": ["electrochemistry", "balancing-half-reactions"],
    "difficulty": "hard"
  },
  {
    "text": "In an electrolytic cell, the cathode is connected to the:",
    "options": ["Negative terminal of the power source; reduction occurs here", "Positive terminal; oxidation occurs here", "Ground; no reaction occurs", "Positive terminal; reduction occurs here"],
    "correct": 0,
    "explanation": "In electrolytic cells, an external power source forces non-spontaneous reactions. The cathode (negative terminal of power source) receives electrons — reduction occurs (cations migrate here). The anode (positive terminal) accepts electrons — oxidation occurs (anions migrate here).",
    "tags": ["electrochemistry", "electrolytic-cell"],
    "difficulty": "medium"
  },
  {
    "text": "Iron rusts (corrodes) electrochemically because iron acts as:",
    "options": ["The anode (oxidized: Fe → Fe²⁺ + 2e⁻) while O₂ is reduced at cathodic areas", "The cathode (reduced)", "A neutral spectator", "An oxidizing agent consuming oxygen"],
    "correct": 0,
    "explanation": "Rusting is an electrochemical process: anodic areas: Fe → Fe²⁺ + 2e⁻; cathodic areas: O₂ + 4H⁺ + 4e⁻ → 2H₂O. Galvanizing with zinc makes zinc the sacrificial anode, protecting the iron beneath.",
    "tags": ["electrochemistry", "corrosion"],
    "difficulty": "medium"
  },
  {
    "text": "The standard hydrogen electrode (SHE) is assigned E° = 0 V because:",
    "options": ["It is chosen as the reference standard; all other E° values are measured relative to it", "Hydrogen has zero reduction potential by nature", "H⁺ has no charge and thus no electrode potential", "It produces no detectable current"],
    "correct": 0,
    "explanation": "The SHE (Pt electrode, 1 M H⁺, H₂ gas at 1 atm) is the arbitrary reference point (E° = 0.00 V by convention). All standard reduction potentials in tables are measured relative to the SHE. This allows direct subtraction to calculate cell potentials.",
    "tags": ["electrochemistry", "standard-hydrogen-electrode"],
    "difficulty": "easy"
  },
  # ── Physics: Circuits ────────────────────────────────────────────────────
  {
    "text": "Three resistors (2Ω, 4Ω, 6Ω) connected in parallel have equivalent resistance:",
    "options": ["≈ 1.09 Ω", "12 Ω", "4 Ω", "0.5 Ω"],
    "correct": 0,
    "explanation": "1/R_eq = 1/2 + 1/4 + 1/6 = 6/12 + 3/12 + 2/12 = 11/12. R_eq = 12/11 ≈ 1.09 Ω. Parallel resistance is always less than the smallest individual resistor.",
    "tags": ["circuits", "parallel-resistors"],
    "difficulty": "medium"
  },
  {
    "text": "The time constant τ = RC for an RC circuit represents:",
    "options": ["The time for the capacitor to reach ~63% of full charge (or decay to ~37%)", "The time to fully charge the capacitor (100%)", "The oscillation period", "The time for current to reach zero"],
    "correct": 0,
    "explanation": "Q(t) = Q_max(1 - e^(-t/RC)). At t = τ = RC, Q = Q_max(1 - e⁻¹) ≈ 0.632 Q_max. After 5τ, the capacitor is >99% charged. During discharge: Q = Q₀e^(-t/RC), so at t = τ, Q ≈ 0.368 Q₀.",
    "tags": ["circuits", "rc-circuit"],
    "difficulty": "medium"
  },
  {
    "text": "Kirchhoff's voltage law (KVL) states:",
    "options": ["The sum of all voltage changes around any closed loop equals zero", "Current into a node equals current out", "Resistance equals voltage divided by current", "Power equals current squared times resistance"],
    "correct": 0,
    "explanation": "KVL (conservation of energy): ΣV = 0 around any closed loop. Electric potential is a state function — returning to the starting point means net ΔV = 0. KCL (Kirchhoff's current law): ΣI = 0 at any node (conservation of charge).",
    "tags": ["circuits", "kvl", "kirchhoffs-laws"],
    "difficulty": "easy"
  },
  {
    "text": "Faraday's law of electromagnetic induction: induced EMF is proportional to:",
    "options": ["The rate of change of magnetic flux (dΦ_B/dt)", "The magnitude of the magnetic field", "The resistance of the conductor", "The charge on moving particles"],
    "correct": 0,
    "explanation": "Faraday's law: EMF = -dΦ_B/dt (where Φ_B = B·A·cosθ). The negative sign reflects Lenz's law: induced current opposes the flux change. This is the basis for electric generators, transformers, and inductive charging.",
    "tags": ["magnetism", "electromagnetic-induction"],
    "difficulty": "medium"
  },
  {
    "text": "A step-up transformer has 100 primary turns and 500 secondary turns. If the primary voltage is 120 V, the secondary voltage is:",
    "options": ["600 V", "24 V", "120 V", "60 V"],
    "correct": 0,
    "explanation": "V_s/V_p = N_s/N_p → V_s = 120 × (500/100) = 600 V. Voltage is stepped up by a factor of 5. By power conservation, current is stepped down by the same factor (I_s = I_p × N_p/N_s = I_p/5).",
    "tags": ["magnetism", "transformer"],
    "difficulty": "medium"
  },
  # ── Physics: Work, Energy, SHM ────────────────────────────────────────────
  {
    "text": "A 2 kg block slides down a frictionless 5 m incline from height h = 5 m. Its speed at the bottom is: (g=10 m/s²)",
    "options": ["10 m/s", "5 m/s", "7.1 m/s", "14.1 m/s"],
    "correct": 0,
    "explanation": "Conservation of energy: mgh = ½mv² → v = √(2gh) = √(2×10×5) = √100 = 10 m/s. Mass cancels — all masses reach the same speed from the same height on frictionless inclines.",
    "tags": ["mechanics", "energy-conservation"],
    "difficulty": "easy"
  },
  {
    "text": "Period of a simple pendulum depends on:",
    "options": ["Length and gravitational acceleration only: T = 2π√(L/g)", "Mass and length", "Mass, length, and amplitude", "Amplitude alone"],
    "correct": 0,
    "explanation": "For small oscillations, T = 2π√(L/g). The period is independent of both mass and amplitude (isochronism). A 1 m pendulum on Earth has T = 2π√(1/9.8) ≈ 2.0 s. On the Moon (g = 1.6 m/s²), the same pendulum would swing about 2.5 times more slowly.",
    "tags": ["mechanics", "pendulum", "shm"],
    "difficulty": "easy"
  },
  {
    "text": "At maximum displacement in SHM, the energy distribution is:",
    "options": ["All potential energy (KE = 0, PE = ½kA²)", "All kinetic energy (PE = 0)", "Equal KE and PE", "Total energy is zero"],
    "correct": 0,
    "explanation": "In SHM: total energy E = ½kA² = constant. At maximum displacement (x = A), velocity = 0 so KE = 0 and all energy is stored as elastic PE = ½kA². At equilibrium (x = 0), PE = 0 and KE = ½kA² is maximum.",
    "tags": ["mechanics", "shm", "energy"],
    "difficulty": "easy"
  },
  {
    "text": "A motor lifts a 100 kg load 10 m in 5 s. The power output is: (g=10 m/s²)",
    "options": ["2000 W", "1000 W", "200 W", "10000 W"],
    "correct": 0,
    "explanation": "W = mgh = 100×10×10 = 10,000 J. P = W/t = 10,000/5 = 2000 W = 2 kW.",
    "tags": ["mechanics", "power"],
    "difficulty": "easy"
  },
  {
    "text": "Resonance occurs when the driving frequency equals the system's natural frequency. In an underdamped oscillator, near resonance the amplitude:",
    "options": ["Grows dramatically (becomes very large for low damping)", "Stays constant regardless of frequency", "Immediately decreases", "Equals the driving amplitude exactly"],
    "correct": 0,
    "explanation": "Resonance transfers energy most efficiently from driver to oscillator. In lightly damped systems, resonance amplitude can be many times the driving amplitude. Heavy damping flattens the resonance peak. Examples: Tacoma Narrows bridge, MRI, musical instrument resonance chambers.",
    "tags": ["mechanics", "resonance"],
    "difficulty": "medium"
  },
  # ── Physics: Light, Sound, Modern Physics ─────────────────────────────────
  {
    "text": "Young's double-slit experiment proves light has wave properties because it produces:",
    "options": ["Alternating bright and dark interference fringes from superposition", "Only bright fringes proportional to intensity", "No pattern at all", "A single bright spot at the center"],
    "correct": 0,
    "explanation": "Constructive interference (bright fringes): path difference = nλ. Destructive interference (dark fringes): (n+½)λ. This superposition requires wave behavior. Photons also create this pattern one at a time, demonstrating wave-particle duality.",
    "tags": ["optics", "double-slit", "interference"],
    "difficulty": "easy"
  },
  {
    "text": "The photoelectric effect shows that below the threshold frequency, electrons are not ejected even with intense light because:",
    "options": ["Photon energy E=hf must exceed the work function; intensity cannot compensate for insufficient frequency", "Electrons are too tightly bound at high frequency", "Intense light heats the metal but doesn't eject electrons", "Only ultraviolet light can ever eject electrons"],
    "correct": 0,
    "explanation": "Classical wave theory predicted any frequency would eject electrons given enough intensity. Einstein showed each photon has E=hf; if hf < work function (φ), no single photon has enough energy to eject an electron regardless of how many photons hit. Increasing intensity increases number of photons, not their energy.",
    "tags": ["modern-physics", "photoelectric-effect"],
    "difficulty": "medium"
  },
  {
    "text": "The de Broglie wavelength λ = h/mv implies that:",
    "options": ["All matter has wave properties; shorter wavelength for faster/heavier objects", "Only light has wave properties", "Heavier objects have longer wavelengths", "Wavelength is independent of speed"],
    "correct": 0,
    "explanation": "λ = h/mv: wavelength decreases as momentum (mv) increases. Fast, heavy objects have negligible wavelengths (undetectable quantum effects). Electrons moving at ~10⁶ m/s have λ ~10⁻¹⁰ m, comparable to atomic spacings — enabling electron microscopy.",
    "tags": ["modern-physics", "de-broglie"],
    "difficulty": "medium"
  },
  {
    "text": "Heisenberg's uncertainty principle (Δx·Δp ≥ ℏ/2) means that:",
    "options": ["The more precisely position is known, the less precisely momentum can be known, and vice versa", "Only one of position or momentum can ever be measured", "Uncertainty reflects only measurement imprecision, not fundamental limits", "Macroscopic objects are also governed by significant uncertainty"],
    "correct": 0,
    "explanation": "The uncertainty principle is a fundamental quantum mechanical limit, not a measurement artifact. Precisely localizing a particle (small Δx) requires a broad range of wave vectors (large Δp), and vice versa. For macroscopic objects, ℏ ≈ 10⁻³⁴ J·s makes this constraint negligible.",
    "tags": ["modern-physics", "heisenberg-uncertainty"],
    "difficulty": "medium"
  },
  {
    "text": "A string (fixed both ends, length L) forms standing waves. Which wavelengths are allowed?",
    "options": ["λ = 2L/n (n = 1, 2, 3, ...): nodes at both ends require integer half-wavelengths to fit", "λ = L/n (full wavelengths only)", "λ = 4L/n (quarter wavelengths)", "Any wavelength that is less than L"],
    "correct": 0,
    "explanation": "Boundary condition: displacement = 0 at both ends (two nodes). This requires L = n(λ/2) → λ = 2L/n. Fundamental (n=1): λ = 2L. Second harmonic (n=2): λ = L. Corresponding frequencies: f_n = nv/2L = nf₁.",
    "tags": ["waves", "standing-waves"],
    "difficulty": "medium"
  },
  {
    "text": "A closed organ pipe (one end closed, one open) of length L has its fundamental frequency at:",
    "options": ["f = v/4L (only odd harmonics present)", "f = v/2L (all harmonics present)", "f = v/L", "f = 2v/L"],
    "correct": 0,
    "explanation": "Closed pipe boundary conditions: node at closed end, antinode at open end. L = λ/4 for fundamental, so λ = 4L and f₁ = v/4L. Only odd harmonics (n = 1, 3, 5, ...) are supported because only these satisfy the boundary conditions.",
    "tags": ["waves", "standing-waves", "organ-pipe"],
    "difficulty": "hard"
  },
  # ── Gas Laws ───────────────────────────────────────────────────────────────
  {
    "text": "The van der Waals equation (P + a/V²)(V - b) = nRT corrects for:",
    "options": ["Intermolecular attractive forces (a) and finite molecular volume (b)", "Quantum effects at low temperature", "Gravitational attraction between gas molecules", "Ionic interactions in polar gases"],
    "correct": 0,
    "explanation": "For ideal gases, molecules have no volume and no intermolecular forces. Real gases deviate: 'a' reduces observed pressure (molecules attract each other, slowing before hitting walls). 'b' reduces available volume (molecules have finite size). Real gases most closely approach ideal behavior at high T and low P.",
    "tags": ["gas-laws", "van-der-waals"],
    "difficulty": "medium"
  },
  {
    "text": "Dalton's law of partial pressures: total pressure of a gas mixture equals:",
    "options": ["Sum of partial pressures: P_total = P₁ + P₂ + P₃ + ...", "Average of partial pressures", "Product of mole fractions times total pressure", "Pressure of the most abundant gas"],
    "correct": 0,
    "explanation": "Each gas in an ideal mixture behaves independently. Partial pressure P_i = x_i × P_total, where x_i is the mole fraction. The sum of all partial pressures equals total pressure. Used to calculate O₂ partial pressure in alveoli (accounting for water vapor and CO₂).",
    "tags": ["gas-laws", "daltons-law"],
    "difficulty": "easy"
  },
  {
    "text": "Graham's law of effusion: the rate of gas effusion is inversely proportional to the square root of molar mass. He (M=4) effuses how much faster than O₂ (M=32)?",
    "options": ["2.83 times faster (√8 = 2.83)", "8 times faster", "4 times faster", "1.41 times faster"],
    "correct": 0,
    "explanation": "Rate_He/Rate_O₂ = √(M_O₂/M_He) = √(32/4) = √8 ≈ 2.83. Lighter gases effuse faster. This principle is used in uranium enrichment (²³⁵UF₆ vs ²³⁸UF₆) and explains why helium balloons deflate faster than air-filled ones.",
    "tags": ["gas-laws", "grahams-law"],
    "difficulty": "medium"
  },
  # ── Nuclear Physics Additional ─────────────────────────────────────────────
  {
    "text": "Gamma (γ) emission from a nucleus:",
    "options": ["Releases energy as a photon; Z and A are unchanged", "Decreases Z by 2 and A by 4", "Increases Z by 1; A unchanged", "Decreases A by 1; Z unchanged"],
    "correct": 0,
    "explanation": "Gamma decay releases excess nuclear energy as a high-energy photon. No nucleons are emitted, so both Z and A remain the same. It typically follows alpha or beta decay as the product nucleus de-excites from a metastable state to its ground state.",
    "tags": ["nuclear-physics", "gamma-decay"],
    "difficulty": "easy"
  },
  {
    "text": "Positron emission (β⁺ decay) results in the nucleus:",
    "options": ["Decreasing Z by 1 while A remains the same (proton → neutron + positron + neutrino)", "Increasing Z by 1 while A remains the same", "Decreasing A by 1", "Decreasing both Z and A"],
    "correct": 0,
    "explanation": "β⁺: p → n + e⁺ + ν_e. The nucleus loses a proton and gains a neutron: Z decreases by 1, A unchanged. Used in PET scanning: ¹⁸F emits a positron which annihilates with an electron to produce two 511 keV gamma rays detected in coincidence.",
    "tags": ["nuclear-physics", "positron-emission"],
    "difficulty": "medium"
  },
  # ── Additional Mechanics ───────────────────────────────────────────────────
  {
    "text": "Angular momentum L = Iω is conserved when:",
    "options": ["No net external torque acts on the system", "No net external force acts", "Moment of inertia is constant", "Angular velocity is constant"],
    "correct": 0,
    "explanation": "dL/dt = τ_net. If τ_ext = 0, L is conserved. A figure skater pulling arms in decreases I; ω increases to maintain L = Iω = constant. Conservation of linear momentum (not angular) requires no net external force.",
    "tags": ["mechanics", "angular-momentum"],
    "difficulty": "medium"
  },
  {
    "text": "In an elastic collision between equal masses where one is initially at rest, the result is:",
    "options": ["The moving mass stops; the stationary mass moves with the original speed", "Both masses move at half the original speed", "The moving mass bounces back; both masses end at half speed", "The moving mass passes through with no change"],
    "correct": 0,
    "explanation": "For elastic collision of equal masses (m₁=m₂), with m₂ initially at rest: v₁' = 0 and v₂' = v₁ (initial speed). This follows from conserving both momentum and kinetic energy simultaneously. Newton's cradle demonstrates this exchange perfectly.",
    "tags": ["mechanics", "elastic-collision"],
    "difficulty": "medium"
  },
  {
    "text": "Gravitational potential energy near Earth's surface is U = mgh. This formula is valid only when:",
    "options": ["Height h is much smaller than Earth's radius (g is approximately constant)", "The object is at rest", "h is measured from Earth's center", "Mass is greater than 1 kg"],
    "correct": 0,
    "explanation": "g = GM/r² varies with distance from Earth's center. For h << R_Earth (~6400 km), g ≈ 9.8 m/s² is nearly constant and U = mgh is an excellent approximation. For large heights (satellites), U = -GMm/r (with the reference at infinity) must be used.",
    "tags": ["mechanics", "gravitational-potential-energy"],
    "difficulty": "medium"
  },
  # ── Optics Additional ─────────────────────────────────────────────────────
  {
    "text": "White light separating into colors when passing through a prism is called dispersion. The color that refracts most (bends most) is:",
    "options": ["Violet (shortest wavelength, highest index of refraction in glass)", "Red (longest wavelength)", "Green (middle wavelength)", "All colors bend equally"],
    "correct": 0,
    "explanation": "Dispersion: n varies with wavelength (higher n for shorter λ). By Snell's law, higher n means more bending. Violet light (λ ~400 nm) has higher n in glass than red (λ ~700 nm), so violet bends more. This is why rainbows have violet on the inside and red on the outside.",
    "tags": ["optics", "dispersion"],
    "difficulty": "easy"
  },
  {
    "text": "A diverging (concave) lens with f = -20 cm forms an image of an object at do = 40 cm. The image distance is:",
    "options": ["-13.3 cm (virtual, on same side as object)", "+40 cm (real)", "-40 cm", "+13.3 cm (real)"],
    "correct": 0,
    "explanation": "1/f = 1/do + 1/di → 1/(-20) = 1/40 + 1/di → 1/di = -1/20 - 1/40 = -2/40 - 1/40 = -3/40 → di = -40/3 ≈ -13.3 cm. Negative di = virtual image on the same side as the object. Diverging lenses always produce virtual, upright, diminished images.",
    "tags": ["optics", "diverging-lens"],
    "difficulty": "medium"
  },
  {
    "text": "The mirror equation 1/f = 1/do + 1/di applies to curved mirrors. A concave mirror (f = 15 cm) with object at do = 45 cm forms an image at di =",
    "options": ["22.5 cm (real, in front of mirror)", "15 cm", "45 cm", "-22.5 cm (virtual, behind mirror)"],
    "correct": 0,
    "explanation": "1/15 = 1/45 + 1/di → 1/di = 1/15 - 1/45 = 3/45 - 1/45 = 2/45 → di = 22.5 cm. Positive di for a mirror means the image is real and in front of the mirror. Magnification m = -di/do = -22.5/45 = -0.5 (inverted, smaller).",
    "tags": ["optics", "curved-mirror"],
    "difficulty": "medium"
  },
  # ── Acid-Base Additional ──────────────────────────────────────────────────
  {
    "text": "A buffer contains 0.1 mol acetic acid and 0.2 mol sodium acetate (pKa = 4.76). The pH is:",
    "options": ["5.06", "4.76", "4.46", "3.76"],
    "correct": 0,
    "explanation": "pH = pKa + log([A⁻]/[HA]) = 4.76 + log(0.2/0.1) = 4.76 + log(2) = 4.76 + 0.30 = 5.06. More conjugate base than acid shifts pH above pKa.",
    "tags": ["acid-base", "buffers", "henderson-hasselbalch"],
    "difficulty": "medium"
  },
  {
    "text": "Lewis acid-base theory defines a Lewis acid as:",
    "options": ["An electron pair acceptor (electrophile)", "A proton donor", "A proton acceptor", "An electron pair donor (nucleophile)"],
    "correct": 0,
    "explanation": "Lewis theory (broadest acid-base definition): Lewis acid = electron pair acceptor; Lewis base = electron pair donor. BF₃, Al³⁺, Fe³⁺ are Lewis acids that cannot donate protons. All Brønsted-Lowry acids are Lewis acids, but not vice versa.",
    "tags": ["acid-base", "lewis-acid-base"],
    "difficulty": "easy"
  },
  {
    "text": "Which best explains why HI is a stronger acid than HF?",
    "options": ["H-I bond is much weaker (longer) than H-F, making proton donation easier", "Iodine is more electronegative than fluorine", "HI has higher molecular weight", "HF ionizes more completely in water"],
    "correct": 0,
    "explanation": "Down a group, bond strength decreases as atomic size increases. H-I bond (bond energy ~297 kJ/mol) is much weaker than H-F (~569 kJ/mol), making H-I much easier to break and H⁺ easier to release. Electronegativity (F >> I) predicts opposite order and does not explain hydrohalic acid trend.",
    "tags": ["acid-base", "acid-strength", "bond-energy"],
    "difficulty": "medium"
  },
  # ── Kinetics Additional ────────────────────────────────────────────────────
  {
    "text": "For a second-order reaction, the half-life t½ = 1/(k[A]₀). As the reaction proceeds, each subsequent half-life:",
    "options": ["Gets longer (because [A]₀ decreases)", "Gets shorter", "Stays the same", "Increases exponentially"],
    "correct": 0,
    "explanation": "Second-order t½ = 1/(k[A]₀). As [A] decreases after each half-life, the next half-life is longer. This contrasts with first-order reactions (constant t½ = 0.693/k). This makes second-order reactions slow down dramatically as concentration falls.",
    "tags": ["kinetics", "second-order"],
    "difficulty": "medium"
  },
  {
    "text": "The rate-determining step in a multi-step mechanism is identified as the step with:",
    "options": ["The highest activation energy (slowest step)", "The lowest activation energy", "The most reactants", "The most stable intermediates"],
    "correct": 0,
    "explanation": "The rate-determining step (RDS) has the highest activation energy and is therefore the slowest step. It acts as the bottleneck: the overall reaction rate cannot exceed the rate of the RDS. The rate law for the overall reaction reflects the elementary rate law of the RDS.",
    "tags": ["kinetics", "rate-determining-step"],
    "difficulty": "easy"
  },
  # ── Equilibrium Additional ─────────────────────────────────────────────────
  {
    "text": "If Q < K for a reaction, the system will:",
    "options": ["Proceed forward (toward products) to reach equilibrium", "Proceed in reverse (toward reactants)", "Already be at equilibrium", "Have no net reaction regardless of concentrations"],
    "correct": 0,
    "explanation": "The reaction quotient Q uses current concentrations; K uses equilibrium concentrations. If Q < K, products are underrepresented relative to equilibrium, so the reaction shifts forward to produce more products. If Q > K, the reaction shifts reverse. Q = K means equilibrium.",
    "tags": ["equilibrium", "reaction-quotient"],
    "difficulty": "easy"
  },
  {
    "text": "Adding more reactant to a system at equilibrium will:",
    "options": ["Shift equilibrium toward products (Q < K, forward reaction increases)", "Shift equilibrium toward reactants", "Have no effect on equilibrium position", "Change the value of K"],
    "correct": 0,
    "explanation": "Adding reactant increases Q denominator (actually decreases Q since Q = [products]/[reactants]). With Q < K, the reaction shifts right to restore equilibrium. The equilibrium constant K is unchanged (it only changes with temperature). This is Le Chatelier's principle.",
    "tags": ["equilibrium", "le-chatelier"],
    "difficulty": "easy"
  },
]

random.seed(77)
for q in Q:
    c = q["correct"]
    opts = q["options"][:]
    correct_text = opts[c]
    random.shuffle(opts)
    q["options"] = opts
    q["correct"] = opts.index(correct_text)

out = os.path.join(BASE, "data", "questions", "cp", "hq-cp-2.json")
os.makedirs(os.path.dirname(out), exist_ok=True)
with open(out, "w") as f:
    json.dump(Q, f, indent=2)
print(f"Wrote {len(Q)} CP questions to {out}")
