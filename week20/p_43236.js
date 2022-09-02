function solution(distance, rocks, n) {
    var answer = 0;
    let min = 0
    let max = distance
    rocks.sort((a,b)=>(a-b))
    
    while (min<=max){
        let mid = Math.floor((min+max)/2)
        let removeCount = 0
        let previous = 0
        
        for (let i = 0; i<rocks.length; i++){
            if(rocks[i]-previous <= mid) 
            {removeCount++ }
            else previous = rocks[i]
        }
        
        if (removeCount > n) max = mid-1
        else min = mid+ 1
        answer = Math.max(answer, min)
        
        
    }
    return answer;
}