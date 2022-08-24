numbers = [5, 0, 2, 7]
function solution(numbers) {
    var answer = [];
    for (let i=0 ; i <numbers.length ;i++){
        for (let j=0 ; j <numbers.length ;j++){
            if(j!==i){
                let sum = numbers[i] + numbers[j]
                answer.push(sum)

            }
    }  

}
    let new_answer = new Set(answer)
    new_answer = [...new_answer]
    new_answer.sort(function(a,b){
        return a-b;
    })
    return new_answer 
}

console.log(solution(numbers))