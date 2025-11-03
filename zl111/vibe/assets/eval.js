// Shared quiz functions for Vibe Coding units (no shuffle, no server)

const secretKey = "vibe_secret_2025";

function decrypt(enc, salt) {
  const xored = new Uint8Array(atob(enc).split('').map(c => c.charCodeAt(0)));
  const result = new Uint8Array(xored.length);
  const keyBytes = new TextEncoder().encode(secretKey);
  for (let i = 0; i < xored.length; i++) {
    result[i] = xored[i] ^ keyBytes[i % keyBytes.length];
  }
  const decoded = new TextDecoder().decode(result);
  return decoded.slice(salt.length);
}

function getSalt(q) {
  return q.slice(1);
}

function checkQuiz(encryptedAnswers, total, unit) {
  let score = 0;

  for (let q in encryptedAnswers) {
    const selected = document.querySelector(`input[name="${q}"]:checked`);
    if (selected) {
      const encodedSelected = btoa(JSON.stringify({ [q]: selected.value }));
      const correct = decrypt(encryptedAnswers[q], getSalt(q));
      if (encodedSelected === correct) score++;
    }
  }

  const result = document.getElementById("result");
  if (score === total) {
    result.textContent = unit === 'prologue' ? "🐳 太棒了！你已全面掌握課文重點！" : "🐳 太棒了！你完全掌握了本課的核心精神！";
    // Mark quiz as passed
    vibeData.quiz_passed[unit] = true;
    saveVibeData();
    updateProgress({ quiz_passed: { [unit]: true } });
  } else if (score >= total / 2) {
    result.textContent = `⚡ 你答對了 ${score} 題，建議再回頭複習一下！`;
  } else {
    result.textContent = unit === 'prologue' ? "💡 再讀一遍課文，深入體會 Vibe Coding！" : "💡 建議再仔細閱讀課文，體會精準表達的重要性！";
  }
}
