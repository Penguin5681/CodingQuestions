const openButton = document.getElementById("open-btn");
const closeButton = document.getElementById("close-btn");
const modal = document.getElementById("promo-modal")
const modalContent = document.getElementById("modal-content");

openButton.addEventListener("click", () => {
    modal.classList.remove("hidden");
});

modal.addEventListener("click", (event) => {
    if (event.target === modal) {
        modal.classList.add("hidden");
    }
});

closeButton.addEventListener("click", () => {
    modal.classList.add("hidden");
});