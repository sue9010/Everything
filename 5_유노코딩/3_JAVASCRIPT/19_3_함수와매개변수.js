function sayAnything(ant, number){
    for (let i = 0; i<number; i++){
        console.log(ant)
    }
    
}

sayAnything("자바스크립트 너무 재밌어",6)
sayAnything("재밌어서 죽겠다.",2)


function oddEven(number){
    if(number %2 ==1){
        return("홀수")
    }else{
        return("짝수")
    }
}

console.log(oddEven(10))
console.log(oddEven(7))