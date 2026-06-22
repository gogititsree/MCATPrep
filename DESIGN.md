# MCAT Master Prep — Requirements & Design Document

## 1. Project Overview

A self-contained, offline-first web application for comprehensive MCAT preparation. The app runs entirely from the local filesystem with no server, build step, or external dependencies. All state is persisted in `localStorage`.

**Target user:** A student self-studying for the MCAT who wants a single unified resource covering study guides, practice exams, and interactive games.

---

## 2. Functional Requirements

### 2.1 Study Guides
- One guide per MCAT section: B/B, C/P, P/S, CARS
- Content organized by topic with collapsible or scrollable sections
- Tables, formula boxes, callout boxes, and key-fact highlights
- Each guide links directly to its corresponding mock exam

### 2.2 Mock Exams
- One exam per section (B/B, C/P, P/S, CARS)
- Multiple mock sets selectable per section (10 sets per section)
- Count-up timer visible during the exam
- Single-choice questions with A–D options
- On submit: highlight correct/incorrect answers, show explanations for every question
- Score summary panel with percentage and qualitative feedback
- Link to study guide and next-section exam from the results panel

### 2.3 Flashcards
- 60+ cards covering high-yield concepts across all sections
- Flip animation (front = term, back = definition)
- Per-card "Known" / "Still Learning" tracking persisted across sessions
- Navigation: previous / next, shuffle
- Spaced-repetition review queue: cards marked "Still Learning" surface again
- Progress counter and section filter

### 2.4 Matching Game
- 8 rounds of 8 term–definition pairs (16 cards per round)
- Cards shuffled each round; select a term then its matching definition
- Wrong pair: shake animation + brief red highlight; auto-deselects
- Correct pair: green highlight + locked (unclickable)
- Stats: elapsed time (count-up), moves, matched count, remaining count
- Best-time tracking per round, persisted via `localStorage`
- Completion banner with time, moves, new-best indicator, and Next Round / Replay buttons

### 2.5 Crossword Puzzle
- Interactive crossword with clue panel (Across / Down columns)
- Click a cell or clue to activate; keyboard input
- Check answer highlighting (correct = green, wrong = red)
- MCAT-themed vocabulary (B/B and P/S topics)

### 2.6 Passage Drill
- One clinical/science passage with 4 MCAT-style questions
- Count-up timer; submit button reveals answers and explanations
- Tracks: passages attempted, perfect scores (4/4), best time (seconds)
- Stats persisted to `localStorage` for dashboard display

### 2.7 Study Dashboard
- Aggregates data from all activities via `localStorage`
- Displays: known flashcard count, due-for-review count, quiz best score, passages attempted, perfect passage runs, best passage time, matching rounds completed, best and average match time
- Daily goal: set a target number of study sessions; "Mark study session" button increments today's count
- Weekly bar chart: 7-day history of daily session counts; bars turn green when daily goal is met
- Quick-action links to flashcards, passage drill, and matching game

### 2.8 Mock Exam Center
- Hub page listing all four section exams
- Shows sets per section, question counts, and a brief description
- Links directly to each exam page

---

## 3. Non-Functional Requirements

| Requirement | Constraint |
|---|---|
| **Offline / no server** | Must open via `file://` in any modern browser with no HTTP server |
| **No external dependencies** | No CDN fonts, icon libraries, or JS frameworks |
| **No build step** | Raw HTML/CSS/JS only; editable with any text editor |
| **Single shared stylesheet** | All pages link to `css/styles.css`; page-specific overrides in a local `<style>` block |
| **Shared exam engine** | All exam/quiz UIs share `js/exam.js` (`MCATExam` class) |
| **localStorage only** | All persistence via `localStorage`; no cookies, IndexedDB, or server calls |
| **Responsive** | Usable on tablet and desktop; mobile breakpoint at 640px |
| **Dark theme** | Fixed dark color scheme via CSS custom properties; no light-mode toggle |

---

## 4. Architecture

### 4.1 File Structure

