const form = document.getElementById("login-form");
const email = document.getElementById("email");
const password = document.getElementById("password");
const message = document.getElementById("msg");

form.addEventListener("submit", (event) => {
    event.preventDefault();

    const emailText = email.value.trim();
    const passText = password.value;

    if (emailText.length == 0) {
        message.classList.remove("hidden");
        message.textContent = "Email is Required";
        message.classList.add("error");
    } else if (!emailText.includes("@")) {
        message.classList.remove("hidden");
        message.classList.add("error");
        message.textContent = "Enter a Valid email";
    } else if (passText.length < 6) {
        message.classList.remove("hidden");
        message.classList.add("error");
        message.textContent = "Password must be at least 6 characters";
    }
})