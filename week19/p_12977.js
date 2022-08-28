function solution(nums) {

    const result = getCombinations(nums, 3);
    let sum = []
    for (let i = 0; i< result.length; i++){
    let ret = result[i].reduce((a, b) => a + b, 0);
        sum.push(ret)
    }
    let answer = sum.length

    for (let i = 0; i < sum.length; i++){
        for(let j = 2; j<=Math.sqrt(sum[i]);j++){
            if(sum[i]%j===0 && sum[i]/j!=1){
            answer-=1 ;
            break;
        }
    }
    }
    return answer

}   
    const getCombinations = function (arr, selectNumber) {
      const results = [];
      if (selectNumber === 1) return arr.map((value) => [value]); 
      arr.forEach((fixed, index, origin) => {
        const rest = origin.slice(index + 1);
        const combinations = getCombinations(rest, selectNumber - 1);
        const attached = combinations.map((combination) => [fixed, ...combination]); 
        results.push(...attached); 
      });
    
      return results; 
    }