```
MCATPrep/
├── index.html                  # Main dashboard / home
├── css/
│   └── styles.css              # Shared stylesheet (all pages)
├── js/
│   └── exam.js                 # Shared MCATExam engine class
├── study-guides/
│   ├── bio-biochem.html        # B/B guide
│   ├── chem-phys.html          # C/P guide
│   ├── psych-soc.html          # P/S guide
│   └── cars.html               # CARS strategy guide
├── mock-exams/
│   ├── index.html              # Mock Exam Center hub
│   ├── bio-biochem-exam.html   # B/B mock exam
│   ├── chem-phys-exam.html     # C/P mock exam
│   ├── psych-soc-exam.html     # P/S mock exam
│   └── cars-exam.html          # CARS mock exam
└── games/
    ├── crossword.html          # Crossword puzzle
    ├── flashcards.html         # Flashcard deck
    ├── matching.html           # Matching game
    ├── passage-drill.html      # Single passage drill
    └── dashboard.html          # Study progress dashboard
```

### 4.2 CSS Architecture

All shared styles live in `css/styles.css`. Page-specific styles go in a `<style>` block in the page's `<head>`. Local styles may override shared ones for that page only.

**CSS custom properties (defined on `:root`):**

| Variable | Value | Usage |
|---|---|---|
| `--bg` | `#0F172A` | Page background |
| `--surface` | `#1E293B` | Card backgrounds |
| `--surface2` | `#253148` | Inputs, option backgrounds |
| `--border` | `#334155` | All borders |
| `--accent` | `#6366F1` | Primary / indigo |
| `--accent2` | `#10B981` | Success / green |
| `--accent3` | `#F59E0B` | Warning / amber |
| `--accent4` | `#EF4444` | Danger / red |
| `--bb-color` | `#10B981` | B/B section color |
| `--cp-color` | `#6366F1` | C/P section color |
| `--ps-color` | `#F59E0B` | P/S section color |
| `--cars-color` | `#EF4444` | CARS section color |

### 4.3 Shared Exam Engine (`js/exam.js`)

`MCATExam` is a plain JS class used by all exam and quiz pages.

**Constructor:** `new MCATExam(questions, containerId, scorePanelId)`

- Renders all questions into `#containerId`
- Starts a count-up timer updating `#exam-timer`
- Tracks selected answer per question in `this.answers`
- Updates `#answered-count` span on each selection

**`exam.submit()`**
- Stops the timer
- Marks correct/incorrect options with CSS classes
- Shows all explanation blocks
- Writes score to `#score-big`, `#score-label`, `#score-detail`
- Shows and scrolls to the score panel

**Question object shape:**
```js
{
  text: string,
  options: string[],   // exactly 4 options
  correct: number,     // 0-based index of correct option
  explanation: string,
  source?: { name: string, url: string }  // optional attribution link
}
```

---

## 5. Data Model (localStorage)

| Key | Type | Written by | Read by | Description |
|---|---|---|---|---|
| `mcat-known` | `string[]` (JSON) | flashcards | dashboard | Card IDs the user marked Known |
| `mcat-unknown` | `string[]` (JSON) | flashcards | dashboard | Card IDs still being learned |
| `mcat-review` | `object` (JSON) | flashcards | dashboard | Spaced-repetition schedule: `{ [cardId]: { nextReview: timestamp } }` |
| `mcat-matching-completed` | `string` (number) | matching | dashboard | Total matching rounds completed (all time) |
| `mcat-match-times` | `object` (JSON) | matching | dashboard | Best time per round: `{ [roundIndex]: seconds }` |
| `mcat-passage-taken` | `string` (number) | passage-drill | dashboard | Total passage attempts |
| `mcat-passage-perfect` | `string` (number) | passage-drill | dashboard | Passage attempts with 4/4 score |
| `mcat-passage-best-time` | `string` (number) | passage-drill | dashboard | Best passage completion time in seconds |
| `mcat-quiz-taken` | `string` (number) | (future) | dashboard | Total quizzes taken |
| `mcat-quiz-best-score` | `string` | (future) | dashboard | Best quiz score |
| `mcat-quiz-streak` | `string` (number) | (future) | dashboard | Quiz streak count |
| `mcat-daily-goal` | `string` (number) | dashboard | dashboard | Target daily study sessions |
| `mcat-daily-progress` | `object` (JSON) | dashboard | dashboard | Sessions per day: `{ "YYYY-MM-DD": count }` |

