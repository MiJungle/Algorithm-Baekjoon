function solution(n, k) {
    var answer = 0;
    let lamb = 12000
    let drink = 2000
    n >=10? answer = 12000*n + (k-(Math.floor(n/10)))*2000: answer = 12000*n + 2000*k
    return answer;
}