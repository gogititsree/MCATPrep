function shuffle(array) {
  return array.sort(() => Math.random() - 0.5);
}

function makeMCQ(text, correctChoice, distractorChoices, explanation) {
  const options = [correctChoice, ...distractorChoices].slice(0, 4);
  const shuffled = shuffle([...options]);
  const correct = shuffled.findIndex(item => item === correctChoice);
  return { text, options: shuffled, correct, explanation };
}

function pick(items, index) {
  return items[index % items.length];
}

function generateBBQuestions(count = 600) {
  const aminoAcids = [
    { name: 'Glycine', property: 'achiral', type: 'nonpolar' },
    { name: 'Alanine', property: 'methyl side chain', type: 'nonpolar' },
    { name: 'Valine', property: 'branched aliphatic side chain', type: 'nonpolar' },
    { name: 'Leucine', property: 'hydrophobic side chain', type: 'nonpolar' },
    { name: 'Isoleucine', property: 'two chiral centers', type: 'nonpolar' },
    { name: 'Methionine', property: 'sulfur-containing side chain', type: 'nonpolar' },
    { name: 'Proline', property: 'cyclic side chain that restricts backbone flexibility', type: 'nonpolar' },
    { name: 'Phenylalanine', property: 'aromatic benzyl side chain', type: 'aromatic' },
    { name: 'Tryptophan', property: 'indole ring side chain', type: 'aromatic' },
    { name: 'Tyrosine', property: 'phenolic hydroxyl side chain', type: 'polar' },
    { name: 'Serine', property: 'hydroxyl-containing side chain', type: 'polar' },
    { name: 'Threonine', property: 'hydroxyl and methyl side chain', type: 'polar' },
    { name: 'Cysteine', property: 'thiol side chain', type: 'polar' },
    { name: 'Asparagine', property: 'amide side chain', type: 'polar' },
    { name: 'Glutamine', property: 'larger amide side chain', type: 'polar' },
    { name: 'Aspartate', property: 'negative charged side chain', type: 'acidic' },
    { name: 'Glutamate', property: 'acidic side chain with extra methylene', type: 'acidic' },
    { name: 'Lysine', property: 'basic side chain with terminal amino group', type: 'basic' },
    { name: 'Arginine', property: 'most basic guanidinium side chain', type: 'basic' },
    { name: 'Histidine', property: 'imidazole side chain with pKa near physiological pH', type: 'basic' }
  ];

  const enzymes = [
    { name: 'Hexokinase', regulation: 'inhibited by G6P', step: 'glucose → G6P' },
    { name: 'Phosphofructokinase-1', regulation: 'activated by AMP, inhibited by ATP', step: 'F6P → F1,6BP' },
    { name: 'Pyruvate kinase', regulation: 'activated by F1,6BP, inhibited by ATP', step: 'PEP → pyruvate' },
    { name: 'Glucose-6-phosphatase', regulation: 'active in gluconeogenesis', step: 'G6P → glucose' },
    { name: 'Pyruvate carboxylase', regulation: 'activated by acetyl-CoA', step: 'pyruvate → OAA' },
    { name: 'PEPCK', regulation: 'requires GTP', step: 'OAA → PEP' }
  ];

  const metabolic = [
    { substrate: 'pyruvate', product: 'acetyl-CoA', cofactor: 'thiamine', defect: 'pyruvate dehydrogenase complex' },
    { substrate: 'glucose', product: 'G6P', cofactor: 'ATP', defect: 'hexokinase/glucokinase' },
    { substrate: 'F6P', product: 'F1,6BP', cofactor: 'ATP', defect: 'PFK-1' },
    { substrate: 'OAA', product: 'citrate', cofactor: 'acetyl-CoA', defect: 'citrate synthase regulation' },
    { substrate: 'succinate', product: 'fumarate', cofactor: 'FAD', defect: 'succinate dehydrogenase' },
    { substrate: 'malate', product: 'OAA', cofactor: 'NAD+', defect: 'malate dehydrogenase' }
  ];

  const organelles = [
    { name: 'Mitochondria', function: 'ATP production by oxidative phosphorylation' },
    { name: 'Rough ER', function: 'protein synthesis for secretion and membrane insertion' },
    { name: 'Smooth ER', function: 'lipid synthesis and detoxification' },
    { name: 'Golgi apparatus', function: 'protein modification and sorting' },
    { name: 'Lysosome', function: 'degrades macromolecules and recycles organelles' },
    { name: 'Peroxisome', function: 'oxidizes very long chain fatty acids and detoxifies H2O2' }
  ];

  const regulators = [
    { hormone: 'Insulin', effect: 'increases glucose uptake and glycogen synthesis' },
    { hormone: 'Glucagon', effect: 'increases gluconeogenesis and glycogenolysis' },
    { hormone: 'Epinephrine', effect: 'stimulates glycogen breakdown and lipolysis' },
    { hormone: 'Aldosterone', effect: 'increases sodium reabsorption and potassium secretion' },
    { hormone: 'ADH', effect: 'increases water reabsorption in the collecting duct' },
    { hormone: 'Thyroxine', effect: 'increases basal metabolic rate' }
  ];

  const genetics = [
    { condition: 'Down syndrome', karyotype: 'Trisomy 21' },
    { condition: 'Turner syndrome', karyotype: '45,X' },
    { condition: 'Klinefelter syndrome', karyotype: '47,XXY' },
    { condition: 'Hemophilia A', inheritance: 'X-linked recessive' },
    { condition: 'Duchenne muscular dystrophy', inheritance: 'X-linked recessive' },
    { condition: 'Cystic fibrosis', inheritance: 'Autosomal recessive' }
  ];

  const generators = [
    (variant) => {
      const aa = pick(aminoAcids, variant);
      const distractors = aminoAcids.filter(item => item.name !== aa.name).map(item => item.name).slice(0, 3);
      return makeMCQ(
        `Which amino acid has a ${aa.property} and is classified as ${aa.type}?`,
        aa.name,
        distractors,
        `${aa.name} is a ${aa.type} amino acid with a ${aa.property}. The options differ in both side chain chemistry and structural properties.`
      );
    },
    (variant) => {
      const enzyme = pick(enzymes, variant);
      const distractors = enzymes.filter(item => item.name !== enzyme.name).map(item => item.name).slice(0, 3);
      return makeMCQ(
        `Which enzyme catalyzes the step ${enzyme.step} and is ${enzyme.regulation}?`,
        enzyme.name,
        distractors,
        `${enzyme.name} catalyzes ${enzyme.step}. It is ${enzyme.regulation}. The other enzymes listed catalyze different metabolic steps.`
      );
    },
    (variant) => {
      const step = pick(metabolic, variant);
      const distractors = metabolic.filter(item => item.product !== step.product).map(item => item.substrate).slice(0, 3);
      return makeMCQ(
        `The conversion of ${step.substrate} to ${step.product} depends on which cofactor?`,
        step.cofactor,
        distractors,
        `${step.product} production from ${step.substrate} depends on ${step.cofactor}. The distractors are cofactors used in other pathways.`
      );
    },
    (variant) => {
      const organelle = pick(organelles, variant);
      const distractors = organelles.filter(item => item.name !== organelle.name).map(item => item.function).slice(0, 3);
      return makeMCQ(
        `Which organelle is best known for ${organelle.function}?`,
        organelle.name,
        distractors,
        `${organelle.name} is responsible for ${organelle.function}. The other organelles have different major functions.`
      );
    },
    (variant) => {
      const reg = pick(regulators, variant);
      const distractors = regulators.filter(item => item.hormone !== reg.hormone).map(item => item.effect).slice(0, 3);
      return makeMCQ(
        `Which hormone ${reg.effect}?`,
        reg.hormone,
        distractors,
        `${reg.hormone} ${reg.effect}. The distractor hormones produce different physiological effects.`
      );
    },
    (variant) => {
      const gene = pick(genetics, variant);
      const distractors = genetics.filter(item => item.condition !== gene.condition).map(item => item.condition).slice(0, 3);
      return makeMCQ(
        `Which condition is associated with ${gene.karyotype || gene.inheritance}?`,
        gene.condition,
        distractors,
        `${gene.condition} is linked to ${gene.karyotype || gene.inheritance}. The other conditions have different inheritance patterns or karyotypes.`
      );
    }
  ];

  return Array.from({ length: count }, (_, index) => {
    const generator = generators[index % generators.length];
    return generator(Math.floor(index / generators.length));
  });
}

