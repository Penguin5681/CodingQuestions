const stars = document.getElementById("stars");
const allStars = stars.querySelectorAll(".star");
const ratingValue = document.getElementById("rating-value");
const resetButton = document.getElementById("reset-btn");
const ratingText = document.getElementById("rating-text");
const labels = ["", "Poor", "Fair", "Good", "Very Good", "Excellent"];

function setRating(n) {
    allStars.forEach((star) => {
        const value = Number(star.dataset.value);
        star.classList.toggle("filled", value <= n);
    });

    ratingValue.textContent = n;
    ratingText.textContent = n > 0 ? labels[n] : "";
}

stars.addEventListener("click", (event) => {
    if (!event.target.dataset.value) return;
    const clickedValue = Number(event.target.dataset.value);
    setRating(clickedValue);
});

resetButton.addEventListener("click", () => setRating(0));
