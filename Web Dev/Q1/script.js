const themeButton = document.getElementById("theme-btn");

themeButton.addEventListener("click", () => {
    const isDark = document.body.classList.toggle("dark");
    themeButton.textContent = isDark ? "Switch to Light" : "Switch to Dark";
});