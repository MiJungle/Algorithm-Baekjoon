// describe("problem6", () => {
//     test("case1", () => {
//       expect(
//         problem6([
//           ["jm@email.com", "제이엠"],
//           ["jason@email.com", "제이슨"],
//           ["woniee@email.com", "워니"],
//           ["mj@email.com", "엠제이"],
//           ["nowm@email.com", "이제엠"],
//         ])
//       ).toEqual(["jason@email.com", "jm@email.com", "mj@email.com"]);
//     });
//   });
  


function problem6(forms) {
    var answer= []

    forms.forEach((form1)=> {
        for(let i =0 ; i < form1[1].length-1; i++){
        let two_letter = form1[1][i] + form1[1][i+1]
        forms.forEach((form2)=> {
            if(form2[1].includes(two_letter)&& forms.indexOf(form1)!= forms.indexOf(form2)){
                if(!answer.includes(form1[0])) answer.push(form1[0])
            }
        })
    }

    })

    answer.sort((a, b) => a.localeCompare(b));
    return answer;
  }
  

  forms = [ ["Bm@email.com", "제이엠오"], 
        ["ason@email.com", "제이슨"], 
        ["woniee@email.com", "워니"], 
        ["mj@email.com", "엠제이"], 
        ["nowm@email.com", "이제엠"] ]

  module.exports = problem6;

  console.log(problem6(forms))
