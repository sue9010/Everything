const loginForm = document.querySelector("#login-form");
const loginInput = document.querySelector("#login-form input");

function onLoginSubmit(tomato) {
  tomato.preventDefault();
  // const username = loginInput.value;
  console.log(tomato);

  // if(username===""){
  //     alert("Please write your name");
  // }else if(username.length>15) {
  //     alert("Your name is too long")
  // }
}

loginForm.addEventListener("submit", onLoginSubmit);
