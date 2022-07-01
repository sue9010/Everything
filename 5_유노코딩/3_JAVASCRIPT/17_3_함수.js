// const sayHello = function(){
//     let number = 3 + 3
//     console.log(number)
// }

// sayHello()
// sayHello()
// sayHello()

sayHello() // 함수보다 앞에 있어도 괜찮음
function sayHello(){
    console.log("Hello")
    console.log("HI")
    console.log("안녕")
}

sayHello()
sayHello()
sayHello()
// sayBye() // 함수보다 앞에 있어서 오류 반환, 뒤의 문장은 실행 안됨


const sayBye = function(){
    console.log("Good bye")
}

sayBye()
sayBye()
sayBye()

function sayHello2(){
    let hello = "문자열 헬로우"
    console.log(hello)
}

sayHello2()

// console.log(hello) 함수 안에서 선언된 변수는 함수 밖에서 호출이 불가능함으로 오류가 반환됨