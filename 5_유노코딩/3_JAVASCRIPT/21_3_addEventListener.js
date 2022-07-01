const btn1 = document.getElementById("one")
const btn2 = document.getElementById("two")
const btn3 = document.getElementById("three")

const handleClick = function(){
    console.log("저를 클릭하셨나요?")
    console.log("이케이케")
}


btn2.addEventListener('click', handleClick)  //콜백함수
btn2.addEventListener('click', function(){
    console.log("또 다른 핸들러가 추가 등록되었다!")
})

// btn2.removeEventListener('click', handleClick)  //위에 btn2.addEventListener('click', handleClick)가 출력 안 되게 함


const handleClick2 = function(event){
    console.log(event)
}
btn3.addEventListener('click', handleClick2)



const handleClick3 = function(event){
    console.log(event.target)
}
btn1.addEventListener('click', handleClick3)
btn2.addEventListener('click', handleClick3)