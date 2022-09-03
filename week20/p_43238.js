function solution(n, times) {
    var answer = 0;
    
    let left = 1
    let right = Math.max(...times)*n
    while (left <= right){
        let mid = Math.floor((right+left)/2)
        let people = 0
        for (time of times){
            people += Math.floor(mid / time)
            if (people >= n){
                break
            }
            
        }
        
        if (people <n){
            left = mid +1
        }
        else if (people >=n){
            answer = mid
            right = mid-1
        }
    }
    
    return answer;
}
n= 6
times = [7,10]

console.log(solution(n,times))

