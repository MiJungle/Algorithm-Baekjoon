function solution(a, b) {
    let arr = []
    for (let i =0; i < a.length ; i++){
        arr.push(a[i]*b[i])
    }
    let answer = 0
    for (let i = 0; i< arr.length ; i++){
        answer += arr[i]
    }
    return answer
}