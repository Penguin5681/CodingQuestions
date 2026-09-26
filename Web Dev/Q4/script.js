const planets = new Map();

planets.set("mars", { name: "Mars", fact: "Olympus Mons on Mars is the tallest volcano in the solar system.", image: "../images/mars.jpg" });

planets.set("venus", { name: "Venus", fact: "Venus is the hottest planet in the solar system.", image: "../images/venus.jpg" });

planets.set("jupiter", { name: "Jupiter", fact: "Jupiter is the largest planet in the solar system.", image: "../images/jupiter.jpg" });

const marsButton = document.getElementById("btn-mars");
const venusButton = document.getElementById("btn-venus");
const jupiterButton = document.getElementById("btn-jupiter");

const planetName = document.getElementById("planet-name");
const planetImage = document.getElementById("planet-image");
const planetFact = document.getElementById("planet-fact");

marsButton.addEventListener("click", () => {
    const info = planets.get("mars");
    planetName.textContent = info.name;
    planetFact.textContent = info.fact;
    planetImage.src = info.image;
});

venusButton.addEventListener("click", () => {
    const info = planets.get("venus");
    planetName.textContent = info.name;
    planetFact.textContent = info.fact;
    planetImage.src = info.image;
});

jupiterButton.addEventListener("click", () => {
    const info = planets.get("jupiter");
    planetName.textContent = info.name;
    planetFact.textContent = info.fact;
    planetImage.src = info.image;
});