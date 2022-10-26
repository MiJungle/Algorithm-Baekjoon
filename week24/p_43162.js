function solution(n, computers) {
    var answer = 0;
    let visited = new Array(n+1).fill(0)
    
    function bfs(i){
        visited[i] = 1
        let queue = [i]
        while(queue.length){
            let next = queue.shift()
            for(let i = 0; i < computers[next-1].length ; i++)
                {
                    if(computers[next-1][i] == 1){
                                            
                    if(visited[i+1] != 1){
                        queue.push(i+1)
                        visited[i+1] = 1
                    }     
                    }

                    
                }
        }
        
    }
    
    for (let i = 1; i <= n; i++){
        if(visited[i] != 1){
            bfs(i)
            answer += 1
        }
    }
    
    
    
    return answer;
}