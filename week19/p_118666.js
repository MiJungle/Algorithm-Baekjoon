
function solution(survey, choices) {

    var dictObject = {R:0 , T:0, C:0, F:0, J:0, M:0, A:0, N:0}
    

        for(let j =0; j < choices.length; j++){
            if (choices[j]<4){
                if(choices[j]===1){
                    dictObject[survey[j][0]]+= 3
                } else if (choices[j]===2){
                    dictObject[survey[j][0]]+= 2
                } else if (choices[j]===3){
                    dictObject[survey[j][0]]+= 1
                }
                
            } else if (choices[j]>4){
                dictObject[survey[j][1]]+= choices[j]-4
                
            }
            
        }
    
    let answer = ""

    if( dictObject["R"] < dictObject["T"]){
        answer += "T"
    } else{
        answer += "R"
    }

    if( dictObject["C"] < dictObject["F"]){
        answer += "F"
    } else{
        answer += "C"
    }


    if( dictObject["J"] < dictObject["M"]){
        answer += "M"
    } else{
        answer += "J"
    }

    if( dictObject["A"] < dictObject["N"]){
        answer += "N"
    } else{
        answer += "A"
    }

    console.log(dictObject["R"])
    console.log(answer)
    console.log(dictObject)
    
    
}

survey = ["AN", "CF", "MJ", "RT", "NA"]	
choices = 	[5, 3, 2, 7, 5]

console.log(solution(survey,choices))