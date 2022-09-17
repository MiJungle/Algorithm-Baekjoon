
function solution(n) {
    var answer = 0;
    
    for(let i =1 ; i <=n ; i++){
        let count = 0
        for(let j = i; j <= n ; j++){
            count += j
            if(count == n) {
                answer += 1
            }
            else if (count >n) break
           
        }
    }
    return answer;
}


// 채점 결과
// 정확성: 75.0
// 효율성: 0.0
// 합계: 75.0 / 100.0?????
//break 여부가 효율성에 영향을 미침

function solution(n) {
    var answer = 0;
    
    for(let i =1 ; i <=n ; i++){
        let count = 0
        for(let j = i; j <= n ; j++){
            count += j
            if(count == n) {
                answer += 1
                break
            }
            else if (count >n) break
           
        }
    }
    
    
    return answer;
}

//brute force
