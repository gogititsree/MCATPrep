#!/usr/bin/env python3
import json, os, random

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

Q = [
  # ── Learning & Conditioning ────────────────────────────────────────────
  {
    "text": "In classical conditioning, an unconditioned stimulus (US) is one that:",
    "options": ["Naturally and automatically triggers a response without prior learning", "Requires training to produce a response", "Was previously neutral before conditioning", "Only works after extinction"],
    "correct": 0,
    "explanation": "An unconditioned stimulus (US) is a stimulus that naturally evokes a response (unconditioned response, UR) without any prior learning. Example: food (US) naturally causes salivation (UR) in Pavlov's experiments.",
    "tags": ["learning", "classical-conditioning"],
    "difficulty": "easy"
  },
  {
    "text": "Extinction in classical conditioning occurs when:",
    "options": ["The conditioned stimulus is repeatedly presented without the unconditioned stimulus", "The conditioned stimulus is paired more strongly with the US", "Spontaneous recovery is prevented permanently", "A new CS is substituted for the original"],
    "correct": 0,
    "explanation": "Extinction involves presenting the CS without the US repeatedly. The conditioned response gradually weakens and disappears. However, spontaneous recovery (temporary return of CR after rest) shows the learning is not fully erased.",
    "tags": ["learning", "classical-conditioning", "extinction"],
    "difficulty": "easy"
  },
  {
    "text": "In operant conditioning, negative reinforcement involves:",
    "options": ["Removing an aversive stimulus to increase a behavior", "Adding an aversive stimulus to decrease a behavior", "Removing a pleasant stimulus to decrease a behavior", "Presenting a reward to increase behavior"],
    "correct": 0,
    "explanation": "Negative reinforcement removes (takes away) an unpleasant/aversive stimulus following a behavior, which increases the frequency of that behavior. Example: taking aspirin to relieve a headache (pain removal reinforces pill-taking behavior).",
    "tags": ["learning", "operant-conditioning", "reinforcement"],
    "difficulty": "medium"
  },
  {
    "text": "A variable ratio schedule of reinforcement produces:",
    "options": ["High, steady response rates that are most resistant to extinction", "Low response rates with long post-reinforcement pauses", "Responses only at fixed intervals", "Decreasing response rates over time"],
    "correct": 0,
    "explanation": "Variable ratio (VR) schedules provide reinforcement after an unpredictable number of responses (e.g., slot machines). This produces high, consistent response rates and the greatest resistance to extinction because organisms never know when the next reinforcement will come.",
    "tags": ["learning", "operant-conditioning", "reinforcement-schedules"],
    "difficulty": "medium"
  },
  {
    "text": "Observational learning (Bandura's social learning theory) requires all of the following EXCEPT:",
    "options": ["Direct experience with the behavior", "Attention to the model", "Retention of what was observed", "Motivation to reproduce the behavior"],
    "correct": 0,
    "explanation": "Bandura identified four components of observational learning: attention, retention, reproduction, and motivation. Direct personal experience is NOT required — observational learning occurs by watching others, which is why it is also called vicarious learning.",
    "tags": ["learning", "social-learning", "bandura"],
    "difficulty": "medium"
  },
  {
    "text": "Habituation is best defined as:",
    "options": ["Decreased responsiveness to a repeated, harmless stimulus", "Increased responsiveness to a stimulus through pairing", "Forgetting a stimulus entirely", "An involuntary reflex response"],
    "correct": 0,
    "explanation": "Habituation is the simplest form of learning: organisms reduce their response to stimuli that are repeatedly encountered and found to be harmless/irrelevant. Example: no longer noticing the ticking of a clock.",
    "tags": ["learning", "habituation"],
    "difficulty": "easy"
  },
  # ── Memory ────────────────────────────────────────────────────────────────
  {
    "text": "Working memory (Baddeley & Hitch model) includes all EXCEPT:",
    "options": ["Long-term episodic memory store", "Central executive", "Phonological loop", "Visuospatial sketchpad"],
    "correct": 0,
    "explanation": "Baddeley's working memory model consists of: (1) central executive (attentional control), (2) phonological loop (verbal/auditory information), (3) visuospatial sketchpad (visual/spatial info), and (4) episodic buffer (links to long-term memory). Long-term episodic memory itself is not a component of working memory.",
    "tags": ["memory", "working-memory", "baddeley"],
    "difficulty": "medium"
  },
  {
    "text": "The serial position effect shows that in free recall, items are best remembered when they are at the:",
    "options": ["Beginning (primacy) and end (recency) of a list", "Middle of a list", "Beginning of a list only", "End of a list only"],
    "correct": 0,
    "explanation": "The serial position effect consists of the primacy effect (better recall for early items — they transferred to long-term memory) and the recency effect (better recall for last items — still in working memory). Middle items are recalled worst.",
    "tags": ["memory", "serial-position", "primacy-recency"],
    "difficulty": "easy"
  },
  {
    "text": "Which type of long-term memory stores how to ride a bike?",
    "options": ["Procedural memory (implicit)", "Episodic memory (explicit)", "Semantic memory (explicit)", "Working memory"],
    "correct": 0,
    "explanation": "Procedural memory is a type of implicit (nondeclarative) long-term memory that stores motor skills and habits. Unlike explicit memory (episodic and semantic), procedural memory is acquired gradually and operates without conscious awareness.",
    "tags": ["memory", "procedural-memory", "implicit-memory"],
    "difficulty": "easy"
  },
  {
    "text": "Retroactive interference occurs when:",
    "options": ["New learning interferes with recall of previously learned information", "Old memories interfere with new learning", "A traumatic event prevents encoding", "Retrieval cues are absent"],
    "correct": 0,
    "explanation": "Retroactive interference: new information interferes backward with old memories. Example: learning Spanish after French makes it harder to recall French. Proactive interference is the opposite: old info interferes with new learning.",
    "tags": ["memory", "interference", "forgetting"],
    "difficulty": "medium"
  },
  {
    "text": "The encoding specificity principle states that memory is best when:",
    "options": ["Retrieval conditions match the context at encoding", "Information is rehearsed at fixed intervals", "Emotional arousal is minimal", "Semantic encoding is used regardless of context"],
    "correct": 0,
    "explanation": "Encoding specificity (Tulving): the same cues present during encoding should be present at retrieval. Context-dependent memory (same physical environment) and state-dependent memory (same physiological state) are applications of this principle.",
    "tags": ["memory", "encoding-specificity", "retrieval"],
    "difficulty": "medium"
  },
  {
    "text": "Anterograde amnesia impairs the ability to:",
    "options": ["Form new memories after the onset of amnesia", "Recall memories from before the amnesia onset", "Retrieve procedural memories", "Process sensory information"],
    "correct": 0,
    "explanation": "Anterograde amnesia is the inability to form new explicit memories after brain damage (e.g., hippocampal damage). Retrograde amnesia is the loss of memories formed before the injury. H.M. (famous case) had severe anterograde amnesia after bilateral hippocampectomy.",
    "tags": ["memory", "amnesia", "anterograde"],
    "difficulty": "easy"
  },
  # ── Cognition & Intelligence ──────────────────────────────────────────────
  {
    "text": "Functional fixedness is a cognitive bias that refers to:",
    "options": ["Inability to see an object being used in a novel way beyond its typical function", "Overreliance on prior experience for problem solving", "Tendency to confirm pre-existing beliefs", "Inability to shift between cognitive tasks"],
    "correct": 0,
    "explanation": "Functional fixedness (Duncker) is a cognitive barrier where people can only perceive an object's typical use, preventing creative problem-solving. Classic example: not recognizing a thumbtack box can be used as a shelf (Duncker candle problem).",
    "tags": ["cognition", "problem-solving", "functional-fixedness"],
    "difficulty": "medium"
  },
  {
    "text": "The availability heuristic leads people to judge probability based on:",
    "options": ["How easily examples come to mind", "Statistical frequency data", "Base rate information", "Rational cost-benefit analysis"],
    "correct": 0,
    "explanation": "The availability heuristic (Tversky & Kahneman): people estimate probability by how easily examples are recalled. Recent or vivid events seem more likely. Example: overestimating plane crash probability after seeing news coverage.",
    "tags": ["cognition", "heuristics", "availability"],
    "difficulty": "easy"
  },
  {
    "text": "Confirmation bias is the tendency to:",
    "options": ["Search for, favor, and remember information confirming pre-existing beliefs", "Overestimate the likelihood of rare events", "Attribute others' behavior to disposition rather than situation", "Underestimate time needed to complete tasks"],
    "correct": 0,
    "explanation": "Confirmation bias is pervasive: people preferentially seek, interpret, and remember information consistent with their existing beliefs, while downplaying contradictory evidence. It contributes to scientific misconduct and everyday reasoning errors.",
    "tags": ["cognition", "biases", "confirmation-bias"],
    "difficulty": "easy"
  },
  {
    "text": "Gardner's theory of multiple intelligences proposes that:",
    "options": ["Intelligence is not a single general factor but consists of multiple distinct abilities", "g (general intelligence) underlies all cognitive performance", "IQ tests capture the full range of human intelligence", "Intelligence is primarily determined by genetics"],
    "correct": 0,
    "explanation": "Howard Gardner proposed at least 8 distinct intelligences (linguistic, logical-mathematical, spatial, musical, bodily-kinesthetic, interpersonal, intrapersonal, naturalist). This contrasts with Spearman's g-factor theory of a single general intelligence.",
    "tags": ["intelligence", "gardner", "multiple-intelligences"],
    "difficulty": "easy"
  },
  # ── Development – Piaget ───────────────────────────────────────────────────
  {
    "text": "According to Piaget, object permanence is acquired during the:",
    "options": ["Sensorimotor stage (birth–2 years)", "Preoperational stage (2–7 years)", "Concrete operational stage (7–12 years)", "Formal operational stage (12+ years)"],
    "correct": 0,
    "explanation": "Object permanence — the understanding that objects continue to exist even when out of sight — is the key achievement of the sensorimotor stage. Before ~8 months, infants act as if hidden objects cease to exist.",
    "tags": ["development", "piaget", "sensorimotor"],
    "difficulty": "easy"
  },
  {
    "text": "Conservation (understanding that quantity remains the same despite changes in shape) is mastered in Piaget's:",
    "options": ["Concrete operational stage", "Preoperational stage", "Sensorimotor stage", "Formal operational stage"],
    "correct": 0,
    "explanation": "Children in the preoperational stage lack conservation (they are fooled by appearance). In the concrete operational stage (~7–12 years), children master conservation of number, mass, volume, and liquid, showing logical thinking about concrete objects.",
    "tags": ["development", "piaget", "conservation"],
    "difficulty": "easy"
  },
  {
    "text": "Piaget's formal operational stage is characterized by:",
    "options": ["Abstract reasoning and hypothetical-deductive thinking", "Egocentric and symbolic thinking", "Conservation and logical operations on concrete objects", "Reflexive behaviors and object permanence"],
    "correct": 0,
    "explanation": "The formal operational stage (adolescence onward) enables abstract thought, systematic hypothesis testing, and reasoning about hypothetical situations. Not all adults reach full formal operations according to Piaget.",
    "tags": ["development", "piaget", "formal-operational"],
    "difficulty": "easy"
  },
  # ── Development – Erikson ─────────────────────────────────────────────────
  {
    "text": "According to Erikson, the central developmental conflict of adolescence is:",
    "options": ["Identity vs. Role Confusion", "Intimacy vs. Isolation", "Industry vs. Inferiority", "Trust vs. Mistrust"],
    "correct": 0,
    "explanation": "Erikson's fifth stage (adolescence): Identity vs. Role Confusion. Adolescents explore different roles and integrate them into a coherent sense of self. Success leads to a stable identity; failure leads to confusion about one's role in society.",
    "tags": ["development", "erikson", "adolescence"],
    "difficulty": "easy"
  },
  {
    "text": "Erikson's stage of Generativity vs. Stagnation occurs during:",
    "options": ["Middle adulthood", "Late adulthood", "Young adulthood", "Adolescence"],
    "correct": 0,
    "explanation": "Generativity vs. Stagnation is Erikson's seventh stage (middle adulthood, ~40–65 years). Generativity involves contributing to society and guiding the next generation. Those who fail to find this purpose stagnate and feel disconnected.",
    "tags": ["development", "erikson", "middle-adulthood"],
    "difficulty": "medium"
  },
  # ── Attachment & Social Development ──────────────────────────────────────
  {
    "text": "In Ainsworth's Strange Situation paradigm, securely attached infants show:",
    "options": ["Distress when caregiver leaves, comfort upon return, and willingness to explore", "No distress when caregiver leaves and avoidance upon return", "Intense distress and resistance to comfort upon return", "No consistent pattern of attachment behavior"],
    "correct": 0,
    "explanation": "Secure attachment (type B): infants are distressed when the caregiver leaves (not indifferent), and they are easily comforted upon return. They use the caregiver as a safe base for exploration. This is the most common attachment style (~60–65%).",
    "tags": ["development", "attachment", "ainsworth"],
    "difficulty": "medium"
  },
  {
    "text": "Vygotsky's Zone of Proximal Development (ZPD) refers to:",
    "options": ["The range between what a child can do alone and what they can do with guidance", "The age range at which cognitive development accelerates most", "The gap between current performance and average performance", "Social skills the child has not yet developed"],
    "correct": 0,
    "explanation": "The ZPD is the distance between actual developmental level (independent problem-solving) and potential developmental level (with guidance from a more capable other). Scaffolding within the ZPD promotes learning and development.",
    "tags": ["development", "vygotsky", "zpd"],
    "difficulty": "easy"
  },
  # ── Motivation & Emotion ──────────────────────────────────────────────────
  {
    "text": "Maslow's hierarchy of needs places which category at the highest level (self-actualization)?",
    "options": ["Realizing one's full potential and pursuing personal growth", "Esteem needs (recognition and status)", "Safety and security needs", "Physiological needs (food, water)"],
    "correct": 0,
    "explanation": "Maslow's hierarchy (bottom to top): physiological → safety → belongingness/love → esteem → self-actualization. Self-actualization is the highest level, representing the fulfillment of one's unique potential and the pursuit of personal growth.",
    "tags": ["motivation", "maslow", "hierarchy-of-needs"],
    "difficulty": "easy"
  },
  {
    "text": "The James-Lange theory of emotion proposes that:",
    "options": ["We experience emotion as a result of perceiving our own physiological arousal", "Physiological arousal and emotional experience occur simultaneously", "Cognitive appraisal of a situation precedes both arousal and emotion", "The thalamus simultaneously sends signals to cortex and body"],
    "correct": 0,
    "explanation": "James-Lange theory: perception of a stimulus → physiological response → emotional experience. 'We are afraid because we run' (not 'we run because we are afraid'). Cannon-Bard challenged this, arguing arousal and emotion are simultaneous.",
    "tags": ["emotion", "james-lange", "theories-of-emotion"],
    "difficulty": "medium"
  },
  {
    "text": "The Schachter-Singer (two-factor) theory of emotion proposes that emotion requires:",
    "options": ["Both physiological arousal AND a cognitive label/attribution for that arousal", "Only physiological arousal without cognition", "Only cognitive appraisal without physiological arousal", "A specific pattern of physiological activation unique to each emotion"],
    "correct": 0,
    "explanation": "Schachter-Singer: emotion = physiological arousal + cognitive attribution. The same state of arousal is labeled differently based on context. Misattribution of arousal experiments (e.g., Dutton & Aron bridge study) support this theory.",
    "tags": ["emotion", "schachter-singer", "two-factor-theory"],
    "difficulty": "medium"
  },
  # ── Personality ───────────────────────────────────────────────────────────
  {
    "text": "Freud's concept of the id operates according to the:",
    "options": ["Pleasure principle — seeking immediate gratification", "Reality principle — negotiating with the external world", "Morality principle — applying ethical standards", "Rationality principle — logical problem-solving"],
    "correct": 0,
    "explanation": "Freud's psychoanalytic theory: the id is the primitive, unconscious part of the mind that operates on the pleasure principle (seeking immediate gratification of instincts). The ego operates on the reality principle, and the superego represents internalized moral standards.",
    "tags": ["personality", "psychoanalytic", "freud"],
    "difficulty": "easy"
  },
  {
    "text": "The Big Five (OCEAN) personality traits include all EXCEPT:",
    "options": ["Authoritarianism", "Openness to experience", "Conscientiousness", "Neuroticism"],
    "correct": 0,
    "explanation": "The Big Five (OCEAN) are: Openness, Conscientiousness, Extraversion, Agreeableness, Neuroticism. Authoritarianism is not part of the Big Five. It is a separate personality construct measuring submissiveness to authority and hostility toward out-groups.",
    "tags": ["personality", "big-five", "trait-theory"],
    "difficulty": "easy"
  },
  {
    "text": "According to Bandura, self-efficacy refers to:",
    "options": ["One's belief in one's ability to perform specific tasks successfully", "The amount of self-esteem a person has", "Objective measure of ability on specific tasks", "Intrinsic motivation for learning"],
    "correct": 0,
    "explanation": "Self-efficacy (Bandura) is the belief in one's own ability to execute behaviors required to produce specific outcomes. High self-efficacy increases persistence and performance. It is distinct from self-esteem (overall self-worth) and actual ability.",
    "tags": ["personality", "social-cognitive", "bandura", "self-efficacy"],
    "difficulty": "easy"
  },
  # ── Psychological Disorders ────────────────────────────────────────────────
  {
    "text": "Which neurotransmitter is most directly implicated in the dopamine hypothesis of schizophrenia?",
    "options": ["Dopamine (excess D2 receptor activity)", "Serotonin", "GABA", "Norepinephrine"],
    "correct": 0,
    "explanation": "The dopamine hypothesis proposes that positive symptoms of schizophrenia result from hyperactivity of dopaminergic pathways (especially mesolimbic). Evidence: antipsychotics block D2 receptors; dopamine-releasing drugs can produce schizophrenia-like psychosis.",
    "tags": ["psychopathology", "schizophrenia", "dopamine"],
    "difficulty": "medium"
  },
  {
    "text": "Major depressive disorder (MDD) is characterized by the presence of:",
    "options": ["Depressed mood or anhedonia most of the day for ≥2 weeks, plus additional symptoms", "Discrete episodes of both mania and depression", "Persistent mild depressive symptoms for ≥2 years", "Psychotic features required for diagnosis"],
    "correct": 0,
    "explanation": "DSM-5 criteria for MDD require ≥5 symptoms during a 2-week period, including depressed mood or anhedonia (loss of pleasure), plus symptoms like changes in sleep/appetite/weight, fatigue, worthlessness, concentration difficulties, and suicidal ideation.",
    "tags": ["psychopathology", "depression", "mdd"],
    "difficulty": "medium"
  },
  {
    "text": "The diathesis-stress model proposes that psychological disorders result from:",
    "options": ["An interaction between biological predisposition (diathesis) and environmental stressors", "Purely biological factors", "Only environmental and social stressors", "Conscious choice to adopt the sick role"],
    "correct": 0,
    "explanation": "The diathesis-stress model: individuals have varying biological vulnerabilities (diathesis — genetic, neurological). Disorders develop when this vulnerability combines with sufficient environmental stress. This biopsychosocial framework underlies much of modern psychopathology.",
    "tags": ["psychopathology", "diathesis-stress", "biopsychosocial"],
    "difficulty": "easy"
  },
  {
    "text": "Cognitive-behavioral therapy (CBT) primarily targets:",
    "options": ["Maladaptive thought patterns and behaviors that maintain psychological disorders", "Unconscious conflicts from childhood", "Brain chemistry through medication", "Social relationships and family systems"],
    "correct": 0,
    "explanation": "CBT is based on Beck's cognitive model: psychological distress is maintained by dysfunctional thought patterns (cognitive distortions) and maladaptive behaviors. Treatment involves identifying and challenging negative cognitions and changing problematic behaviors.",
    "tags": ["therapy", "cbt", "cognitive-behavioral"],
    "difficulty": "easy"
  },
  # ── Social Psychology ──────────────────────────────────────────────────────
  {
    "text": "The fundamental attribution error is the tendency to:",
    "options": ["Overestimate dispositional factors and underestimate situational factors when explaining others' behavior", "Underestimate one's own ability relative to others", "Attribute successes to internal factors and failures to external factors", "Overestimate the influence of situations on behavior"],
    "correct": 0,
    "explanation": "FAE (correspondence bias): observers tend to attribute others' behaviors to their internal disposition (personality, character) while underweighting situational forces. Example: assuming someone who is rude had a bad night rather than is just rude. Less common when judging our own behavior (actor-observer bias).",
    "tags": ["social-psychology", "attribution", "fundamental-attribution-error"],
    "difficulty": "easy"
  },
  {
    "text": "Stanley Milgram's obedience experiments demonstrated that:",
    "options": ["Ordinary people would administer apparently dangerous electric shocks under authority pressure", "People resist obeying authority when given clear instructions", "Situational factors are less important than personality in predicting obedience", "Only aggressive individuals obey destructive orders"],
    "correct": 0,
    "explanation": "Milgram found ~65% of participants delivered maximum shocks (450V) to a screaming confederate when instructed by an authority figure (experimenter). This demonstrated the powerful role of situational factors (legitimate authority, agentic state) in producing destructive obedience.",
    "tags": ["social-psychology", "obedience", "milgram"],
    "difficulty": "easy"
  },
  {
    "text": "Cognitive dissonance theory (Festinger) predicts that when people behave inconsistently with their attitudes, they will:",
    "options": ["Experience discomfort and change their attitude or behavior to reduce the inconsistency", "Ignore the inconsistency and maintain the attitude", "Seek external justification without changing attitude", "Experience positive affect from the inconsistency"],
    "correct": 0,
    "explanation": "Cognitive dissonance is the discomfort arising from holding contradictory cognitions (attitude vs. behavior). People are motivated to reduce dissonance by changing an attitude, changing behavior, or adding new cognitions. Classic study: paid $1 (vs $20) to lie → more attitude change.",
    "tags": ["social-psychology", "cognitive-dissonance", "festinger"],
    "difficulty": "medium"
  },
  {
    "text": "Social facilitation refers to the phenomenon where the presence of others:",
    "options": ["Improves performance on easy/well-learned tasks but impairs performance on difficult/novel tasks", "Always improves performance regardless of task difficulty", "Always impairs performance", "Has no effect on performance"],
    "correct": 0,
    "explanation": "Social facilitation (Zajonc): the mere presence of others enhances arousal. For simple or well-practiced tasks, increased arousal improves the dominant (learned) response. For difficult or new tasks, arousal enhances incorrect responses, impairing performance.",
    "tags": ["social-psychology", "social-facilitation", "zajonc"],
    "difficulty": "medium"
  },
  {
    "text": "Groupthink occurs when a highly cohesive group:",
    "options": ["Prioritizes consensus and harmony over critical evaluation of alternatives", "Engages in rigorous debate to reach the best decision", "Contains members with highly diverse viewpoints", "Is led by a weak or uninvolved leader"],
    "correct": 0,
    "explanation": "Groupthink (Janis): in highly cohesive groups with strong leadership, members suppress dissent to maintain harmony. Symptoms include illusion of invulnerability, collective rationalization, and self-censorship. Examples: Bay of Pigs invasion, space shuttle Challenger decision.",
    "tags": ["social-psychology", "groupthink", "group-decision-making"],
    "difficulty": "easy"
  },
  {
    "text": "The bystander effect (Darley & Latané) explains that:",
    "options": ["As the number of observers increases, each individual is less likely to help (diffusion of responsibility)", "More observers means more help is provided", "Bystanders always help in emergencies", "Only personality traits predict helping behavior"],
    "correct": 0,
    "explanation": "Bystander effect: in an emergency, individuals are less likely to intervene when others are present. Diffusion of responsibility (each person feels less personally responsible) and pluralistic ignorance (looking to others for cues) explain why Kitty Genovese's assault was witnessed but not reported.",
    "tags": ["social-psychology", "bystander-effect", "prosocial-behavior"],
    "difficulty": "easy"
  },
  # ── Sociology – Social Stratification ────────────────────────────────────
  {
    "text": "Social stratification refers to:",
    "options": ["A system by which society ranks categories of people in a hierarchy based on wealth, power, and prestige", "Individual social mobility within a society", "Cultural differences between societies", "Geographic distribution of populations"],
    "correct": 0,
    "explanation": "Social stratification is the hierarchical arrangement of individuals/groups in society, typically based on socioeconomic status (SES), which encompasses wealth (assets), income, occupational prestige, and educational attainment. It creates unequal access to resources.",
    "tags": ["sociology", "stratification", "ses"],
    "difficulty": "easy"
  },
  {
    "text": "The conflict theory perspective (Marx) emphasizes that social inequality:",
    "options": ["Results from competition over limited resources where powerful groups dominate", "Serves a necessary function in motivating people to fill important roles", "Is a natural outcome of individual differences in ability", "Is largely explained by cultural values and norms"],
    "correct": 0,
    "explanation": "Marxist conflict theory: society is structured around competition for scarce resources. The bourgeoisie (capitalist class) control the means of production and exploit the proletariat (working class), perpetuating inequality. This contrasts with functionalism's view that stratification is necessary.",
    "tags": ["sociology", "conflict-theory", "marx"],
    "difficulty": "medium"
  },
  {
    "text": "Social capital, as described by Bourdieu and Putnam, refers to:",
    "options": ["Resources derived from one's social networks and relationships", "Economic wealth accumulated by individuals", "Cultural knowledge and skills from education", "Political power held by individuals"],
    "correct": 0,
    "explanation": "Social capital encompasses the networks, norms of reciprocity, and trust that enable collective action and access to resources. Bridging social capital connects diverse groups; bonding social capital strengthens ties within groups. Higher social capital is associated with better health outcomes.",
    "tags": ["sociology", "social-capital", "bourdieu"],
    "difficulty": "medium"
  },
  {
    "text": "The sick role, as described by Parsons, includes the expectation that sick individuals will:",
    "options": ["Seek medical help and try to recover, in exchange for exemption from normal duties", "Be responsible for their own illness", "Maintain their normal social roles during illness", "Be excluded from social obligations permanently"],
    "correct": 0,
    "explanation": "Parsons' sick role theory: illness is a social status with rights (exemption from normal duties, not held responsible for illness) and obligations (must seek medical help, desire to recover). This functionalist view frames medicine as a form of social control.",
    "tags": ["sociology", "sick-role", "parsons", "health"],
    "difficulty": "medium"
  },
  # ── Sociology – Socialization & Culture ────────────────────────────────────
  {
    "text": "Primary socialization occurs:",
    "options": ["During childhood, primarily through the family, teaching basic norms and values", "In adulthood when entering new social roles", "Through formal education and workplace", "Through peer groups in adolescence"],
    "correct": 0,
    "explanation": "Primary socialization is the first and most important phase, occurring in early childhood primarily through the family. Children learn language, basic norms, values, and worldview. Secondary socialization occurs later through schools, peers, workplaces, and media.",
    "tags": ["sociology", "socialization"],
    "difficulty": "easy"
  },
  {
    "text": "Cultural relativism is the principle that:",
    "options": ["Behaviors and beliefs should be understood in the context of their own culture, not judged by external standards", "Some cultures are objectively superior to others", "All cultures share universal moral standards", "Cultural practices that harm individuals must be condemned"],
    "correct": 0,
    "explanation": "Cultural relativism: practices, values, and beliefs of a culture should be evaluated within their own cultural context rather than by the standards of the observer's culture. This is a methodological stance distinct from moral relativism, and contrasts with ethnocentrism.",
    "tags": ["sociology", "cultural-relativism", "culture"],
    "difficulty": "easy"
  },
  {
    "text": "Erving Goffman's concept of stigma refers to:",
    "options": ["A deeply discrediting attribute that reduces a person from a whole person to a tainted, discounted one", "A positive social label given to high-status individuals", "A ritual of social greeting", "The process of primary socialization"],
    "correct": 0,
    "explanation": "Goffman's stigma: a social attribute that is deeply discrediting, reducing the bearer in others' minds from a whole person to a discounted one. Three types: tribal stigma (group membership), abominations of the body (physical), and blemishes of individual character (behavioral).",
    "tags": ["sociology", "stigma", "goffman"],
    "difficulty": "medium"
  },
  # ── Sociology – Race, Class, Gender ──────────────────────────────────────
  {
    "text": "Intersectionality (Crenshaw) is the concept that:",
    "options": ["Multiple social identities (race, gender, class) overlap to create unique experiences of privilege or oppression", "Social identities can only be analyzed separately", "Race is more important than class in shaping inequality", "All forms of discrimination stem from a single source"],
    "correct": 0,
    "explanation": "Intersectionality recognizes that race, class, gender, sexuality, disability, and other identities intersect, creating qualitatively different experiences that cannot be reduced to the sum of individual identities. Developed by Kimberlé Crenshaw to address Black women's experiences not captured by race OR gender analysis alone.",
    "tags": ["sociology", "intersectionality", "crenshaw"],
    "difficulty": "medium"
  },
  {
    "text": "The glass ceiling metaphor refers to:",
    "options": ["Invisible barriers preventing women and minorities from advancing to senior positions", "Transparency of corporate governance", "Glass floors preventing downward mobility", "Formal legal prohibitions on employment discrimination"],
    "correct": 0,
    "explanation": "The glass ceiling describes invisible, informal barriers (discrimination, exclusion from networks, implicit bias) that prevent qualified women and minorities from rising to the highest levels of organizational hierarchies, despite apparent equal opportunity.",
    "tags": ["sociology", "glass-ceiling", "gender-inequality"],
    "difficulty": "easy"
  },
  # ── Research Methods ──────────────────────────────────────────────────────
  {
    "text": "A double-blind experimental design means that:",
    "options": ["Neither the participants nor the researchers administering the intervention know who is in the treatment vs. control group", "Only participants are unaware of the group assignment", "Both variables are measured blind to hypothesis", "Two separate groups are tested independently"],
    "correct": 0,
    "explanation": "In double-blind designs, both participants (preventing placebo effects) and the researchers who interact with them (preventing experimenter bias/demand characteristics) are unaware of group assignment. This controls for both participant and researcher expectations.",
    "tags": ["research-methods", "experimental-design", "blind-studies"],
    "difficulty": "easy"
  },
  {
    "text": "A correlation of r = -0.85 between stress and immune function indicates:",
    "options": ["A strong negative relationship: as stress increases, immune function decreases", "A weak relationship between stress and immunity", "Stress causes immune dysfunction", "Immunity is the independent variable"],
    "correct": 0,
    "explanation": "Correlation coefficients range from -1 to +1. r = -0.85 is a strong (large magnitude) negative correlation: higher stress is associated with lower immune function. Importantly, correlation does not imply causation — a third variable could explain the relationship.",
    "tags": ["research-methods", "correlation"],
    "difficulty": "easy"
  },
  {
    "text": "Internal validity in research refers to:",
    "options": ["The degree to which results accurately reflect a causal relationship between variables within the study", "The degree to which results generalize to other populations", "The reliability of measurements over time", "The extent to which a measure assesses what it intends to measure"],
    "correct": 0,
    "explanation": "Internal validity concerns whether changes in the dependent variable were actually caused by the independent variable. Threats include confounds, selection bias, history effects, and maturation. External validity refers to generalizability.",
    "tags": ["research-methods", "validity", "internal-validity"],
    "difficulty": "medium"
  },
  {
    "text": "The p-value in hypothesis testing represents:",
    "options": ["The probability of obtaining results as extreme as observed, assuming the null hypothesis is true", "The probability that the null hypothesis is true", "The probability that the research hypothesis is true", "The effect size of the intervention"],
    "correct": 0,
    "explanation": "The p-value is the probability of observing data as extreme as the sample data (or more extreme), given that the null hypothesis is true. A p-value < 0.05 means there is less than a 5% chance of getting these results by chance alone (if H₀ is true).",
    "tags": ["research-methods", "statistics", "hypothesis-testing"],
    "difficulty": "medium"
  },
  # ── Health Psychology & Behavior ─────────────────────────────────────────
  {
    "text": "The health belief model predicts that people will take health action when they perceive:",
    "options": ["Susceptibility to illness, severity of illness, benefits of action outweigh barriers", "Only the benefits of the health action", "Strong social norms to act healthily", "High self-efficacy regardless of perceived threat"],
    "correct": 0,
    "explanation": "The Health Belief Model (Rosenstock): health behavior depends on perceived susceptibility (I'm at risk), perceived severity (it's serious), perceived benefits (action helps), and perceived barriers (costs of action). Cues to action and self-efficacy are also incorporated.",
    "tags": ["health-psychology", "health-belief-model"],
    "difficulty": "medium"
  },
  {
    "text": "The General Adaptation Syndrome (Selye) describes the body's response to stress in stages:",
    "options": ["Alarm → Resistance → Exhaustion", "Exhaustion → Resistance → Alarm", "Alarm → Exhaustion → Recovery", "Resistance → Alarm → Exhaustion"],
    "correct": 0,
    "explanation": "Selye's GAS: (1) Alarm — fight-or-flight activation (HPA axis, sympathetic NS). (2) Resistance — sustained mobilization of resources if stressor persists. (3) Exhaustion — depletion of resources leading to immune suppression, disease, and potential death.",
    "tags": ["health-psychology", "stress", "general-adaptation-syndrome"],
    "difficulty": "easy"
  },
  # ── Perception & Sensation ────────────────────────────────────────────────
  {
    "text": "Signal detection theory distinguishes between:",
    "options": ["Sensitivity (d') and response criterion (β) as separate components of detection", "Absolute threshold and just-noticeable difference", "Top-down and bottom-up processing", "Rods and cones in visual detection"],
    "correct": 0,
    "explanation": "Signal Detection Theory (SDT): sensitivity (d') measures the observer's ability to discriminate signal from noise, while criterion (β) reflects response bias (willingness to say yes). This separates true perceptual ability from decision-making tendencies.",
    "tags": ["perception", "signal-detection-theory"],
    "difficulty": "hard"
  },
  {
    "text": "The trichromatic (Young-Helmholtz) theory of color vision states that:",
    "options": ["Three types of cones respond maximally to red, green, and blue wavelengths; other colors from combinations", "Color perception is based on opponent processes (red/green, blue/yellow)", "Rods in the retina are responsible for color vision", "Color is perceived by a single photoreceptor type"],
    "correct": 0,
    "explanation": "Young-Helmholtz: three cone types (S, M, L — short, medium, long wavelength). Color perception arises from the relative activation pattern across the three cone types. The opponent process theory (Hering) operates at the ganglion cell level and both theories are needed for complete color vision.",
    "tags": ["perception", "color-vision", "trichromatic-theory"],
    "difficulty": "medium"
  },
  # ── Biological Bases of Behavior ──────────────────────────────────────────
  {
    "text": "The hypothalamus plays a key role in:",
    "options": ["Regulating homeostasis (hunger, thirst, temperature, circadian rhythms), linking nervous and endocrine systems", "Higher-order reasoning and planning", "Long-term memory formation", "Visual processing"],
    "correct": 0,
    "explanation": "The hypothalamus, though small, is critical for homeostasis: it regulates hunger (lateral hypothalamus = hunger center, ventromedial = satiety center), thirst, body temperature, sleep-wake cycles, and the HPA axis (stress response). It controls the pituitary gland.",
    "tags": ["biological-psychology", "hypothalamus", "homeostasis"],
    "difficulty": "easy"
  },
  {
    "text": "The limbic system is primarily associated with:",
    "options": ["Emotional processing and memory formation (amygdala, hippocampus)", "Motor coordination and balance", "Language comprehension and production", "Primary sensory processing"],
    "correct": 0,
    "explanation": "The limbic system includes the amygdala (emotional processing, fear conditioning, threat detection), hippocampus (explicit memory formation, spatial navigation), cingulate cortex, and hypothalamus. It mediates emotion-memory integration.",
    "tags": ["biological-psychology", "limbic-system", "emotion"],
    "difficulty": "easy"
  },
  {
    "text": "Long-term potentiation (LTP) is considered a synaptic mechanism for learning and memory because it involves:",
    "options": ["Strengthening of synaptic connections through repeated stimulation (NMDA receptor activation)", "Elimination of synaptic connections through disuse", "Reduced neurotransmitter release at active synapses", "Myelination of neuronal axons"],
    "correct": 0,
    "explanation": "LTP: high-frequency stimulation of a synapse leads to long-lasting increase in synaptic strength. NMDA receptors act as coincidence detectors (require both presynaptic glutamate release AND postsynaptic depolarization). AMPA receptor insertion increases sensitivity. LTP is impaired by hippocampal damage.",
    "tags": ["biological-psychology", "ltp", "synaptic-plasticity", "memory"],
    "difficulty": "medium"
  },
  {
    "text": "Which neurotransmitter is most directly implicated in Parkinson's disease?",
    "options": ["Dopamine (loss of dopaminergic neurons in substantia nigra)", "Serotonin", "Acetylcholine", "GABA"],
    "correct": 0,
    "explanation": "Parkinson's disease results from progressive degeneration of dopaminergic neurons in the substantia nigra pars compacta. These neurons project to the striatum (nigrostriatal pathway), and their loss disrupts motor control. Treatment: L-DOPA (dopamine precursor).",
    "tags": ["biological-psychology", "parkinson", "dopamine", "basal-ganglia"],
    "difficulty": "easy"
  },
  # ── Language & Communication ──────────────────────────────────────────────
  {
    "text": "Broca's area damage results in:",
    "options": ["Broca's aphasia: nonfluent, halting speech production with intact comprehension", "Wernicke's aphasia: fluent but meaningless speech", "Alexia: inability to read", "Agrammatism with intact phonology"],
    "correct": 0,
    "explanation": "Broca's area (left inferior frontal gyrus) is critical for speech production and grammar. Damage causes Broca's aphasia: labored, telegraphic speech (function words omitted) but relatively preserved comprehension. Wernicke's area damage (left temporal) causes fluent but nonsensical speech with poor comprehension.",
    "tags": ["language", "brocas-area", "aphasia"],
    "difficulty": "medium"
  },
  {
    "text": "The Sapir-Whorf hypothesis (linguistic relativity) proposes that:",
    "options": ["Language influences or determines thought and perception of reality", "Thought is universal and independent of language", "Language acquisition follows a critical period determined by genetics", "Grammar is innate (Universal Grammar)"],
    "correct": 0,
    "explanation": "Sapir-Whorf: the language we speak shapes how we think about and perceive the world. The strong version (linguistic determinism) claims language determines thought; the weak version (linguistic relativity) claims language influences but does not determine thought. Color perception studies provide mixed evidence.",
    "tags": ["language", "sapir-whorf", "linguistic-relativity"],
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

out = os.path.join(BASE, "data", "questions", "ps", "hq-ps.json")
os.makedirs(os.path.dirname(out), exist_ok=True)
with open(out, "w") as f:
    json.dump(Q, f, indent=2)
print(f"Wrote {len(Q)} PS questions to {out}")
