const left = document.getElementById("left");
const bio = document.getElementById("bio");
const saveBtn = document.getElementById("save-btn");

bio.addEventListener("input", (event) => {
    const currentText = event.target.value;
    const remaining = 80 - currentText.length;
    left.textContent = remaining;

    saveBtn.disabled = remaining <= 0;

    left.classList.remove("warning", "empty");

    if (remaining <= 0) {
        left.classList.add("empty");
    } else if (remaining <= 10) {
        left.classList.add("warning");
    }
});