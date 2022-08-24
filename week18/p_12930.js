function solution(s) {
    var answer = '';
    const new_s = s.split(' ')
    for (let i =0 ; i < new_s.length ; i++){
        
        for(let j = 0; j < new_s[i].length;j++){
            if (j %2 ==0 ) {
                answer += new_s[i][j].toUpperCase()                
            } 
            else if ( j%2 != 0){
                answer += new_s[i][j].toLowerCase()
            }
        }
        if (i !== new_s.length-1){
        answer += " "}
        
    }
    return answer;
}