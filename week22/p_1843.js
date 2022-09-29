https://velog.io/@longroadhome/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-LV.4-%EC%82%AC%EC%B9%99%EC%97%B0%EC%82%B0
function solution (arr) {
    const operandsCount = Math.ceil(arr.length / 2);
    const max_dp = new Array(operandsCount).fill().map(_ => new Array(operandsCount).fill(-Infinity));
    const min_dp = new Array(operandsCount).fill().map(_ => new Array(operandsCount).fill(Infinity));
    
    for(let i = 0; i < operandsCount; i++) {
      max_dp[i][i] = +arr[i*2];
      min_dp[i][i] = +arr[i*2];
    }
    
    for(let cnt = 1; cnt < operandsCount; cnt++) {
      for(let i = 0; i < operandsCount - cnt; i++) {
        const j = i + cnt;
        for(let k = i; k < j; k++) {
          if (arr[k*2+1] === '+') {
            max_dp[i][j] = Math.max(max_dp[i][j], max_dp[i][k] + max_dp[k+1][j]);
            min_dp[i][j] = Math.min(min_dp[i][j], min_dp[i][k] + min_dp[k+1][j]);
          } else {
            max_dp[i][j] = Math.max(max_dp[i][j], max_dp[i][k] - min_dp[k+1][j]);
            min_dp[i][j] = Math.min(min_dp[i][j], min_dp[i][k] - max_dp[k+1][j]);
          }
        }
      }
    }
    
    return max_dp[0][operandsCount-1];
  }
  //어떻게 dp로 풀것인가?
  //점화식 
  // dp[i] = dp[i-1] + ~
  //dp[i]= dp[i-1]- ~