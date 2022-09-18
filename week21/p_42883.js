
function solution(number, k) {
    var answer = '';
    const stack = [];
    
    for(let i =0; i<number.length; i++){
        const el = number[i];
        
        while(k>0&& stack[stack.length-1]<el){
            stack.pop();
            k--;
        }
        stack.push(el);
    }
    stack.splice(stack.length-k,k);
    answer = stack.join("")
    return answer;
}





function solution(number, k) {
    var answer = '';
    let remove = 0
    
    while (remove != k){
        let left =0 
        let right = left + 1
        while(right != number.length){
            if(Number(number[left])<Number(number[right])){
                answer += number[right]
                remove += 1
                

            }
            else {answer += number[left]}
            left = right
            right += 1
        }
        
        
    }
    return answer;
}
//앞의 자리부터, n+1숫자가 크면, n번째 인덱스 제거
// left = 0 right = 1
// left < right, left 제거,  left = right, right +=1 