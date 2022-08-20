
strings = ["a", "ab", "a"]	
n = 1
function solution(strings, n) {
    let answer = []
    let strindex = []
    for(let i = 0; i < strings.length ; i ++){
        strindex.push([strings[i].slice(n,strings[i].length), i])
    }
    strindex.sort()
    console.log(strindex)
    for (let i =0; i <strindex.length; i++){
        
        answer.push(strings[strindex[i][1]])
    }
    
  return answer
}

console.log(solution(strings,n))