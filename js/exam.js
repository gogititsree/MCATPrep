// Shared exam engine
class MCATExam {
  constructor(questions, containerId, scorePanelId) {
    this.questions = questions;
    this.container = document.getElementById(containerId);
    this.scorePanel = document.getElementById(scorePanelId);
    this.answers = {};
    this.submitted = false;
    this.startTime = Date.now();
    this.timerEl = document.getElementById('exam-timer');
    this.countEl = document.getElementById('answered-count');
    this.render();
    if (this.timerEl) this.startTimer();
  }

  startTimer() {
    this.timerInterval = setInterval(() => {
      const elapsed = Math.floor((Date.now() - this.startTime) / 1000);
      const m = Math.floor(elapsed / 60).toString().padStart(2, '0');
      const s = (elapsed % 60).toString().padStart(2, '0');
      this.timerEl.textContent = m + ':' + s;
    }, 1000);
  }

  render() {
    this.container.innerHTML = '';
    this.questions.forEach((q, qi) => {
      const block = document.createElement('div');
      block.className = 'question-block';
      block.id = 'q-' + qi;

      const questionNumber = document.createElement('div');
      questionNumber.className = 'question-number';
      questionNumber.textContent = `Question ${qi + 1} of ${this.questions.length}`;

      const questionText = document.createElement('div');
      questionText.className = 'question-text';
      questionText.textContent = q.text;

      const optionsContainer = document.createElement('div');
      optionsContainer.className = 'options';
      optionsContainer.id = `opts-${qi}`;

      const letters = ['A','B','C','D'];
      q.options.forEach((opt, oi) => {
        const option = document.createElement('div');
        option.className = 'option';
        option.dataset.qi = qi;
        option.dataset.oi = oi;
        option.addEventListener('click', () => this.select(qi, oi));

        const letterSpan = document.createElement('span');
        letterSpan.className = 'option-letter';
        letterSpan.textContent = letters[oi];

        const labelSpan = document.createElement('span');
        labelSpan.textContent = opt;

        option.append(letterSpan, labelSpan);
        optionsContainer.appendChild(option);
      });

      const explanation = document.createElement('div');
      explanation.className = 'explanation';
      explanation.id = `exp-${qi}`;

      const correctStrong = document.createElement('strong');
      correctStrong.textContent = `✅ Correct Answer: ${letters[q.correct]}`;
      explanation.appendChild(correctStrong);
      explanation.appendChild(document.createElement('br'));
      explanation.appendChild(document.createTextNode(q.explanation || ''));

      if (q.source) {
        const sourceDiv = document.createElement('div');
        sourceDiv.className = 'source';
        sourceDiv.textContent = 'Source: ';

        const sourceLink = document.createElement('a');
        sourceLink.href = q.source.url || '#';
        sourceLink.target = '_blank';
        sourceLink.rel = 'noopener';
        sourceLink.textContent = q.source.name || 'source';

        sourceDiv.appendChild(sourceLink);
        explanation.appendChild(sourceDiv);
      }

      block.append(questionNumber, questionText, optionsContainer, explanation);
      this.container.appendChild(block);
    });
  }

  select(qi, oi) {
    if (this.submitted) return;
    this.answers[qi] = oi;

    document.querySelectorAll(`#opts-${qi} .option`).forEach((el, i) => {
      el.classList.toggle('selected', i === oi);
    });

    if (this.countEl) {
      this.countEl.textContent = Object.keys(this.answers).length;
    }
  }

  submit() {
    if (this.submitted) return;
    this.submitted = true;
    if (this.timerInterval) clearInterval(this.timerInterval);

    let correct = 0;
    this.questions.forEach((q, qi) => {
      const chosen = this.answers[qi];
      const opts = document.querySelectorAll(`#opts-${qi} .option`);
      opts[q.correct].classList.add('correct');
      if (chosen !== undefined && chosen !== q.correct) {
        opts[chosen].classList.add('incorrect');
      }
      if (chosen === q.correct) correct++;
      document.getElementById('exp-' + qi).classList.add('show');
    });

    const pct = Math.round((correct / this.questions.length) * 100);
    const scoreEl = document.getElementById('score-big');
    const labelEl = document.getElementById('score-label');
    const detailEl = document.getElementById('score-detail');

    if (scoreEl) scoreEl.textContent = correct + '/' + this.questions.length;
    if (labelEl) labelEl.textContent = pct + '% correct';
    if (detailEl) {
      let msg = pct >= 80 ? '🎉 Excellent! You\'re in great shape.' :
                pct >= 60 ? '📚 Good work — review the missed questions.' :
                '💪 Keep studying — go back to the study guide!';
      detailEl.textContent = msg;
    }

    if (this.scorePanel) {
      this.scorePanel.classList.add('show');
      this.scorePanel.scrollIntoView({ behavior: 'smooth' });
    }
  }
}
