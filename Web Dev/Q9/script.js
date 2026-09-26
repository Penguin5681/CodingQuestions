const body = document.body;

const faqItems = body.querySelectorAll(".faq-item");

faqItems.forEach(item => {
    item.addEventListener("click", () => {
        item.children[1].classList.toggle("hidden");
        
        item.querySelector(".icon").textContent = item.children[1].classList.contains("hidden") ? "+" : "-";
    })
});
