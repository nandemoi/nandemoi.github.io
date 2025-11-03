// Unit 1 (mock demo): phrase builder + AI stub, no real execution
let stepIndex = 0;
let currentAISuggest = '';

const steps = [
  {
    id: 1,
    tiles: [
      '請做一個', '會打招呼的', 'Python 程式', '顯示', 'Hello, World!', '圓形', '烏龜', '好玩', '聲音', '鳴人', '老師好帥'
    ],
    target: ['請做一個', '會打招呼的', 'Python 程式', '顯示', 'Hello, World!'],
    aiMsg: '先用 print() 顯示固定文字，建立最小可運作的範例。',
    code: 'print("Hello, World!")\n',
    expected: 'Hello, World!\n'
  },
  {
    id: 2,
    tiles: [
      '把變數', 'name', '設為', 'Alice', '並顯示', 'Hello, Alice!', '馬上', '重來'
    ],
    target: ['把變數', 'name', '設為', 'Alice', '並顯示', 'Hello, Alice!'],
    aiMsg: '引入變數以便後續更換名字，使用 f-string 格式化輸出。',
    code: 'name = "Alice"\nprint(f"Hello, {name}!")\n',
    expected: 'Hello, Alice!\n'
  },
  {
    id: 3,
    tiles: [
      '列出', '1 到 5', '的平方', '每行顯示 數字 與 平方', '使用 迴圈', '請'
    ],
    target: ['列出', '1 到 5', '的平方', '每行顯示 數字 與 平方', '使用 迴圈'],
    aiMsg: '用 range 與迴圈產生表格。',
    code: 'for x in range(1, 6):\n    print(x, x*x)\n',
    expected: '1 1\n2 4\n3 9\n4 16\n5 25\n'
  }
];

function renderTiles() {
  const bank = document.getElementById('tileBank');
  const canvas = document.getElementById('tileCanvas');
  bank.innerHTML = '';
  canvas.innerHTML = '';
  const s = steps[stepIndex];
  // shuffle tiles each render
  const shuffled = s.tiles.slice();
  for (let i = shuffled.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
  }
  shuffled.forEach((t, i) => {
    const el = document.createElement('span');
    el.className = 'tile linky';
    el.textContent = t;
    el.dataset.idx = String(i);
    el.addEventListener('click', () => addToCanvas(el));
    bank.appendChild(el);
  });
  updateStepStatus();
}

function addToCanvas(tileEl) {
  if (tileEl.classList.contains('used')) return;
  const canvas = document.getElementById('tileCanvas');
  const clone = tileEl.cloneNode(true);
  clone.classList.remove('used');
  clone.classList.add('on-canvas');
  clone.addEventListener('click', () => removeFromCanvas(clone));
  canvas.appendChild(clone);
  tileEl.classList.add('used');
}

function removeFromCanvas(cloneEl) {
  const bank = document.getElementById('tileBank');
  // find matching bank tile by text
  const text = cloneEl.textContent;
  Array.from(bank.children).forEach(el => {
    if (el.textContent === text && el.classList.contains('used')) el.classList.remove('used');
  });
  cloneEl.remove();
}

function checkSentence() {
  const canvas = document.getElementById('tileCanvas');
  const chosen = Array.from(canvas.children).map(el => el.textContent);
  const target = steps[stepIndex].target;
  const aiMd = document.getElementById('aiMdBody');
  const applyBtn = document.getElementById('applyToCode');

  if (chosen.length !== target.length || !chosen.every((t, i) => t === target[i])) {
    // Legit AI response in markdown area
    const msg = [
      '# 我不太明白你的意思 🤔',
      '',
      '請試著包含：',
      '- 要做什麼（例：做一個會打招呼的程式）',
      '- 如何呈現（顯示/輸出什麼）',
      '- 關鍵字（Hello, World! 等）'
    ].join('\n');
    renderMarkdownTo(aiMd, msg);
    applyBtn.disabled = true;
    applyBtn.style.display = 'none';
    showNarrativeTip('提示：從最小可行開始。例如：「請做一個會打招呼的 Python 程式顯示 Hello, World!」');
    return;
  }

  // success: provide AI code suggestion; ask for acceptance via button
  const s = steps[stepIndex];
  // Rich, didactic explanation above the code (markdown)
  let verbose = '';
  if (s.id === 1) {
    verbose = [
      '# 很好的開始！先建立最小可行結果 (MVP)',
      '',
      '思考方式：',
      '- 先確認輸出可以正常顯示 → 顯示一行文字即可。',
      '- 讓結果可驗證 → 我們應該清楚知道螢幕會出現什麼。',
      '- 選擇直覺工具 → 用 Python 的 `print()` 把內容印到螢幕。',
      '為什麼是 Hello, World? 因為它能快速證明：環境 OK、語法 OK、輸出 OK。',
      '',
      '你可以預測：執行後應看到一行 `Hello, World!`（沒有多餘符號）',
      '',
      '```python',
      s.code.trimEnd(),
      '```'
    ].join('\n');
  } else if (s.id === 2) {
    verbose = [
      '# 抽換要素：從示例走向通用',
      '',
      '思考方式：',
      '- 抽換名字為變數 `name`，之後可輕易更換。',
      '- 用 f-string 把文字與變數自然拼接：`f"Hello, {name}!"`',
      '- 可驗證輸出 → 預期顯示 `Hello, Alice!`，換名會同步改變。',
      '',
      '你可以預測：把 `name = "Alice"` 改為 `"Bob"`，輸出將是 `Hello, Bob!`',
      '',
      '```python',
      s.code.trimEnd(),
      '```'
    ].join('\n');
  } else if (s.id === 3) {
    verbose = [
      '# 模式化：把重複交給迴圈',
      '',
      '思考方式：',
      '- 數列來源 → 需要 1 到 5：使用 `range(1, 6)`',
      '- 規律運算 → 平方是 `x*x`，隨 x 變動重複',
      '- 輸出格式 → 每行印 `x` 與 `x*x`，方便比對',
      '- 自我檢查 → 心算 1→1, 2→4, 3→9, 4→16, 5→25 與結果比對',
      '',
      '你可以預測：應有五行輸出，第二欄永遠是第一欄的平方。',
      '',
      '```python',
      s.code.trimEnd(),
      '```'
    ].join('\n');
  }
  renderMarkdownTo(aiMd, verbose);
  currentAISuggest = s.code;
  applyBtn.disabled = false;
  applyBtn.style.display = 'inline-block';
  onInputLegit();

  // store step progress
  try { updateProgress({ quiz_passed: { [`unit1_step_${s.id}`]: true } }); } catch (_) {}
}

