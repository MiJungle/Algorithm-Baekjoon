function solution(n) {
    let new_n = Array.from(String(n))
    let answer = new_n.sort().reverse().join('')

    return Number(answer)
}