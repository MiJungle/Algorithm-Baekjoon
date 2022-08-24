function solution(people, limit) {
    let answer=0;
    people.sort((a,b)=>b-a);
    let peopleCnt=people.length;
    for(let i=0;i<peopleCnt;i++){
        if(people[i]+people[peopleCnt-1]<=limit){
            peopleCnt--;
        }
        answer++;
    }
    return answer;
}

// function solution(n) {
//     let answer = []
//     while(n){
//         if (n%3){
//             answer.push( n%3)
//             n= parseInt(n/3)
//         } else{
//             answer.push(4)
//             n = parseInt(n/3) -1
//         }
//     }
//     let final = answer.reverse().join("")
//     return final

// }