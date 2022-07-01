console.log(document.querySelector("h1"))
console.log(document.querySelector("p"))
console.log(document.querySelector("#text"))
console.log(document.querySelector(".paragraph"))
console.log(document.querySelector(".par")) //.오타가 나서 null 반환

console.log(document.getElementById("text"))
console.log(document.getElementById("p"))  // id 가 아님으로 null 반환

const h1 = document.querySelector("h1")
const p = document.getElementById("text")

console.log(h1.textContent)
h1.textContent = "변경된 제목입니다."

p.textContent = "겟 엘리먼트 바이 아이디"
console.log(p.textContent)