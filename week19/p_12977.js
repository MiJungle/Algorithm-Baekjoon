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
      if (selectNumber === 1) return arr.map((value) => [value]); // 1개씩 택할 때, 바로 모든 배열의 원소 return
    
      arr.forEach((fixed, index, origin) => {
        const rest = origin.slice(index + 1); // 해당하는 fixed를 제외한 나머지 뒤
        const combinations = getCombinations(rest, selectNumber - 1); // 나머지에 대해서 조합을 구한다.
        const attached = combinations.map((combination) => [fixed, ...combination]); //  돌아온 조합에 떼 놓은(fixed) 값 붙이기
        results.push(...attached); // 배열 spread syntax 로 모두다 push
      });
    
      return results; // 결과 담긴 results return
    }

    nums = [1,2,3,4]	
    console.log(solution(nums))