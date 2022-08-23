stages = [2, 1, 2, 6, 2, 4, 3, 3]	
N = 5

function solution(N,stages){
    let divide = []
    let count = 0

    for (let i = 1; i<=N; i++){
        for (let j = 0; j<stages.length; j++){
            if (stages[j]>= i){
                count += 1
            }

        }
        divide.push([stages.filter(x=>x==i).length / count,i])
        count = 0

    }
divide.sort((a,b)=>{return b[0]-a[0]})

let answer = []
for(let i = 0; i<divide.length; i++){
    answer.push(divide[i][1])
}



return answer
}

console.log(solution(N,stages))