function applyToCode() {
  if (!currentAISuggest) return;
  const wrap = document.getElementById('codeDraftWrap');
  const codeDraft = document.getElementById('codeDraft');
  codeDraft.textContent = currentAISuggest;
  if (wrap) wrap.style.display = 'block';
  Prism.highlightAllUnder(document);
  // enable run after acceptance
  const runBtn = document.getElementById('runMock');
  if (runBtn) runBtn.disabled = false;
}

function runMockExecution() {
  const out = document.getElementById('mockOutput');
  const s = steps[stepIndex];
  const text = (s.expected || '').toString();
  out.textContent = '';
  // slow-motion typewriter effect
  const runBtn = document.getElementById('runMock');
  if (runBtn) runBtn.disabled = true;
  let i = 0;
  const speed = 25; // ms per char
  const timer = setInterval(() => {
    out.textContent += text[i] || '';
    i++;
    if (i >= text.length) {
      clearInterval(timer);
      if (runBtn) runBtn.disabled = false;
    }
  }, speed);
}

function clearSentence() {
  const canvas = document.getElementById('tileCanvas');
  canvas.innerHTML = '';
  document.querySelectorAll('#tileBank .tile.used').forEach(el => el.classList.remove('used'));
}

// Minimal markdown renderer for AI panel
function renderMarkdownTo(container, md) {
  if (!container) return;
  // Parse fenced code blocks
  const lines = md.split(/\r?\n/);
  let html = '';
  let inCode = false;
  let codeLang = '';
  let listOpen = false;
  function closeList(){ if(listOpen){ html += '</ul>'; listOpen=false; } }
  for (let raw of lines) {
    const line = raw;
    const fence = line.match(/^```(.*)/);
    if (fence) {
      if (!inCode) {
        inCode = true; codeLang = (fence[1] || '').trim();
        html += `<pre><code class="language-${codeLang || 'text'}">`;
      } else {
        html += '</code></pre>';
        inCode = false; codeLang = '';
      }
      continue;
    }
    if (inCode) { html += line.replace(/</g,'&lt;').replace(/>/g,'&gt;') + '\n'; continue; }

    if (/^#\s+/.test(line)) { closeList(); html += `<h3>${line.replace(/^#\s+/, '')}</h3>`; continue; }
    if (/^-\s+/.test(line)) { if(!listOpen){ html += '<ul>'; listOpen=true; } html += `<li>${line.replace(/^-\s+/, '')}</li>`; continue; }
    if (line.trim() === '') { closeList(); html += '<br/>'; continue; }
    // inline code
    const p = line.replace(/`([^`]+)`/g, '<code>$1</code>');
    html += `<p>${p}</p>`;
  }
  closeList();
  container.innerHTML = html;
  try { Prism.highlightAllUnder(container); } catch(_) {}
}

function showExpected() {
  const out = document.getElementById('mockOutput');
  out.textContent = steps[stepIndex].expected || '';
}

function nextStep() {
  if (stepIndex < steps.length - 1) {
    stepIndex++;
    clearSentence();
    renderTiles();
  } else {
    // finished all steps
    try { updateProgress({ quiz_passed: { unit1: true } }); } catch (_) {}
    const status = document.getElementById('stepStatus');
    if (status) status.textContent = '完成！🎉';
  }
}

function updateStepStatus() {
  const status = document.getElementById('stepStatus');
  if (status) status.textContent = `步驟 ${stepIndex + 1} / ${steps.length}`;
}

// Narrative content loaded from built fragments
let narrativeIndex = 0;
const INPUT_STAGE = 1; // when to enable input (step 2)
let narrativeDone = false;

function currentUnitId() {
  try { return (typeof unitFromHref === 'function') ? (unitFromHref(window.location.href) || 'unit1') : 'unit1'; }
  catch(_) { return 'unit1'; }
}

async function renderNarrative() {
  const box = document.getElementById('narrativeContent');
  if (!box) return;
  const unit = currentUnitId();
  const stepNo = narrativeIndex + 1;
  const url = `assets/narrative/${unit}/step${stepNo}.html`;
  try {
    const res = await fetch(url, { cache: 'no-store' });
    if (!res.ok) throw new Error(String(res.status));
    const html = await res.text();
    box.innerHTML = html;
    // Toggle external Next based on internal presence or input stage
    const extNext = document.getElementById('narrativeNext');
    if (extNext) {
      const hasInternalNext = !!box.querySelector('button[data-action="next"]');
      if (narrativeIndex === INPUT_STAGE || hasInternalNext) {
        extNext.style.display = 'none';
      } else {
        extNext.style.display = '';
      }
    }
    // Delegate internal narrative action buttons (e.g., [button:next])
    box.addEventListener('click', (ev) => {
      const btn = ev.target.closest && ev.target.closest('button[data-action]');
      if (!btn) return;
      const action = btn.getAttribute('data-action');
      if (action === 'next') document.getElementById('narrativeNext')?.click();
      if (action === 'accept') document.getElementById('applyToCode')?.click();
      if (action === 'run') document.getElementById('runMock')?.click();
    }, { once: true });
  } catch (_) {
    narrativeDone = true;
    const nextBtn = document.getElementById('narrativeNext');
    if (nextBtn) nextBtn.style.display = 'none';
  }
}

function showNarrativeTip(msg) {
  const box = document.getElementById('narrativeContent');
  if (!box) return;
  const tip = document.createElement('div');
  tip.style.marginTop = '8px';
  tip.style.padding = '6px 8px';
  tip.style.borderLeft = '3px solid #4a6cf7';
  tip.style.background = '#f3f6ff';
  tip.style.color = '#1f2937';
  tip.style.fontSize = '0.95rem';
  tip.textContent = msg;
  box.appendChild(tip);
}

function setTitleState({input, ai, code, out}) {
  const m = { dim: 'title-dim', hot: 'title-hot', norm: 'title-norm' };
  const els = {
    input: document.getElementById('titleInput'),
    ai: document.getElementById('titleAI'),
    code: document.getElementById('titleCode'),
    out: document.getElementById('titleOut')
  };
  for (const [key, el] of Object.entries(els)) {
    if (!el) continue;
    el.classList.remove('title-dim', 'title-hot', 'title-norm', 'blink');
    const state = arguments[0][key];
    if (state && m[state]) {
      el.classList.add(m[state]);
      if (state === 'hot') {
        // blink briefly to draw attention; remove on animation end
        el.classList.add('blink');
        el.addEventListener('animationend', () => el.classList.remove('blink'), { once: true });
      }
    }
  }
}
function dimAllTitles() { setTitleState({ input:'dim', ai:'dim', code:'dim', out:'dim' }); }
function focusInputTitle() { setTitleState({ input:'hot', ai:'dim', code:'dim', out:'dim' }); }
function onInputLegit() { setTitleState({ input:'norm', ai:'hot', code:'dim', out:'dim' }); }
function onAcceptToCode() { setTitleState({ input:'norm', ai:'norm', code:'hot', out:'dim' }); }
function onRunExecution() { setTitleState({ input:'norm', ai:'norm', code:'norm', out:'hot' }); }
window.markOutputNormal = function() { // call from narrative when ready
  setTitleState({ input:'norm', ai:'norm', code:'norm', out:'norm' });
};

window.addEventListener('DOMContentLoaded', () => {
  const cb = document.getElementById('checkSentence'); if (cb) cb.textContent = '送出';
  const clr = document.getElementById('clearSentence'); if (clr) clr.textContent = '清空';
  // wire controls
  const checkBtn = document.getElementById('checkSentence');
  const clearBtn = document.getElementById('clearSentence');
  checkBtn.addEventListener('click', () => {
    checkSentence();
  });
  clearBtn.addEventListener('click', clearSentence);
  const applyBtn = document.getElementById('applyToCode');
  applyBtn.style.display = 'none';
  applyBtn.addEventListener('click', () => { applyToCode(); onAcceptToCode(); });
  document.getElementById('runMock').addEventListener('click', () => { runMockExecution(); onRunExecution(); });

  // narrative Next controls the pacing
  const nextBtn = document.getElementById('narrativeNext');
  nextBtn.addEventListener('click', async () => {
    if (narrativeDone) return;
    narrativeIndex++;
    await renderNarrative();
    if (narrativeIndex === INPUT_STAGE) {
      // enable input and lay out tiles
      checkBtn.disabled = false;
      clearBtn.disabled = false;
      renderTiles();
      focusInputTitle();
      // hide Next to focus on the task
      nextBtn.style.display = 'none';
    }
  });

  renderNarrative();
  dimAllTitles();
  // do not render tiles yet; wait until narrative asks for input
});
