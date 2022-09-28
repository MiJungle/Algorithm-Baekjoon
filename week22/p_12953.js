function LCM(m, n) {
    let lcm = m * n;
    while (m % n) [m, n] = [n, m % n];
    return lcm / n;
  }
   
  function solution(arr) {
    let lcm = LCM(arr[0], arr[1]);
    for (let i = 2; i < arr.length; i++) lcm = LCM(lcm, arr[i]);
    return lcm;
  }
  //1 2 / 1 2 3 6/  1 2 4 8 / 1 2 7 14 
  // 1 2 / 2 3 / 2 *3 / 2 7 
  // 2*3 3 7 

