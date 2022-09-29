function solution(arr1, arr2) {
    let answer = [];
    
    for(let i = 0; i < arr1.length; i++) {
      answer.push([]);
      for(let j = 0; j < arr2[0].length; j++) {
        let sum = 0;
        for(let n = 0; n < arr2.length; n++) {
          sum += (arr1[i][n] * arr2[n][j]);
        }
        answer[i].push(sum);
      }
    }
    return answer;
  }
  
  // 14  33
  // 32  33
  // 41
  
  // 3*2 2*2 3*2
  // [arr1[0][0]*arr2[0][0] + arr1[0][1]*arr2[1][0]]
  //[arr1[0][0]*arr2[0][1] + arr1[0][1]*arr2[1][1]]
  
  //[arr1[1][0]*arr2[0][0] + arr1[0][1]*arr2[1][0]]
  //[arr1[0][0]*arr2[0][1] + arr1[0][1]*arr2[1][1]]