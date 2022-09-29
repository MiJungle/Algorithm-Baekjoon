
// 채점 결과
// 정확성: 30.0
// 합계: 30.0 / 100.0

function solution(n, left, right) {
    var answer = [];
    
    for(let i = 1; i<=n; i++){
        let arr = []
        for(let j= 1 ; j<=n; j++){
            if(i>=j) arr.push(i)
            else arr.push(j)
        }
        answer = answer.concat(arr)
    }
    let final = answer.slice(left,right+1)
    return final
    
}

// 123 223 333
//1234 2234 3334 4444
// 1234
// 2234
// 3334
// 4444

// 12345
// 22345
// 33345
// 44445
// 55555