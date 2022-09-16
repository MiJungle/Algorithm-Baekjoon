
//초기 접근 //무지의 먹방 라이브 42891 와 비슷하다고 생각도 듬


function solution(stones, k) {
    var answer = 0;
    
    while(true){
        for(let i = 0 ; i<stones.length; i++){
            if(stones [i]>0){
                stones[i]-= 1
            }else if(
    (stones[i-1]==0 && stones[i]==0 && stones[i+1]==0) ||
    (stones[i-2]==0 && stones[i-1]==0 && stones[i]==0) ||
    (stones[i]==0 && stones[i+1]==0 && stones[i+2]==0)) 
            {
            return answer}
           } answer += 1
    }
}
    
    
///[2,4,5,3,2,1,4,2,5,1] 1
//[1,3,4,2,1,0,3,1,4,1] 2
//[0,2,3,1,0,0,2,0,3,0] 3
//[0,1,2,0,0,0,1,0,2,0]
//가장 min 숫자가 0 이되고나서, 까지 모두가 돌수 있음
// 연속해서 0 이 세개 나오면 안됨. 
// 0이된걸 기준으로 -1 -2 index 도 0 이거나 
// -1 +1 index도 0 이거나
// +1 +2 index도 0 인 경우 그 다음사람이 못 건너게됨. 