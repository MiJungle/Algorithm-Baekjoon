function solution(n, money) {
    let dp=[1].concat(Array(n).fill(0));
    money.forEach(v=>{
        dp[v]+=1;
        for(let i=v+1;i<=n;i++){
            dp[i]+=dp[i-v];
        }
    })
    return dp[n];
}
//dp fibonacci?//배낭문제 
// money [1,2,5]
// n = 1 1가지
// n = 2 1, 1/ 1 : 2가지
// n = 3 1 1 1 / 1 2 : 2가지
// n = 4 1 1 1 1 / 2 2 / 1 1 2 : 3가지
// n = 5 1 1 1 1 1 / 1 1 1 2/ 1 2 2 / 5 : 3가지 

