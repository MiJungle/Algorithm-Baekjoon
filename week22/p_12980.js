
// 채점 결과
// 정확성: 60.0
// 효율성: 40.0
// 합계: 100.0 / 100.0

function solution(n)
{
    var ans = 1;

   while(n!= 1){
       if(n%2==0) n = n/2
       else {
           n = n -1
           ans += 1 }
   }

    return ans;
}