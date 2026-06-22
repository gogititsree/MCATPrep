const fs = require('fs');
const path = require('path');
const Ajv = require('ajv');
const glob = require('glob');

const SCHEMA_PATH = path.join(__dirname, '..', 'data', 'schema', 'question-schema.json');
const DATA_DIR = path.join(__dirname, '..', 'data', 'questions');
const CARS_DIR = path.join(__dirname, '..', 'data', 'cars');
const OUT_DIR = path.join(__dirname, '..', 'exams');

function readJSON(file) {
  return JSON.parse(fs.readFileSync(file, 'utf8'));
}

function ensure(dir) {
  if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });
}

function validateQuestions(schema, arr, filePath) {
  const ajv = new Ajv();
  const validate = ajv.compile(schema);
  let ok = true;
  arr.forEach((q, i) => {
    const valid = validate(q);
    if (!valid) {
      console.error(`Validation error in ${filePath}[${i}]:`, validate.errors);
      ok = false;
    }
  });
  return ok;
}

function collectSection(sectionDir) {
  const files = glob.sync('**/*.json', { cwd: sectionDir, absolute: true });
  let all = [];
  files.forEach(f => {
    const data = readJSON(f);
    if (Array.isArray(data)) all = all.concat(data);
    else if (Array.isArray(data.questions)) all = all.concat(data.questions);
  });
  return all;
}

function build() {
  ensure(OUT_DIR);
  const schema = readJSON(SCHEMA_PATH);

  const sections = ['bb','cp','ps'];
  sections.forEach(section => {
    const sectionDir = path.join(DATA_DIR, section);
    if (!fs.existsSync(sectionDir)) return;
    const files = glob.sync('**/*.json', { cwd: sectionDir, absolute: true });
    let all = [];
    files.forEach(f => {
      const data = readJSON(f);
      if (!Array.isArray(data)) return;
      const ok = validateQuestions(schema, data, f);
      if (!ok) process.exitCode = 2;
      all = all.concat(data);
    });

    // Create at most 25 exams, 25 items each
    const perExam = 25;
    ensure(path.join(OUT_DIR, section));
    for (let i = 0; i < Math.min(25, Math.floor(all.length / perExam) || 1); i++) {
      const start = i * perExam;
      const exam = all.slice(start, start + perExam);
      const outFile = path.join(OUT_DIR, section, `exam-${String(i+1).padStart(2,'0')}.json`);
      fs.writeFileSync(outFile, JSON.stringify(exam, null, 2), 'utf8');
      console.log('Wrote', outFile);
    }
  });

  // Handle CARS passages
  if (fs.existsSync(CARS_DIR)) {
    ensure(path.join(OUT_DIR, 'cars'));
    const carsFiles = glob.sync('**/*.json', { cwd: CARS_DIR, absolute: true });
    let allPassages = [];
    carsFiles.forEach(f => {
      const data = readJSON(f);
      if (Array.isArray(data)) allPassages = allPassages.concat(data);
      else if (data && data.passageText) allPassages.push(data);
    });
    // group 3 passages per exam
    const perCarsExam = 3;
    for (let i = 0; i < Math.min(25, Math.floor(allPassages.length / perCarsExam) || 1); i++) {
      const start = i * perCarsExam;
      const bundle = allPassages.slice(start, start + perCarsExam);
      const outFile = path.join(OUT_DIR, 'cars', `exam-${String(i+1).padStart(2,'0')}.json`);
      fs.writeFileSync(outFile, JSON.stringify(bundle, null, 2), 'utf8');
      console.log('Wrote', outFile);
    }
  }
}

build();
