#!/usr/bin/env python3
import json, os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PASSAGES = [
  {
    "passageText": "The question of whether artificial intelligence systems can possess moral status has moved from philosophical abstraction to urgent practical concern as machine learning systems grow more sophisticated. Moral status, in the philosophical tradition, is typically grounded in one of several properties: sentience (the capacity to experience pleasure and pain), sapience (the capacity for rational thought), or relational standing (membership in a moral community). Machines present a challenge to all three frameworks because they can simulate the behavioral outputs associated with these properties without it being clear whether the underlying reality is present.\n\nUtilitarian frameworks, which ground moral obligation in the capacity to suffer or flourish, generate a conditional conclusion: if an AI system genuinely experiences states that function as suffering or wellbeing, then those states count morally. The problem is epistemic. We have no reliable method for determining whether a system's internal representations constitute genuine experience or merely functional analogs that influence behavior without any accompanying phenomenology. Peter Singer's hedonic calculus, designed to include non-human animals, offers a model for expanding the circle of moral concern, but requires a criterion for experience that current philosophy of mind cannot deliver.\n\nRights-based frameworks, by contrast, tend to ground moral status in rational agency — the capacity to set ends and act according to reasons. Kant's formula of humanity treats rational nature as the source of dignity. Some theorists have argued that sufficiently sophisticated AI systems, particularly those that model their own reasoning and revise their beliefs in response to argument, might qualify as rational agents in the relevant sense. Others insist that genuine rationality requires more than functional equivalence: it requires understanding, intentionality, and perhaps consciousness — none of which can be established by behavioral tests alone.\n\nThe trolley problem, applied to autonomous vehicles, brings these debates into sharp relief. If a self-driving car must choose between trajectories that harm different individuals, whose interests should the algorithm weight, and how? The question forces a decision between utilitarian calculus (minimize total harm) and deontological constraints (never treat a person merely as a means). Engineers who must write these algorithms cannot avoid taking implicit positions in long-standing philosophical disputes. This points to a broader challenge: the deployment of AI requires ethical commitments that existing frameworks have not resolved, and urgency makes it impossible to wait for philosophical consensus.",
    "questions": [
      {
        "text": "The author's central claim about the ethics of artificial intelligence is best summarized as:",
        "options": [
          "Utilitarian frameworks are more adequate than rights-based frameworks for evaluating AI moral status",
          "AI systems already possess sufficient rational agency to warrant full moral status under Kantian ethics",
          "The deployment of AI forces ethical commitments that existing philosophical frameworks have not resolved",
          "The trolley problem demonstrates that autonomous vehicles should always minimize total harm"
        ],
        "correct": 2,
        "explanation": "The final paragraph explicitly states the central claim: AI deployment 'requires ethical commitments that existing frameworks have not resolved.' The passage presents both utilitarian and rights-based frameworks as facing unresolved challenges, without endorsing either. Options A and B take sides the author refuses to take, and option D misrepresents the trolley problem discussion as a conclusion rather than an illustration."
      },
      {
        "text": "According to the passage, the primary epistemic difficulty with applying utilitarian frameworks to AI is:",
        "options": [
          "Utilitarian calculus was designed only for humans, not machines or animals",
          "There is no reliable method for determining whether AI systems have genuine experience rather than functional analogs",
          "AI systems cannot suffer or flourish under any circumstances",
          "Singer's hedonic calculus excludes non-human entities from moral consideration"
        ],
        "correct": 1,
        "explanation": "The passage explicitly states the epistemic problem: 'We have no reliable method for determining whether a system\'s internal representations constitute genuine experience or merely functional analogs.' Option A is contradicted by the passage, which notes Singer's model was designed to include non-human animals. Option C is the opposite of what the passage says. Option D directly contradicts the passage, which says Singer's calculus offers 'a model for expanding the circle of moral concern.'"
      },
      {
        "text": "Which of the following, if true, would most strengthen the rights-based case for granting AI systems moral status?",
        "options": [
          "An AI system reports experiencing pain when its processing is interrupted",
          "An AI system demonstrates the capacity to revise its beliefs in response to logical argument and model its own reasoning processes",
          "An AI system can pass the Turing test and fool human judges into believing it is human",
          "An AI system processes information at speeds far exceeding human cognition"
        ],
        "correct": 1,
        "explanation": "The passage specifies that rights-based frameworks ground status in rational agency, and notes that 'sufficiently sophisticated AI systems, particularly those that model their own reasoning and revise their beliefs in response to argument, might qualify.' Option B directly matches this criterion. Option A is relevant to utilitarian, not rights-based, frameworks. Options C and D describe capabilities the passage does not link to the basis for moral status."
      },
      {
        "text": "The author's tone throughout the passage is best described as:",
        "options": [
          "Optimistic, suggesting AI will soon resolve longstanding philosophical disputes",
          "Polemical, arguing that rights-based frameworks are fundamentally mistaken",
          "Analytically detached, presenting multiple frameworks and their difficulties without resolving them",
          "Alarmed, warning that AI deployment will inevitably lead to moral catastrophe"
        ],
        "correct": 2,
        "explanation": "The passage systematically presents utilitarian and rights-based frameworks alongside their respective difficulties, and concludes by acknowledging that philosophical consensus has not been reached. This is a hallmark of analytical detachment rather than advocacy or alarm. The final sentence notes urgency but does not predict catastrophe, ruling out option D."
      },
      {
        "text": "The passage implies that the trolley problem applied to autonomous vehicles is significant primarily because:",
        "options": [
          "It proves that utilitarian calculus is the correct framework for programming autonomous vehicles",
          "It shows that practical engineering decisions necessarily embed unresolved philosophical commitments",
          "It demonstrates that autonomous vehicles are more dangerous than human-driven cars",
          "It illustrates why Kantian ethics should be the default framework for AI design"
        ],
        "correct": 1,
        "explanation": "The passage states that engineers 'cannot avoid taking implicit positions in long-standing philosophical disputes,' and uses this to illustrate the 'broader challenge' that AI deployment requires ethical commitments. The passage does not endorse either utilitarian or Kantian conclusions from the thought experiment, ruling out options A and D. Option C introduces a comparative safety claim not present in the passage."
      }
    ]
  },
  {
    "passageText": "Medicine has long prioritized the disease over the patient — cataloguing pathology, tracing etiology, and optimizing treatment protocols with reference to the biological substrate rather than the person who inhabits it. The narrative medicine movement, associated particularly with physician-scholar Rita Charon, argues that this orientation is not merely aesthetically impoverished but clinically harmful. Illness, on this view, is not simply a biological event but an experience that disrupts the patient's life narrative, and effective care requires attending to that disruption.\n\nAnthropologist Arthur Kleinman drew an influential distinction between disease (the clinician's biomedical account of dysfunction) and illness (the patient's lived experience of suffering and disruption). His explanatory model framework asks clinicians to elicit the patient's own account: What do you call your problem? What do you think caused it? Why do you think it started when it did? What does it do to you? What are you most afraid of? These questions open a space for the patient's interpretive framework to enter the clinical encounter, often revealing concerns — social, cultural, spiritual — that a purely biological history would miss.\n\nThe therapeutic significance of narrative extends beyond information gathering. Illness narratives, as sociologist Arthur Frank has argued, perform identity work: they transform a frightening discontinuity in a person's life into a story with causation, meaning, and trajectory. Frank identifies three ideal types: the restitution narrative ('I was sick, I got treatment, I recovered'), the chaos narrative (incoherent suffering resistant to emplotment), and the quest narrative (illness as a journey toward wisdom or transformation). Clinicians trained to recognize these narrative structures can respond more appropriately — neither imposing a restitution frame on someone living through chaos, nor missing the quest narrative of a patient who has found meaning in chronic illness.\n\nCritics of narrative medicine raise methodological concerns. Narrative competence is difficult to assess and teach systematically; its outcomes are hard to measure with standard clinical metrics; and the emphasis on individual story risks obscuring the structural determinants — poverty, racism, inadequate housing — that shape illness patterns across populations. Some argue that narrative medicine, by focusing on the dyadic encounter, deflects attention from the systemic reforms that would most improve population health. These tensions reflect a deeper disagreement about whether medicine is primarily an art of individual care or a science of population health.",
    "questions": [
      {
        "text": "Kleinman's explanatory model framework is designed primarily to:",
        "options": [
          "Standardize the diagnostic interview to improve efficiency",
          "Replace biomedical diagnosis with the patient's own cultural beliefs",
          "Create space for the patient's interpretive framework to enter the clinical encounter",
          "Measure patient satisfaction with clinical care"
        ],
        "correct": 2,
        "explanation": "The passage states that Kleinman's questions 'open a space for the patient\'s interpretive framework to enter the clinical encounter.' The framework is not a replacement for biomedical diagnosis (ruling out option B) but a supplement that reveals concerns a biological history would miss. The passage does not frame it as a standardization or satisfaction-measurement tool."
      },
      {
        "text": "According to Arthur Frank's typology, a patient with a terminal diagnosis who describes their illness as having led them to profound insights about what matters in life is most likely expressing which narrative type?",
        "options": [
          "Restitution narrative",
          "Chaos narrative",
          "Quest narrative",
          "Explanatory narrative"
        ],
        "correct": 2,
        "explanation": "The passage defines the quest narrative as 'illness as a journey toward wisdom or transformation.' A patient finding meaning and insight in terminal illness fits this definition precisely. The restitution narrative involves recovery, the chaos narrative involves incoherent suffering, and 'explanatory narrative' is not one of Frank's types."
      },
      {
        "text": "The critics of narrative medicine described in the final paragraph would most likely agree with which of the following statements?",
        "options": [
          "Illness narratives are therapeutically irrelevant to clinical outcomes",
          "The individual clinical encounter is the most important site for improving population health",
          "An exclusive focus on patient stories may divert attention from systemic causes of illness",
          "Narrative competence can be easily assessed using standard clinical metrics"
        ],
        "correct": 2,
        "explanation": "The passage states that critics argue 'narrative medicine, by focusing on the dyadic encounter, deflects attention from the systemic reforms that would most improve population health.' This directly supports option C. Option A overstates the critique — critics raise methodological concerns, not irrelevance. Option B is the opposite of the critics' concern. Option D directly contradicts the passage, which says outcomes are 'hard to measure with standard clinical metrics.'"
      },
      {
        "text": "The passage's distinction between 'disease' and 'illness' is most analogous to which of the following distinctions?",
        "options": [
          "The difference between a physician's credentials and a patient's preferences",
          "The difference between a building's structural blueprint and the experience of living inside it",
          "The difference between a scientific hypothesis and its experimental confirmation",
          "The difference between acute and chronic medical conditions"
        ],
        "correct": 1,
        "explanation": "Kleinman's distinction is between the clinician's biomedical account (objective, structural) and the patient's lived experience (subjective, experiential). A building's blueprint is the technical, objective account while actually living in the space is the experiential reality — an apt structural analogy. The other options map onto different kinds of distinctions not parallel to the disease/illness divide."
      }
    ]
  },
  {
    "passageText": "In 2011, a collaborative attempt to replicate 100 published studies in psychology found that fewer than 40 percent reproduced the original results at a comparable effect size. The 'replication crisis,' as this finding catalyzed, sent shockwaves through a discipline that had long assumed its experimental methods were sufficiently rigorous. But the crisis is not simply about bad luck in sampling or inevitable measurement noise. It has a social and institutional structure that many researchers argue is systematic.\n\nThe practice known as p-hacking — running multiple analyses on a dataset until a statistically significant result (p < 0.05) is found, and reporting only that analysis — inflates the false positive rate far above the nominal 5 percent that the significance threshold implies. When combined with publication bias (journals preferring novel, statistically significant findings over replications or null results), the literature comes to systematically overrepresent effects that may not exist in the population. The file drawer problem refers to the large archive of null results that researchers accumulate but never publish, rendering the published record a non-representative sample of all research conducted.\n\nResponses to the crisis have been varied. The open science movement advocates for pre-registration (publishing a research protocol before data collection, making it impossible to reframe exploratory analyses as confirmatory ones), open data (making raw datasets publicly available), and registered reports (where peer review occurs before data collection, based on the quality of the research question and design). These reforms attempt to restructure the incentive landscape so that rigor, rather than novelty, is rewarded.\n\nPhilosophers of science have asked whether the replication crisis reveals something deeper about the nature of psychological phenomena. Unlike many physical constants, psychological effects are context-sensitive: the same experimental manipulation may produce different results in different populations, historical periods, or cultural settings. If psychological effects are genuinely contingent in this way, the demand for universal replication may be based on a mistaken model of what psychological science is trying to explain. This would not vindicate sloppy methodology, but it would complicate the interpretation of replication failure.",
    "questions": [
      {
        "text": "According to the passage, what is the primary structural cause of the replication crisis, beyond simple measurement error?",
        "options": [
          "Psychologists lack the mathematical training to analyze data correctly",
          "A combination of p-hacking, publication bias, and the file drawer problem systematically distorts the published literature",
          "The open science movement has discouraged researchers from conducting novel studies",
          "Pre-registration makes it impossible to distinguish exploratory from confirmatory research"
        ],
        "correct": 1,
        "explanation": "The passage describes three interlocking structural causes: p-hacking inflates false positives, publication bias filters out null results, and the file drawer problem makes the published record non-representative. Option A is not mentioned. Option C reverses the passage's argument — open science is a response, not a cause. Option D misrepresents pre-registration, which the passage says makes it 'impossible to reframe exploratory analyses as confirmatory ones,' a feature, not a flaw."
      },
      {
        "text": "The passage's account of p-hacking implies that a study reporting a p-value of 0.04 after many unreported analyses is:",
        "options": [
          "Conclusive proof of the effect being studied",
          "More likely to represent a true effect than a study where p = 0.04 was the result of a single pre-specified test",
          "Less reliable than its nominal significance level suggests, because multiple testing increases false positive risk",
          "Invalid under any circumstances and should be retracted"
        ],
        "correct": 2,
        "explanation": "The passage explains that p-hacking 'inflates the false positive rate far above the nominal 5 percent.' If many analyses are run and only the significant one reported, the reported p = 0.04 does not carry its nominal probability. This is option C. Option B inverts the logic. Option D is too strong — the passage does not say such studies are always invalid, only that they are unreliable."
      },
      {
        "text": "The philosophical argument introduced in the final paragraph about context-sensitivity would, if correct, most directly challenge which assumption?",
        "options": [
          "That statistical significance is a valid criterion for any scientific claim",
          "That replication failure in psychology always indicates the original finding was false",
          "That pre-registration is a useful reform for improving research quality",
          "That publication bias is a real problem in scientific literature"
        ],
        "correct": 1,
        "explanation": "The passage argues that if psychological effects are genuinely context-sensitive across populations and historical periods, then 'the demand for universal replication may be based on a mistaken model.' This directly challenges the assumption that replication failure proves the original finding was false — it might instead reflect genuine variation. The argument does not challenge statistical methods, pre-registration, or publication bias as concepts."
      },
      {
        "text": "Which of the following reforms described in the passage most directly addresses the problem of researchers presenting post-hoc analyses as if they were planned in advance?",
        "options": [
          "Open data sharing",
          "Pre-registration of research protocols",
          "Registered reports with post-publication peer review",
          "Increasing journal acceptance rates for null results"
        ],
        "correct": 1,
        "explanation": "The passage specifically defines pre-registration as 'publishing a research protocol before data collection, making it impossible to reframe exploratory analyses as confirmatory ones.' This directly targets the problem of post-hoc presentation. Open data addresses transparency but not the confirmatory/exploratory distinction. Registered reports focus on pre-data peer review. Accepting null results addresses publication bias, not p-hacking."
      },
      {
        "text": "The author's attitude toward the replication crisis is best characterized as:",
        "options": [
          "Dismissive, suggesting the crisis has been exaggerated by critics of psychology",
          "Alarmed, arguing that psychology should be abandoned as a science",
          "Analytically engaged, examining structural causes, proposed reforms, and philosophical complications",
          "Defensive, primarily concerned with protecting psychology's reputation"
        ],
        "correct": 2,
        "explanation": "The passage examines the crisis's structural causes (p-hacking, publication bias), describes reform efforts (open science), and raises philosophical complications (context-sensitivity) without dismissing or catastrophizing. This is an analytically engaged treatment. The author neither defends psychology's status quo nor calls for its abandonment."
      }
    ]
  },
  {
    "passageText": "In 1951, Henrietta Lacks, a Black woman from Baltimore, was treated for cervical cancer at Johns Hopkins Hospital. Cells taken from her tumor — without her knowledge or consent — proved unusually durable in laboratory culture, becoming the first human cell line to survive and reproduce indefinitely outside the body. HeLa cells, as they came to be called, went on to underpin vaccines, cancer research, and gene mapping projects, generating billions of dollars in commercial value. Lacks herself died that year, and her family remained unaware of her cells' existence for decades. When they learned the truth in the 1970s, they could neither afford adequate health insurance nor share in the profits their mother's biology had generated.\n\nThe Lacks case is emblematic of a broader pattern in the relationship between Western biomedical research and marginalized populations. Anthropologist Adriana Petryna has documented the 'outsourcing' of clinical trials to low-income countries, where regulatory regimes are weaker, labor is cheaper, and — crucially — populations may lack the resources to refuse participation or seek alternatives. Critics argue that these arrangements repeat the extractive logic of colonialism: knowledge and profit flow toward wealthy institutions and nations while risk is borne disproportionately by those with the fewest alternatives.\n\nIndigenous communities have raised parallel concerns about the extraction of traditional ecological and medical knowledge. Plants used medicinally for centuries by indigenous peoples have been synthesized, patented, and sold by pharmaceutical companies, with little acknowledgment of their origins and no benefit sharing with the communities whose knowledge made the discoveries possible. The Convention on Biological Diversity and the Nagoya Protocol represent international attempts to address 'biopiracy,' but enforcement remains uneven and contested.\n\nDecolonizing medicine involves more than correcting discrete injustices. Scholars such as Frantz Fanon and, more recently, Achille Mbembe have argued that the epistemological frameworks of Western medicine — its categories of disease, its standards of evidence, its models of the body — are themselves shaped by colonial history and may systematically marginalize non-Western healing traditions. This does not imply that evidence-based medicine is simply a Western bias; it does imply that what counts as evidence, and whose knowledge is recognized as knowledge, are questions that cannot be separated from the political history of the institutions that answer them.",
    "questions": [
      {
        "text": "The primary argument the author develops across all four paragraphs is that:",
        "options": [
          "HeLa cells represent an isolated ethical failure that has since been corrected by modern consent protocols",
          "Western biomedical research has systematically extracted knowledge and biological material from marginalized populations without adequate consent or benefit sharing",
          "Indigenous medical knowledge is superior to evidence-based medicine and should replace it",
          "Clinical trials should be prohibited in low-income countries until regulatory regimes are strengthened"
        ],
        "correct": 1,
        "explanation": "The passage moves from HeLa cells to clinical trial outsourcing to biopiracy to epistemological colonialism, building a cumulative argument about systematic extraction and inequity. Option A incorrectly characterizes the Lacks case as isolated and corrected. Option C is a misreading — the final paragraph explicitly says the argument 'does not imply that evidence-based medicine is simply a Western bias.' Option D is a policy prescription the author does not make."
      },
      {
        "text": "According to the passage, what is the significance of the fact that Lacks's family 'could neither afford adequate health insurance nor share in the profits'?",
        "options": [
          "It suggests that Johns Hopkins Hospital acted illegally under existing consent laws",
          "It illustrates the irony that the community bearing the costs of medical research did not share in its benefits",
          "It shows that the financial value of HeLa cells was not recognized until the 1970s",
          "It implies that the Lacks family should have been named co-inventors on subsequent patents"
        ],
        "correct": 1,
        "explanation": "The passage uses the Lacks family's situation to illustrate the extractive dynamic: Lacks's biology generated enormous commercial and scientific value while her family bore costs (no health coverage) and received no benefits. This supports the broader 'extractive logic of colonialism' argument. The passage does not address legality, the timing of financial recognition, or patent law specifically."
      },
      {
        "text": "The passage implies that the Nagoya Protocol and Convention on Biological Diversity are significant but insufficient because:",
        "options": [
          "They were negotiated without input from indigenous communities",
          "They prohibit all forms of bioprospecting regardless of benefit-sharing arrangements",
          "Enforcement of these international frameworks remains uneven and contested",
          "They apply only to plant-based medicines and not to human cell lines"
        ],
        "correct": 2,
        "explanation": "The passage states that these frameworks 'represent international attempts to address biopiracy, but enforcement remains uneven and contested.' This directly supports option C. The other options introduce specifics not found in the passage."
      },
      {
        "text": "The argument in the final paragraph most closely resembles which of the following claims?",
        "options": [
          "Scientific methods are culturally neutral and therefore universally valid",
          "The standards by which knowledge claims are evaluated are themselves shaped by the historical and political contexts of the institutions that set them",
          "Non-Western healing traditions have been conclusively proven to be as effective as evidence-based medicine",
          "Colonial history is irrelevant to the practice of contemporary biomedicine"
        ],
        "correct": 1,
        "explanation": "The final paragraph argues that 'what counts as evidence, and whose knowledge is recognized as knowledge, are questions that cannot be separated from the political history of the institutions that answer them.' This is a claim about the situated, historically shaped nature of epistemic standards — directly paralleled by option B. Option A is what the passage is arguing against. Option C overstates the claim, which is about recognition and evidence standards, not comparative effectiveness."
      }
    ]
  },
  {
    "passageText": "Few aesthetic questions have proved more philosophically vexing than whether music is intrinsically sad or happy, independently of the listener who hears it. The debate turns on a prior question: what kind of thing is a musical work? If music is a purely formal structure — patterns of pitch and rhythm — then emotional predicates apply to it only derivatively, by analogy to the human states it expresses or induces. If music is, in some sense, an expressive act whose meaning is partly constituted by the intentions and cultural contexts of its makers, then emotional descriptions may be genuinely applicable in a richer sense.\n\nThe philosopher Peter Kivy distinguished between 'the sad man' and 'the Saint Bernard.' A sad man's face expresses his inner emotional state; a Saint Bernard's face looks sad without the dog necessarily experiencing sadness. Kivy argued that much music is more like the Saint Bernard — it has a contour, a quality, that warrants the description 'sad' without implying that the music itself experiences anything or that listeners must feel sad in response. This cognitivist position holds that hearing sadness in music is a matter of perception rather than affect: we hear the sad quality in the descending melodic line or the minor mode without necessarily being moved to sadness ourselves.\n\nOpponents of cognitivism argue that this account misses the emotional power that gives music its significance. The arousal theory holds that music is sad if and only if it reliably induces sadness in appropriately situated listeners. This view struggles with two difficulties: first, the paradox of enjoying sad music (if sad music makes us sad, why do we seek it out?), and second, empirical variation in response (music that one listener finds deeply moving, another may find tedious). Cross-cultural research complicates the picture further. Some studies have found that certain musical features — tempo, mode, pitch range — correlate with emotional attributions across cultures, suggesting universal perceptual mechanisms. But the meanings of those mechanisms and the experiences they ground remain culturally mediated.\n\nThe distinction between absolute music (instrumental music with no programmatic content) and program music (music depicting a scene, narrative, or extramusical idea) adds another dimension. Program music invites listeners to interpret emotional content through an external referent; absolute music makes that referent unavailable, raising the question of whether emotional predicates can be grounded in purely musical structure. Hanslick's formalist answer — that music's content is nothing but 'tonally moving forms' — remains provocative precisely because it challenges listeners' phenomenological certainty that they hear something more.",
    "questions": [
      {
        "text": "Kivy's 'Saint Bernard' analogy is intended to illustrate which claim?",
        "options": [
          "Music can express sadness through its formal qualities without the music or listener necessarily experiencing that emotion",
          "Dogs are better than humans at expressing emotions through physical appearance",
          "All music is fundamentally about the emotions of its composer",
          "The arousal theory correctly identifies sadness in music with the sadness it induces in listeners"
        ],
        "correct": 0,
        "explanation": "The passage explains that Kivy uses the Saint Bernard to distinguish expressive appearance from inner emotional state: the dog's face looks sad without the dog experiencing sadness. Applied to music, this means music can have a 'sad quality' as a formal feature without implying the music experiences sadness or that listeners must feel sad. This is option A. The analogy does not make claims about dogs per se, and it explicitly opposes the arousal theory."
      },
      {
        "text": "The 'paradox of enjoying sad music,' as the passage describes it, is a challenge specifically to:",
        "options": [
          "Kivy's cognitivist position",
          "The arousal theory of musical emotion",
          "The formalist position articulated by Hanslick",
          "Cross-cultural research on musical universals"
        ],
        "correct": 1,
        "explanation": "The passage explicitly states that the arousal theory 'struggles with two difficulties: first, the paradox of enjoying sad music (if sad music makes us sad, why do we seek it out?).' The paradox challenges arousal theory because that theory defines sad music by its capacity to induce sadness — which should make it aversive. It does not target Kivy's cognitivism, which does not require listeners to feel sad."
      },
      {
        "text": "Which of the following findings from cross-cultural research would most strongly support the cognitivist position over the arousal theory?",
        "options": [
          "Listeners from different cultures reliably feel sadness when hearing a particular piece",
          "Listeners from different cultures reliably perceive a descending minor-mode melody as having a sad quality, even when their self-reported emotional response varies",
          "Music composed in a major key is universally preferred over music in a minor key",
          "The emotional responses of musicians are more consistent cross-culturally than those of non-musicians"
        ],
        "correct": 1,
        "explanation": "Cognitivism holds that hearing sadness is a matter of perception rather than affect — we perceive the sad quality without necessarily being moved. Finding consistent cross-cultural perception of sad quality alongside variable emotional responses would support cognitivism (consistent perception) over arousal theory (which predicts consistent emotional induction). Option A would support arousal theory. Options C and D do not directly adjudicate between cognitivism and arousal theory."
      },
      {
        "text": "The author's reference to Hanslick's formalism as 'provocative precisely because it challenges listeners' phenomenological certainty' implies that:",
        "options": [
          "Most music theorists now accept Hanslick's view as correct",
          "Listeners typically experience music as expressing something beyond pure tonal form, making the formalist denial counterintuitive",
          "Phenomenological certainty is a reliable guide to the correct aesthetic theory",
          "Program music supports Hanslick's formalism more than absolute music does"
        ],
        "correct": 1,
        "explanation": "The passage says Hanslick's view is 'provocative' because it challenges what listeners feel certain they are experiencing — that they hear something more than tonal form. This implies that listeners' phenomenological certainty points in the opposite direction from formalism, making the denial striking. Option A is not implied. Option C is contradicted by the framing — the passage notes the challenge to phenomenological certainty without endorsing it as a reliable guide. Option D inverts the relationship: absolute music, not program music, is where formalism is most at issue."
      }
    ]
  },
  {
    "passageText": "The relationship between economic growth and environmental sustainability has been among the most contested questions in development economics. For much of the twentieth century, growth was treated as the solution to environmental problems as well as poverty: richer societies, the argument went, could afford cleaner technologies and would demand better environmental quality as incomes rose. The Environmental Kuznets Curve (EKC) hypothesis gave this intuition empirical form, suggesting an inverted-U relationship between income per capita and pollution: environmental degradation worsens during early industrialization, then improves as economies develop.\n\nThe EKC has attracted sustained criticism. Empirical support is inconsistent across different pollutants and national contexts: air quality in wealthy nations may improve partly because pollution-intensive industries have been relocated to lower-income countries rather than eliminated. Carbon dioxide, whose atmospheric accumulation drives climate change, shows no clear Kuznets inflection point in historical data. Critics argue that the EKC reflects regulatory capacity and political will, not automatic market processes, and that those same processes can be deployed without waiting for sufficient wealth to accumulate.\n\nThe degrowth movement takes a more radical position. Drawing on the work of economist Herman Daly and the earlier metaphor of economist Kenneth Boulding's 'spaceship Earth' — a closed system with finite resource stocks — degrowth theorists argue that the biophysical limits of the planet make perpetual GDP growth physically impossible and that the pursuit of growth in wealthy nations is not only unnecessary but actively harmful. They propose instead a 'steady-state economy' that maintains stocks of natural and manufactured capital without net growth.\n\nThe standard objection to degrowth is distributional: if the global economy stops growing, how are billions of people still living in poverty to improve their material conditions? Degrowth theorists respond that the relevant question is not whether growth should occur everywhere but whether growth remains the appropriate organizing goal for already-wealthy societies, and that redistribution within and between nations could raise living standards for the poor without requiring aggregate expansion. GDP itself, critics add, is a poor welfare measure: it counts environmental cleanup as growth, while counting unpaid domestic labor, leisure, and subjective wellbeing not at all.",
    "questions": [
      {
        "text": "The Environmental Kuznets Curve hypothesis predicts that:",
        "options": [
          "Environmental quality continuously improves as incomes rise",
          "Environmental degradation increases indefinitely with industrial development",
          "Environmental quality first worsens and then improves as income per capita rises",
          "Carbon dioxide emissions follow the same trajectory as other air pollutants in wealthy nations"
        ],
        "correct": 2,
        "explanation": "The passage describes the EKC as 'an inverted-U relationship between income per capita and pollution: environmental degradation worsens during early industrialization, then improves as economies develop.' This is option C. Option A describes only the second half. Option D is explicitly contradicted — the passage states CO2 'shows no clear Kuznets inflection point in historical data.'"
      },
      {
        "text": "The passage states that one reason air quality improvements in wealthy nations may not validate the EKC is:",
        "options": [
          "Wealthy nations have lower industrial output than developing nations",
          "Improvements may reflect the relocation of polluting industries abroad rather than actual pollution elimination",
          "Air quality metrics used in EKC studies are unreliable",
          "The EKC applies only to water pollution, not air quality"
        ],
        "correct": 1,
        "explanation": "The passage explicitly states that air quality in wealthy nations 'may improve partly because pollution-intensive industries have been relocated to lower-income countries rather than eliminated.' This is a displacement critique, not genuine decoupling. The other options introduce claims not made in the passage."
      },
      {
        "text": "Boulding's 'spaceship Earth' metaphor is invoked in the passage to support which argument?",
        "options": [
          "International cooperation on climate change requires treating the Earth as a shared vessel",
          "The planet's finite resource stocks make perpetual GDP growth physically impossible",
          "Space exploration offers a potential solution to resource scarcity",
          "Wealthy nations should assist developing nations with technology transfer"
        ],
        "correct": 1,
        "explanation": "The passage uses 'spaceship Earth — a closed system with finite resource stocks' to support the degrowth claim that 'the biophysical limits of the planet make perpetual GDP growth physically impossible.' The metaphor is about finitude and closure, not cooperation, space exploration, or technology transfer."
      },
      {
        "text": "Degrowth theorists' response to the distributional objection, as described in the passage, assumes which of the following?",
        "options": [
          "Global GDP must continue growing for poverty reduction to be achievable",
          "Redistribution between and within nations could raise living standards for the poor independently of aggregate growth",
          "GDP is an accurate measure of welfare in both wealthy and poor nations",
          "Wealthy nations have already achieved sufficient material conditions and require no further development"
        ],
        "correct": 1,
        "explanation": "The passage states that degrowth theorists respond to the distributional objection by arguing 'that redistribution within and between nations could raise living standards for the poor without requiring aggregate expansion.' This is option B. Option A is the objection they are responding against. Option C is contradicted by the final sentence, which criticizes GDP as a welfare measure. Option D overstates the argument — the passage says degrowth is the appropriate goal for 'already-wealthy societies,' not a universal prescription."
      }
    ]
  },
  {
    "passageText": "What makes you the same person you were ten years ago? You share almost none of the same cells, your beliefs and values may have shifted substantially, and many memories from that period are inaccessible or distorted. The philosophy of personal identity asks whether there is a fact of the matter about what personal identity consists in, and if so, what that fact is.\n\nLocke's influential answer was psychological continuity: what makes a later person the same as an earlier one is an overlapping chain of memories and psychological connections. His criterion focused specifically on memory — person A at time T2 is identical to person B at T1 if A can remember experiences had by B. This view has intuitive appeal in many cases but generates counterintuitive results in others. Derek Parfit, the most influential twentieth-century philosopher of personal identity, argued via thought experiments involving fission and teleportation that identity is not what matters in survival. If your brain were divided and each hemisphere transplanted into a separate body, there would be no fact of the matter about which resulting person is 'really you,' but there would be two people each psychologically continuous with you. Parfit concluded that what matters is psychological continuity itself, not the further fact of numerical identity.\n\nDementia presents a clinically urgent version of these philosophical puzzles. As cognitive function deteriorates, the psychological connections that constitute identity on Locke's account unravel. Does the patient in advanced dementia have the same interests as the person who wrote advance directives years earlier? The Precedent Autonomy debate asks whether the earlier, competent self should have binding authority over the current self, or whether the current self — with its own apparent preferences, even if no longer philosophically sophisticated — has independent moral standing.\n\nBuddhist philosophy offers a strikingly different framework. The doctrine of anatta (no-self) holds that personal identity is a conceptual construction imposed on a stream of causally connected but not substantially unified mental events. Far from being a troubling metaphysical truth, the recognition of no-self is, in Buddhist practice, the beginning of liberation from suffering — since much of what causes suffering derives from the false belief that there is a fixed, permanent self to protect and gratify. The resonances between Parfit's analytical conclusions and Buddhist metaphysics are not coincidental: Parfit acknowledged direct influence.",
    "questions": [
      {
        "text": "According to the passage, Parfit's thought experiments about fission are intended to show that:",
        "options": [
          "Psychological continuity is not sufficient for personal identity",
          "Memory is the only reliable criterion for personal identity",
          "Personal identity is what matters in survival, not psychological continuity",
          "Numerical identity is not what matters in survival; psychological continuity is"
        ],
        "correct": 3,
        "explanation": "The passage states that Parfit 'concluded that what matters is psychological continuity itself, not the further fact of numerical identity.' The fission case shows that numerical identity can be indeterminate (no fact about which branch is 'really you') while psychological continuity can still obtain. Options A and B mischaracterize the argument. Option C inverts the conclusion — Parfit says identity (not psychological continuity) is what does NOT matter."
      },
      {
        "text": "The 'Precedent Autonomy' debate described in the passage is best understood as a conflict between:",
        "options": [
          "Medical efficiency and patient rights",
          "The authority of a former, competent self and the interests of a current self with diminished cognition",
          "The legal validity of advance directives and their clinical implementation",
          "Utilitarian and deontological approaches to medical decision-making"
        ],
        "correct": 1,
        "explanation": "The passage frames Precedent Autonomy as asking 'whether the earlier, competent self should have binding authority over the current self, or whether the current self — with its own apparent preferences — has independent moral standing.' This is directly option B. The passage does not frame the debate in terms of efficiency, legal validity, or utilitarian versus deontological frameworks."
      },
      {
        "text": "The passage suggests that Parfit's conclusions are related to Buddhist anatta because:",
        "options": [
          "Both claim that personal identity is constituted by memory alone",
          "Both deny that there is a substantial, unified self persisting through time",
          "Both argue that the self is permanent but unknowable",
          "Parfit borrowed his teleportation thought experiment from Buddhist texts"
        ],
        "correct": 1,
        "explanation": "The passage notes that anatta holds 'personal identity is a conceptual construction imposed on a stream of causally connected but not substantially unified mental events,' and Parfit concludes that 'identity is not what matters.' Both frameworks converge on the denial of a substantive, persistent self. Option A is Locke's view, not Parfit's or Buddhism's. Option C contradicts both — neither claims the self is permanent. Option D is not mentioned in the passage."
      },
      {
        "text": "Based on the passage, which of the following cases would most directly challenge Locke's memory-based criterion of personal identity?",
        "options": [
          "A person who has vivid memories of their childhood but whose personality has changed dramatically",
          "A person who has no memory of a crime they committed while sleepwalking but is biologically continuous with the person who committed it",
          "A person who undergoes a teleportation that perfectly preserves their psychological states",
          "A person whose advance directive conflicts with the medical team's clinical judgment"
        ],
        "correct": 1,
        "explanation": "Locke's memory criterion implies that if person A cannot remember actions performed by B, A is not identical to B. The sleepwalking case creates a problem: intuitively we hold the person morally responsible, suggesting biological or other continuity matters, but Locke's criterion would say the waking person is not the same as the sleepwalker. This directly challenges the memory criterion. Option A is consistent with Locke (memory present = identity). Option C would support, not challenge, psychological continuity theories. Option D is about advance directives, not personal identity criteria."
      }
    ]
  },
  {
    "passageText": "How children acquire language — moving from babble to full grammatical competence in a matter of years, with minimal explicit instruction — has fascinated and divided linguists for decades. The nativist position, associated above all with Noam Chomsky, holds that the speed and uniformity of language acquisition cannot be explained by general learning mechanisms alone. Children are exposed to impoverished and error-laden input (the 'poverty of the stimulus'), yet converge on correct grammatical knowledge far beyond what the input unambiguously supports. Chomsky's postulate of Universal Grammar — an innate, domain-specific cognitive system that constrains the space of possible human languages — was designed to solve this learnability problem.\n\nUsage-based theories, developed by researchers including Michael Tomasello and his collaborators, challenge nativism on empirical and theoretical grounds. Language acquisition, on this view, emerges from the interaction of domain-general cognitive capacities — pattern recognition, statistical learning, intention reading — with the rich, structured input of social interaction. Children do not acquire abstract grammatical categories wholesale but build them incrementally from specific instances, generalizing with increasing scope as experience accumulates. This approach predicts that early language should be item-specific and bound to particular social routines, a prediction borne out by naturalistic corpus studies.\n\nThe critical period hypothesis adds a developmental dimension: there is a window, roughly from birth to puberty, during which full native competence is readily acquired, and after which the process is effortful and incomplete. Evidence comes from cases of language deprivation (feral children, deaf individuals denied sign language during childhood), second language acquisition data, and neuroimaging studies showing shifts in cortical organization after the critical period closes. The hypothesis is consistent with both nativist and usage-based accounts: nativists interpret it as evidence of a maturational schedule built into Universal Grammar; usage-based theorists see it as reflecting the general neurodevelopmental constraints on plasticity.\n\nBilingualism research has moved from the old deficit model — which treated two languages as competing and reducing competence in each — toward findings of cognitive advantage. Bilingual individuals, managing two competing linguistic systems from early childhood, appear to show enhanced executive function, particularly in tasks requiring selective attention and interference suppression. Proposed mechanisms include the constant practice of monitoring which language is appropriate and suppressing the other. The findings are contested, with some large-sample studies failing to replicate the advantage, but the debate has productively displaced the assumption that monolingualism is the cognitive norm.",
    "questions": [
      {
        "text": "The 'poverty of the stimulus' argument, as described in the passage, is intended to support which conclusion?",
        "options": [
          "Children in low-income environments acquire language more slowly than wealthy peers",
          "General learning mechanisms are sufficient to explain language acquisition given sufficient input",
          "The speed and uniformity of language acquisition requires an innate language-specific mechanism",
          "Children learn grammar primarily through explicit parental correction"
        ],
        "correct": 2,
        "explanation": "The passage explains that children 'converge on correct grammatical knowledge far beyond what the input unambiguously supports,' and that this is what the poverty of the stimulus argument invokes. The argument concludes that general learning from input cannot explain the outcome, supporting the nativist postulate of Universal Grammar. Option A misreads 'poverty of the stimulus' as literal poverty. Option B is the position the argument is designed to challenge. Option D is not mentioned."
      },
      {
        "text": "Which of the following predictions follows from the usage-based theory, according to the passage?",
        "options": [
          "Children should show evidence of abstract grammatical categories from the earliest stages of language production",
          "Children learning different languages should converge on identical early grammatical structures",
          "Early language should be item-specific and tied to particular social routines",
          "Children deprived of social interaction should nonetheless acquire language through pattern recognition alone"
        ],
        "correct": 2,
        "explanation": "The passage states that usage-based theory 'predicts that early language should be item-specific and bound to particular social routines, a prediction borne out by naturalistic corpus studies.' Option A is the nativist prediction — that abstract categories are present from the start. Option B is also more consistent with Universal Grammar. Option D contradicts the usage-based emphasis on social interaction."
      },
      {
        "text": "The passage presents the critical period hypothesis as notable primarily because:",
        "options": [
          "It is consistent with nativist theory but incompatible with usage-based approaches",
          "It applies only to second language acquisition, not to first language acquisition",
          "Both nativist and usage-based theorists can accommodate it, each interpreting it differently",
          "It has been definitively proven by cases of language deprivation alone"
        ],
        "correct": 2,
        "explanation": "The passage explicitly states that 'the hypothesis is consistent with both nativist and usage-based accounts' and then describes how each side interprets it. This is option C. Option A incorrectly states incompatibility with usage-based theories. Option B is contradicted — evidence comes from first-language deprivation as well. Option D overstates the evidential status; the passage lists multiple sources of evidence without claiming definitive proof."
      },
      {
        "text": "The author describes the 'old deficit model' of bilingualism in order to:",
        "options": [
          "Argue that bilingualism genuinely reduces grammatical competence in each language",
          "Contrast it with more recent research suggesting cognitive advantages from bilingualism",
          "Explain why bilingual children perform worse on standardized tests",
          "Support the nativist claim that Universal Grammar operates in one language at a time"
        ],
        "correct": 1,
        "explanation": "The passage explicitly contrasts the 'old deficit model' with 'findings of cognitive advantage' in bilingual individuals, noting that the debate 'has productively displaced the assumption that monolingualism is the cognitive norm.' The deficit model is introduced as a historical foil. Options A, C, and D misrepresent the passage's purpose and content."
      }
    ]
  },
  {
    "passageText": "William James, writing in 1890, defined attention as 'the taking possession by the mind, in clear and vivid form, of one out of what seem several simultaneously possible objects or trains of thought.' That definition captures something essential: attention is selective, effortful, and limited. It is not simply passive reception of input but active allocation of cognitive resources, with the consequence that what falls outside the spotlight is perceived, if at all, in degraded form. Experiments on inattentional blindness — the failure to notice a gorilla walking across a basketball court when attention is otherwise occupied — demonstrate how dramatically the attended and unattended differ in phenomenal salience.\n\nDual-process theory, associated with psychologists Keith Stanovich and Richard West and popularized by Daniel Kahneman, distinguishes between System 1 (fast, automatic, associative, low-effort) and System 2 (slow, deliberate, rule-governed, high-effort) modes of cognition. Attention is the currency of System 2: deliberate reasoning draws on a limited attentional budget, and the depletion of that budget through 'cognitive load' impairs subsequent performance on tasks requiring controlled attention. The theory has been used to explain a wide range of phenomena, from implicit bias (System 1's automatic associations) to logical errors (System 2's susceptibility to fatigue and distraction).\n\nThe attention economy framework, developed by economists and media theorists including Herbert Simon and Michael Goldhaber, applies these insights to the information environment. In an era of information abundance, scarcity shifts from information to attention: the resource being competed for by media platforms, advertisers, and technology companies is not the provision of information but the capture of time and focus. This framework illuminates the design logic of social media platforms — infinite scroll, variable reward schedules, notification systems — as deliberate architectures for maximizing attentional capture and minimizing voluntary disengagement.\n\nCritics of the attention economy framing argue that it tends toward technological determinism and passive victimhood, underestimating the capacity of users to exercise agency and digital literacy. Others raise normative questions about what sustained, undistracted attention makes possible — deep reading, creative work, democratic deliberation — and what its systematic disruption forecloses. The philosopher Simone Weil, in a different register, argued that the capacity for sustained, selfless attention was a moral and spiritual faculty; its cultivation was inseparable from the development of character. Whether that cultivation is compatible with the current information environment is an open question.",
    "questions": [
      {
        "text": "The gorilla experiment cited in the first paragraph is used to illustrate which specific claim?",
        "options": [
          "Humans have a limited working memory capacity",
          "Attention is a passive process that registers all available stimuli equally",
          "Unattended objects are perceived dramatically less clearly than attended ones",
          "System 2 processing is more reliable than System 1 in detecting unexpected events"
        ],
        "correct": 2,
        "explanation": "The passage introduces the gorilla experiment immediately after claiming that 'what falls outside the spotlight is perceived, if at all, in degraded form.' The experiment demonstrates how dramatically attended and unattended objects differ in salience — you can miss a gorilla entirely when attention is elsewhere. Option B is the opposite of the claim the experiment supports. The experiment is not about working memory capacity (A) or dual-process theory (D), which is introduced later."
      },
      {
        "text": "According to dual-process theory as described in the passage, cognitive load affects performance primarily by:",
        "options": [
          "Increasing the speed of System 1 processing",
          "Depleting the attentional budget available for System 2 reasoning",
          "Causing permanent damage to working memory circuits",
          "Making System 2 and System 1 operate simultaneously"
        ],
        "correct": 1,
        "explanation": "The passage states that 'deliberate reasoning draws on a limited attentional budget, and the depletion of that budget through cognitive load impairs subsequent performance on tasks requiring controlled attention.' This is option B — cognitive load depletes the System 2 attentional budget. Option A is not mentioned. Option C introduces neurological permanence not implied by the passage. Option D misrepresents the relationship between systems."
      },
      {
        "text": "The 'attention economy' framework implies that social media platforms' design features such as infinite scroll and variable reward schedules are primarily aimed at:",
        "options": [
          "Providing users with the most relevant and useful information possible",
          "Reducing cognitive load so that users can engage more deeply with content",
          "Maximizing attentional capture and minimizing voluntary disengagement",
          "Promoting System 2 deliberative reasoning among users"
        ],
        "correct": 2,
        "explanation": "The passage explicitly states that these features are 'deliberate architectures for maximizing attentional capture and minimizing voluntary disengagement.' This is option C. Options A and B describe different, more benign design goals inconsistent with the passage's framing. Option D contradicts the passage — variable reward schedules and infinite scroll are System 1 exploitation mechanisms, not System 2 promoters."
      },
      {
        "text": "Simone Weil's view, as described in the passage, adds which dimension to the discussion of attention that the earlier frameworks do not explicitly address?",
        "options": [
          "The neurological basis of attentional capacity",
          "The economic value of attention as a competitive resource",
          "The moral and spiritual significance of the capacity for sustained, selfless attention",
          "The role of dual-process theory in explaining attentional failure"
        ],
        "correct": 2,
        "explanation": "The passage introduces Weil in the final paragraph to add a normative, moral, and spiritual dimension: attention as a faculty whose cultivation is 'inseparable from the development of character.' This is not a dimension of James's phenomenological analysis, Kahneman's cognitive theory, or the attention economy's economic framework. Options A, B, and D correspond to frameworks already discussed earlier in the passage."
      }
    ]
  },
  {
    "passageText": "Chronic pain represents one of medicine's most challenging clinical and conceptual problems. Unlike acute pain, which functions as a warning signal of tissue damage and typically resolves with healing, chronic pain persists long after the original injury — and often in the complete absence of identifiable tissue pathology. This persistence led to decades of clinical skepticism, with patients whose pain could not be explained by detectable damage labeled as malingerers, psychosomatic cases, or drug-seekers. The biomedical model, which sought a one-to-one correspondence between tissue damage and reported pain, was an inadequate framework for understanding chronic pain's complexity.\n\nRonald Melzack and Patrick Wall's gate control theory, proposed in 1965, offered a neurological basis for the modulation of pain signals. The theory proposed that pain transmission is regulated by a 'gate' in the spinal dorsal horn, which can be opened or closed by peripheral nerve signals and by descending messages from the brain. This meant that psychological and emotional states — anxiety, attention, expectation — could modulate the pain signal before it reached conscious experience. Gate control theory was later revised and extended into neuromatrix theory, which emphasized the brain as an active generator of pain experience rather than a passive receiver of peripheral signals.\n\nThe biopsychosocial model, developed by George Engel as a critique of biomedicine, holds that illness is always the product of interacting biological, psychological, and social factors. Applied to chronic pain, this model highlights the role of pain catastrophizing (the tendency to ruminate on pain, magnify its threat, and feel helpless in its presence), psychological comorbidities, social support, and the healthcare system's own responses. Central sensitization — the neurological phenomenon in which the central nervous system becomes persistently hyperexcitable, amplifying pain signals in the absence of ongoing tissue damage — provides a biological mechanism for the persistence of pain that psychological factors can both trigger and sustain.\n\nPlacebo analgesia has proven particularly illuminating. Placebos produce genuine neurobiological changes — activating endogenous opioid systems, reducing spinal nociceptive processing — not mere subjective distortion. This finding has two implications: first, that the mind-body distinction underlying biomedical skepticism about chronic pain was always oversimplified; and second, that the therapeutic relationship itself, through its effects on expectation and trust, is a neurobiologically active component of treatment, not merely a confound to be controlled.",
    "questions": [
      {
        "text": "The passage implies that biomedical skepticism toward chronic pain patients whose pain lacked identifiable tissue damage was:",
        "options": [
          "Justified given the state of neurological knowledge before gate control theory",
          "Based on a framework that required one-to-one correspondence between damage and pain, which was an inadequate model",
          "Primarily motivated by financial concerns about prescription drug costs",
          "Correct in identifying psychological factors as the exclusive cause of unexplained pain"
        ],
        "correct": 1,
        "explanation": "The passage states that 'the biomedical model, which sought a one-to-one correspondence between tissue damage and reported pain, was an inadequate framework for understanding chronic pain.' The dismissal of such patients followed from this inadequate model. Option A partially acknowledges historical context but frames the skepticism as justified, which the passage does not. Option C introduces financial motivations not mentioned. Option D overstates — the passage discusses psychological factors as modulating, not exclusively causing, pain."
      },
      {
        "text": "Gate control theory was significant because it provided a mechanism for which observation?",
        "options": [
          "Chronic pain always corresponds to identifiable peripheral tissue damage",
          "Psychological and emotional states can modulate pain signals before they reach conscious experience",
          "Placebos produce genuine neurobiological changes in the opioid system",
          "Central sensitization is the primary cause of all chronic pain conditions"
        ],
        "correct": 1,
        "explanation": "The passage states that gate control theory showed 'psychological and emotional states — anxiety, attention, expectation — could modulate the pain signal before it reached conscious experience.' This is option B. Option A is the biomedical model the theory helped displace. Option C describes placebo research, discussed in a different paragraph. Option D describes central sensitization, a separate concept."
      },
      {
        "text": "Pain catastrophizing, as described in the passage, is an example of which category of factor in the biopsychosocial model?",
        "options": [
          "Biological",
          "Social",
          "Psychological",
          "Neurological"
        ],
        "correct": 2,
        "explanation": "The passage lists catastrophizing alongside 'psychological comorbidities' and distinguishes it from biological factors (central sensitization) and social factors (social support, healthcare system responses). Catastrophizing — ruminating on pain, magnifying its threat, feeling helpless — is a cognitive-emotional pattern, which is a psychological factor. Neurological is a subcategory of biological and not one of the three biopsychosocial categories."
      },
      {
        "text": "The discussion of placebo analgesia in the final paragraph most directly challenges which assumption?",
        "options": [
          "That chronic pain patients are reliable reporters of their own experience",
          "That the therapeutic relationship has any clinical significance",
          "That a sharp distinction between mind and body is an adequate framework for understanding pain",
          "That endogenous opioid systems exist"
        ],
        "correct": 2,
        "explanation": "The passage concludes from placebo research that 'the mind-body distinction underlying biomedical skepticism about chronic pain was always oversimplified.' Placebos produce real neurobiological changes, demonstrating that mental states (expectation, trust) have direct biological effects — collapsing the sharp mind-body divide. Option B is the opposite of what the passage claims: the therapeutic relationship is 'neurobiologically active,' implying it has clinical significance. Options A and D are not challenged by the placebo discussion."
      },
      {
        "text": "Central sensitization is introduced in the passage primarily to:",
        "options": [
          "Explain why all chronic pain has a psychological cause",
          "Provide a biological mechanism for pain persistence that psychological factors can influence",
          "Demonstrate that peripheral nerve signals are the primary determinants of pain intensity",
          "Support the view that chronic pain patients are exaggerating their symptoms"
        ],
        "correct": 1,
        "explanation": "The passage describes central sensitization as 'the neurological phenomenon in which the central nervous system becomes persistently hyperexcitable, amplifying pain signals in the absence of ongoing tissue damage' and notes that 'psychological factors can both trigger and sustain' it. Its role is to bridge the biological and psychological dimensions of the biopsychosocial model. Option A overstates — the passage says psychological factors interact with, not exclusively cause, sensitization. Option C contradicts the concept of central (not peripheral) sensitization. Option D is opposite to the passage's intent."
      }
    ]
  },
  {
    "passageText": "The problem of other minds asks how we can know that other people have conscious inner lives — that there is 'something it is like' to be them, in Thomas Nagel's influential formulation. Nagel's essay 'What Is It Like to Be a Bat?' argued that the subjective, first-person character of conscious experience is irreducible to any third-person, objective description, however complete. We can know all the neurophysiology of bat echolocation without thereby knowing what it is like to experience the world through sonar. The same gulf, Nagel implies, separates any two conscious beings whose experiential structures differ sufficiently.\n\nTwo major philosophical frameworks address how we understand other minds. Theory-theory holds that we attribute mental states to others by applying a folk-psychological theory — a set of generalizations about how mental states cause behavior. When we observe someone reach for an umbrella, we infer the belief that it will rain and the desire to stay dry. This attribution is inferential, third-personal, and explicitly representational. Simulation theory, by contrast, holds that we understand others by running their situation through our own cognitive systems — we simulate their perspective by imaginatively taking up their point of view, using our own mental processes as a model.\n\nThe discovery of mirror neurons in macaque monkeys in the 1990s appeared to offer a neural substrate for simulation theory. These neurons fire both when the monkey performs an action and when it observes the same action performed by another. Some researchers extrapolated to human empathy: perhaps the capacity to resonate with others' emotions is grounded in a neural mirroring system that directly maps observed action and emotion onto the observer's own motor and affective systems. The claim attracted enormous popular interest but also significant scientific criticism, with critics arguing that the function of mirror neurons remains poorly understood and that the leap from macaque motor neurons to human empathy is empirically unwarranted.\n\nResearch on autism has added practical stakes to these theoretical debates. Early accounts portrayed autism as a deficit in a 'theory of mind' module — an impaired capacity to attribute mental states to others, explaining social difficulties. More recent research has complicated this picture, suggesting that autistic individuals may process social information differently rather than lacking social cognition entirely, and raising questions about whose model of normal social cognition is being used as the standard. The double empathy problem, proposed by researcher Damian Milton, holds that the difficulties in autistic-neurotypical interaction reflect a bidirectional mismatch: neurotypical individuals also have difficulty understanding autistic experience, but this difficulty is rarely pathologized because neurotypical norms dominate the clinical gaze.",
    "questions": [
      {
        "text": "Nagel's 'bat' argument is intended to demonstrate that:",
        "options": [
          "Bats have richer conscious experiences than humans",
          "Neuroscience will eventually provide a complete account of all conscious experience",
          "The subjective character of experience cannot be captured by any objective, third-person description",
          "Simulation theory is more adequate than theory-theory for understanding other minds"
        ],
        "correct": 2,
        "explanation": "The passage explains that Nagel argues 'the subjective, first-person character of conscious experience is irreducible to any third-person, objective description, however complete.' We could know all bat neurophysiology without knowing what echolocation experience is like. The argument is about the limits of objective description, not comparative richness (A), neuroscience's prospects (B), or adjudicating between simulation and theory-theory (D)."
      },
      {
        "text": "According to the passage, simulation theory differs from theory-theory in that simulation theory holds:",
        "options": [
          "We understand others by applying a set of generalizations about how mental states cause behavior",
          "We understand others by imaginatively taking up their perspective using our own mental processes as a model",
          "Mirror neurons provide direct evidence that social cognition is purely neurological",
          "Autistic individuals have an impaired theory of mind module"
        ],
        "correct": 1,
        "explanation": "The passage defines simulation theory as understanding others 'by running their situation through our own cognitive systems — we simulate their perspective by imaginatively taking up their point of view.' Option A is theory-theory. Options C and D describe other claims in the passage not used to define simulation theory."
      },
      {
        "text": "The critics of mirror neuron research described in the passage would most likely object to which claim?",
        "options": [
          "Mirror neurons fire during both action performance and observation in macaques",
          "Human empathy is directly and adequately explained by a neural mirroring system analogous to macaque mirror neurons",
          "Autistic individuals process social information differently from neurotypical individuals",
          "Theory-theory requires explicit representational inference"
        ],
        "correct": 1,
        "explanation": "The passage states that critics argue 'the function of mirror neurons remains poorly understood and that the leap from macaque motor neurons to human empathy is empirically unwarranted.' The critics do not dispute the macaque findings per se (A) — they object to the extrapolation to human empathy. Options C and D are claims not attributed to mirror neuron advocates, so they are not what the critics are objecting to."
      },
      {
        "text": "The 'double empathy problem' proposed by Milton challenges which assumption underlying early autism research?",
        "options": [
          "That autistic individuals experience difficulties in social interaction",
          "That social cognitive difficulties are bidirectional, affecting neurotypical individuals equally",
          "That the neurotypical model of social cognition is a neutral, universal standard rather than a particular perspective",
          "That mirror neurons underlie all forms of social understanding"
        ],
        "correct": 2,
        "explanation": "The passage describes the double empathy problem as holding that 'neurotypical individuals also have difficulty understanding autistic experience, but this difficulty is rarely pathologized because neurotypical norms dominate the clinical gaze.' This challenges the assumption that the neurotypical standard is neutral and universal. Option A is not challenged — the passage acknowledges social difficulties. Option B partially misrepresents the argument: Milton does say difficulties are bidirectional, but the key point is about pathologization, not equality. Option D concerns mirror neurons, a separate issue."
      }
    ]
  },
  {
    "passageText": "The twentieth century witnessed the largest migration in human history: the movement of populations from rural to urban environments. By 2007, for the first time, more than half of the world's population lived in cities, a proportion projected to reach two-thirds by mid-century. This shift raises fundamental questions not only about economic development and infrastructure but about what conditions support or undermine human flourishing.\n\nJane Jacobs, in her landmark 1961 work on American cities, argued against the prevailing urban renewal ideology that had produced vast housing projects and single-use zoning. Vital neighborhoods, Jacobs contended, required diversity — of use, of building age, of resident income — and density sufficient to generate the casual street life that she saw as the connective tissue of community. Jacobs's empirical eye captured something that planners' abstract models missed: the 'intricate ballet' of the street was not chaos to be rationalized but an evolved, self-organizing social order. Her critique of top-down planning anticipated later complexity theorists who saw cities as emergent systems rather than designed machines.\n\nThe sociologist Georg Simmel, writing in 1903, offered a darker analysis. The metropolitan dweller, confronted by the overwhelming stimulation of urban life — the speed, noise, variety, and anonymity — develops a 'blasé attitude' as a psychological defense. Rather than experiencing each person and event with fresh emotional engagement, the urbanite cultivates detachment and reserve. Simmel's analysis is not simply a complaint about city life; it is a structural argument: the very features that make cities productive and stimulating — their scale, anonymity, and sensory intensity — necessarily generate psychological alienation.\n\nRay Oldenburg's concept of 'third places' — neither home (first place) nor work (second place), but the taverns, barbershops, coffee houses, and public squares that serve as informal gathering grounds — identifies what urban design often fails to provide and what human community requires. Third places are characterized by accessible location, low cost, playfulness, and the presence of regulars; they function as social levelers, crossing class and status lines. Their decline — attributed variously to automobile-centric planning, long commutes, and the privatization of public space — is implicated in the epidemic of loneliness that social scientists have documented in contemporary affluent societies. The tension between the solitude that allows for individual depth and the community that sustains psychological health remains one of urbanization's unresolved inheritances.",
    "questions": [
      {
        "text": "Jane Jacobs's critique of urban renewal is best summarized as arguing that:",
        "options": [
          "Cities should be planned as efficiently as possible to maximize economic output",
          "Vital urban life requires the diversity and density that top-down single-use zoning destroys",
          "Urban renewal projects improved community life by replacing deteriorated housing",
          "Cities are too complex to be studied empirically and should be governed by planners' intuition"
        ],
        "correct": 1,
        "explanation": "The passage states that Jacobs argued against 'single-use zoning' and for diversity of 'use, building age, and resident income' and sufficient density to generate 'casual street life.' Her critique targeted top-down planning as destroying the evolved social order of streets. Option C contradicts Jacobs's critique. Option A and D misrepresent her view — she was skeptical of planners' abstract models, not an advocate for planning efficiency."
      },
      {
        "text": "Simmel's concept of the 'blasé attitude' is presented in the passage as:",
        "options": [
          "A moral failing of urban residents who should be more engaged with their communities",
          "A structural consequence of the same urban features that also make cities productive",
          "Evidence that cities are inherently inferior to rural environments for human flourishing",
          "A temporary adaptation that disappears as city residents become more experienced"
        ],
        "correct": 1,
        "explanation": "The passage states that Simmel's analysis is 'not simply a complaint' but 'a structural argument: the very features that make cities productive and stimulating — their scale, anonymity, and sensory intensity — necessarily generate psychological alienation.' This is option B — the blasé attitude is a structural consequence, not a moral failing (A), not evidence of rural superiority (C — which goes beyond Simmel's analysis), and not described as temporary (D)."
      },
      {
        "text": "According to the passage, third places serve which social function that first and second places do not?",
        "options": [
          "Providing spaces for professional networking and career advancement",
          "Serving as informal, accessible gathering grounds that cross class and status lines",
          "Offering private spaces for individual reflection and solitude",
          "Replacing the need for home and workplace in modern urban settings"
        ],
        "correct": 1,
        "explanation": "The passage defines third places as 'informal gathering grounds' that 'function as social levelers, crossing class and status lines.' Option A describes a function the passage does not attribute to third places. Option C describes solitude, which the passage mentions as a tension against community but does not associate with third places. Option D misrepresents Oldenburg — third places are a third category, not a replacement for the first two."
      },
      {
        "text": "The author's final sentence about 'the tension between solitude and community' implies that:",
        "options": [
          "Urban design has successfully resolved the conflict between individual depth and communal health",
          "The decline of third places is the only factor responsible for contemporary loneliness",
          "The challenge of balancing individual solitude and communal connection remains an ongoing problem in urban life",
          "Urbanization has definitively harmed human flourishing compared to pre-urban societies"
        ],
        "correct": 2,
        "explanation": "The passage closes by describing this tension as 'one of urbanization's unresolved inheritances,' explicitly signaling that it remains an ongoing, unresolved challenge. Option A contradicts 'unresolved.' Option B overstates — the passage describes the decline of third places as 'implicated in' loneliness, not as the only cause. Option D is not supported — the passage examines both costs and benefits of urban life without declaring it a net harm."
      }
    ]
  }
]

out = os.path.join(BASE, "data", "cars", "hq-cars-2.json")
os.makedirs(os.path.dirname(out), exist_ok=True)
with open(out, "w") as f:
    json.dump(PASSAGES, f, indent=2)
total_q = sum(len(p["questions"]) for p in PASSAGES)
print(f"Wrote {len(PASSAGES)} CARS passages ({total_q} questions) to {out}")
