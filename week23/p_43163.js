
    function solution(begin, target, words) {
        let visited = []
        let queue = [[begin,0]]
        
        while(queue.length){
            let [w,c] = queue.shift()
            if(w === target) return c
            words.forEach((word)=> {
                if(!visited.includes(word)){
                    if(checked(w,word)){
                        queue.push([word, ++c])
                        visited.push(word)
                    }
                    
                }
            })        
        }
    
        return 0              
    }
        function checked(str1, str2){
            let cnt = 0
            for(let i = 0;i <str1.length; i++){
                if(str1[i]!==str2[i]) cnt +=1
            }
            return cnt === 1
        }
        