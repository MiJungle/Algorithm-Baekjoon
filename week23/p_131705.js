function solution(number) {
    var answer = 0;
    let combo = func(number,3)
    combo.forEach((arr)=> {
        let sum = arr.reduce(function(a, b){
            return a + b;}, 0);
        
        if(sum=== 0 ) answer += 1
    })
    return answer
}

//sort를 해 3개 combination으로 뽑고 그걸 sum 이 0 이면 answer += 1

const func = function(arr, selectNumber) {
  const results = [];
  
  if(selectNumber === 1) return arr.map((el) => [el]);
  
  arr.forEach((fixed, index, arr) => {
    const new_arr = arr.slice(index+1)
    const combination = func(new_arr, selectNumber -1);
    
    const attached = combination.map((el) => [fixed, ...el]);
    results.push(...attached);
  });
  return results
};

    