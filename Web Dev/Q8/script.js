const tabs = document.querySelector(".tabs");
const childrens = tabs.children;
// const body = document.body;
const tabPanel = document.querySelectorAll(".tab-panel");

Array.from(childrens).forEach(tab => {
    tab.addEventListener("click", () => {
        Array.from(childrens).forEach(children => {
            children.classList.remove("active");
        });

        tab.classList.add("active");

        Array.from(tabPanel).forEach(panel => {
            if (tab.attributes.getNamedItem("data-tab").value == panel.attributes.getNamedItem("id").value) {
                Array.from(tabPanel).forEach(panel => {
                    panel.classList.add("hidden");

                })
                panel.classList.remove("hidden");
            }
        })
        document.getElementById("current").textContent = `Current tab: ${tab.attributes.getNamedItem("data-tab").value}`;
    });
})