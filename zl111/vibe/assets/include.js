// Simple HTML include utility.
// Usage: <div data-include="components/header.html"></div>
(function(){
  async function includeOnce(root) {
    const nodes = (root || document).querySelectorAll('[data-include]');
    for (const el of nodes) {
      const file = el.getAttribute('data-include');
      if (!file) continue;
      try {
        const res = await fetch(file, { cache: 'no-cache' });
        if (res.ok) {
          el.innerHTML = await res.text();
        } else {
          el.innerHTML = '<!-- include failed: ' + file + ' -->';
        }
      } catch (e) {
        el.innerHTML = '<!-- include error: ' + file + ' -->';
      } finally {
        el.removeAttribute('data-include');
      }
    }
  }
  window.includeHTML = async function() {
    // Keep resolving until no include tags left (supports nested includes)
    for (let i = 0; i < 5; i++) {
      const before = document.querySelectorAll('[data-include]').length;
      if (!before) break;
      await includeOnce(document);
      const after = document.querySelectorAll('[data-include]').length;
      if (after === 0 || after === before) break;
    }
  };
  // Auto-run on DOM ready
  document.addEventListener('DOMContentLoaded', () => {
    window.includeHTML();
  });
})();
