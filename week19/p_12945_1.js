function solution(n) {
    let memo = [0,1];
      for(let i = 2; i <=n; i++){
          memo[i] = (memo[i-2]+memo[i-1])
      }
      return memo[n]%1234567;
  }

  console.log(solution(5))