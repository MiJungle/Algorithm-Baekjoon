//https://velog.io/@longroadhome/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-LV.3-%EA%B0%80%EC%9E%A5-%EA%B8%B4-%ED%8C%B0%EB%A6%B0%EB%93%9C%EB%A1%AC-JS


function solution(s) {
    let answer = 1;
    const len = s.length;
    const dp = new Array(len).fill().map(_ => new Array(len).fill(false));
    
    for(let i = 0; i < len; i++) {
      dp[i][i] = true;
    }
    
    for(let i = 0; i < len - 1; i++) {
      if(s[i] === s[i+1]) {
        dp[i][i+1] = true;
        answer = 2;
      }
    }
    
    for(let i = 3; i <= len; i++) {
      for(let start = 0; start <= len - i; start++) {
        const end = start + i - 1;
        if(s[start] === s[end] && dp[start+1][end-1]) {
          dp[start][end] = true;
          answer = Math.max(answer, i);
        }
      }
    }
    
    return answer;
  }
  //초기 접근

function solution(s)
{
    var answer = 0;

    for (let i= 0; i<s.length; i++){
        for(let j = i+1; j<s.length-1;j++){
            let len = parseInt((j-i)/2) +1
            let front, back
            if(len %2 ===0) {//숫자개수가 짝수
                 front = [...s].slice(i,i+len/2+1)
                 back = [...s].slice(i+len/2+1, j+1)
            }
            else {
             front = [...s].slice(i, i+len/2)
             back = [...s].slice(i+len/2, j+1)
            }
            console.log(front, back)
            if (front.join('')== back.reverse().join('')){
                answer = Math.max(answer, front.join('').length)
            }
        }
    }
    
}

//투포인터? 
// 01 02 03 04 05 0 ~ 
// 12 13 14 15 16 
// 23 24 25 26 
// 뒤집은 배열이랑 앞 배열이랑 같으면, max 값으로 갱신