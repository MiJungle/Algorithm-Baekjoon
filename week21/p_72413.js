//다익스트라인 것은 맞춤
// https://school.programmers.co.kr/learn/courses/30/lessons/72413

function solution(n, s, a, b, fares) {
    //지점 크기만큼 2차원 배열 및 자기자신 0으로 변경
    let pathMap = Array.from(Array(n), () => new Array(n).fill(Infinity));
    pathMap = pathMap.map((item, index) => {
      let temp = [...item];
      temp[index] = 0;
      return temp;
    });
  
    // 요금 채우기
    fares.forEach(([from, to, fee]) => {
      pathMap[from - 1][to - 1] = fee;
      pathMap[to - 1][from - 1] = fee;
    });
  
    //플루이드 와셜 알고리즘, 모든 경로 최소값 찾기
    for (let k = 0; k < n; k++) {
      for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
          pathMap[i][j] = Math.min(pathMap[i][j], pathMap[i][k] + pathMap[k][j]);
        }
      }
    }
  
    //합승 최소 요금 찾기
    let answer = Infinity;
    for (let i = 0; i < n; i++) {
      answer = Math.min(answer, pathMap[s - 1][i] + pathMap[a - 1][i] + pathMap[b - 1][i]);
      console.log(pathMap[s - 1][i] + pathMap[a - 1][i] + pathMap[b - 1][i]);
    }
  
    return answer;
  }
  