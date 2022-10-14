function solution(n, computers) {
    var answer = 0;
    let visited = new Array(n+1).fill(0);
    
    function bfs(k){
        visited[k] = 1
        let q = [k]
        while(q.length){
            let i = q.shift()
           for (let m = 0; m < computers[i-1].length ; m++){
               if(computers[i-1][m] == 1&&visited[m+1]==0){
                   q.push(m+1)
                   visited[m+1]= 1
               }
           }
        }
    }
    
    for(let i = 1; i <=n ; i++){
        if(visited[i]!=1){
            bfs(i)
            answer +=1 
        }
    }
    
    return answer
    
}
