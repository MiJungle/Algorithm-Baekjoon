function solution(s) {
    var answer = '';
    let new_s = Array.from(s)
    return new_s.sort().reverse().join("");
}