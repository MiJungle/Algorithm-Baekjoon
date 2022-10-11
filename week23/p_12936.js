
function solution(n, k) {
    const answer = [];
    const people = Array.from({ length: n }, (_, i) => i + 1);
    let caseNum = people.reduce((ac, v) => ac * v, 1)
    
    while (answer.length < n) {
        caseNum = caseNum / people.length;
        answer.push(...people.splice(Math.floor((k - 1) / caseNum), 1));
        k = k % caseNum;
    }

    return answer;
}

function solution(n, k) {
    var answer 
    let num = []
    for (let i = 1; i <= n ; i++) num.push(i)
    
    var permute = function(nums,k){
    var result = [];
    var backtrack = (i, nums) => {
      if(i===nums.length){
        result.push(nums.slice());
        return;
      }  
      for(let j = i; j < nums.length; j++){
        [nums[i],nums[j]] = [nums[j],nums[i]];
        backtrack(i+1, nums);
        [nums[i],nums[j]] = [nums[j],nums[i]];
      }
    }
    backtrack(0, nums);
    answer = result

  };
  permute(num,k);
  return (answer[k-1])
    // return answer;
}

