https://velog.io/@longroadhome/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-LV.4-%EB%8B%A8%EC%96%B4-%ED%8D%BC%EC%A6%90
//이전에 사용한 패턴을 재사용한다
// b : b
// ba : b/a 또는 ba
// ban : b/a/n 또는 ba/n 또는 ban
// bana : b/a/n/a 또는 ba/n/a 또는 bana

//점화식은 어떻게 도출하는가?



function solution (strs, t) {
    const n = t.length;
    const dp = new Array(n).fill(Infinity);
    
    for(let i = 0; i < n; i++) {
      const current = t.substr(0, i+1);
      
      for(const str of strs) {
        if (current.endsWith(str)) {
          const diff = current.length - str.length;
          
          if (!diff) {
            dp[i] = 1;
          } else {
            dp[i] = Math.min(dp[i], dp[diff-1] + 1);
          }
        }
      }
    }
    return dp[n-1] === Infinity ? -1 : dp[n-1];
  }