// Parse CLID from URL parameter
const urlParams = new URLSearchParams(window.location.search);
let clid = null;
if (urlParams.has('clid')) {
    try {
        clid = atob(urlParams.get('clid'));
        localStorage.setItem('clid', clid);
    } catch(e) {
        console.error('Invalid CLID parameter:', e);
        alert('Invalid CLID parameter');
    }
}
if (!clid) {
    alert('無法連接伺服器：仍可操作唯進度將不會登錄');
}

if (clid) {
    document.querySelectorAll('a[href*="lesson"]').forEach(link => {
        const url = new URL(link.href, window.location.origin);
        url.searchParams.set('clid', btoa(clid));
        link.href = url.href;
    });
}

// Utility function to update progress
async function updateProgress(data) {
    if (!clid) return;
    try {
        const encodedData = btoa(JSON.stringify(data));
        const response = await fetch('http://elton-m1.local:5050/update-progress', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ clid, prog: encodedData })
        });
        const result = await response.json();
        const decoded = JSON.parse(atob(result.data));
        if (decoded.handshake !== 'ok') {
            alert(decoded.error || 'Progress update failed');
        }
    } catch (e) {
        console.error('Progress update error:', e);
    }
}

