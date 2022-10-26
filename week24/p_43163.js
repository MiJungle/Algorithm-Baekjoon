function solution(begin, target, words) {
    var answer = 0;
    function bfs(begin,words){
        let queue = [begin]
        while(queue.length){
            let compare = queue.shift()
            words.forEach((word)=> {
                console.log(word)
            if(word === target) return answer    
            else if(change(word,compare)){
                queue.push(word)
                answer += 1
            }
        })
        }
    // } return 0
    
    }  
    function change(word1, word2){
        console.log(word1, word2)
        let count = 0
        for(let i =0 ; i < word1.length ; i++){
            if (word1[i] != word2[i]) count +=1
        }
        return (count == 1) 
    }
        
    console.log(bfs(begin,words))
}


begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]	
console.log(solution(begin,target,words))

// words.forEach((word)=>{
//     console.log(word)
// })