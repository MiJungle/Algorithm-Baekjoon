https://haerang94.tistory.com/327

//초기 접근 방법
// function solution(n, costs) {
//     var answer = 0;
//     costs.sort((a,b)=> a[2]-b[2])
//     console.log(costs)
//     let island = []
    
//     for(let i =0; i <n ; i++){
//         if(island.includes(costs[i][0])===false || island.includes(costs[i][1])===false){
//             island.push(costs[i][0])
//             island.push(costs[i][1])
//             answer += costs[i][2]
//         }
//     }
//     return answer;
// }