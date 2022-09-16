//초기 접근 방법
// A[6,4,3,2] B[6,3,3,2] -> 0 
// 0 -1 0 0 / 0 -1 0 1 
// 6 2 3 3
//숫자중 크거나 같은 숫자가 있으면 그걸 넣고,
// 숫자가 작은경우, 가장 작은 숫자를 넣고
// 반복 


function solution (A, B) {
    let answer = 0;
    
    A.sort((a,b) => b-a); //[7,5,3,1]
    B.sort((a,b) => a-b); //[2,2,6,8]
    
    for(const a of A) {
      const max = B[B.length - 1];
      if(a < max) {
        answer++;
        B.pop();
      }
    }
    
    return answer;
  }


// function solution(A, B) {
//     var answer = 0;
//     A.sort((a,b)=> (b-a))
//     B.sort((a,b)=> (b-a))
//     let arr = []
    
//     for (let i =0; i <B.length ; i++){
//         if(A[i]> B[i]) {
//             let k = B[B.length-1]
//             let m = B[i]
//             B.splice(i,1,k)
//             B.splice(B.length-1,1,m)
//         }
    
//     }
//     for(let i = 0 ; i <B.length; i++){
//         if (A[i]<B[i]) answer += 1
//     }
    
//     return answer;
// }

