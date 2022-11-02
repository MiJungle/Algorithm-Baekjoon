function problem1(pobi, crong) {
    var answer;
    if(pobi[1]-pobi[0]!= 1 && crong[1]-crong[0] !=1 )return -1 
    if(pobi.length!=2 && crong.length!=2) return -1

    let p_sum1 = 0 
    let p_mul1 = 1
    let p_sum2 = 0
    let p_mul2 = 1
    for(let i= 0 ; i<String(pobi[0]).length ; i++){
        p_sum1 += Number(String(pobi[0])[i])
        p_mul1 *= Number(String(pobi[0])[i])
    }

    for(let i = 0; i <String(pobi[1]).length; i++){
        p_sum2 += Number(String(pobi[1])[i])
        p_mul2 *= Number(String(pobi[1])[i])
    }

    let p_sum = Math.max(p_sum1,p_sum2)
    let p_mul = Math.max(p_mul1, p_mul2)

    let pobi_num = Math.max(p_sum, p_mul)

    let c_sum1 = 0 
    let c_mul1 = 1
    let c_sum2 = 0
    let c_mul2 = 1
    for(let i= 0 ; i<String(crong[0]).length ; i++){
        c_sum1 += Number(String(crong[0])[i])
        c_mul1 *= Number(String(crong[0])[i])
    }
    for(let i = 0; i <String(crong[1]).length; i++){
        c_sum2 += Number(String(crong[1])[i])
        c_mul2 *= Number(String(crong[1])[i])
    }
    let c_sum = Math.max(c_sum1,c_sum2)
    let c_mul = Math.max(c_mul1, c_mul2)

    let crong_num = Math.max(c_sum, c_mul)

    if(pobi_num > crong_num) answer = 1
    else if(pobi_num < crong_num) answer = 2
    else if (pobi_num == crong_num) answer = 0
    return answer;
  }

  let a = 123
  
  pobi = [97,98]
  crong = [197,198]

  console.log(problem1(pobi, crong))
  module.exports = problem1;


//   describe("problem1", () => {
//     test("case1", () => {
//       expect(problem1([97, 98], [197, 198])).toEqual(0);
//     });
// 63 72
// 63 72
  
//     test("case2", () => {
//       expect(problem1([131, 132], [211, 212])).toEqual(1);
//     });
  
//     test("case3", () => {
//       expect(problem1([99, 102], [211, 212])).toEqual(-1);
//     });
//   });
  