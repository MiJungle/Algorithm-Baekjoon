//https://velog.io/@longroadhome/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-LV.4-%EC%A7%80%ED%98%95-%ED%8E%B8%EC%A7%91
function solution (land, P, Q) {
    const blocks = land.flat().sort((a,b) => a-b);
    const total = blocks.reduce((a,b) => a+b);
    
    let floor = -1;
    let prev = 0;
    let answer = Infinity;
    
    for (let i = 0; i < blocks.length; i++) {
      if (floor !== blocks[i]) {
        floor = blocks[i];
        
        const willBeAddedCount = blocks[i]*i - prev;
        const willBeDeletedCount = total - prev - (blocks.length-i)*blocks[i];
        const result = willBeAddedCount*P + willBeDeletedCount*Q;
        
        if (answer > result) answer = result;
      }
      
      prev += blocks[i];
    }
    
    return answer;
  }



// 채점 결과
// 정확성: 45.3
// 효율성: 0.0
// 합계: 45.3 / 100.0

function solution(land, P, Q) {
    var answer = 2e9;
    let height = -2e9
    for(let l of land){
        for (let i = 0; i < l.length; i++){
            height = Math.max(height, l[i])
        }
    }
    while(height >0 ){
        let cost = 0
        for(let l of land){
            l.filter(a=> a > height).forEach(a => {
                cost += (a-height)*Q
            })
            l.filter(a=> a < height).forEach(a => {
                cost += (height-a)*P
            })     
        }
    answer = Math.min(cost, answer)
    height -= 1

    }
    return answer;
}
//이분탐색? 나무자르기같은 느낌
//나무 길이들의 평균값을 mid로 놓고
//그거보다 크면 자르고 , 작으면 늘리고
// 그냥 큰 숫자부터???