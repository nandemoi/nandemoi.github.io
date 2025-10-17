// Local-only utilities and progress storage (no server, no params)

// Add hover effect for nav bar (bind after DOM is ready)
function bindNavHover() {
  document.querySelectorAll('nav a').forEach(link => {
    const nav = link.closest('nav');
    if (!nav) return;
    link.addEventListener('mouseenter', () => { nav.style.backgroundColor = '#3a5cf7'; });
    link.addEventListener('mouseleave', () => { nav.style.backgroundColor = '#4a6cf7'; });
  });
}
});

// Vibe course data management (localStorage only)
let vibeData = {
    quiz_passed: {},
    reflections: {}
};

function initVibeData() {
    const stored = localStorage.getItem('vibe_course_data');
    if (stored) {
        try { vibeData = JSON.parse(stored); } catch(_) {}
    }
}

function saveVibeData() {
    localStorage.setItem('vibe_course_data', JSON.stringify(vibeData));
}

function updateVibeProgress(data) {
  if (data.quiz_passed) Object.assign(vibeData.quiz_passed, data.quiz_passed);
  if (data.reflections) Object.assign(vibeData.reflections, data.reflections);
  saveVibeData();
}

function getUnits() {
    // Ordered list of units in this course
    return ['prologue', 'unit1', 'epilogue'];
}

function unitFromHref(href) {
    try {
        const url = new URL(href, window.location.origin);
        const file = url.pathname.split('/').pop();
        if (!file) return null;
        if (file.startsWith('unit')) return file.replace('.html', '');
        if (file === 'prologue.html') return 'prologue';
        if (file === 'epilogue.html') return 'epilogue';
        return null;
    } catch (_) { return null; }
}

// Progress gating disabled (all units enabled)
function isUnitEnabled(unit) { return true; }
function enforceUnitAccessOnLoad() { /* no-op */ }
function markLockedLinks() { /* no-op */ }

// Update progress locally
async function updateProgress(data) {
  updateVibeProgress(data);
  return Promise.resolve();
}

window.addEventListener('DOMContentLoaded', () => {
    try { initVibeData(); } catch(_) {}
    try { markLockedLinks(); } catch (_) {}
    try { enforceUnitAccessOnLoad(); } catch (_) {}
    try { bindNavHover(); } catch(_) {}
});
window.addEventListener('load', () => { try { bindNavHover(); } catch(_) {} });
