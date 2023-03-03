const form = document.querySelector("#loginForm");

form.addEventListener("submit", (event) => {
  event.preventDefault();

  const username = form.elements.username.value;
  const password = form.elements.password.value;

  if (username === "admin" && password === "password") {
    window.location.href = "main.html";
  } else {
    alert("Please confirm ID or password");
  }
});
