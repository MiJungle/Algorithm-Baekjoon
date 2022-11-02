function solution(maps) {
    let n = maps[0].length
    let m = maps.length
    let visited = [...maps]
    let dx = [-1,1,0,0]
    let dy = [0,0,-1,1]
    
    function bfs(a,b){
        let queue = [[a,b]]
        while (queue.length){
            let [x,y] = queue.shift()
            for(let i =0 ; i <4; i++){
                let nx = x + dx[i]
                let ny = y + dy[i]

                if(nx >=0 && nx <n && ny >=0 && ny<m&& maps[nx][ny]===1){
                    queue.push([nx,ny])
                    visited[nx][ny] = visited[x][y] + 1
                
                }
                
            }
        
        } 
    }
    bfs(0,0)
    
    if(visited[n-1][m-1]==1) return -1
    return visited[n-1][m-1]
}

//bfs로 이동하면서 좌표에 도착하면 끄탐.