function solution(begin, target, words) {
    var answer = 0;
    
    function bfs(){
        let queue = [begin]
        
        while(queue.length){
            let word = queue.shift()
            if (word === target) return answer
            words.forEach((compare)=> {
                if(needToChange(word,compare) ){
                    
                   queue.push(compare)
                    answer += 1
                   }
            })
        }
        
    answer = 0
}

    function needToChange(word1,word2){
        let count = 0
        for(let i = 0 ; i <word1.length; i++){
            if (word1[i] != word2[i]) count += 1
        }
        return count === 1
    }

bfs()
return answer;
}