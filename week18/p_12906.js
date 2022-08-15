#javascript

function solution(arr)
{
    let answer = [];
    
    
    for (let i = 0; i < arr.length; i++){
        answer.length===0? answer.push(arr[i]): (arr[i]!==answer[answer.length-1]?answer.push(arr[i]):null)
       
    }
    return answer
    
}

