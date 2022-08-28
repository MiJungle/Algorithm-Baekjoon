function solution(s) {
    var answer = '';
    let arr = s.split(" ")
    let nums = []
    for ( i of arr) nums.push(Number(i))
    answer += Math.min(...nums)
    answer += " "
    answer += Math.max(...nums)

    return answer;
}