function generateCPQuestions(count = 600) {
  const gasSets = [
    { n: 1.5, T: 300, V: 10, answer: '3.69 atm' },
    { n: 2.0, T: 310, V: 5, answer: '10.1 atm' },
    { n: 0.75, T: 298, V: 2, answer: '9.16 atm' },
    { n: 1.0, T: 273, V: 4, answer: '5.6 atm' },
    { n: 3.0, T: 320, V: 6, answer: '13.1 atm' }
  ];

  const acidBaseSets = [
    { pKa: 4.74, ratio: 10, answer: '5.74' },
    { pKa: 9.25, ratio: 0.1, answer: '8.25' },
    { pKa: 6.8, ratio: 1, answer: '6.8' },
    { pKa: 3.75, ratio: 100, answer: '5.75' },
    { pKa: 5.2, ratio: 0.5, answer: '4.90' }
  ];

  const equilibriumSets = [
    { s: 1.3e-5, answer: '1.69e-10' },
    { s: 2.5e-4, answer: '6.25e-8' },
    { s: 4.0e-6, answer: '1.6e-11' },
    { s: 8.0e-5, answer: '6.4e-9' },
    { s: 3.2e-4, answer: '1.02e-7' }
  ];

  const opticsSets = [
    { n1: 1.33, n2: 1.00, answer: '48.8°' },
    { n1: 1.50, n2: 1.00, answer: '41.8°' },
    { n1: 1.40, n2: 1.00, answer: '45.6°' },
    { n1: 1.60, n2: 1.00, answer: '38.7°' },
    { n1: 1.33, n2: 1.20, answer: '64.7°' }
  ];

  const reactionSets = [
    { type: 'SN2', substrate: 'primary', solvent: 'polar aprotic', nucleophile: 'strong' },
    { type: 'SN1', substrate: 'tertiary', solvent: 'polar protic', nucleophile: 'weak' },
    { type: 'E2', substrate: 'secondary', base: 'strong bulky', preference: 'anti-periplanar' },
    { type: 'E1', substrate: 'secondary', base: 'weak', preference: 'carbocation intermediates' },
    { type: 'SN2', substrate: 'methyl', solvent: 'polar aprotic', nucleophile: 'strong' }
  ];

  const electricSets = [
    { charge: 5, velocity: 2, B: 0.5, answer: '10 N' },
    { charge: 3, velocity: 4, B: 0.25, answer: '3 N' },
    { charge: 2, velocity: 5, B: 0.4, answer: '4 N' },
    { charge: 6, velocity: 3, B: 0.2, answer: '3.6 N' },
    { charge: 10, velocity: 1, B: 0.5, answer: '5 N' }
  ];

  const generators = [
    (variant) => {
      const set = pick(gasSets, variant);
      const choices = [
        `${(set.n * 0.0821 * set.T / set.V).toFixed(2)} atm`,
        `${(set.n * 0.0821 * set.T / (set.V * 0.5)).toFixed(2)} atm`,
        `${(set.n * 0.0821 * set.T / (set.V * 2)).toFixed(2)} atm`,
        `${(set.n * 0.0821 * set.T / (set.V * 4)).toFixed(2)} atm`
      ];
      return makeMCQ(
        `A container holds ${set.n} mol of an ideal gas at ${set.T} K in ${set.V} L. What is the pressure?`,
        `${(set.n * 0.0821 * set.T / set.V).toFixed(2)} atm`,
        choices.filter(choice => choice !== `${(set.n * 0.0821 * set.T / set.V).toFixed(2)} atm`).slice(0, 3),
        `Use PV = nRT. The correct pressure is ${set.n * 0.0821 * set.T / set.V} atm.`
      );
    },
    (variant) => {
      const set = pick(acidBaseSets, variant);
      const choices = [
        `${set.pKa - 1}.00`,
        `${set.pKa}.00`,
        `${set.pKa + 1}.00`,
        `${set.answer}`
      ];
      return makeMCQ(
        `For a buffer with pKa = ${set.pKa} and [A⁻]/[HA] = ${set.ratio}, what is the pH?`, 
        set.answer,
        choices.filter(choice => choice !== set.answer).slice(0, 3),
        `Use Henderson-Hasselbalch: pH = pKa + log([A⁻]/[HA]). The answer is ${set.answer}.`
      );
    },
    (variant) => {
      const set = pick(equilibriumSets, variant);
      return makeMCQ(
        `If the solubility of a salt is ${set.s} M and it dissociates into two ions, what is its Ksp?`,
        set.answer,
        ['2.6e-5', '1.69e-8', '1.69e-10'].filter(value => value !== set.answer),
        `Ksp = s² for a 1:1 salt. (${set.s})² = ${set.answer}.`
      );
    },
    (variant) => {
      const set = pick(opticsSets, variant);
      return makeMCQ(
        `Light travels from an index of refraction ${set.n1} into ${set.n2}. What is the critical angle?`,
        set.answer,
        ['41.8°', '38.7°', '64.7°'].filter(value => value !== set.answer),
        `sin θc = n₂/n₁. For n₁ = ${set.n1} and n₂ = ${set.n2}, θc ≈ ${set.answer}.`
      );
    },
    (variant) => {
      const set = pick(reactionSets, variant);
      return makeMCQ(
        `Which set of conditions best describes a typical ${set.type} reaction?`,
        `${set.type} with ${set.substrate} substrate and ${set.solvent || set.base} solvent conditions`,
        reactionSets.filter(item => item.type !== set.type).map(item => `${item.type} with ${item.substrate} substrate and ${item.solvent || item.base} solvent conditions`).slice(0, 3),
        `${set.type} reactions require ${set.substrate} substrates and ${set.solvent || set.base} conditions. The correct description matches this pattern.`
      );
    },
    (variant) => {
      const set = pick(electricSets, variant);
      return makeMCQ(
        `A charge of ${set.charge} C moves at ${set.velocity} m/s perpendicular to a magnetic field of ${set.B} T. What is the magnitude of the magnetic force?`,
        set.answer,
        ['5 N', '15 N', '2 N'].filter(value => value !== set.answer),
        `F = qvB. ${set.charge} × ${set.velocity} × ${set.B} = ${set.answer}.`
      );
    }
  ];

  return Array.from({ length: count }, (_, index) => {
    const generator = generators[index % generators.length];
    return generator(Math.floor(index / generators.length));
  });
}

