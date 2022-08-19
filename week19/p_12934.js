function solution(n) {
    if(Number.isInteger(Math.sqrt(n))  === true){
        return (Math.sqrt(n)+1)*(Math.sqrt(n)+1)
    } else {
        return -1
    }
}