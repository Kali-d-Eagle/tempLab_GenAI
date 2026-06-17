// List of program IDs
const programIds = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

// DOM Elements
const buttonsContainer = document.getElementById('buttons-container');
const toastContainer = document.getElementById('toast-container');

// Render 10 buttons
function init() {
  programIds.forEach(id => {
    const btn = document.createElement('button');
    btn.className = 'btn-primary';
    btn.innerHTML = `
      <svg fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
        <path stroke-linecap="round" stroke-linejoin="round" d="M3 16.5v2.25A2.25 2.25 0 005.25 21h13.5A2.25 2.25 0 0021 18.75V16.5M16.5 12L12 16.5m0 0L7.5 12m4.5 4.5V3"></path>
      </svg>
      ${id}
    `;
    btn.onclick = () => handleAction(id);
    buttonsContainer.appendChild(btn);
  });
}

// Show simple toast message
function showToast(message) {
  const toast = document.createElement('div');
  toast.className = 'toast';
  toast.innerHTML = `
    <svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
      <path stroke-linecap="round" stroke-linejoin="round" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
    </svg>
    <span>${message}</span>
  `;

  toastContainer.appendChild(toast);

  setTimeout(() => {
    toast.style.animation = 'toastFadeOut 0.2s ease forwards';
    setTimeout(() => {
      toast.remove();
    }, 200);
  }, 2500);
}

// Clipboard copy utility
async function copyToClipboard(text) {
  try {
    await navigator.clipboard.writeText(text);
    return true;
  } catch (err) {
    const textarea = document.createElement('textarea');
    textarea.value = text;
    textarea.style.position = 'fixed';
    document.body.appendChild(textarea);
    textarea.focus();
    textarea.select();
    try {
      document.execCommand('copy');
      document.body.removeChild(textarea);
      return true;
    } catch (e) {
      document.body.removeChild(textarea);
      return false;
    }
  }
}

// Action: Fetch from programs/program{id}.py, copy to clipboard, and trigger download
async function handleAction(id) {
  const actualPath = `programs/program${id}.py`;

  try {
    // 1. Fetch code dynamically from the physical file (no redundancy)
    const response = await fetch(actualPath);
    if (!response.ok) throw new Error("Failed to load file content");
    const codeText = await response.text();

    // 2. Copy the text to clipboard
    const copied = await copyToClipboard(codeText);

    // 3. Trigger download of the physical file
    const link = document.createElement('a');
    link.href = actualPath;
    link.download = `program${id}.py`;
    link.style.display = 'none';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);

    if (copied) {
      showToast(`Program ${id} copied & downloaded!`);
    } else {
      showToast(`Program ${id} downloaded!`);
    }
  } catch (err) {
    console.warn("Fetch failed (likely running offline via file:// protocol). Triggering download fallback.", err);

    // Fallback: trigger download directly
    const link = document.createElement('a');
    link.href = actualPath;
    link.download = `program${id}.py`;
    link.style.display = 'none';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);

    showToast(`Program ${id} downloaded!`);
  }
}

window.addEventListener('DOMContentLoaded', init);
