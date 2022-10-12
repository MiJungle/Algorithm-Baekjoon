// 채점 결과
// 정확성: 13.3
// 합계: 13.3 / 100.0

function solution(s) {
    var answer = [];
    let num = []
    let group = []
    for(let i = 0 ; i <s.length; i++){
        if(Number.isInteger(Number(s[i])) ) {
            group.push(Number(s[i]) )
        }

        else if (s[i]==="}") {
            num.push(group)
            group = []}
    }
    console.log(num)
    num.sort((a,b)=> a.length - b.length)
    for(let j = 0; j<num.length; j++){
        for(let k =0; k < num[j].length; k++){
            if(!answer.includes(num[j][k])){
                answer.push(num[j][k])
            }
        }
    }
    return answer
}
//
///