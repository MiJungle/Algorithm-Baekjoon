// describe("problem5", () => {
//     test("case1", () => {
//       expect(problem5(50237)).toEqual([1, 0, 0, 0, 0, 2, 0, 3, 7]);
//     });
  
//     test("case2", () => {
//       expect(problem5(15000)).toEqual([0, 1, 1, 0, 0, 0, 0, 0, 0]);
//     });
//   });




function problem5(money) {
    var answer=[]
    let type = [50000,10000,5000,1000,500,100,50,10,1]
    let new_money = money

    for(let i = 0 ; i < 10; i++){
        if(new_money >= type[i]){
            answer.push (Math.floor(new_money/type[i]))
        }
        else if(new_money < type[i]){
            answer.push (0)
        }
        new_money = new_money - type[i]*answer[i]

    }

    return answer;
  }
  
  module.exports = problem5;
  money = 15000
console.log(problem5(money))

