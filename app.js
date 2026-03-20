// =============================================
//  Together For Better Mental Health
//  GAD-7 Checkpoint — App Logic
// =============================================

var questions = [
  { text: "Nervous, anxious or on edge?",                 img: IMAGES["q1"], color: "#4285F4" },
  { text: "Unable to stop or control worrying?",          img: IMAGES["q2"], color: "#34A853" },
  { text: "Worry too much about different things?",       img: IMAGES["q3"], color: "#34A853" },
  { text: "Having trouble relaxing?",                     img: IMAGES["q4"], color: "#FBBC05" },
  { text: "So restless that you cannot sit still?",       img: IMAGES["q5"], color: "#FBBC05" },
  { text: "Become easily annoyed or irritable?",          img: IMAGES["q6"], color: "#A13FEF" },
  { text: "Feeling afraid something awful might happen?", img: IMAGES["q7"], color: "#A13FEF" }
];

var options = [
  { text: "Not at all",               value: 0 },
  { text: "Several days",             value: 1 },
  { text: "More than half the days",  value: 2 },
  { text: "Nearly every day",         value: 3 }
];

// State — use 'answerHistory' to avoid collision with browser's window.history API
var currentStep   = 0;
var totalScore    = 0;
var answerHistory = [];

// ── Init ──────────────────────────────────────
document.getElementById("homeChar").src   = IMAGES["calm"];
document.getElementById("resultChar").src = IMAGES["calm"];

// ── Screen Switching ──────────────────────────
function showScreen(id) {
  var screens = document.querySelectorAll(".screen");
  for (var i = 0; i < screens.length; i++) {
    screens[i].classList.remove("active");
  }
  document.getElementById(id).classList.add("active");
}

// ── Dot Progress ──────────────────────────────
function buildDots(activeIndex) {
  var row = document.getElementById("dotsRow");
  row.innerHTML = "";
  for (var i = 0; i < questions.length; i++) {
    var d = document.createElement("div");
    d.className = i === activeIndex ? "dot active" : "dot";
    row.appendChild(d);
  }
}

// ── Quiz Flow ─────────────────────────────────
function startQuiz() {
  currentStep   = 0;
  totalScore    = 0;
  answerHistory = [];
  renderQuestion();
  showScreen("screen-question");
}

function renderQuestion() {
  var q = questions[currentStep];

  // Top colour bar
  document.getElementById("topBar").style.background = q.color;

  // Dots
  buildDots(currentStep);

  // Question text
  document.getElementById("questionText").textContent = q.text;

  // Character — re-trigger CSS animation on each new question
  var el = document.getElementById("qChar");
  el.style.animation = "none";
  el.src = q.img;
  el.offsetHeight; // force reflow
  el.style.animation = "";

  // Answer buttons
  var list = document.getElementById("answersList");
  list.innerHTML = "";
  for (var i = 0; i < options.length; i++) {
    (function(opt) {
      var btn = document.createElement("button");
      btn.className   = "btn";
      btn.textContent = opt.text;
      btn.onclick = function() { recordAnswer(opt.value); };
      list.appendChild(btn);
    })(options[i]);
  }
}

function recordAnswer(value) {
  answerHistory.push({ step: currentStep, value: value });
  totalScore += value;
  currentStep++;
  if (currentStep < questions.length) {
    renderQuestion();
  } else {
    showResults();
  }
}

function goBack() {
  if (currentStep === 0) {
    resetQuiz();
    return;
  }
  var last = answerHistory.pop();
  totalScore  -= last.value;
  currentStep  = last.step;
  renderQuestion();
}

// ── Results ───────────────────────────────────
function showResults() {
  document.getElementById("resultScore").textContent = totalScore;

  var band = document.getElementById("resultBand");
  var cls, title, msg;

  if (totalScore <= 4) {
    cls   = "minimal";
    title = "Minimal Anxiety";
    msg   = "Your score suggests minimal symptoms. Keep prioritizing your well-being!";
  } else if (totalScore <= 9) {
    cls   = "mild";
    title = "Mild Anxiety";
    msg   = "Your score indicates mild anxiety. Consider reviewing our brochure for daily management and breathing techniques.";
  } else if (totalScore <= 14) {
    cls   = "moderate";
    title = "Moderate Anxiety";
    msg   = "Your score indicates moderate anxiety symptoms. We recommend exploring the support resources and counseling information at our booth.";
  } else {
    cls   = "severe";
    title = "Severe Anxiety";
    msg   = "Your score indicates severe anxiety symptoms. Please consider reaching out to a healthcare professional or campus counseling services for support.";
  }

  band.innerHTML = '<div class="result-band ' + cls + '"><h3>' + title + '</h3><p>' + msg + '</p></div>';
  document.getElementById("topBar").style.background = "var(--teal)";
  showScreen("screen-result");
}

// ── Reset ─────────────────────────────────────
function resetQuiz() {
  currentStep   = 0;
  totalScore    = 0;
  answerHistory = [];
  document.getElementById("topBar").style.background = "transparent";
  showScreen("screen-home");
}

// ── Contact ───────────────────────────────────
function showContact() {
  alert("Contact us at your campus mental health booth!");
}
