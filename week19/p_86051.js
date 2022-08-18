function solution(numbers){
    let answer = 0
    let exist = 0
    for (let i = 0; i <= 9 ; i++){
        for (let j = 0; j < numbers.length ; j++){
            if (i===numbers[j]){
                exist = 1
            }
        }
        if(exist === 0){
            answer += i
        }
        exist = 0
    }
return answer

}

numbers = [1,2,3,4,6,7,8,0]	
console.log(solution(numbers))