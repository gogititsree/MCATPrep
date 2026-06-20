const fs = require('fs');
const path = require('path');
const vm = require('vm');

const QB_PATH = path.join(__dirname, '..', 'js', 'question-bank.js');
const OUT_DIR = path.join(__dirname, '..', 'data');

function ensure(dir) { if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true }); }

const code = fs.readFileSync(QB_PATH, 'utf8');

// Run in a sandboxed context to capture globals
const sandbox = {};
vm.createContext(sandbox);
let result = null;
try {
  const wrapped = code + "\n; (function(){ return { B_B_QUESTIONS: (typeof B_B_QUESTIONS !== 'undefined'? B_B_QUESTIONS:null), C_P_QUESTIONS: (typeof C_P_QUESTIONS !== 'undefined'? C_P_QUESTIONS:null), P_S_QUESTIONS: (typeof P_S_QUESTIONS !== 'undefined'? P_S_QUESTIONS:null), CARS_PASSAGES: (typeof CARS_PASSAGES !== 'undefined'? CARS_PASSAGES:null) }; })();";
  result = vm.runInContext(wrapped, sandbox, { filename: 'question-bank.js' });
} catch (e) {
  console.error('Error running question-bank.js in VM:', e);
  process.exit(1);
}

ensure(path.join(OUT_DIR, 'questions', 'bb'));
ensure(path.join(OUT_DIR, 'questions', 'cp'));
ensure(path.join(OUT_DIR, 'questions', 'ps'));
ensure(path.join(OUT_DIR, 'cars'));


function writeIfExistsVar(varData, outPath, name) {
  if (varData) {
    fs.writeFileSync(outPath, JSON.stringify(varData, null, 2), 'utf8');
    console.log('Wrote', outPath);
  } else {
    console.warn('No', name, 'found in result');
  }
}

writeIfExistsVar(result && result.B_B_QUESTIONS, path.join(OUT_DIR, 'questions', 'bb', 'all-bb.json'), 'B_B_QUESTIONS');
writeIfExistsVar(result && result.C_P_QUESTIONS, path.join(OUT_DIR, 'questions', 'cp', 'all-cp.json'), 'C_P_QUESTIONS');
writeIfExistsVar(result && result.P_S_QUESTIONS, path.join(OUT_DIR, 'questions', 'ps', 'all-ps.json'), 'P_S_QUESTIONS');
writeIfExistsVar(result && result.CARS_PASSAGES, path.join(OUT_DIR, 'cars', 'all-cars.json'), 'CARS_PASSAGES');

console.log('Export complete.');
