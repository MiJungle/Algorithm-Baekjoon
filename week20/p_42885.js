
// 효율성 0
// function solution(people, limit) {
//     var answer = 0;    
//     people.sort((a,b)=> (b-a))
    
//     while(people.length){
//         let right = people.shift()
//         if(people.length===0){
//             answer += 1
//             return answer
//         }
//         else {
//             let left = people.pop()
//             if(right + left > limit){
//                 people.push(left)   
//             }

//             answer += 1
//         }
//     }
//     return answer;
// }