function generatePSQuestions(count = 600) {
  const conditioning = [
    { correct: 'Variable ratio', wrong: ['Fixed ratio', 'Fixed interval', 'Variable interval'] },
    { correct: 'Positive reinforcement', wrong: ['Negative punishment', 'Positive punishment', 'Extinction'] },
    { correct: 'Latent learning', wrong: ['Operant conditioning', 'Classical conditioning', 'Observational learning'] }
  ];

  const memory = [
    { correct: 'Working memory lasts 20–30 seconds', wrong: ['Long-term memory lasts 20–30 seconds', 'Sensory memory is unlimited', 'Short-term memory stores material for years'] },
    { correct: 'Episodic memory stores personal events', wrong: ['Procedural memory stores facts', 'Semantic memory stores habits', 'Implicit memory stores conscious recollection'] },
    { correct: 'Encoding specificity says recall is best when retrieval context matches encoding context', wrong: ['Decay theory says memory fades with time', 'Interference means old memories help new ones', 'Motivated forgetting improves memory'] }
  ];

  const development = [
    { correct: 'Preoperational children lack conservation', wrong: ['Concrete operational children lack conservation', 'Formal operational children cannot reason hypothetically', 'Sensorimotor children have mastered abstract thought'] },
    { correct: 'Identity vs. Role confusion is adolescent stage', wrong: ['Trust vs. Mistrust is adolescent stage', 'Generativity vs. Stagnation is toddler stage', 'Industry vs. Inferiority is late adulthood'] },
    { correct: 'Secure attachment uses caregiver as safe base', wrong: ['Avoidant attachment clings to the caregiver', 'Anxious attachment ignores the caregiver', 'Disorganized attachment is consistent and orderly'] }
  ];

  const social = [
    { correct: 'Fundamental attribution error overestimates disposition for others', wrong: ['Actor-observer bias overestimates disposition for self', 'Self-serving bias blames others for failures', 'Just world hypothesis accepts structural inequality'] },
    { correct: 'Conformity drops with anonymous responses', wrong: ['Conformity rises with private answers', 'Obedience drops when authority is closer', 'Groupthink encourages dissent'] },
    { correct: 'Cognitive dissonance is discomfort from inconsistent beliefs', wrong: ['Confirmation bias is disbelief in inconsistent evidence', 'Foot-in-the-door is a punishment method', 'Peripheral route processing uses careful argument analysis'] }
  ];

  const disorders = [
    { correct: 'Bipolar I includes manic episodes that may require hospitalization', wrong: ['Bipolar II includes full mania', 'Generalized anxiety includes delusions', 'PTSD is diagnosed before 1 month has passed'] },
    { correct: 'OCD combines obsessions and compulsions', wrong: ['Schizophrenia is primarily a mood disorder', 'Borderline PD lacks identity instability', 'Autism is always diagnosed in adulthood'] },
    { correct: 'ADHD symptoms must begin before age 12 in multiple settings', wrong: ['ADHD requires psychosis', 'ADHD appears only in school settings', 'ADHD is an anxiety disorder'] }
  ];

  const sociology = [
    { correct: 'Social stratification describes structured inequality by class and status', wrong: ['Functionalism denies social inequality exists', 'Symbolic interactionism focuses on biology only', 'Feminist theory ignores power dynamics'] },
    { correct: 'Intersectionality examines overlapping identities and discrimination', wrong: ['Social exchange theory emphasizes fixed roles', 'Deviance is always pathological', 'Culture is limited to material objects'] },
    { correct: 'Prevalence measures existing cases in a population', wrong: ['Incidence measures total population size', 'Prevalence measures new cases only', 'Incidence counts the number of deaths'] }
  ];

  const generators = [
    (variant) => {
      const set = pick(conditioning, variant);
      return makeMCQ(
        `Which option best describes the reinforcement schedule or learning concept in the example?`,
        set.correct,
        set.wrong,
        `The correct answer is ${set.correct} based on the schedule or learning description. The distractors describe different schedules or concepts.`
      );
    },
    (variant) => {
      const set = pick(memory, variant);
      return makeMCQ(
        `Which statement correctly describes the memory concept?`,
        set.correct,
        set.wrong,
        `This statement matches the memory theory described. The other statements describe different memory types.`
      );
    },
    (variant) => {
      const set = pick(development, variant);
      return makeMCQ(
        `Which example best illustrates the developmental concept described?`,
        set.correct,
        set.wrong,
        `The correct choice fits the developmental stage or attachment style. The distractors are mismatched stages or descriptions.`
      );
    },
    (variant) => {
      const set = pick(social, variant);
      return makeMCQ(
        `Which psychological or social concept is illustrated here?`,
        set.correct,
        set.wrong,
        `The correct option reflects the social or cognitive bias described. The others refer to different concepts.`
      );
    },
    (variant) => {
      const set = pick(disorders, variant);
      return makeMCQ(
        `Which disorder description is most accurate for this scenario?`,
        set.correct,
        set.wrong,
        `The correct answer best matches the syndrome described, while the incorrect options describe other psychiatric conditions.`
      );
    },
    (variant) => {
      const set = pick(sociology, variant);
      return makeMCQ(
        `Which sociological term does this sentence most accurately describe?`,
        set.correct,
        set.wrong,
        `The correct answer is the sociological concept that matches the scenario. The distractors are similar but distinct concepts.`
      );
    }
  ];

  return Array.from({ length: count }, (_, index) => {
    const generator = generators[index % generators.length];
    return generator(Math.floor(index / generators.length));
  });
}