---

## 6. Navigation Conventions

### 6.1 Game Pages (inside `games/`)
Each game page's nav shows all 4 other games and links back to the home logo. The current page is omitted from the nav links (no self-links).

| Page | Nav shows |
|---|---|
| crossword.html | Flashcards, Matching, Passage Drill, Dashboard |
| flashcards.html | Crossword, Matching, Passage Drill, Dashboard |
| matching.html | Crossword, Flashcards, Passage Drill, Dashboard |
| passage-drill.html | Crossword, Flashcards, Matching, Dashboard |
| dashboard.html | Crossword, Flashcards, Matching, Passage Drill |

### 6.2 Study Guide Pages (inside `study-guides/`)
Each guide's nav shows the other 3 section guides and a colored "Take Exam" button linking to its exam.

### 6.3 Mock Exam Pages (inside `mock-exams/`)
Minimal nav: logo (home) + link to the corresponding study guide. Timer was intentionally removed from the nav to avoid duplicate element IDs conflicting with the shared `MCATExam` timer logic.

---

## 7. Content Scope

### B/B Study Guide topics
Amino acids & protein structure, enzyme kinetics (Michaelis-Menten, inhibition types), metabolism (glycolysis, TCA, ETC, fatty acid oxidation, gluconeogenesis), molecular biology (replication, transcription, translation, DNA repair), cell biology, genetics (Mendelian, pedigrees, population genetics), physiology (cardiovascular, respiratory, renal, endocrine).

### C/P Study Guide topics
General chemistry (atomic structure, bonding, thermodynamics, kinetics, equilibrium, acids/bases, electrochemistry), organic chemistry (nomenclature, stereochemistry, reactions: SN1/SN2/E1/E2, carbonyl chemistry, spectroscopy), physics (kinematics, forces, energy, fluids, waves, optics, electricity & magnetism).

### P/S Study Guide topics
Neuroscience (brain regions, neurotransmitters, action potentials), learning (classical/operant conditioning, observational learning), memory (types, disorders, forgetting), developmental psychology, personality theories, psychological disorders, social psychology (attribution, conformity, obedience, group dynamics), sociology (theories, stratification, inequality, culture).

### CARS Study Guide topics
Passage strategies, question-type taxonomy, elimination strategies, time management, common traps, 6-week practice plan.

### Matching Game rounds (8 rounds × 8 pairs)
1. Enzyme Kinetics
2. Metabolism
3. Molecular Biology
4. General Chemistry
5. Physics
6. Psychology: Learning
7. Psychology: Memory & Cognition
8. Sociology & Social Psychology

---

## 8. Known Limitations & Future Work

| Item | Notes |
|---|---|
| Single passage drill | Only one passage is currently implemented; adding more requires duplicating the passage + question array |
| Quiz stats unimplemented | `mcat-quiz-taken`, `mcat-quiz-best-score`, `mcat-quiz-streak` keys are read by the dashboard but never written — the quiz feature is planned but not yet built |
| No cross-device sync | localStorage is browser- and device-local; no export/import mechanism |
| Mock exam questions | Each exam currently has 20 questions rather than the real MCAT's 59; question banks are hardcoded per file |
| Passage drill timer | The timer counts up (elapsed time); a countdown variant with an auto-submit at time-limit would be more exam-realistic |
| Crossword puzzle | Content is fixed; adding new puzzles requires editing the grid and clue arrays directly |
| No progress reset UI | Users cannot clear individual sections of localStorage without opening browser dev tools |
