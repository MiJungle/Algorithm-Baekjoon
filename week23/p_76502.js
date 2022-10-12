

// 채점 결과
// 정확성: 35.7
// 합계: 35.7 / 100.0


function solution(s) {
    var answer = 0;
    for (let j =0 ; j <s.length; j ++){
        let new_s = s.slice(1,s.length) + s[0]
        s = new_s
        let small = 0, middle = 0 , big = 0
    for(let i =0 ; i <s.length; i ++){
        if (new_s[i]== "\(") small += 1
        else if (new_s[i] =="\)") {
         if (small >0) {small-=1} 
            else small-=1 
            break;}
        else if (new_s[i]=="\{") middle += 1
        else if (new_s[i]=="\}")  {if (middle >0) {middle-=1} 
            else middle-=1
            break;}
        else if (new_s[i]=="\[") big += 1
        else if (new_s[i]=="\]") {if (big >0) {big-=1} 
            else big -= 1
             break;}
    }
    if (small ===0 && middle ===0 && big === 0) answer += 1
            
        }
    return answer
}

s="[](){}"
console.log(solution(s))


// let a = "[](){}"
// let new_a = a.slice(1,a.length) + a[0]
// a = new_a
// console.log(new_a)
// console.log(a)


//회전을 해도 안되는 조건:
//올바른 괄호 문자열인지 어떻게 확인?
//중괄호, 소괄호, 대괄호 변수를 따로 둬서, open의 경우 숫자를 1씩 올린다 
// close 경우 숫자를 1씩 뺀다
// 음수가 되는경우 바로 올바르지 않은 문자열 