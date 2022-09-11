function solution(n) {
    let ans = 0;
  
    const DFS = (open, close) => {
      if (open + close === n * 2) {
        if (open === n && close === n) ans++;
        return;
      }
      if (open > close) {
        DFS(open, close + 1);
      }
      DFS(open + 1, close);
      return;
    };
  
    DFS(0, 0);
    return ans;
  }