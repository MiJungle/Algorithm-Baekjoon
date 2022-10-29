// describe("problem7", () => {
//     test("case1", () => {
//       expect(
//         problem7(
//           "mrko",
//           [
//             ["donut", "andole"],
//             ["donut", "jun"],
//             ["donut", "mrko"],
//             ["shakevan", "andole"],
//             ["shakevan", "jun"],
//             ["shakevan", "mrko"],
//           ],
//           ["bedi", "bedi", "donut", "bedi", "shakevan"]
//         )
//       ).toEqual(["andole", "jun", "bedi"]);
//     });
//   });

function problem7(user, friends, visitors) {
    var answer= []
    let user_friend = []
    let scores = {}

    friends.forEach((friend)=> {
        scores[friend[0]]= 0
        scores[friend[1]]= 0
        if( friend.includes(user)){
            let i = friend.indexOf(user)
            user_friend.push(friend[1-i])
        }
    })
    friends.forEach((friend)=> {
        user_friend.forEach((mutual)=> {
            if(friend.includes(mutual)){
                let i = friend.indexOf(mutual)
                if(friend[1-i]!= user) scores[friend[1-i]] += 10
            }
        })
    })

    visitors.forEach((visitor)=> {
        console.log(visitor)
        scores[visitor] = (scores[visitor]||0) + 1
    })

var sortable = [];
for (var name in scores) {
  sortable.push([name, scores[name]]);
}
// A.sort((a,b)=> b[0]-a[0]||a[1]-b[1])
// console.log(A)
// sortable.sort((a,b)=> a[0]-b[0])
sortable.sort((a,b)=> {return a[0] === b[0]? 0: a[0]<b[0]?-1:1;})
sortable.sort((a,b)=> b[1]-a[1])

for (let i =0 ; i <5; i++){
    answer.push(sortable[i][0])
}
// console.log(scores)
console.log("sort",sortable)
    //let user friend = []
    //name = {
        // andole: 0
        // donut, 0
        // jun, 0]
    // }
    //friends 중 mrko 를 includes 한다면, 그 이름을 배열에 담는다. 
    // 다른 반복문에서 user friend있는 친구의 점수를 10점씩 더해주고
    /// visitors 점수들도 1점씩 더해주고
    // 점수순, 이름 알파벳 순으로 나열해서 출력한다. 
    return answer;
  }
  
user = "mrko"
friends = [ 
    ["donut", "andole"], 
    ["donut", "jun"], 
    ["donut", "mrko"], 
    ["shakevan", "andole"], 
    ["shakevan", "jun"], 
    ["shakevan", "mrko"] ]

visitors= ["bedi", "bedi", "donut", "bedi", "shakevan"]
console.log(problem7(user, friends, visitors))
module.exports = problem7;