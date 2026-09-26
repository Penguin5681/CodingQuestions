const info = new Map();

info.set('india', { capital: "New Delhi", currency: "INR" });
info.set('japan', { capital: "Tokyo", currency: "JPY" });
info.set('brazil', { capital: "Brasília", currency: "BRL" });

const countryDropdown = document.getElementById("country-select");

countryDropdown.addEventListener("change", (event) => {
    const currentSelectedCountry = countryDropdown.value;
    const currentSelectedCountryInfo = info.get(currentSelectedCountry);

    if (currentSelectedCountryInfo) {
        document.getElementById("country-info").textContent = "Capital: " + currentSelectedCountryInfo.capital + " Currency: " + currentSelectedCountryInfo.currency; 
    } else {
        document.getElementById("country-info").textContent = "";
    }

});