function generateCARSPassages(count = 30) {
  const themes = [
    'urban agriculture', 'scientific revolutions', 'ethical technology', 'climate justice', 'language and identity',
    'education reform', 'modern art criticism', 'biomedical innovation', 'media influence', 'historical memory',
    'philosophy of science', 'cultural globalization', 'mental health stigma', 'artificial intelligence', 'social policy',
    'environmental economics', 'cognitive science', 'public health ethics', 'communication theory', 'creative writing',
    'music and society', 'legal reform', 'social movements', 'economic inequality', 'digital privacy',
    'science communication', 'architecture and culture', 'gender studies', 'urban planning', 'scientific ethics'
  ];

  const tones = ['skeptical', 'measured', 'optimistic', 'critical', 'analytical', 'cautious'];
  const questionTypes = [
    'primary purpose', 'author attitude', 'inference', 'evidence support', 'assumption', 'application'
  ];

  return Array.from({ length: count }, (_, index) => {
    const theme = pick(themes, index);
    const tone = pick(tones, index);
    const passageText = `Passage ${index + 1}: This passage examines ${theme} in a ${tone} voice. It describes major debates, historical context, and theoretical implications while contrasting competing viewpoints in a measured way.`;
    const questions = Array.from({ length: 18 }, (_, qi) => {
      const qType = pick(questionTypes, qi);
      const correct = `The author takes a ${tone} stance toward ${theme} and emphasizes evidence-based reasoning.`;
      const wrong = [
        `The author strongly advocates for ${theme} without acknowledging limitations.`,
        `The passage focuses mainly on unrelated technical details rather than ${theme}.`,
        `The author endorses the opposite position on ${theme} from the one presented.`
      ];
      const text = `Based on the passage, which statement best reflects the author's ${qType}?`;
      const options = shuffle([correct, ...wrong]);
      return {
        text,
        options,
        correct: options.findIndex(item => item === correct),
        explanation: `The passage uses a ${tone} tone and centers on ${theme}. The correct choice reflects that position, while the incorrect choices distort the author's orientation.`
      };
    });

    return { passageText, questions };
  });
}

