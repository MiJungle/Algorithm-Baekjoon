// https://ashrock.kr/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98/%EC%BF%A0%ED%82%A4%EA%B5%AC%EC%9E%85/
function solution(cookie) {
    const n = cookie.length;
    let answer = 0;
    
    for (let l=0; l<n-1; l++){
        let m = l;
        let r = l+1;
        let big = cookie[m];
        let small = cookie[r];
        while (m < n && r < n){
            if (big === small) answer = Math.max(answer, big);
            if (big <= small){
                m++;
                if (m < n){
                    big += cookie[m];
                    small -= cookie[m];
                }
                if (m === r){
                    r++;
                    if (r < n) small += cookie[r];
                }
            }
            else if (big > small){
                r++;
                if (r < n) small += cookie[r];
            }
        }
    }
    
    return answer;
}



function solution(cookie) {
    let total = sum(cookie)
    let mid = parseInt(total/2)

    let pointer1 = 0,
        pointer2
    
    while(mid != 0){
        let sum1 = 0
        let sum2 = 0
        
        for(let i = pointer1; i < cookie.length; i++){
            if(sum1 === mid && i+1 != cookie.length) {
                pointer2 = i+1 
                break
            }
            sum1 += cookie[i]
        }
        for (let i = pointer2 ; i< cookie.length; i++){
            if(sum2 === mid) return mid
            else {
                sum2 += cookie[i]
            }
        }
        
        mid -= 1
    }
    
    return 0
    
}
const sum = (arr) => arr.reduce((accum, value)=>{return accum+value},0)
//쿠키 개수 커지게 할 조건?
//0부터 차례대로 더해, 3이 된 순간 -> 그 index부터 더해, 
// for i - 3되었을 때, 그 index로 설정해주고
//그 index부터 더해줌, 3이 되면 출력,
//아닌 경우 mid 를 -1
// 다더해서 mid 값을 구해 3 될때까지, 
//leftpointer 0 계속 더해나가 3이될때까지,되면
// right pointer = 그 인덱스 + 1부터 계속 더해나가 //3이되면 return
//안되면 mid값을 줄여
