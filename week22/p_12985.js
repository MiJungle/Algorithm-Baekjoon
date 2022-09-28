https://school.programmers.co.kr/learn/courses/30/lessons/12985

function solution(n,a,b) {
    let answer = 0;
    let numA = a;
    let numB = b;
    
    while(numA !== numB) {
        numA = Math.ceil(numA / 2);
        numB = Math.ceil(numB / 2);
        answer++;
    }
    
    return answer;
}