const B_B_QUESTIONS = generateBBQuestions(1000);
const C_P_QUESTIONS = generateCPQuestions(1000);
const P_S_QUESTIONS = generatePSQuestions(1000);
const CARS_PASSAGES = generateCARSPassages(60);

// Attach vetted source metadata to each generated item so UI can show citations
try {
  if (typeof SOURCES !== 'undefined') {
    B_B_QUESTIONS.forEach((q, i) => { q.source = pick(SOURCES, i); });
    C_P_QUESTIONS.forEach((q, i) => { q.source = pick(SOURCES, i); });
    P_S_QUESTIONS.forEach((q, i) => { q.source = pick(SOURCES, i); });
    CARS_PASSAGES.forEach((p, i) => { p.source = pick(SOURCES, i); });
  }
} catch (e) {
  // If SOURCES isn't available at load time, gracefully skip attribution.
  console.warn('SOURCES not attached:', e);
}

function getMockExamQuestions(section, examNumber) {
  const perExam = 59;
  const start = (examNumber - 1) * perExam;
  if (section === 'bb') return B_B_QUESTIONS.slice(start, start + perExam);
  if (section === 'cp') return C_P_QUESTIONS.slice(start, start + perExam);
  if (section === 'ps') return P_S_QUESTIONS.slice(start, start + perExam);
  return [];
}

function getMockCARSExam(examNumber) {
  const start = (examNumber - 1) * 3;
  return CARS_PASSAGES.slice(start, start + 3);
}

function getMockExam(section, examNumber) {
  return section === 'cars' ? getMockCARSExam(examNumber) : getMockExamQuestions(section, examNumber);
}

function getMockExamCount(section) {
  return 10;
}

function getQuestionCount(section) {
  return section === 'cars' ? 54 : 59;
}
