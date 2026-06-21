#!/usr/bin/env python3
import json, os, random

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

Q = [
  # ── 1. MORAL DEVELOPMENT ─────────────────────────────────────────────────
  {
    "text": "According to Kohlberg's theory, a child who obeys rules to avoid punishment is operating at which level?",
    "options": ["Preconventional", "Conventional", "Postconventional", "Moral realism"],
    "correct": 0,
    "explanation": "Kohlberg's preconventional level (stages 1–2) is characterized by self-interest and avoiding punishment (stage 1) or seeking rewards (stage 2). Conventional reasoning follows social norms; postconventional reasoning uses abstract principles. Moral realism is Piaget's term, not Kohlberg's.",
    "tags": ["moral-development", "kohlberg", "preconventional"],
    "difficulty": "easy"
  },
  {
    "text": "A teenager argues that rules should be followed because they maintain social order and uphold the law. This reflects Kohlberg's:",
    "options": ["Stage 4 — law and order orientation", "Stage 2 — instrumental purpose", "Stage 5 — social contract", "Stage 6 — universal ethical principles"],
    "correct": 0,
    "explanation": "Stage 4 (law and order) emphasizes maintaining societal rules for social stability — a conventional-level orientation. Stage 2 is self-interested bargaining. Stage 5 views laws as social contracts that can be changed; stage 6 appeals to universal abstract principles like justice.",
    "tags": ["moral-development", "kohlberg", "stage-4"],
    "difficulty": "medium"
  },
  {
    "text": "In the Heinz dilemma, a person who concludes that Heinz should steal the drug because human life is a universal value superior to property laws is reasoning at Kohlberg's:",
    "options": ["Postconventional level, stage 6", "Conventional level, stage 4", "Preconventional level, stage 2", "Postconventional level, stage 5"],
    "correct": 0,
    "explanation": "Stage 6 (universal ethical principles) involves self-chosen abstract principles such as the sanctity of human life that transcend specific laws. Stage 5 would frame this as a social contract issue; stage 4 would uphold the law against theft. Stage 2 would focus on personal gain.",
    "tags": ["moral-development", "kohlberg", "heinz-dilemma", "postconventional"],
    "difficulty": "medium"
  },
  {
    "text": "Carol Gilligan criticized Kohlberg's theory primarily because:",
    "options": ["It was based on male samples and undervalued care-based reasoning more common in women", "It did not include a preconventional stage", "It overemphasized emotion over cognition", "It failed to account for cross-cultural differences in punishment"],
    "correct": 0,
    "explanation": "Gilligan argued that Kohlberg's model, derived from studies of boys/men, privileged justice-based reasoning and scored women lower. She proposed an ethic of care centered on relationships and responsibilities, contrasting with Kohlberg's ethic of justice. Gilligan did not dispute the existence of preconventional reasoning.",
    "tags": ["moral-development", "gilligan", "care-ethics"],
    "difficulty": "medium"
  },
  {
    "text": "Gilligan's ethic of care differs from Kohlberg's ethic of justice in that it emphasizes:",
    "options": ["Maintaining relationships and responding to others' needs rather than applying universal rules", "Abstract principles of fairness applied impartially", "Punishment avoidance in early moral development", "Stage-based progression from self-interest to social norms"],
    "correct": 0,
    "explanation": "Gilligan's care ethics focuses on context, relationships, and responsibility to others — not universal rules applied impartially. Kohlberg's justice ethics uses abstract, impartial principles. Both theorists accept developmental progression, but Gilligan questions whether justice should be the highest stage.",
    "tags": ["moral-development", "gilligan", "care-ethics", "justice-ethics"],
    "difficulty": "medium"
  },
  {
    "text": "How does Piaget's concept of moral realism differ from Kohlberg's preconventional morality?",
    "options": ["Moral realism judges acts by consequences/damage regardless of intent; Kohlberg's stage 1 focuses on punishment avoidance", "Moral realism emphasizes intent; Kohlberg's preconventional stage emphasizes rules", "Both concepts are identical and interchangeable", "Piaget's moral realism corresponds to Kohlberg's postconventional stage"],
    "correct": 0,
    "explanation": "Piaget's moral realism (heteronomous morality) judges acts by their objective consequences (e.g., breaking 15 cups accidentally is worse than breaking 1 deliberately). Kohlberg's stage 1 focuses on avoiding punishment. They partially overlap developmentally but differ in conceptual emphasis.",
    "tags": ["moral-development", "piaget", "moral-realism", "kohlberg"],
    "difficulty": "hard"
  },
  {
    "text": "A person in Kohlberg's stage 3 ('good boy/good girl') would most likely reason:",
    "options": ["'I should act in ways that make others like and approve of me'", "'I must obey laws to keep society functioning'", "'I act morally to avoid punishment'", "'I follow universal principles of human dignity'"],
    "correct": 0,
    "explanation": "Stage 3 (interpersonal concordance) is motivated by social approval and being seen as a 'good person.' Stage 4 emphasizes law and social order. Stage 1 is about avoiding punishment. Stage 6 involves universal ethical principles.",
    "tags": ["moral-development", "kohlberg", "stage-3", "conventional"],
    "difficulty": "easy"
  },
  {
    "text": "Research on Kohlberg's stages shows that most adults in Western societies reason primarily at which level?",
    "options": ["Conventional", "Preconventional", "Postconventional", "Universal ethical principles"],
    "correct": 0,
    "explanation": "Cross-cultural research indicates most adults reason at the conventional level (stages 3–4), following social norms and laws. Preconventional reasoning is typical of young children. Postconventional reasoning (stages 5–6) is relatively rare; stage 6 is almost never empirically observed.",
    "tags": ["moral-development", "kohlberg", "conventional"],
    "difficulty": "easy"
  },
  {
    "text": "A vignette: Maria, age 8, says the boy who broke 10 cups accidentally is naughtier than the boy who broke 1 cup on purpose. This illustrates:",
    "options": ["Piaget's moral realism (heteronomous morality)", "Kohlberg's preconventional stage 1", "Gilligan's care ethics in development", "Kohlberg's conventional morality"],
    "correct": 0,
    "explanation": "Piaget's moral realism judges acts by objective outcomes (damage done) rather than intent. Children in the heteronomous stage cannot yet integrate intention into moral judgment. This typically shifts around age 9–10 into autonomous morality where intent matters.",
    "tags": ["moral-development", "piaget", "moral-realism", "heteronomous"],
    "difficulty": "medium"
  },
  {
    "text": "Kohlberg's postconventional level is distinguished from the conventional level by:",
    "options": ["Reasoning from self-chosen abstract principles that may supersede existing laws", "Strict adherence to social rules and laws", "Seeking approval from peers and authority figures", "Avoiding punishment as the primary motivator"],
    "correct": 0,
    "explanation": "Postconventional morality (stages 5–6) involves recognizing that moral principles are self-chosen and can conflict with laws — laws are judged by their conformity to moral principles. Conventional morality upholds existing social contracts and laws. Punishment avoidance is preconventional.",
    "tags": ["moral-development", "kohlberg", "postconventional"],
    "difficulty": "medium"
  },
  {
    "text": "A college student argues that the death penalty is wrong regardless of what the law says because all human life has inherent dignity. Kohlberg would classify this as:",
    "options": ["Stage 6 — universal ethical principles", "Stage 5 — social contract", "Stage 4 — law and order", "Stage 3 — interpersonal concordance"],
    "correct": 0,
    "explanation": "Stage 6 involves self-chosen universal principles (e.g., human dignity, sanctity of life) that transcend law. Stage 5 would accept laws as social contracts changeable by democratic process. Stage 4 would defer to whatever the law prescribes.",
    "tags": ["moral-development", "kohlberg", "stage-6", "universal-principles"],
    "difficulty": "medium"
  },
  {
    "text": "Which of the following best describes Kohlberg's stage 5 reasoning?",
    "options": ["Laws are social contracts that serve human welfare and can be changed through democratic processes", "Rules are absolute and must be followed regardless of circumstances", "Moral behavior is driven by avoiding personal punishment", "The best action is the one that gains the most social approval"],
    "correct": 0,
    "explanation": "Stage 5 (social contract/legalistic orientation) views laws as flexible agreements made for the greatest good; unjust laws can be changed through legitimate means. Stage 4 treats rules as absolute; stage 1 focuses on punishment; stage 3 focuses on social approval.",
    "tags": ["moral-development", "kohlberg", "stage-5", "social-contract"],
    "difficulty": "medium"
  },
  {
    "text": "Adolescent moral reasoning, according to Kohlberg, typically advances from preconventional to conventional primarily due to:",
    "options": ["Expanding social perspective-taking and cognitive development (formal operations)", "Biological maturation of the prefrontal cortex alone", "Parental punishment of rule violations", "Decreasing egocentrism without any cognitive change"],
    "correct": 0,
    "explanation": "Kohlberg linked moral development to cognitive development (Piaget) and social role-taking ability. As adolescents develop formal operations and can consider others' perspectives, they progress to conventional reasoning. Prefrontal maturation plays a role but is not Kohlberg's primary explanation.",
    "tags": ["moral-development", "kohlberg", "adolescence", "perspective-taking"],
    "difficulty": "hard"
  },
  {
    "text": "A key methodological criticism of Kohlberg's research is that:",
    "options": ["He studied primarily White, middle-class males, limiting cross-cultural and gender generalizability", "He relied on brain imaging data that was inaccurate", "His dilemmas were too simple to reveal nuanced moral reasoning", "He never tested children below age 12"],
    "correct": 0,
    "explanation": "Kohlberg's original studies used male participants, which Gilligan and others used to argue the theory is androcentric. Cross-cultural research also shows variation in stage attainment. These sampling limitations undermine generalizability. Kohlberg used verbal dilemmas and studied children as young as 10.",
    "tags": ["moral-development", "kohlberg", "criticism", "sampling-bias"],
    "difficulty": "medium"
  },
  {
    "text": "In Gilligan's care-oriented model of moral development, the highest level involves:",
    "options": ["Balancing care for self and care for others as equally valid moral concerns", "Universal abstract justice principles", "Obedience to conventional social norms", "Self-sacrifice for the benefit of all others"],
    "correct": 0,
    "explanation": "Gilligan's highest level integrates care for self and care for others — moving beyond self-sacrifice (level 2) to recognize that both self and others deserve moral consideration. This integration of care and self-interest is her equivalent to mature moral reasoning. Universal justice principles characterize Kohlberg's level 3.",
    "tags": ["moral-development", "gilligan", "care-ethics", "advanced"],
    "difficulty": "hard"
  },

  # ── 2. PSYCHOPATHOLOGY – ANXIETY & RELATED DISORDERS ────────────────────
  {
    "text": "A patient experiences recurrent, unexpected panic attacks and persistent worry about future attacks for more than one month. The most likely DSM-5 diagnosis is:",
    "options": ["Panic disorder", "Generalized anxiety disorder", "Social anxiety disorder", "Specific phobia"],
    "correct": 0,
    "explanation": "Panic disorder requires recurrent unexpected panic attacks plus at least one month of persistent concern about future attacks or maladaptive behavioral changes. GAD involves chronic excessive worry about multiple topics without discrete panic attacks. Social anxiety is fear of social evaluation; specific phobia is fear of a specific object/situation.",
    "tags": ["psychopathology", "anxiety", "panic-disorder", "DSM-5"],
    "difficulty": "easy"
  },
  {
    "text": "Which brain structure is most implicated in the fear response that underlies anxiety disorders?",
    "options": ["Amygdala", "Hippocampus", "Prefrontal cortex", "Cerebellum"],
    "correct": 0,
    "explanation": "The amygdala is central to fear conditioning and threat detection; hyperactivity of the amygdala is associated with anxiety disorders including PTSD and phobias. The hippocampus is involved in contextual fear memory. The prefrontal cortex regulates/inhibits amygdala activity. The cerebellum coordinates movement.",
    "tags": ["psychopathology", "anxiety", "amygdala", "biological-basis"],
    "difficulty": "easy"
  },
  {
    "text": "OCD is distinguished from generalized anxiety disorder primarily by the presence of:",
    "options": ["Intrusive, unwanted obsessions and compulsive rituals performed to reduce anxiety", "Excessive, uncontrollable worry about multiple life areas", "Avoidance of specific feared objects or situations", "Hyperarousal and re-experiencing of a traumatic event"],
    "correct": 0,
    "explanation": "OCD is defined by obsessions (intrusive thoughts) and compulsions (rituals to neutralize anxiety), not generalized worry. GAD involves pervasive worry about multiple domains. Specific phobia involves situational avoidance. PTSD involves trauma re-experiencing and hyperarousal.",
    "tags": ["psychopathology", "OCD", "anxiety", "DSM-5"],
    "difficulty": "easy"
  },
  {
    "text": "Exposure and Response Prevention (ERP) is the first-line psychological treatment for OCD because it:",
    "options": ["Prevents compulsive rituals so the patient learns obsessions are tolerable without neutralizing them", "Teaches relaxation techniques to reduce overall arousal", "Restructures negative automatic thoughts about self-worth", "Uses systematic desensitization with a fear hierarchy"],
    "correct": 0,
    "explanation": "ERP exposes patients to feared stimuli while preventing compulsive responses, allowing anxiety to habituate without reinforcement from rituals. This breaks the negative reinforcement cycle that maintains OCD. Relaxation is not sufficient. Cognitive restructuring is CBT. Systematic desensitization is used for phobias.",
    "tags": ["psychopathology", "OCD", "ERP", "treatment"],
    "difficulty": "medium"
  },
  {
    "text": "A combat veteran has nightmares about battle, avoids talking about the war, feels emotionally numb, and is easily startled by loud noises. These symptoms suggest:",
    "options": ["PTSD", "Panic disorder", "GAD", "Acute stress disorder"],
    "correct": 0,
    "explanation": "PTSD criteria include intrusion (nightmares, flashbacks), avoidance (avoiding reminders), negative alterations in cognition/mood (emotional numbing), and hyperarousal (exaggerated startle). Panic disorder involves unexpected attacks without trauma context. Acute stress disorder is similar but resolves within one month post-trauma.",
    "tags": ["psychopathology", "PTSD", "DSM-5", "hyperarousal"],
    "difficulty": "easy"
  },
  {
    "text": "The HPA axis contributes to anxiety disorders by:",
    "options": ["Sustaining cortisol release that maintains hyperarousal and sensitizes the amygdala", "Directly suppressing the amygdala to prevent fear responses", "Releasing oxytocin that increases social anxiety", "Downregulating norepinephrine in the locus coeruleus"],
    "correct": 0,
    "explanation": "Chronic stress activates the HPA axis, producing cortisol that can sensitize amygdala fear circuits and impair prefrontal regulatory control — contributing to anxiety and PTSD. The amygdala is not suppressed by cortisol; rather, chronic cortisol enhances its reactivity. Oxytocin is associated with bonding, not anxiety per se.",
    "tags": ["psychopathology", "anxiety", "HPA-axis", "cortisol", "biological"],
    "difficulty": "hard"
  },
  {
    "text": "Which of the following best distinguishes social anxiety disorder from normal shyness?",
    "options": ["Social anxiety causes significant distress and impairs functioning; shyness does not meet clinical threshold", "Social anxiety is biological; shyness is purely learned", "Social anxiety only occurs with strangers; shyness occurs with everyone", "Shyness responds to medication; social anxiety does not"],
    "correct": 0,
    "explanation": "DSM-5 requires that symptoms cause significant distress or functional impairment to qualify as a disorder. Social anxiety and shyness overlap phenomenologically; the clinical distinction is severity, distress, and interference with daily life. Social anxiety can involve familiar people and responds to SSRIs and CBT.",
    "tags": ["psychopathology", "social-anxiety", "DSM-5", "clinical-threshold"],
    "difficulty": "medium"
  },
  {
    "text": "A patient washes her hands 50 times per day believing germs will kill her family if she doesn't. She recognizes the belief is irrational but cannot stop. This best illustrates:",
    "options": ["OCD with contamination obsessions and washing compulsions", "Illness anxiety disorder", "Specific phobia — germs", "PTSD re-experiencing"],
    "correct": 0,
    "explanation": "OCD involves intrusive obsessions (fear of contamination) and repetitive compulsions (handwashing) performed to neutralize anxiety. Insight is preserved (recognizes irrationality) in most OCD cases. Illness anxiety involves fear of having a disease, not contaminating others. Specific phobia does not involve rituals.",
    "tags": ["psychopathology", "OCD", "contamination", "compulsions"],
    "difficulty": "easy"
  },
  {
    "text": "Which PTSD symptom cluster involves emotional detachment, inability to experience positive emotions, and distorted blame of self?",
    "options": ["Negative alterations in cognition and mood", "Intrusion symptoms", "Avoidance symptoms", "Hyperarousal symptoms"],
    "correct": 0,
    "explanation": "DSM-5 PTSD criterion D ('negative alterations in cognition and mood') includes emotional numbing, persistent negative emotional states, distorted self-blame, and inability to experience positive emotions. Intrusion = flashbacks/nightmares. Avoidance = avoiding reminders. Hyperarousal = startle, insomnia, irritability.",
    "tags": ["psychopathology", "PTSD", "DSM-5", "negative-cognitions"],
    "difficulty": "medium"
  },
  {
    "text": "Generalized anxiety disorder (GAD) is best characterized by:",
    "options": ["Excessive, difficult-to-control worry about multiple topics lasting at least 6 months", "Recurrent unexpected panic attacks and fear of future attacks", "Persistent avoidance of social situations due to fear of embarrassment", "Intrusive thoughts followed by neutralizing rituals"],
    "correct": 0,
    "explanation": "GAD requires at least 6 months of excessive worry across multiple domains (work, health, family) that is difficult to control. Panic disorder involves unexpected attacks. Social anxiety disorder involves social evaluation fears. OCD involves obsessions and compulsions.",
    "tags": ["psychopathology", "GAD", "DSM-5", "anxiety"],
    "difficulty": "easy"
  },
  {
    "text": "A phobia of flying develops after a plane turbulence event; the person avoids all air travel. Avoidance maintains the phobia because:",
    "options": ["It provides negative reinforcement and prevents extinction of the conditioned fear response", "It is positively reinforced by pleasurable ground travel", "The amygdala cannot form new fear memories without exposure", "Avoidance triggers the HPA axis, strengthening the phobia"],
    "correct": 0,
    "explanation": "Avoidance is negatively reinforced (reduces anxiety), maintaining the phobia by preventing extinction. Without exposure, the conditioned fear response is never extinguished. This is why exposure-based therapies (systematic desensitization, flooding) are effective — they force extinction by blocking avoidance.",
    "tags": ["psychopathology", "phobia", "avoidance", "negative-reinforcement", "extinction"],
    "difficulty": "medium"
  },
  {
    "text": "Which neurotransmitter system is most targeted by first-line pharmacological treatment for both GAD and social anxiety disorder?",
    "options": ["Serotonin (SSRIs)", "Dopamine (antipsychotics)", "Acetylcholine (anticholinergics)", "Histamine (antihistamines)"],
    "correct": 0,
    "explanation": "SSRIs (selective serotonin reuptake inhibitors) are first-line pharmacotherapy for GAD, social anxiety disorder, panic disorder, and PTSD. Antipsychotics target dopamine for psychotic disorders. Anticholinergics treat movement disorders. Antihistamines have mild anxiolytic effects but are not first-line.",
    "tags": ["psychopathology", "anxiety", "SSRIs", "serotonin", "pharmacology"],
    "difficulty": "medium"
  },
  {
    "text": "The cognitive model of panic disorder posits that attacks are maintained by:",
    "options": ["Catastrophic misinterpretation of normal bodily sensations as signs of imminent danger", "Failure of the amygdala to habituate to repeated stimuli", "Conditioned fear responses to external situations", "Deficient serotonin preventing inhibition of fear circuits"],
    "correct": 0,
    "explanation": "Clark's cognitive model: individuals with panic disorder catastrophically misinterpret benign physical sensations (rapid heart rate, dizziness) as dangerous (heart attack, 'going crazy'), creating a positive feedback loop. CBT targets these misinterpretations. Amygdala habituation, classical conditioning, and serotonin deficiency are biological perspectives.",
    "tags": ["psychopathology", "panic-disorder", "cognitive-model", "catastrophic-misinterpretation"],
    "difficulty": "hard"
  },
  {
    "text": "PTSD differs from acute stress disorder primarily in terms of:",
    "options": ["Duration — PTSD symptoms persist beyond one month post-trauma", "Type of trauma required for diagnosis", "Presence of hyperarousal symptoms", "Whether avoidance is present"],
    "correct": 0,
    "explanation": "Acute stress disorder shares many PTSD symptom clusters but is diagnosed when symptoms last 3 days to 1 month post-trauma. PTSD is diagnosed when symptoms persist beyond one month. Both require traumatic event exposure. Both can include hyperarousal and avoidance.",
    "tags": ["psychopathology", "PTSD", "acute-stress-disorder", "duration", "DSM-5"],
    "difficulty": "medium"
  },
  {
    "text": "A patient with a specific phobia of dogs has a heart rate spike when she hears barking even without seeing a dog. This demonstrates:",
    "options": ["Stimulus generalization of conditioned fear", "Spontaneous recovery of extinguished fear", "Incubation of fear", "Preparedness theory"],
    "correct": 0,
    "explanation": "Stimulus generalization: the conditioned fear response (originally to dogs) generalizes to other stimuli associated with dogs (barking). Spontaneous recovery is the return of an extinguished response after a rest period. Incubation refers to fear strengthening over time. Preparedness theory explains why certain fears are more easily conditioned.",
    "tags": ["psychopathology", "phobia", "stimulus-generalization", "conditioning"],
    "difficulty": "medium"
  },

  # ── 3. BIPOLAR, PERSONALITY & EATING DISORDERS ──────────────────────────
  {
    "text": "Bipolar I disorder is distinguished from bipolar II disorder primarily by:",
    "options": ["Bipolar I requires at least one full manic episode; bipolar II requires at least one hypomanic episode", "Bipolar I involves only depression; bipolar II involves only mania", "Bipolar II episodes are more severe and require hospitalization", "Bipolar I does not include depressive episodes"],
    "correct": 0,
    "explanation": "Bipolar I: at least one full manic episode (≥7 days or requiring hospitalization). Bipolar II: at least one hypomanic episode (≥4 days, not severe enough for hospitalization) plus at least one major depressive episode. Bipolar I often includes depressive episodes though they are not required for diagnosis.",
    "tags": ["psychopathology", "bipolar", "bipolar-I", "bipolar-II", "DSM-5"],
    "difficulty": "easy"
  },
  {
    "text": "Hypomania differs from full mania primarily in that:",
    "options": ["Hypomania does not cause marked impairment or require hospitalization and lacks psychotic features", "Hypomania involves more severe sleep disturbance", "Hypomania lasts longer than mania", "Hypomania includes grandiose delusions; mania does not"],
    "correct": 0,
    "explanation": "Hypomania (≥4 days) differs from mania in severity: it does not cause marked functional impairment, does not require hospitalization, and lacks psychotic features. Mania causes significant impairment and may include psychosis. Duration for mania is ≥7 days or any duration if hospitalization is needed.",
    "tags": ["psychopathology", "bipolar", "hypomania", "mania", "DSM-5"],
    "difficulty": "medium"
  },
  {
    "text": "A patient has intense fear of abandonment, unstable relationships that alternate between idealization and devaluation, chronic emptiness, and impulsive self-harm. The most likely diagnosis is:",
    "options": ["Borderline personality disorder", "Bipolar II disorder", "Histrionic personality disorder", "Antisocial personality disorder"],
    "correct": 0,
    "explanation": "Borderline PD (BPD) is characterized by identity instability, fear of abandonment, splitting (idealization/devaluation), affective dysregulation, impulsivity, and self-harm. Bipolar II involves episodic mood changes. Histrionic PD involves excessive emotionality and attention-seeking without the same identity disturbance.",
    "tags": ["psychopathology", "borderline-PD", "personality-disorders", "DSM-5"],
    "difficulty": "easy"
  },
  {
    "text": "The defense mechanism most associated with borderline personality disorder is:",
    "options": ["Splitting (seeing people as all-good or all-bad)", "Rationalization", "Sublimation", "Intellectualization"],
    "correct": 0,
    "explanation": "Splitting is a primitive defense mechanism in which objects/people are viewed as entirely good or entirely bad, unable to be integrated. It is a hallmark of BPD. Rationalization involves justifying unacceptable behavior with logical reasons. Sublimation channels impulses into socially acceptable activities.",
    "tags": ["psychopathology", "borderline-PD", "splitting", "defense-mechanisms"],
    "difficulty": "medium"
  },
  {
    "text": "Antisocial personality disorder (ASPD) is characterized by all of the following EXCEPT:",
    "options": ["Fear of abandonment and identity disturbance", "Persistent disregard for others' rights", "Deceitfulness and manipulation for personal gain", "Lack of remorse for harmful behavior"],
    "correct": 0,
    "explanation": "Fear of abandonment and identity disturbance are hallmarks of borderline PD, not ASPD. ASPD is characterized by a pervasive pattern of disregard for others' rights, deceitfulness, impulsivity, aggressiveness, and lack of remorse. ASPD requires evidence of conduct disorder before age 15.",
    "tags": ["psychopathology", "antisocial-PD", "ASPD", "personality-disorders"],
    "difficulty": "medium"
  },
  {
    "text": "Which of the following medical complications is most specifically associated with purging behavior in bulimia nervosa?",
    "options": ["Hypokalemia, dental erosion, and parotid gland enlargement", "Lanugo hair growth and amenorrhea", "Osteoporosis due to calcium malabsorption", "Bradycardia from starvation-induced cardiac muscle loss"],
    "correct": 0,
    "explanation": "Purging (self-induced vomiting) causes hypokalemia (electrolyte loss), dental erosion (acid from gastric contents), and parotid gland swelling (Russell's sign). Lanugo, amenorrhea, osteoporosis, and bradycardia are associated with anorexia nervosa from starvation/malnutrition.",
    "tags": ["psychopathology", "bulimia-nervosa", "medical-complications", "eating-disorders"],
    "difficulty": "medium"
  },
  {
    "text": "The cognitive distortion most central to anorexia nervosa is:",
    "options": ["Overvaluation of thinness and distorted body image despite being underweight", "Fear of choking or vomiting when eating in public", "Belief that food is contaminated and will cause illness", "Catastrophizing normal fluctuations in body weight as total failure"],
    "correct": 0,
    "explanation": "Anorexia nervosa involves intense fear of weight gain and a distorted body image — patients perceive themselves as overweight despite being medically underweight. Fear of choking in public is more consistent with ARFID (avoidant/restrictive food intake disorder). Contamination fears are associated with OCD.",
    "tags": ["psychopathology", "anorexia-nervosa", "cognitive-distortion", "body-image"],
    "difficulty": "easy"
  },
  {
    "text": "Dialectical behavior therapy (DBT) was originally developed to treat which condition?",
    "options": ["Borderline personality disorder", "Anorexia nervosa", "Bipolar I disorder", "Antisocial personality disorder"],
    "correct": 0,
    "explanation": "DBT (Linehan) was developed for BPD and emphasizes dialectical balance between acceptance and change. It includes individual therapy, skills groups (mindfulness, distress tolerance, emotional regulation, interpersonal effectiveness). DBT is now used for other conditions but was designed for BPD.",
    "tags": ["psychopathology", "borderline-PD", "DBT", "treatment"],
    "difficulty": "medium"
  },
  {
    "text": "A patient with bipolar disorder reports needing only 3 hours of sleep, starting multiple business ventures simultaneously, and speaking so rapidly others cannot follow her. These symptoms are best described as:",
    "options": ["A manic episode with decreased need for sleep, goal-directed activity, and pressured speech", "A hypomanic episode because symptoms are not severe enough", "Major depressive episode with psychomotor agitation", "A mixed state because some depressive symptoms are present"],
    "correct": 0,
    "explanation": "Decreased need for sleep, increased goal-directed activity, and pressured speech are classic manic symptoms. Without knowing duration and impairment level, the described symptoms sound consistent with full mania. Hypomania requires less impairment. Depressive episodes involve slowing/fatigue, not elevated energy.",
    "tags": ["psychopathology", "bipolar", "mania", "symptoms"],
    "difficulty": "medium"
  },
  {
    "text": "Anorexia nervosa has the highest mortality rate of any psychiatric disorder primarily due to:",
    "options": ["Medical complications of starvation (cardiac arrhythmias, electrolyte imbalances) and elevated suicide risk", "Chronic liver failure from malnutrition", "Overdose from diuretic misuse", "Secondary immunodeficiency from vitamin deficiencies"],
    "correct": 0,
    "explanation": "Anorexia nervosa's mortality is driven by medical complications of starvation (arrhythmias from electrolyte imbalances, especially hypokalemia; cardiac muscle wasting causing bradycardia) and suicide. It has the highest mortality of any psychiatric disorder. Liver failure and immunodeficiency are not primary causes of death.",
    "tags": ["psychopathology", "anorexia-nervosa", "mortality", "medical-complications"],
    "difficulty": "medium"
  },
  {
    "text": "The cluster B personality disorders in DSM-5 include which of the following groupings?",
    "options": ["Antisocial, borderline, histrionic, and narcissistic personality disorders", "Paranoid, schizoid, and schizotypal personality disorders", "Avoidant, dependent, and obsessive-compulsive personality disorders", "Schizotypal, borderline, and avoidant personality disorders"],
    "correct": 0,
    "explanation": "DSM-5 clusters: Cluster A (odd/eccentric) = paranoid, schizoid, schizotypal; Cluster B (dramatic/emotional/erratic) = antisocial, borderline, histrionic, narcissistic; Cluster C (anxious/fearful) = avoidant, dependent, OCPD. Knowing the three clusters is MCAT-testable.",
    "tags": ["psychopathology", "personality-disorders", "cluster-B", "DSM-5"],
    "difficulty": "medium"
  },
  {
    "text": "Lithium is a first-line mood stabilizer for bipolar disorder. Its mechanism is best described as:",
    "options": ["Modulating inositol phosphate and glycogen synthase kinase-3 signaling, affecting neuronal excitability", "Blocking dopamine D2 receptors to prevent mania", "Enhancing GABA inhibition to stabilize mood", "Inhibiting serotonin reuptake to prevent depressive episodes"],
    "correct": 0,
    "explanation": "Lithium's precise mechanism is debated but involves inhibition of inositol monophosphatase and GSK-3β, affecting second messenger systems and neuroprotection. It is not primarily a dopamine blocker (antipsychotics), GABA enhancer (benzodiazepines/valproate), or SSRI. Its narrow therapeutic window requires blood level monitoring.",
    "tags": ["psychopathology", "bipolar", "lithium", "pharmacology"],
    "difficulty": "hard"
  },
  {
    "text": "Which of the following is a key difference between binge-eating disorder and bulimia nervosa?",
    "options": ["Binge-eating disorder lacks compensatory behaviors (purging, excessive exercise) after binges", "Binge-eating disorder involves restriction between binges; bulimia does not", "Bulimia nervosa does not involve distress about bingeing; binge-eating disorder does", "They are clinically identical but differ only in frequency of binges"],
    "correct": 0,
    "explanation": "Binge-eating disorder (BED) involves recurrent binges with marked distress but NO compensatory behaviors. Bulimia nervosa involves binges followed by compensatory behaviors (purging, fasting, excessive exercise) to prevent weight gain. BED was added as a separate diagnosis in DSM-5.",
    "tags": ["psychopathology", "eating-disorders", "binge-eating-disorder", "bulimia-nervosa"],
    "difficulty": "medium"
  },
  {
    "text": "Affective dysregulation in BPD is best understood as:",
    "options": ["Rapid, intense mood shifts triggered by interpersonal stressors, distinct from the episodic mood changes in bipolar disorder", "Persistent elevated mood lasting days to weeks", "Depressive episodes meeting full MDD criteria", "Psychotic breaks during periods of extreme stress"],
    "correct": 0,
    "explanation": "BPD affective dysregulation involves rapid mood shifts (lasting hours) usually triggered by interpersonal events, contrasting with bipolar mood episodes that last days to weeks without necessarily requiring interpersonal triggers. Brief psychotic episodes can occur in BPD under stress (stress-related paranoia), but psychosis is not the defining feature.",
    "tags": ["psychopathology", "borderline-PD", "affective-dysregulation", "bipolar-differential"],
    "difficulty": "hard"
  },
  {
    "text": "A vignette: A patient restricts food intake severely, exercises 4 hours daily, denies being underweight, and has lost 30 lbs in 3 months. Her BMI is 15. Which treatment approach addresses her core cognitive distortion?",
    "options": ["Cognitive-behavioral therapy targeting body image distortion and fear of weight gain", "Exposure and response prevention for contamination obsessions", "Dialectical behavior therapy focusing on interpersonal effectiveness", "Motivational interviewing to address ambivalence about substance use"],
    "correct": 0,
    "explanation": "Anorexia nervosa's core cognitive features (overvaluation of thinness, distorted body image) are targeted in CBT for eating disorders and enhanced CBT (CBT-E). ERP is for OCD. DBT is used in some AN protocols but addresses emotional dysregulation, not the primary body image distortion. MI is for substance use.",
    "tags": ["psychopathology", "anorexia-nervosa", "CBT", "treatment", "vignette"],
    "difficulty": "medium"
  },

  # ── 4. ADVANCED DEVELOPMENTAL PSYCHOLOGY ────────────────────────────────
  {
    "text": "Bowlby's attachment theory proposes that attachment behavior evolved because it:",
    "options": ["Increases infant survival by keeping infants close to caregivers who provide protection", "Develops solely through classical conditioning of feeding", "Is learned from observing other infants and caregivers", "Serves primarily emotional rather than adaptive functions"],
    "correct": 0,
    "explanation": "Bowlby argued attachment is an evolutionarily adaptive behavioral system — proximity to caregivers increases survival by providing protection from predators. This contrasts with earlier views (Harlow, Bowlby himself influenced by ethology) that attachment derives solely from feeding (drive reduction) or conditioning.",
    "tags": ["developmental", "bowlby", "attachment", "evolutionary-basis"],
    "difficulty": "easy"
  },
  {
    "text": "An 'internal working model' in Bowlby's attachment theory refers to:",
    "options": ["A mental representation of self and others formed through early attachment experiences that guides future relationships", "A behavioral script for seeking proximity when threatened", "The neural circuit in the amygdala activated during separation", "A cognitive schema for problem-solving developed in Piaget's concrete operational stage"],
    "correct": 0,
    "explanation": "Internal working models are cognitive/emotional representations of the self (as worthy of love or not) and others (as reliable or not) derived from early caregiver interactions. These models influence expectations and behavior in later relationships. They are mental constructs, not specific neural circuits or Piagetian schemas.",
    "tags": ["developmental", "bowlby", "internal-working-model", "attachment"],
    "difficulty": "medium"
  },
  {
    "text": "Thomas and Chess identified three temperament types in their New York Longitudinal Study. The 'difficult' child temperament is characterized by:",
    "options": ["Negative mood, irregular routines, intense emotional reactions, and slow adaptation to change", "Easy adaptability, regular routines, and positive mood", "Low activity level and slow but eventual adaptation to new situations", "High sociability and positive reactions to new stimuli"],
    "correct": 0,
    "explanation": "Thomas & Chess's 'difficult' temperament: negative mood, biological irregularity (sleep/feeding), high intensity of reactions, and slow adaptability. 'Easy' children (60%): positive mood, regularity, adaptability. 'Slow-to-warm' children: low activity, mild negative reactions initially but eventual adaptation.",
    "tags": ["developmental", "temperament", "thomas-chess", "difficult"],
    "difficulty": "medium"
  },
  {
    "text": "What is the typical sequence of early language milestones?",
    "options": ["Cooing → babbling → holophrases → telegraphic speech → multi-word sentences", "Babbling → cooing → holophrases → telegraphic speech", "Holophrases → babbling → telegraphic speech → cooing", "Cooing → holophrases → babbling → telegraphic speech"],
    "correct": 0,
    "explanation": "Language milestones: cooing (2–3 months, vowel sounds) → babbling (6–8 months, consonant-vowel repetition) → holophrases (12 months, single words representing whole sentences) → telegraphic speech (18–24 months, two-word utterances like 'more milk') → multi-word sentences. Babbling always precedes holophrases.",
    "tags": ["developmental", "language", "milestones", "babbling", "holophrases"],
    "difficulty": "easy"
  },
  {
    "text": "James Marcia's identity 'foreclosure' status describes adolescents who:",
    "options": ["Have committed to an identity without exploring alternatives, often adopting parental values uncritically", "Have explored identity options but not yet made a commitment", "Have neither explored nor committed to an identity", "Have explored various identities and made a firm commitment"],
    "correct": 0,
    "explanation": "Marcia's four statuses: foreclosure (commitment without exploration), moratorium (exploration without commitment), diffusion (no exploration or commitment), achievement (exploration followed by commitment). Foreclosed individuals often adopt parents' values without questioning them.",
    "tags": ["developmental", "marcia", "identity", "foreclosure", "adolescence"],
    "difficulty": "medium"
  },
  {
    "text": "Marcia's identity 'moratorium' status is characterized by:",
    "options": ["Active exploration of identity options without yet making a commitment", "Commitment to an identity adopted from authority figures without personal exploration", "Lack of both exploration and commitment", "Stable identity achieved through exploration and commitment"],
    "correct": 0,
    "explanation": "Moratorium: the adolescent is actively exploring various roles and ideologies but has not yet committed. Foreclosure = commitment without exploration. Diffusion = no exploration or commitment. Achievement = exploration followed by commitment. Moratorium is often necessary before achieving a stable identity.",
    "tags": ["developmental", "marcia", "identity", "moratorium"],
    "difficulty": "medium"
  },
  {
    "text": "Kübler-Ross's five stages of grief (DABDA) are, in order:",
    "options": ["Denial, Anger, Bargaining, Depression, Acceptance", "Anger, Denial, Bargaining, Acceptance, Depression", "Denial, Depression, Anger, Bargaining, Acceptance", "Bargaining, Denial, Anger, Depression, Acceptance"],
    "correct": 0,
    "explanation": "DABDA: Denial → Anger → Bargaining → Depression → Acceptance. Kübler-Ross identified these stages in terminally ill patients. Importantly, these stages are not linear — people may skip stages or return to earlier ones. The model applies to any significant loss, not only death.",
    "tags": ["developmental", "kubler-ross", "grief", "stages"],
    "difficulty": "easy"
  },
  {
    "text": "Bowlby's concept of the 'secure base' refers to:",
    "options": ["The caregiver functioning as a safe haven from which the infant can confidently explore the environment", "A brain region that regulates attachment behavior", "The toddler's preference for familiar environments over novel ones", "A cognitive map of safe and unsafe locations formed in childhood"],
    "correct": 0,
    "explanation": "The secure base is a caregiver who provides emotional security, allowing the infant to explore confidently knowing the caregiver is available if distress arises. This concept bridges Ainsworth's Strange Situation findings with Bowlby's evolutionary theory — secure attachment promotes exploration and healthy development.",
    "tags": ["developmental", "bowlby", "secure-base", "attachment"],
    "difficulty": "easy"
  },
  {
    "text": "A 14-month-old consistently explores a new room but returns to her mother when a stranger enters and is easily comforted upon mother's return. This pattern indicates:",
    "options": ["Secure attachment", "Anxious-ambivalent attachment", "Avoidant attachment", "Disorganized attachment"],
    "correct": 0,
    "explanation": "Secure attachment (Ainsworth): uses caregiver as secure base for exploration, shows distress at separation, seeks comfort upon reunion and is easily calmed. Anxious-ambivalent infants show distress and difficulty being comforted. Avoidant infants show little distress and ignore the caregiver. Disorganized shows no consistent strategy.",
    "tags": ["developmental", "attachment", "ainsworth", "secure"],
    "difficulty": "easy"
  },
  {
    "text": "The 'slow-to-warm-up' temperament type (Thomas & Chess) is distinguished from the 'difficult' type primarily by:",
    "options": ["Low initial positive reactions that eventually improve with repeated exposure; difficult children do not adapt as readily", "Higher intensity of negative emotional reactions", "Greater biological irregularity in sleep and feeding", "Inability to adapt even with repeated exposure to new situations"],
    "correct": 0,
    "explanation": "Slow-to-warm children show mild negative reactions initially but gradually adapt with repeated, low-pressure exposure. Difficult children show intense negative reactions and poor adaptability even with time. Both types show initial withdrawal, but slow-to-warm children show lower intensity and eventual adaptation.",
    "tags": ["developmental", "temperament", "slow-to-warm", "thomas-chess"],
    "difficulty": "hard"
  },
  {
    "text": "Telegraphic speech, occurring around age 18–24 months, is best described as:",
    "options": ["Two-word utterances that convey meaning using content words while omitting grammatical function words", "Single-word utterances that represent whole concepts", "Grammatically complete sentences with simplified vocabulary", "Repetitive babbling with adult-like intonation patterns"],
    "correct": 0,
    "explanation": "Telegraphic speech: children use two-word phrases combining content words (nouns, verbs) while omitting function words (articles, prepositions) — e.g., 'more milk,' 'daddy go.' Holophrases are single-word representations. Babbling precedes telegraphic speech.",
    "tags": ["developmental", "language", "telegraphic-speech", "milestones"],
    "difficulty": "easy"
  },
  {
    "text": "Which of Marcia's identity statuses is associated with the best long-term psychological outcomes (highest self-esteem, clearest sense of purpose)?",
    "options": ["Identity achievement", "Moratorium", "Foreclosure", "Diffusion"],
    "correct": 0,
    "explanation": "Identity achievement (exploration followed by commitment) is associated with highest self-esteem, mature reasoning, and psychological well-being. Moratorium shows high anxiety during exploration. Foreclosure shows rigidity. Diffusion is associated with highest anxiety, low self-esteem, and poor psychological outcomes.",
    "tags": ["developmental", "marcia", "identity-achievement", "outcomes"],
    "difficulty": "medium"
  },
  {
    "text": "A key evolutionary argument in Bowlby's attachment theory is that the attachment behavioral system is activated by:",
    "options": ["Perceived threat, which triggers proximity-seeking to the caregiver as a protective strategy", "Hunger, which reinforces proximity through feeding (drive reduction)", "Social learning from observing other infants", "Cognitive development reaching the sensorimotor stage"],
    "correct": 0,
    "explanation": "Bowlby proposed that perceived threats (fear, pain, unfamiliarity) activate the attachment behavioral system, motivating proximity-seeking. This is the evolutionary basis — proximity to caregivers provides protection. Drive reduction theory (proximity = food source) was rejected by Harlow's contact comfort experiments.",
    "tags": ["developmental", "bowlby", "attachment", "evolutionary", "threat"],
    "difficulty": "medium"
  },
  {
    "text": "Critical periods in language acquisition suggest that exposure to language must occur:",
    "options": ["Before puberty for full native-like language acquisition to occur", "Within the first 6 months of life for any language development", "After cognitive development reaches formal operations", "Only during the babbling stage or language cannot develop"],
    "correct": 0,
    "explanation": "Lenneberg's critical period hypothesis: language acquisition is optimal before puberty due to neural plasticity. Evidence includes Genie (language deprivation case) and second-language accent acquisition. Children exposed to language before puberty achieve native-like fluency; those exposed after do not. Babbling is important but not the only window.",
    "tags": ["developmental", "language", "critical-period", "lenneberg"],
    "difficulty": "medium"
  },
  {
    "text": "The 'goodness of fit' concept in Thomas & Chess's temperament research refers to:",
    "options": ["The match between a child's temperament and parental expectations/environment, which predicts adjustment", "The degree to which temperament type is inherited from biological parents", "The compatibility between difficult and easy temperament siblings", "A child's ability to adapt temperament style to different social contexts"],
    "correct": 0,
    "explanation": "Goodness of fit: adjustment outcomes depend not just on temperament type but on how well the environment accommodates the child's temperament. A 'difficult' child raised with patient, structured parenting may have good outcomes. Poor fit (e.g., demanding parents with a slow-to-warm child) predicts behavioral problems.",
    "tags": ["developmental", "temperament", "goodness-of-fit", "thomas-chess"],
    "difficulty": "hard"
  },

  # ── 5. PERSONALITY ASSESSMENT ────────────────────────────────────────────
  {
    "text": "The MMPI-2 is best classified as a(n):",
    "options": ["Objective self-report personality inventory", "Projective technique relying on ambiguous stimuli", "Neuropsychological battery assessing cognitive deficits", "Structured clinical interview format"],
    "correct": 0,
    "explanation": "The MMPI-2 is an objective self-report inventory with empirically derived scales and validity scales. It requires true/false responses to 567 items. Projective techniques (Rorschach, TAT) use ambiguous stimuli. Neuropsychological batteries assess brain-behavior relationships.",
    "tags": ["personality-assessment", "MMPI", "objective-assessment"],
    "difficulty": "easy"
  },
  {
    "text": "A key advantage of the MMPI-2 over projective tests is that it:",
    "options": ["Has established validity scales that detect underreporting (defensiveness) and overreporting (malingering)", "Can reveal unconscious conflicts that self-report cannot access", "Requires no reading ability to complete", "Is free from cultural bias due to its empirical derivation"],
    "correct": 0,
    "explanation": "The MMPI-2 includes validity scales (L = lie scale, F = infrequency, K = defensiveness, Fp) to detect response biases like malingering or defensiveness. This is a major advantage over projective tests. Projective tests theoretically access unconscious material. MMPI-2 requires reading ability (6th-grade level) and is not free from cultural bias.",
    "tags": ["personality-assessment", "MMPI", "validity-scales", "malingering"],
    "difficulty": "medium"
  },
  {
    "text": "The Rorschach inkblot test is classified as a projective technique because:",
    "options": ["Subjects project psychological needs, conflicts, and personality characteristics onto ambiguous stimuli", "It projects visual images onto a screen for subjects to identify", "It uses standardized, unambiguous stimuli to elicit responses", "Examiners project expected responses based on clinical training"],
    "correct": 0,
    "explanation": "Projective tests use ambiguous stimuli (inkblots, vague pictures) to elicit responses that are assumed to reflect the respondent's unconscious processes, needs, and personality characteristics. The ambiguity allows projection of internal states. Objective tests use unambiguous stimuli with structured response formats.",
    "tags": ["personality-assessment", "rorschach", "projective-tests"],
    "difficulty": "easy"
  },
  {
    "text": "A major criticism of the Rorschach inkblot test is that it:",
    "options": ["Has questionable interrater reliability and limited evidence of diagnostic validity", "Is too transparent, making dissimulation easy", "Measures only conscious, accessible personality traits", "Has been standardized on populations that are too large to be meaningful"],
    "correct": 0,
    "explanation": "The Rorschach has been criticized for poor interrater reliability (even with the Exner Comprehensive System) and limited criterion validity for clinical diagnosis. It scores complex verbal responses subjectively. Objective tests (MMPI) have better reliability. Transparency/dissimulation is a concern for objective tests, not projective.",
    "tags": ["personality-assessment", "rorschach", "criticism", "reliability", "validity"],
    "difficulty": "medium"
  },
  {
    "text": "The Thematic Apperception Test (TAT) requires subjects to:",
    "options": ["Create stories about ambiguous pictures, which are analyzed for themes revealing underlying motivations", "Sort cards depicting personality traits from most to least characteristic", "Respond true or false to a series of self-descriptive statements", "Identify shapes in inkblots as quickly as possible"],
    "correct": 0,
    "explanation": "The TAT (Murray) presents pictures of ambiguous social scenes and asks subjects to narrate a story. Themes in the stories are assumed to reflect needs, motivations, and conflicts. McClelland used a TAT-derived measure to assess need for achievement. Inkblot responses characterize the Rorschach.",
    "tags": ["personality-assessment", "TAT", "projective", "murray"],
    "difficulty": "easy"
  },
  {
    "text": "Which psychometric property refers to the consistency of a test in measuring the same construct across time?",
    "options": ["Test-retest reliability", "Content validity", "Criterion validity", "Construct validity"],
    "correct": 0,
    "explanation": "Test-retest reliability measures temporal consistency — administering the same test twice yields similar scores. Content validity assesses whether test items represent all aspects of the construct. Criterion validity compares test scores to external outcomes. Construct validity assesses whether the test measures the intended theoretical construct.",
    "tags": ["personality-assessment", "psychometrics", "test-retest-reliability"],
    "difficulty": "easy"
  },
  {
    "text": "Standardization of a psychological test involves:",
    "options": ["Establishing uniform administration procedures and norms from a representative sample", "Ensuring all test items are novel and non-overlapping", "Translating a test into multiple languages for cross-cultural use", "Removing items that show cultural bias through statistical analysis"],
    "correct": 0,
    "explanation": "Standardization requires establishing uniform conditions for administering, scoring, and interpreting a test, and developing normative data from a representative sample so individual scores can be compared to the population. Item analysis for bias is one step in test development but not the definition of standardization.",
    "tags": ["personality-assessment", "psychometrics", "standardization", "norms"],
    "difficulty": "medium"
  },
  {
    "text": "Construct validity of a personality test can be demonstrated by showing:",
    "options": ["Convergent evidence (correlates with similar measures) and discriminant evidence (does not correlate with unrelated measures)", "High internal consistency (Cronbach's alpha)", "The test predicts future behavior in real-world settings", "Agreement between two different raters scoring the same responses"],
    "correct": 0,
    "explanation": "Construct validity (Campbell & Fiske's multitrait-multimethod matrix) requires convergent validity (correlation with theoretically related measures) and discriminant validity (low correlation with theoretically unrelated measures). Internal consistency reflects reliability. Predictive validity (future behavior) is a type of criterion validity. Interrater agreement is a reliability measure.",
    "tags": ["personality-assessment", "psychometrics", "construct-validity"],
    "difficulty": "hard"
  },
  {
    "text": "A behavioral assessment approach to personality would emphasize:",
    "options": ["Observing specific behaviors in defined situations rather than inferring underlying traits or unconscious processes", "Analyzing unconscious conflicts projected onto ambiguous stimuli", "Administering standardized questionnaires to identify trait profiles", "Assessing neural correlates of personality using brain imaging"],
    "correct": 0,
    "explanation": "Behavioral assessment (rooted in behaviorism) focuses on observable, measurable behaviors in specific contexts, avoiding inferences about unobservable traits or unconscious processes. Psychodynamic assessment (projective tests) infers unconscious dynamics. Trait assessment uses questionnaires. Brain imaging reflects biological approaches.",
    "tags": ["personality-assessment", "behavioral-assessment", "behaviorism"],
    "difficulty": "medium"
  },
  {
    "text": "A psychodynamic approach to personality assessment would be most likely to use:",
    "options": ["Projective tests (Rorschach, TAT) and free association to access unconscious processes", "Structured behavioral observations in natural settings", "Self-report inventories with validated scales", "Neuropsychological tests of executive function"],
    "correct": 0,
    "explanation": "Psychodynamic assessment assumes that important personality processes are unconscious and cannot be directly observed or self-reported; projective tests and free association are used to access these processes indirectly. Behavioral assessments use observation; trait assessments use self-report; neuropsychological tests assess brain functions.",
    "tags": ["personality-assessment", "psychodynamic", "projective", "unconscious"],
    "difficulty": "easy"
  },
  {
    "text": "A researcher correlates MMPI-2 scores with psychiatric diagnoses made by structured clinical interview. This assesses the test's:",
    "options": ["Criterion validity (concurrent validity)", "Content validity", "Test-retest reliability", "Internal consistency"],
    "correct": 0,
    "explanation": "Criterion validity (concurrent): comparing test scores to an external criterion measured at the same time (diagnosis via interview). Predictive validity uses future criteria. Content validity assesses item representativeness. Test-retest and internal consistency are reliability measures.",
    "tags": ["personality-assessment", "psychometrics", "criterion-validity"],
    "difficulty": "medium"
  },
  {
    "text": "The 'base rate' problem in personality assessment refers to:",
    "options": ["The fact that tests must account for how rare a disorder is in the population to maximize diagnostic accuracy", "The frequency with which items appear on a standardized test", "The rate at which test scores change over time due to practice effects", "The proportion of items that a sample correctly endorses"],
    "correct": 0,
    "explanation": "Base rate problem: if a disorder is rare (e.g., 1% prevalence), even a highly accurate test will generate many false positives. Positive predictive value depends on both test sensitivity/specificity AND the prevalence (base rate) of the condition. Ignoring base rates leads to overdiagnosis of rare conditions.",
    "tags": ["personality-assessment", "psychometrics", "base-rate", "diagnostic-accuracy"],
    "difficulty": "hard"
  },
  {
    "text": "Which of the following is an advantage of projective tests over self-report measures?",
    "options": ["They are less susceptible to deliberate faking or impression management", "They have stronger empirical reliability and validity data", "They are less time-consuming to administer and score", "They provide normative data applicable across all cultural groups"],
    "correct": 0,
    "explanation": "Because projective stimuli are ambiguous and the purpose is not obvious, respondents cannot easily control their responses to create a desired impression (though sophisticated test-takers can). Self-report measures can be faked more easily. Projective tests generally have weaker reliability/validity, are time-consuming, and have limited cross-cultural norms.",
    "tags": ["personality-assessment", "projective-tests", "faking", "impression-management"],
    "difficulty": "medium"
  },
  {
    "text": "Interrater reliability is most important for which type of assessment?",
    "options": ["Projective tests where scoring requires clinical judgment", "True/false self-report inventories with automated scoring", "Computer-administered cognitive tests", "Multiple-choice personality questionnaires"],
    "correct": 0,
    "explanation": "Interrater reliability (agreement between scorers) is critical for assessments requiring subjective clinical judgment — projective tests, behavioral observations, and open-ended interviews. Objective measures with automated scoring have perfect interrater agreement by design. Multiple-choice questionnaires are also objectively scored.",
    "tags": ["personality-assessment", "psychometrics", "interrater-reliability"],
    "difficulty": "medium"
  },
  {
    "text": "A test has high internal consistency (Cronbach's alpha = 0.92) but only moderate test-retest reliability (r = 0.55). This pattern suggests:",
    "options": ["The items are highly intercorrelated but scores fluctuate over time, possibly measuring a state rather than a stable trait", "The test is measuring multiple distinct constructs", "The test is valid but not reliable", "Standardization norms need to be updated"],
    "correct": 0,
    "explanation": "High internal consistency (items coherent) plus low test-retest reliability (scores unstable over time) suggests the test may be measuring a psychological state (mood, anxiety today) rather than a stable trait. Reliability is necessary for validity but they are distinct properties. Validity cannot exceed reliability.",
    "tags": ["personality-assessment", "psychometrics", "reliability", "state-vs-trait"],
    "difficulty": "hard"
  },

  # ── 6. MOTIVATION ADVANCED ───────────────────────────────────────────────
  {
    "text": "Self-determination theory (Deci & Ryan) proposes that intrinsic motivation is optimal when which three basic psychological needs are satisfied?",
    "options": ["Autonomy, competence, and relatedness", "Achievement, affiliation, and power", "Safety, esteem, and self-actualization", "Hunger, thirst, and sexual drive reduction"],
    "correct": 0,
    "explanation": "SDT posits three universal psychological needs: autonomy (feeling volitional control), competence (feeling effective), and relatedness (feeling connected to others). When these are satisfied, intrinsic motivation and psychological well-being are enhanced. Achievement/affiliation/power are McClelland's needs. Maslow's hierarchy includes safety, esteem, and self-actualization.",
    "tags": ["motivation", "SDT", "self-determination-theory", "deci-ryan"],
    "difficulty": "easy"
  },
  {
    "text": "The overjustification effect (undermining effect) predicts that:",
    "options": ["Adding external rewards for an already intrinsically motivating activity reduces intrinsic motivation", "Intrinsic motivation always overcomes external reward systems", "External rewards increase intrinsic interest when given unexpectedly", "Tasks with no external rewards will never be completed"],
    "correct": 0,
    "explanation": "The overjustification effect (Lepper et al.): when people are given external rewards for activities they already find intrinsically interesting, intrinsic motivation decreases. The person attributes their engagement to the external reward rather than genuine interest. Unexpected rewards have less negative impact on intrinsic motivation.",
    "tags": ["motivation", "overjustification", "intrinsic-motivation", "extrinsic-reward"],
    "difficulty": "medium"
  },
  {
    "text": "McClelland's need for achievement (nAch) is best assessed using:",
    "options": ["TAT stories scored for achievement themes", "Direct self-report questionnaires about career goals", "Behavioral observation of task persistence", "Implicit association tests measuring response latency"],
    "correct": 0,
    "explanation": "McClelland used a TAT-derived scoring system to measure nAch — stories written to ambiguous pictures are scored for achievement imagery. McClelland argued that implicit motives like nAch are best captured through projective/implicit methods rather than self-report, which measures explicit self-concept of achievement.",
    "tags": ["motivation", "mcclelland", "nAch", "TAT"],
    "difficulty": "medium"
  },
  {
    "text": "According to Weiner's attribution theory of achievement, a student who attributes failure to low ability is making an attribution that is:",
    "options": ["Internal, stable, and uncontrollable", "External, stable, and controllable", "Internal, unstable, and controllable", "External, unstable, and uncontrollable"],
    "correct": 0,
    "explanation": "Weiner's 3-dimensional model: ability is internal (within the person), stable (doesn't change easily), and uncontrollable (can't be directly changed). Attributing failure to ability predicts low expectancy for future success and helplessness. Effort is internal/unstable/controllable — more adaptive for motivation.",
    "tags": ["motivation", "weiner", "attribution-theory", "achievement"],
    "difficulty": "medium"
  },
  {
    "text": "Which attribution for academic success is most likely to sustain motivation for future challenges?",
    "options": ["Internal, unstable, controllable (e.g., effort)", "External, stable, uncontrollable (e.g., task ease)", "Internal, stable, uncontrollable (e.g., innate ability)", "External, unstable, uncontrollable (e.g., luck)"],
    "correct": 0,
    "explanation": "Effort attributions (internal, unstable, controllable) sustain motivation because success is attributed to something the person can repeat and control. Ability attributions are less controllable. External attributions (luck, easy task) undermine pride and motivation. Controllability and instability mean the student can improve through future effort.",
    "tags": ["motivation", "weiner", "attribution-theory", "effort"],
    "difficulty": "hard"
  },
  {
    "text": "Drive reduction theory (Hull) proposes that motivation arises from:",
    "options": ["Biological needs creating internal tension (drives) that motivate behavior to restore homeostasis", "External incentives that pull behavior toward desirable stimuli", "Curiosity and intrinsic interest in novel stimulation", "Cognitive appraisals of expected reward value"],
    "correct": 0,
    "explanation": "Hull's drive reduction theory: biological needs (hunger, thirst) create internal tension (drives) that motivate behavior; behaviors that reduce the drive are reinforced (negative reinforcement). Incentive theory focuses on external motivators (pull). Curiosity is an intrinsic/optimal arousal concept. Cognitive appraisals characterize expectancy-value theories.",
    "tags": ["motivation", "drive-reduction", "hull", "homeostasis"],
    "difficulty": "medium"
  },
  {
    "text": "Incentive theory differs from drive reduction theory in that it emphasizes:",
    "options": ["External stimuli that pull behavior toward goals, rather than internal deficits that push behavior", "Biological homeostasis as the primary source of motivation", "The role of unconscious conflicts in directing behavior", "Cognitive evaluation of one's own competence"],
    "correct": 0,
    "explanation": "Incentive theory: behavior is motivated by external rewards (incentives) that attract/pull — money, food, praise. This explains why people seek pleasures even when no drive deficit exists. Drive reduction theory emphasizes internal push (deficit → drive → behavior → drive reduction). Both contribute to a complete account of motivation.",
    "tags": ["motivation", "incentive-theory", "drive-reduction"],
    "difficulty": "medium"
  },
  {
    "text": "A student who practices piano for hours because she finds it deeply enjoyable and personally meaningful is demonstrating:",
    "options": ["Intrinsic motivation", "Identified regulation (SDT)", "Introjected regulation (SDT)", "External regulation"],
    "correct": 0,
    "explanation": "Intrinsic motivation: engaging in an activity for the inherent satisfaction and enjoyment. SDT's autonomy continuum: external regulation (do it for reward/avoid punishment) → introjected (do it to avoid guilt) → identified (value the activity) → integrated → intrinsic (purely enjoyable). Practicing for personal enjoyment is intrinsic.",
    "tags": ["motivation", "intrinsic-motivation", "SDT"],
    "difficulty": "easy"
  },
  {
    "text": "The Yerkes-Dodson law describes the relationship between arousal and performance as:",
    "options": ["An inverted U-shape, with optimal performance at moderate arousal levels", "A linear positive relationship — more arousal always improves performance", "A linear negative relationship — higher arousal always impairs performance", "No consistent relationship, depending entirely on task difficulty"],
    "correct": 0,
    "explanation": "Yerkes-Dodson law: performance is best at moderate arousal. Too little arousal = poor motivation; too much = anxiety/interference. The optimal arousal level varies with task complexity — simple tasks benefit from higher arousal; complex tasks require lower arousal for peak performance. This is an inverted U-curve.",
    "tags": ["motivation", "yerkes-dodson", "arousal", "performance"],
    "difficulty": "easy"
  },
  {
    "text": "According to SDT, a manager who gives employees choice in how to complete tasks, provides positive competency feedback, and fosters team cohesion is supporting:",
    "options": ["Autonomy, competence, and relatedness simultaneously", "Only extrinsic motivation through feedback", "Drive reduction through task completion", "Incentive theory through external rewards"],
    "correct": 0,
    "explanation": "SDT: giving choice supports autonomy; positive feedback on effectiveness supports competence; team cohesion supports relatedness. All three basic needs being met predicts the highest intrinsic motivation, engagement, and well-being. Feedback alone (praise without choice) supports competence but may undermine autonomy.",
    "tags": ["motivation", "SDT", "autonomy", "competence", "relatedness"],
    "difficulty": "medium"
  },
  {
    "text": "Students who believe intelligence is fixed (entity theory) vs. malleable (incremental theory) differ in attribution patterns after failure. Entity theorists are more likely to attribute failure to:",
    "options": ["Fixed internal ability, leading to helpless responses", "Insufficient effort, leading to increased persistence", "External circumstances, maintaining self-esteem", "Bad luck, which predicts optimism for future success"],
    "correct": 0,
    "explanation": "Dweck's mindset theory: entity (fixed) theorists attribute failure to stable, uncontrollable ability → helplessness (Weiner: internal/stable/uncontrollable). Incremental (growth) theorists attribute failure to effort → mastery orientation. Entity mindset predicts avoidance of challenges; incremental mindset predicts persistence.",
    "tags": ["motivation", "dweck", "mindset", "entity-theory", "attribution"],
    "difficulty": "hard"
  },
  {
    "text": "McClelland found that individuals high in need for achievement (nAch) prefer tasks that are:",
    "options": ["Moderately difficult, where success depends on skill and where feedback is available", "Very easy, guaranteeing frequent success", "Extremely difficult, demonstrating exceptional ability", "Irrelevant to personal performance, like games of pure chance"],
    "correct": 0,
    "explanation": "High nAch individuals prefer tasks with moderate difficulty — difficult enough to be challenging and skill-dependent, but achievable. They want feedback on performance to know whether they succeeded through effort and skill. Easy tasks lack challenge; impossible tasks give no success feedback; chance tasks don't reflect ability.",
    "tags": ["motivation", "mcclelland", "nAch", "task-difficulty"],
    "difficulty": "medium"
  },
  {
    "text": "According to Deci & Ryan, adding verbal rewards (praise for a well-done job) to intrinsically motivating tasks tends to:",
    "options": ["Enhance intrinsic motivation by supporting competence feelings when informational", "Always undermine intrinsic motivation through overjustification", "Have no effect on intrinsic motivation regardless of context", "Decrease intrinsic motivation only in children, not adults"],
    "correct": 0,
    "explanation": "SDT distinguishes between informational and controlling rewards. Verbal praise that provides specific competency-related information (informational aspect) can enhance intrinsic motivation by satisfying the competence need. Controlling rewards that undermine autonomy reduce intrinsic motivation. This is a nuance beyond the basic overjustification effect.",
    "tags": ["motivation", "SDT", "verbal-rewards", "competence", "informational"],
    "difficulty": "hard"
  },
  {
    "text": "The Zeigarnik effect, relevant to motivation, refers to:",
    "options": ["People remember uncompleted tasks better than completed ones, suggesting tension from unfinished goals maintains motivation", "People forget failure experiences more readily than success experiences", "Motivation increases linearly as a task nears completion", "Arousal always impairs memory for complex tasks"],
    "correct": 0,
    "explanation": "The Zeigarnik effect: incomplete tasks create cognitive/motivational tension that keeps them in mind until completed. This relates to goal-directed motivation — the system remains 'activated' for unfinished goals. Yerkes-Dodson addresses arousal-performance; neither forgetting failure nor linear motivation matches the Zeigarnik effect.",
    "tags": ["motivation", "zeigarnik-effect", "goal-pursuit", "memory"],
    "difficulty": "medium"
  },
  {
    "text": "A child who used to love drawing begins drawing only when promised a sticker, and stops drawing when stickers are no longer given. This demonstrates:",
    "options": ["Overjustification effect — extrinsic reward undermined intrinsic motivation", "Operant extinction of a previously reinforced behavior", "Learned helplessness from reward removal", "Drive reduction — the sticker satisfied the 'drawing drive'"],
    "correct": 0,
    "explanation": "Lepper's overjustification/undermining effect: rewarding intrinsically motivated behavior shifts the child's attribution from 'I draw because I enjoy it' to 'I draw to get stickers.' When stickers stop, the child perceives no reason to draw. This demonstrates how extrinsic rewards can undermine intrinsic motivation for already-enjoyable activities.",
    "tags": ["motivation", "overjustification", "extrinsic-reward", "intrinsic-motivation"],
    "difficulty": "medium"
  },

  # ── 7. ADVANCED SOCIAL INFLUENCE ────────────────────────────────────────
  {
    "text": "In Asch's conformity experiments, participants gave obviously wrong answers to line-length judgments when:",
    "options": ["Confederates unanimously gave an incorrect answer, demonstrating normative social influence", "The correct answer was ambiguous or unclear", "Participants were told their answers would be made public", "Confederates were perceived as experts in visual measurement"],
    "correct": 0,
    "explanation": "Asch showed participants gave wrong answers on unambiguous line judgments when all confederates unanimously chose the wrong line. This demonstrates normative social influence — conforming to avoid social rejection. Informational influence occurs when the situation is ambiguous. Unanimity of confederates is key — one dissenter dramatically reduces conformity.",
    "tags": ["social-influence", "asch", "conformity", "normative-social-influence"],
    "difficulty": "easy"
  },
  {
    "text": "Informational social influence is most likely to occur when:",
    "options": ["The situation is ambiguous or the person lacks expertise and looks to others for guidance", "The person wants to be liked by the group", "The authority figure is physically present", "The group is highly cohesive and has clear norms"],
    "correct": 0,
    "explanation": "Informational social influence: using others' behavior as information to guide correct behavior, especially in ambiguous or novel situations where one lacks personal expertise. Normative social influence is driven by wanting social approval. Physical presence of authority relates to Milgram obedience.",
    "tags": ["social-influence", "informational-social-influence", "ambiguity"],
    "difficulty": "medium"
  },
  {
    "text": "The foot-in-the-door technique works because of:",
    "options": ["Consistency motivation and self-perception — agreeing to a small request creates an identity as a 'helpful person' who then complies with larger requests", "Reciprocity — the person feels obligated to return a favor", "Scarcity — the limited-time offer increases perceived value", "Social proof — seeing others comply increases willingness"],
    "correct": 0,
    "explanation": "Foot-in-the-door (Freedman & Fraser): small initial commitment creates self-perception as a compliant, helpful person, leading to larger compliance. This leverages consistency motivation (people want their behavior to match their self-image). Reciprocity, scarcity, and social proof are Cialdini's other influence principles.",
    "tags": ["social-influence", "foot-in-the-door", "consistency", "self-perception"],
    "difficulty": "medium"
  },
  {
    "text": "The door-in-the-face technique is based on which principle?",
    "options": ["Reciprocal concession — after a large request is refused, a smaller request seems like a concession the person feels obligated to reciprocate", "Consistency — a small initial yes leads to larger commitments", "Commitment — public commitment to a position increases later compliance", "Social proof — majority behavior defines appropriate response"],
    "correct": 0,
    "explanation": "Door-in-the-face (Cialdini): a large initial request is made and refused; then a smaller target request is made. The requester's concession to a smaller ask creates reciprocal pressure on the target to also concede. This exploits the reciprocity norm. Foot-in-the-door uses consistency/self-perception instead.",
    "tags": ["social-influence", "door-in-the-face", "reciprocity", "concession"],
    "difficulty": "medium"
  },
  {
    "text": "Cialdini's principle of scarcity influences compliance because:",
    "options": ["People assign more value to things that are rare or becoming unavailable (reactance theory)", "People imitate the behavior of the majority who possess scarce items", "Limited availability signals authority and expertise", "Scarcity creates commitment through public statements of desire"],
    "correct": 0,
    "explanation": "Scarcity: items perceived as rare are valued more highly (psychological reactance — restricted freedom increases desire). 'Only 3 left!' increases purchase likelihood. Social proof involves majority behavior. Authority involves credibility. Commitment involves public consistency.",
    "tags": ["social-influence", "scarcity", "cialdini", "reactance"],
    "difficulty": "medium"
  },
  {
    "text": "Moscovici's research on minority influence showed that a consistent minority can change majority opinion by:",
    "options": ["Demonstrating conviction and consistency over time, causing the majority to engage in deeper processing of the minority's position", "Holding formal authority positions in the group", "Using normative pressure through social exclusion threats", "Offering material incentives for attitude change"],
    "correct": 0,
    "explanation": "Moscovici's minority influence: consistent, confident minorities shift majority views through informational influence — their consistency signals genuine conviction and causes majority members to reconsider their position. This is conversion (private attitude change) rather than compliance. Authority and normative pressure characterize majority influence.",
    "tags": ["social-influence", "moscovici", "minority-influence", "consistency"],
    "difficulty": "medium"
  },
  {
    "text": "Group polarization refers to the tendency for group discussion to:",
    "options": ["Amplify the initial predominant tendency of the group, making moderate positions more extreme", "Move toward compromise between opposing positions", "Produce conformity to the group average", "Increase individual variance in opinions after discussion"],
    "correct": 0,
    "explanation": "Group polarization (Moscovici & Zavalloni): group discussion strengthens the initially dominant position — if the group initially leans risky, discussion makes them more risk-taking (risky shift); if cautious, more cautious. This occurs via persuasive argument theory and social comparison. It differs from groupthink, which involves premature consensus.",
    "tags": ["social-influence", "group-polarization", "group-dynamics"],
    "difficulty": "medium"
  },
  {
    "text": "Groupshift refers to which specific phenomenon?",
    "options": ["The tendency for groups to make more extreme decisions than individual members would make alone", "The shift from external to internal locus of control in group settings", "The movement from majority to minority opinion following Moscovici-style conversion", "The change in leadership roles that occurs when group composition changes"],
    "correct": 0,
    "explanation": "Groupshift (related to group polarization): group decisions shift to more extreme positions than the average pre-discussion individual positions. This can be toward greater risk (risky shift) or greater caution depending on initial group tendency. Group polarization is the broader phenomenon; groupshift emphasizes the direction of the change.",
    "tags": ["social-influence", "groupshift", "group-polarization"],
    "difficulty": "medium"
  },
  {
    "text": "In Asch's experiments, what single change most dramatically reduced conformity?",
    "options": ["Presence of one confederate who gave the correct answer (a social supporter)", "Making the task more difficult", "Increasing the size of the confederate group beyond 3", "Allowing participants to respond in writing rather than aloud"],
    "correct": 0,
    "explanation": "Having just one 'ally' (confederate who gave the correct answer) reduced conformity from ~37% to ~5–10%. The ally breaks unanimity, making it easier for participants to resist normative pressure. Group size beyond 3–4 confederates has diminishing returns on conformity. Written responses reduce normative but not informational pressure.",
    "tags": ["social-influence", "asch", "conformity", "social-supporter"],
    "difficulty": "hard"
  },
  {
    "text": "The reciprocity norm (Cialdini) states that:",
    "options": ["People feel obligated to return favors, gifts, or concessions received from others", "People comply with requests that are consistent with their prior behavior", "People follow the lead of those they respect as experts", "People value items more when they are rare or in short supply"],
    "correct": 0,
    "explanation": "Reciprocity: receiving a gift or favor creates a sense of obligation to reciprocate. This universal social norm is exploited commercially (free samples, gifts before requests). Consistency underlies foot-in-the-door. Authority involves expert credibility. Scarcity involves limited availability.",
    "tags": ["social-influence", "reciprocity", "cialdini", "compliance"],
    "difficulty": "easy"
  },
  {
    "text": "A vignette: Customers in a supermarket were offered free cheese samples; those who received samples were significantly more likely to purchase the cheese. This best illustrates:",
    "options": ["Reciprocity norm", "Mere exposure effect", "Social proof", "Foot-in-the-door technique"],
    "correct": 0,
    "explanation": "Free samples exploit the reciprocity norm — receiving a gift creates obligation to return the favor (purchase). Mere exposure effect (Zajonc) would predict that repeated exposure to the cheese increases liking. Social proof would involve observing others purchase. Foot-in-the-door would require an initial small purchase before a larger request.",
    "tags": ["social-influence", "reciprocity", "cialdini", "vignette"],
    "difficulty": "medium"
  },
  {
    "text": "Social proof, as a compliance principle, works because:",
    "options": ["People assume that if many others are doing something, it must be the correct or appropriate behavior", "They feel socially excluded if they do not conform to visible majority behavior", "Majority behavior creates a commitment that the individual feels obligated to match", "Repeated observation of majority behavior increases the perceived value of an item"],
    "correct": 0,
    "explanation": "Social proof (Cialdini): people look to others to determine appropriate behavior — 'everyone is doing it, so it must be right.' This is informational social influence. Social exclusion motivation is normative influence. Commitment is consistency. Increased value from observation is exposure or scarcity.",
    "tags": ["social-influence", "social-proof", "cialdini", "informational-influence"],
    "difficulty": "medium"
  },
  {
    "text": "Normative social influence and informational social influence are distinguished by:",
    "options": ["Normative: driven by desire for approval; informational: driven by desire to be accurate using others as information", "Normative: occurs only in expert groups; informational: in non-expert groups", "Normative: produces permanent attitude change; informational: only temporary compliance", "They are interchangeable terms for the same process"],
    "correct": 0,
    "explanation": "Normative influence: conforming to gain approval or avoid rejection (public compliance without private acceptance). Informational influence: genuinely using others' behavior as evidence about reality, especially in ambiguous situations (may produce private acceptance). They differ in motivation and are not interchangeable.",
    "tags": ["social-influence", "normative", "informational", "distinction"],
    "difficulty": "medium"
  },
  {
    "text": "A salesperson first shows a customer a very expensive car, then suggests a moderately priced car that now seems reasonable by comparison. This technique is called:",
    "options": ["Door-in-the-face / contrast principle", "Foot-in-the-door", "Lowballing", "Scarcity"],
    "correct": 0,
    "explanation": "This uses the contrast principle (related to door-in-the-face) — the moderately priced car seems cheaper after the expensive anchor. The door-in-the-face also uses this contrast, but involves making a large request first and then the target request as a concession. Lowballing quotes a low price initially and raises it after commitment. Scarcity involves limited availability.",
    "tags": ["social-influence", "door-in-the-face", "contrast-principle", "anchoring"],
    "difficulty": "hard"
  },
  {
    "text": "Which aspect of Asch's conformity findings supports the power of normative social influence specifically?",
    "options": ["Conformity dropped dramatically when the task was done anonymously (writing responses), even when confederates still gave wrong answers aloud", "Conformity was highest when the task was ambiguous", "Conformity was reduced by expertise in visual perception", "Conformity increased with group size regardless of unanimity"],
    "correct": 0,
    "explanation": "When participants could respond privately (anonymously), conformity dropped substantially — showing that much of the conformity in Asch's original paradigm was normative (driven by public exposure/social pressure) rather than truly believing the wrong answer. Anonymous conditions reduce normative but not informational pressure.",
    "tags": ["social-influence", "asch", "conformity", "normative", "anonymity"],
    "difficulty": "hard"
  },

  # ── 8. SOCIOLOGY – POVERTY & SOCIAL MOBILITY ────────────────────────────
  {
    "text": "Absolute poverty is best defined as:",
    "options": ["Lacking resources necessary for basic survival (food, shelter, healthcare)", "Having significantly less income or wealth than the median of one's society", "Experiencing downward social mobility across generations", "Being excluded from social participation due to low income"],
    "correct": 0,
    "explanation": "Absolute poverty: a threshold based on basic survival needs — insufficient income for food, shelter, clothing, and basic healthcare. Relative poverty is defined in relation to the societal median or average (e.g., below 60% of median income). Social exclusion is related but distinct from absolute deprivation.",
    "tags": ["sociology", "poverty", "absolute-poverty"],
    "difficulty": "easy"
  },
  {
    "text": "Relative poverty measures are important because they capture:",
    "options": ["Social exclusion and inequality relative to prevailing living standards in a society", "Whether a person has enough to survive biologically", "The absolute number of individuals below a poverty threshold", "Cross-national comparisons using purchasing power parity"],
    "correct": 0,
    "explanation": "Relative poverty acknowledges that deprivation is context-dependent — being poor in a wealthy society involves social exclusion, inability to participate in normal activities, and relative disadvantage, even if basic biological survival is met. Absolute poverty focuses on survival needs. Both measures are useful for different purposes.",
    "tags": ["sociology", "poverty", "relative-poverty", "social-exclusion"],
    "difficulty": "medium"
  },
  {
    "text": "Oscar Lewis's 'culture of poverty' thesis argues that:",
    "options": ["The poor develop a distinct set of values, behaviors, and attitudes that perpetuate poverty across generations", "Poverty results from structural factors like labor market exclusion and racial discrimination", "Absolute poverty is caused by lack of human capital (education and skills)", "The welfare state creates dependency that prevents economic mobility"],
    "correct": 0,
    "explanation": "Lewis argued that the poor develop a subculture (fatalism, present-orientation, low aspirations) that becomes self-perpetuating across generations independent of structural barriers. Critics (Wilson, Gans) argue this 'blames the victim' and underestimates structural determinants of poverty. Both structural and cultural factors interact.",
    "tags": ["sociology", "poverty", "culture-of-poverty", "oscar-lewis"],
    "difficulty": "medium"
  },
  {
    "text": "A major sociological critique of the 'culture of poverty' thesis is that it:",
    "options": ["Attributes poverty to individual values rather than structural barriers like discrimination and labor market inequality", "Overestimates the role of class consciousness in poverty persistence", "Fails to recognize any cultural differences between poor and wealthy communities", "Ignores the role of education in upward mobility"],
    "correct": 0,
    "explanation": "Critics (Wilson's 'The Truly Disadvantaged,' Gans) argue that Lewis pathologized the poor by attributing poverty to their culture rather than to structural factors (deindustrialization, housing segregation, labor market exclusion). The culture-of-poverty thesis has been used to justify reducing welfare rather than addressing structural inequalities.",
    "tags": ["sociology", "poverty", "culture-of-poverty", "structural-factors", "critique"],
    "difficulty": "medium"
  },
  {
    "text": "Intergenerational social mobility refers to:",
    "options": ["Changes in social class position between parents and their adult children", "Movement within an individual's own career over their lifetime", "The total amount of movement between classes in a society", "Geographic relocation associated with class change"],
    "correct": 0,
    "explanation": "Intergenerational mobility: comparing social class between generations (parent vs. child). Intragenerational mobility: movement within one's own lifetime/career. Both are key measures in stratification research. Low intergenerational mobility (strong parent-child correlations) indicates a rigid class system.",
    "tags": ["sociology", "social-mobility", "intergenerational-mobility"],
    "difficulty": "easy"
  },
  {
    "text": "Bourdieu's concept of 'cultural capital' most directly explains how social inequality is reproduced through:",
    "options": ["Differential possession of cultural knowledge, skills, and credentials that are valued in educational and professional contexts", "Legal barriers preventing lower-class individuals from accessing higher education", "Differential access to financial resources for schooling", "Biological differences in cognitive ability between social classes"],
    "correct": 0,
    "explanation": "Bourdieu: cultural capital (knowledge of dominant culture, educational credentials, linguistic facility) is unequally distributed and converts to economic and social advantage in educational and labor markets. This reproduces class inequality without overt discrimination. Financial barriers are economic capital; legal barriers are structural constraints.",
    "tags": ["sociology", "bourdieu", "cultural-capital", "social-reproduction"],
    "difficulty": "medium"
  },
  {
    "text": "The Matthew effect in sociology refers to:",
    "options": ["The cumulative advantage process by which those who start ahead gain more resources over time ('the rich get richer')", "Downward mobility that follows unexpected economic shocks", "Social stratification based on religious credentials", "The process by which welfare dependency perpetuates poverty"],
    "correct": 0,
    "explanation": "The Matthew effect (Merton, from Matthew 25:29 — 'to him who has, more shall be given'): early advantages (better schooling, social networks, income) compound over time, widening inequality. This explains why initial class differences grow rather than shrink over time despite formal equal opportunity.",
    "tags": ["sociology", "matthew-effect", "cumulative-advantage", "merton"],
    "difficulty": "medium"
  },
  {
    "text": "Which of the following best distinguishes income from wealth in discussions of social stratification?",
    "options": ["Income is the flow of money earned in a period; wealth (net worth) is the stock of accumulated assets minus liabilities", "Income includes all assets; wealth refers only to inherited property", "They are synonymous in stratification research", "Wealth is earned; income is inherited"],
    "correct": 0,
    "explanation": "Income = current earnings (wages, salary) — a flow. Wealth (net worth) = total assets minus total liabilities — a stock that accumulates. Racial and class wealth gaps are larger than income gaps because wealth compounds through inheritance and investment. Using income alone understates true economic inequality.",
    "tags": ["sociology", "poverty", "income", "wealth", "stratification"],
    "difficulty": "easy"
  },
  {
    "text": "Meritocracy as a sociological concept is problematic because:",
    "options": ["Access to achievement is shaped by ascribed characteristics (race, class, gender) and structural barriers, not merit alone", "It accurately describes how most industrial societies allocate rewards", "It overstates the importance of achieved characteristics like education", "It was developed to critique capitalism rather than describe it"],
    "correct": 0,
    "explanation": "The meritocracy myth: while meritocracy ideologically claims rewards go to the most talented/hardworking, structural barriers (discrimination, differential access to quality education, inherited wealth) mean starting positions are unequal. Bourdieu's cultural capital, Merton's anomie, and empirical mobility research all challenge pure meritocracy.",
    "tags": ["sociology", "meritocracy", "stratification", "structural-barriers"],
    "difficulty": "medium"
  },
  {
    "text": "Bourdieu's 'field theory' posits that social life is organized into:",
    "options": ["Relatively autonomous social arenas (fields) with their own rules and forms of capital that determine position", "A single hierarchical structure determined entirely by economic capital", "Cultural groups united by shared values and norms (Durkheimian collectivism)", "Rational actor calculations of cost-benefit in social interactions"],
    "correct": 0,
    "explanation": "Bourdieu's field: semi-autonomous social spaces (academic, artistic, economic, political) each with their own logic, rules, and stakes. Position within a field is determined by the volume and composition of relevant capital (economic, social, cultural). This multi-dimensional view contrasts with purely economic or purely cultural accounts.",
    "tags": ["sociology", "bourdieu", "field-theory", "capital"],
    "difficulty": "hard"
  },
  {
    "text": "Absolute social mobility can be high while relative social mobility remains low when:",
    "options": ["The overall economy grows (so more people move up), but class position relative to others stays about the same", "Immigration increases total population but not the number of high-status positions", "Welfare programs raise absolute income without changing relative rankings", "Educational credentials expand but their economic value decreases"],
    "correct": 0,
    "explanation": "Absolute mobility measures how many people are in a higher class than their parents (rising tide lifts all boats in economic growth). Relative mobility measures whether one's chance of ending up in a particular class depends on parental class — i.e., equality of opportunity. Societies can have high absolute but low relative mobility.",
    "tags": ["sociology", "social-mobility", "absolute-vs-relative-mobility"],
    "difficulty": "hard"
  },
  {
    "text": "Bourdieu's concept of 'social capital' refers to:",
    "options": ["Resources derived from social networks and connections — who you know and the obligations and trust these relationships create", "The cultural knowledge and tastes that signal class membership", "The economic resources and assets held by a social group", "The formal educational credentials obtained through schooling"],
    "correct": 0,
    "explanation": "Social capital (Bourdieu): resources embedded in social relationships and networks — connections, trust, group membership. Cultural capital: knowledge, taste, credentials. Economic capital: financial assets. Educational credentials are a form of institutionalized cultural capital. All three forms of capital can be converted into one another.",
    "tags": ["sociology", "bourdieu", "social-capital", "networks"],
    "difficulty": "medium"
  },
  {
    "text": "A researcher finds that children from wealthy families attend better schools, gain better credentials, and obtain higher-paying jobs despite equal cognitive ability as children from poor families. This best illustrates:",
    "options": ["Bourdieu's social reproduction through cultural and economic capital advantage", "The culture of poverty perpetuating economic disadvantage", "Merton's strain theory explaining deviance through legitimate vs. illegitimate means", "Weber's Protestant ethic linking religious values to economic success"],
    "correct": 0,
    "explanation": "Bourdieu's social reproduction: advantage is transmitted through capital (economic, cultural, social) across generations, not through biological ability. Equal ability with unequal outcomes demonstrates structural advantage. Culture of poverty blames the poor's values. Merton's strain theory addresses deviance. Weber addressed religious-economic links.",
    "tags": ["sociology", "bourdieu", "social-reproduction", "inequality", "vignette"],
    "difficulty": "medium"
  },
  {
    "text": "Which sociological concept best describes the process where early advantages in education compound over time to produce vastly unequal outcomes?",
    "options": ["Cumulative advantage (Matthew effect)", "Downward leveling norms", "Relative deprivation theory", "Bourgeois habitus formation"],
    "correct": 0,
    "explanation": "Cumulative advantage (Matthew effect): advantages at one stage (better kindergarten preparation → better elementary school performance → better high school → college → career) compound over time. This explains widening inequality despite formal equal opportunity. Relative deprivation is subjective comparison to others, not a process of compounding.",
    "tags": ["sociology", "cumulative-advantage", "matthew-effect", "inequality"],
    "difficulty": "medium"
  },
  {
    "text": "Intragenerational social mobility refers to:",
    "options": ["Changes in social class position within an individual's own lifetime and career", "Class differences between generations in the same family", "Geographic mobility associated with economic opportunity", "The overall rate of class movement in a society across all generations"],
    "correct": 0,
    "explanation": "Intragenerational mobility: movement within one person's own career (e.g., starting as a factory worker and becoming a manager). Intergenerational mobility compares positions between parents and children. Both are measured in stratification research to assess the openness of a society's class system.",
    "tags": ["sociology", "social-mobility", "intragenerational-mobility"],
    "difficulty": "easy"
  },

  # ── 9. BRAIN IMAGING & HEMISPHERIC SPECIALIZATION ───────────────────────
  {
    "text": "Functional MRI (fMRI) measures brain activity by detecting:",
    "options": ["Blood oxygen level-dependent (BOLD) signal changes related to neural activity", "Electrical activity of cortical neurons via scalp electrodes", "Radioactive tracer uptake reflecting glucose metabolism", "Structural differences in white and gray matter density"],
    "correct": 0,
    "explanation": "fMRI measures the BOLD signal — hemoglobin's differential magnetic properties when oxygenated vs. deoxygenated, reflecting local blood flow changes that proxy neural activity. EEG measures electrical activity. PET uses radioactive tracers to measure glucose metabolism or neurotransmitter binding. Structural MRI and CT measure anatomy, not function.",
    "tags": ["biological-psych", "brain-imaging", "fMRI", "BOLD"],
    "difficulty": "easy"
  },
  {
    "text": "Compared to fMRI, EEG has which resolution advantage?",
    "options": ["Superior temporal resolution (milliseconds) because it directly measures electrical neural signals in real time", "Superior spatial resolution for localizing activity to specific cortical layers", "Better ability to image subcortical structures like the amygdala", "Less susceptibility to movement artifacts"],
    "correct": 0,
    "explanation": "EEG records electrical potentials at the scalp with millisecond temporal resolution, capturing the actual timing of neural events. fMRI is limited by hemodynamic lag (~5-second BOLD response) — excellent spatial resolution (~1–3 mm) but poor temporal resolution. Neither EEG nor fMRI images subcortical structures well; fMRI is better for deep structures.",
    "tags": ["biological-psych", "brain-imaging", "EEG", "temporal-resolution"],
    "difficulty": "medium"
  },
  {
    "text": "PET scans differ from fMRI in that PET:",
    "options": ["Uses injected radioactive tracers to measure metabolism or receptor binding; fMRI uses magnetic fields and radio waves", "Has better spatial resolution and no radiation exposure", "Measures brain structure rather than function", "Is faster and cheaper to administer"],
    "correct": 0,
    "explanation": "PET (positron emission tomography): radioactive tracer (e.g., [18F]FDG for glucose metabolism, or labeled ligands for receptor binding) is injected; gamma rays are detected. fMRI uses magnetic fields and requires no radiation. PET has poorer spatial resolution than fMRI and involves radiation. PET is expensive and slow compared to fMRI.",
    "tags": ["biological-psych", "brain-imaging", "PET", "fMRI", "comparison"],
    "difficulty": "medium"
  },
  {
    "text": "Sperry and Gazzaniga's split-brain research demonstrated that after corpus callosum severing:",
    "options": ["Information presented to one visual field can only be verbally reported if processed by the left hemisphere", "Both hemispheres have equal language capabilities", "The right hemisphere cannot process spatial information", "Language is processed equally by both hemispheres in most people"],
    "correct": 0,
    "explanation": "Split-brain findings: visual input from the right visual field (processed by left hemisphere) can be verbally reported; left visual field input (processed by right hemisphere) cannot be named but can be identified by the left hand. This demonstrated left hemispheric language dominance and hemispheric specialization.",
    "tags": ["biological-psych", "split-brain", "sperry-gazzaniga", "hemispheric-specialization"],
    "difficulty": "medium"
  },
  {
    "text": "The corpus callosum's primary function is to:",
    "options": ["Transfer information and coordinate activity between the left and right cerebral hemispheres", "Regulate sleep-wake cycles via circadian inputs", "Coordinate fine motor movements via the cerebellum", "Control emotional regulation through amygdala connections"],
    "correct": 0,
    "explanation": "The corpus callosum is a massive white matter bundle of ~250 million axons connecting the two hemispheres, enabling interhemispheric communication. Severing it (callosotomy for epilepsy) creates split-brain phenomena. Sleep-wake regulation involves the SCN and brainstem. Motor coordination involves the cerebellum.",
    "tags": ["biological-psych", "corpus-callosum", "hemispheric-communication"],
    "difficulty": "easy"
  },
  {
    "text": "Hemispheric lateralization in language typically shows:",
    "options": ["Left hemisphere dominant for language production and comprehension in ~95% of right-handed individuals", "Right hemisphere dominant for language in most people", "Language distributed equally across both hemispheres with no dominant side", "Left hemisphere for comprehension; right hemisphere for production"],
    "correct": 0,
    "explanation": "About 95% of right-handers and ~70% of left-handers show left hemisphere language dominance (Broca's and Wernicke's areas). The right hemisphere contributes to prosody, metaphor, and narrative. Damage to Broca's area (left frontal) impairs production; Wernicke's area (left temporal) impairs comprehension.",
    "tags": ["biological-psych", "hemispheric-lateralization", "language", "left-hemisphere"],
    "difficulty": "easy"
  },
  {
    "text": "Right hemisphere specialization is most associated with which cognitive functions?",
    "options": ["Visuospatial processing, face recognition, musical perception, and emotional prosody", "Language production, analytical reasoning, and phonological processing", "Motor control of the right hand and language comprehension", "Declarative memory consolidation and fear conditioning"],
    "correct": 0,
    "explanation": "Right hemisphere: visuospatial tasks, global/holistic processing, face recognition (prosopagnosia from right temporal damage), musical perception, emotional tone of speech (prosody). Left hemisphere: language, analytical processing, sequential reasoning. These are tendencies — not absolute — and vary with individual differences.",
    "tags": ["biological-psych", "right-hemisphere", "visuospatial", "face-recognition"],
    "difficulty": "medium"
  },
  {
    "text": "Contralateral organization of the motor and sensory cortex means that:",
    "options": ["Each hemisphere controls and receives sensation from the opposite side of the body", "Both hemispheres jointly control each limb with equal contribution", "The right hemisphere controls only the right hand and foot", "Sensory and motor processing are in the same cortical region for each body part"],
    "correct": 0,
    "explanation": "Contralateral (crossed) organization: the left motor cortex controls the right side of the body and vice versa; left somatosensory cortex receives sensation from the right body side. This is established by pyramidal tract crossing in the medulla. Brain lesions cause deficits on the opposite body side.",
    "tags": ["biological-psych", "contralateral-organization", "motor-cortex", "sensory-cortex"],
    "difficulty": "easy"
  },
  {
    "text": "A researcher needs to study the precise timing of neural activity during a cognitive task with millisecond accuracy. Which imaging technique is most appropriate?",
    "options": ["EEG", "fMRI", "PET", "CT"],
    "correct": 0,
    "explanation": "EEG has millisecond temporal resolution, ideal for studying the timing of cognitive processes (event-related potentials, P300). fMRI has ~1–2 second temporal resolution (limited by BOLD hemodynamic lag). PET is even slower. CT measures brain structure only, not function.",
    "tags": ["biological-psych", "brain-imaging", "EEG", "temporal-resolution", "research-design"],
    "difficulty": "medium"
  },
  {
    "text": "A patient has damage to the corpus callosum. When a key is placed in her left hand out of sight, she cannot name what she is holding but can select a matching key from a set using her left hand. This demonstrates:",
    "options": ["Right hemisphere processes the left-hand sensation but lacks language; left hand/right hemisphere can still identify objects non-verbally", "Left hemisphere processes left-hand sensation and selects matching objects", "Language production is bilaterally distributed in this patient", "The right hemisphere gained language ability after corpus callosum damage"],
    "correct": 0,
    "explanation": "Left hand → right hemisphere (contralateral). The right hemisphere recognizes the key (visuospatial/tactile processing) and controls the left hand to identify a match. But the right hemisphere cannot access the left hemisphere's language system (corpus callosum is severed), so the patient cannot verbally name it. Classic split-brain demonstration.",
    "tags": ["biological-psych", "split-brain", "corpus-callosum", "hemispheric-specialization", "vignette"],
    "difficulty": "hard"
  },
  {
    "text": "Structural MRI is preferred over CT for imaging soft brain tissue because:",
    "options": ["MRI provides much better contrast between gray and white matter and does not use ionizing radiation", "MRI is faster to acquire than CT", "MRI can detect acute blood/hemorrhage better than CT", "MRI is less expensive and more widely available"],
    "correct": 0,
    "explanation": "MRI provides superior soft tissue contrast (distinguishing gray matter, white matter, CSF) using radio waves and magnetic fields without ionizing radiation. CT is faster (useful in emergencies), better for detecting acute hemorrhage and bone, and more widely available. MRI is more expensive and slower.",
    "tags": ["biological-psych", "brain-imaging", "MRI", "CT", "comparison"],
    "difficulty": "medium"
  },
  {
    "text": "The 'interpreter' mechanism described by Gazzaniga in split-brain research refers to:",
    "options": ["The left hemisphere's tendency to construct post-hoc narratives to explain actions generated by the right hemisphere", "The right hemisphere's ability to interpret complex social situations", "The corpus callosum mediating between conflicting hemispheric interpretations", "A brain region that integrates sensory information from both visual fields"],
    "correct": 0,
    "explanation": "Gazzaniga's 'interpreter': the left hemisphere confabulates coherent explanations for actions (generated by the right hemisphere or other processes) that it cannot directly access. E.g., if the right hemisphere causes the left hand to pick up a shovel, the left hemisphere might say 'I'm going to clean the garage' without knowing the true cause.",
    "tags": ["biological-psych", "gazzaniga", "interpreter", "split-brain", "confabulation"],
    "difficulty": "hard"
  },
  {
    "text": "Which brain imaging technique is best suited for studying neuroreceptor density and neurotransmitter binding in living patients?",
    "options": ["PET with radiolabeled ligands", "fMRI", "EEG", "Diffusion tensor imaging (DTI)"],
    "correct": 0,
    "explanation": "PET with radiolabeled receptor ligands (e.g., [11C]raclopride for dopamine D2 receptors) directly measures receptor binding and neurotransmitter availability. This is used to study dopamine in schizophrenia/Parkinson's, serotonin in depression. fMRI measures blood flow; EEG measures electrical activity; DTI maps white matter tracts.",
    "tags": ["biological-psych", "PET", "neurotransmitter-binding", "receptors"],
    "difficulty": "hard"
  },
  {
    "text": "Which statement about hemispheric specialization is most accurate based on contemporary neuroscience?",
    "options": ["Most cognitive functions involve networks distributed across both hemispheres, with tendencies toward lateralization rather than strict dichotomy", "Specific cognitive functions are entirely contained within one hemisphere with no cross-hemispheric contribution", "The right hemisphere is language-dominant in most left-handed people", "Hemispheric specialization is fully established at birth with no developmental change"],
    "correct": 0,
    "explanation": "Modern neuroscience views hemispheric specialization as graded tendencies — most complex cognitive functions recruit bilateral networks. Language dominance is left-lateralized in most people, but the right hemisphere contributes to discourse, prosody, and metaphor. Specialization continues to develop through childhood. Pure right-hemisphere language dominance is atypical even in left-handers.",
    "tags": ["biological-psych", "hemispheric-specialization", "lateralization", "contemporary-neuroscience"],
    "difficulty": "medium"
  },
  {
    "text": "CT scans use which physical principle to generate brain images?",
    "options": ["Multiple X-ray beams taken at different angles to reconstruct cross-sectional images of tissue density", "Magnetic fields and radio waves to measure proton relaxation in tissue", "Radioactive tracer uptake visualized by gamma ray detection", "Electrical potentials from scalp electrodes reflecting cortical activity"],
    "correct": 0,
    "explanation": "CT (computed tomography): multiple X-ray projections from different angles are reconstructed into cross-sectional images based on tissue density. Bone appears white (dense); air black; brain tissue in between. MRI uses magnetic fields/radio waves. PET uses gamma rays from radioactive tracers. EEG uses electrical potentials.",
    "tags": ["biological-psych", "CT", "brain-imaging", "X-ray"],
    "difficulty": "easy"
  },

  # ── 10. PSYCHOLOGICAL THERAPIES ADVANCED ─────────────────────────────────
  {
    "text": "In psychodynamic therapy, 'transference' refers to:",
    "options": ["The client unconsciously redirecting feelings from past significant relationships onto the therapist", "The therapist projecting their own feelings onto the client", "A client's intellectual insight about childhood experiences", "The transfer of skills learned in therapy to real-world situations"],
    "correct": 0,
    "explanation": "Transference: the client unconsciously displaces emotions, expectations, and patterns from important past relationships (typically parents) onto the therapist. Working through transference is central to psychodynamic therapy. Countertransference is the therapist's emotional reactions to the client. Insight is cognitive, not an interpersonal projection.",
    "tags": ["psychotherapy", "psychodynamic", "transference"],
    "difficulty": "easy"
  },
  {
    "text": "Free association in psychodynamic therapy involves:",
    "options": ["The client verbalizing all thoughts and feelings without censorship, allowing unconscious material to emerge", "The therapist freely associating between sessions to prepare interpretations", "Structured word-association tasks to measure reaction time differences", "The client freely choosing which memories to discuss each session"],
    "correct": 0,
    "explanation": "Free association (Freud): the client says whatever comes to mind without self-censorship. This is the 'fundamental rule' of psychoanalysis, intended to bypass ego defenses and allow unconscious material to surface for interpretation. Structured word-association is a research task (Jung). Therapist preparation is not free association.",
    "tags": ["psychotherapy", "psychodynamic", "free-association", "freud"],
    "difficulty": "easy"
  },
  {
    "text": "Which defense mechanism involves unconsciously pushing threatening thoughts or memories out of conscious awareness?",
    "options": ["Repression", "Suppression", "Rationalization", "Projection"],
    "correct": 0,
    "explanation": "Repression: unconscious exclusion of threatening memories, impulses, or desires from awareness. It is the foundational defense in Freudian theory. Suppression is the conscious decision to not think about something. Rationalization provides false logical justifications. Projection attributes one's own unacceptable feelings to others.",
    "tags": ["psychotherapy", "psychodynamic", "defense-mechanisms", "repression"],
    "difficulty": "easy"
  },
  {
    "text": "A person angry at their boss comes home and yells at their spouse. This illustrates which defense mechanism?",
    "options": ["Displacement", "Projection", "Reaction formation", "Sublimation"],
    "correct": 0,
    "explanation": "Displacement: redirecting emotion from a threatening target (boss) to a safer one (spouse). Projection involves attributing one's own feelings to others ('my boss is angry, not me'). Reaction formation expresses the opposite of one's true feelings. Sublimation channels impulses into socially constructive behavior.",
    "tags": ["psychotherapy", "psychodynamic", "defense-mechanisms", "displacement"],
    "difficulty": "easy"
  },
  {
    "text": "A person with unconscious hostility becomes an outspoken peace activist. This illustrates:",
    "options": ["Reaction formation", "Sublimation", "Displacement", "Rationalization"],
    "correct": 0,
    "explanation": "Reaction formation: expressing the opposite of one's true, unconscious impulse (hostility → pacifism). Sublimation channels impulses into socially acceptable activities without expressing their opposite (e.g., channeling aggression into competitive sports). Displacement redirects to a different target; rationalization justifies behavior.",
    "tags": ["psychotherapy", "psychodynamic", "defense-mechanisms", "reaction-formation"],
    "difficulty": "medium"
  },
  {
    "text": "Rogers' person-centered therapy holds that therapeutic change requires the therapist to provide:",
    "options": ["Unconditional positive regard, empathy, and genuineness (congruence)", "Systematic reinforcement of adaptive behaviors", "Interpretation of unconscious conflicts and transference", "Structured problem-solving and cognitive restructuring"],
    "correct": 0,
    "explanation": "Rogers' core conditions: unconditional positive regard (accepting the client without judgment), empathy (accurately understanding the client's experience), and genuineness/congruence (therapist is authentic). These are the necessary and sufficient conditions for therapeutic change in humanistic therapy, contrasting with psychodynamic interpretation or behavioral techniques.",
    "tags": ["psychotherapy", "humanistic", "rogers", "person-centered", "UPR"],
    "difficulty": "easy"
  },
  {
    "text": "Unconditional positive regard in Rogers' therapy means:",
    "options": ["Accepting and valuing the client as a person regardless of their thoughts, feelings, or behaviors without judgment", "Agreeing with everything the client says to build rapport", "Providing positive reinforcement for adaptive behaviors", "Treating all clients equally regardless of diagnosis"],
    "correct": 0,
    "explanation": "UPR: the therapist communicates acceptance of the client's inherent worth unconditionally — not contingent on the client's behavior or beliefs. This creates psychological safety for self-exploration and growth. It does not mean agreeing with the client or providing behavioral reinforcement.",
    "tags": ["psychotherapy", "humanistic", "rogers", "unconditional-positive-regard"],
    "difficulty": "easy"
  },
  {
    "text": "EMDR (Eye Movement Desensitization and Reprocessing) for PTSD involves:",
    "options": ["Processing traumatic memories while engaging in bilateral stimulation (eye movements, taps, or tones) to facilitate memory reprocessing", "Prolonged imaginal exposure to traumatic memories while preventing escape behaviors", "Cognitive restructuring of trauma-related beliefs using Socratic questioning", "Pharmacological blockade of memory consolidation immediately post-trauma"],
    "correct": 0,
    "explanation": "EMDR: the client focuses on a traumatic memory while following the therapist's moving finger (or bilateral auditory/tactile stimulation). The mechanism is debated but may involve dual attention that facilitates emotional processing and memory integration. Prolonged exposure is a distinct CBT-based exposure therapy. Cognitive restructuring is CPT (cognitive processing therapy).",
    "tags": ["psychotherapy", "EMDR", "PTSD", "bilateral-stimulation"],
    "difficulty": "medium"
  },
  {
    "text": "Exposure therapy for phobias works through which primary mechanism?",
    "options": ["Extinction of conditioned fear responses by exposing the client to feared stimuli without the feared consequence", "Reinforcing approach behavior toward feared stimuli with rewards", "Restructuring cognitive appraisals of the threatening stimulus", "Providing insight into the developmental origins of the phobia"],
    "correct": 0,
    "explanation": "Exposure therapy: repeated, systematic confrontation with feared stimuli without safety behaviors, allowing the conditioned fear response to extinguish. The feared consequence (CS–no US pairing) violates the learned association. Behavioral reinforcement, cognitive restructuring, and insight are distinct therapeutic elements.",
    "tags": ["psychotherapy", "exposure-therapy", "phobia", "extinction"],
    "difficulty": "medium"
  },
  {
    "text": "Motivational interviewing (MI) is best used for:",
    "options": ["Exploring and resolving ambivalence about behavior change in clients who are not yet ready to change", "Teaching specific coping skills to clients actively engaged in therapy", "Exposing clients to feared situations in a graded hierarchy", "Analyzing transference relationships to resolve unconscious conflicts"],
    "correct": 0,
    "explanation": "MI (Miller & Rollnick): a collaborative, person-centered approach that explores and resolves ambivalence about change, particularly useful in the precontemplation and contemplation stages of the transtheoretical model. It uses reflective listening, affirmation, and evoking 'change talk.' Skill training is CBT; exposure is for anxiety disorders; transference is psychodynamic.",
    "tags": ["psychotherapy", "motivational-interviewing", "ambivalence", "behavior-change"],
    "difficulty": "medium"
  },
  {
    "text": "Sublimation as a defense mechanism is considered one of the most mature because it:",
    "options": ["Channels socially unacceptable impulses into constructive, socially valued activities", "Completely eliminates the underlying impulse from consciousness", "Redirects the impulse to a different but similar object", "Creates intellectualized understanding of the impulse without emotional processing"],
    "correct": 0,
    "explanation": "Sublimation channels unacceptable drives (aggression, sexuality) into socially productive outlets (art, athletics, medicine). It is 'mature' because the impulse is expressed in a functional way rather than being repressed, denied, or misdirected. Repression eliminates from consciousness. Displacement redirects to a safer target. Intellectualization avoids emotional experience.",
    "tags": ["psychotherapy", "psychodynamic", "defense-mechanisms", "sublimation"],
    "difficulty": "medium"
  },
  {
    "text": "The humanistic therapy emphasis on the client's 'actualizing tendency' refers to:",
    "options": ["An innate drive toward growth, fulfillment, and realization of one's full potential", "The tendency to actualize specific skills through behavioral rehearsal", "The drive to reduce biological needs and restore homeostasis", "An unconscious force that shapes personality development in childhood"],
    "correct": 0,
    "explanation": "Rogers' actualizing tendency: all organisms have an innate drive toward growth, health, and the full development of their capacities. Psychological problems arise when this tendency is blocked (e.g., by conditions of worth). This is the core motivational concept in humanistic psychology, contrasting with drive reduction (homeostasis) or psychoanalytic drives.",
    "tags": ["psychotherapy", "humanistic", "rogers", "actualizing-tendency"],
    "difficulty": "medium"
  },
  {
    "text": "Projection as a defense mechanism involves:",
    "options": ["Attributing one's own unacceptable impulses, feelings, or traits to another person", "Reverting to behaviors characteristic of an earlier developmental stage", "Compartmentalizing contradictory emotions to avoid anxiety", "Justifying unacceptable behavior with socially acceptable reasons"],
    "correct": 0,
    "explanation": "Projection: 'I don't hate him — he hates me.' One's own unacceptable impulse is perceived as belonging to someone else. Regression is reverting to earlier behaviors under stress. Splitting (BPD) is seeing others as all-good or all-bad. Rationalization provides false logical justifications.",
    "tags": ["psychotherapy", "psychodynamic", "defense-mechanisms", "projection"],
    "difficulty": "medium"
  },
  {
    "text": "A therapist using person-centered therapy would LEAST likely:",
    "options": ["Offer specific interpretations of the client's unconscious conflicts", "Reflect the client's feelings back to them", "Accept the client without judgment regardless of their behavior", "Maintain genuineness and authenticity in the therapeutic relationship"],
    "correct": 0,
    "explanation": "Interpretation of unconscious conflicts is a psychodynamic technique, not person-centered therapy. Rogers explicitly rejected the therapist as expert who provides interpretations; the client is the expert on their own experience. Reflection, UPR, and congruence ARE the core techniques of Rogerian therapy.",
    "tags": ["psychotherapy", "humanistic", "rogers", "person-centered", "interpretation"],
    "difficulty": "medium"
  },
  {
    "text": "A vignette: A client with alcohol use disorder enters therapy ambivalent about quitting — he acknowledges harms but values social drinking. He is in the contemplation stage. The MOST appropriate initial therapeutic approach is:",
    "options": ["Motivational interviewing to explore ambivalence and evoke intrinsic motivation to change", "Immediate exposure therapy to reduce alcohol cravings", "Systematic desensitization to social situations triggering drinking", "Insight-oriented psychodynamic therapy to explore childhood trauma"],
    "correct": 0,
    "explanation": "MI is specifically designed for the contemplation stage — when clients acknowledge a problem but are ambivalent about change. It uses empathic reflection and evokes 'change talk.' Jumping straight to skills or exposure assumes motivation already exists. Psychodynamic therapy doesn't target behavioral ambivalence directly.",
    "tags": ["psychotherapy", "motivational-interviewing", "substance-use", "contemplation", "vignette"],
    "difficulty": "medium"
  },
  {
    "text": "Rationalization as a defense mechanism involves:",
    "options": ["Constructing logical, socially acceptable explanations for behavior driven by unacceptable motives", "Channeling unacceptable impulses into constructive activities", "Denying the reality of a threatening situation entirely", "Attributing one's own hostile feelings to another person"],
    "correct": 0,
    "explanation": "Rationalization: creating plausible but false post-hoc justifications for behavior motivated by unacceptable impulses ('I fired him for performance reasons, not personal dislike'). Sublimation channels impulses constructively. Denial rejects external reality. Projection attributes one's feelings to others.",
    "tags": ["psychotherapy", "psychodynamic", "defense-mechanisms", "rationalization"],
    "difficulty": "easy"
  },
]

random.seed(88)
for q in Q:
    c = q["correct"]
    opts = q["options"][:]
    correct_text = opts[c]
    random.shuffle(opts)
    q["options"] = opts
    q["correct"] = opts.index(correct_text)

out = os.path.join(BASE, "data", "questions", "ps", "hq-ps-3.json")
os.makedirs(os.path.dirname(out), exist_ok=True)
with open(out, "w") as f:
    json.dump(Q, f, indent=2)
print(f"Wrote {len(Q)} PS questions to {out}")
