function noReturn(){
    console.log("반환하지 않는다. 아무것도!")
}
const result = noReturn()
console.log(result)




function thereIsReturn(){
    console.log("반환한다. 무언가를")
    let num = 5
    return num
    return 10,20,30,40,50  // 마지막 1개인 50만 반환됨
}
const result2 = thereIsReturn()
console.log(result2)