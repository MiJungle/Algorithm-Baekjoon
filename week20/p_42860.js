function solution(name) {
    var answer = 0;
    let isa =0 ; 
    let alpha = ["A","B","C","D","E",
                 "F","G","H","I","J",
                 "K","L","M","N","O",
                 "P","Q","R","S","T",
                 "U","V","W","X","Y",
                 "Z"
                ]
    for (let i = 0; i <name.length;i++){
        if(i===0){
            answer += Math.min(alpha.indexOf(name[i]), 26- alpha.indexOf(name[i]) +1)
        }
        else {
            if(name[i]==="A"){
                isa += 1
            }
            else {
                answer += Math.min(alpha.indexOf(name[i]), 26- alpha.indexOf(name[i]) +1)
                console.log(answer)

                // answer += Math.min(isa+1, -isa+name.length-1)
            }
            
        }
        
        
    }
    return answer;
}