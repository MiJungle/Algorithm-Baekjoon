describe("problem6", () => {
    test("case1", () => {
      expect(
        problem6([
          ["jm@email.com", "제이엠"],
          ["jason@email.com", "제이슨"],
          ["woniee@email.com", "워니"],
          ["mj@email.com", "엠제이"],
          ["nowm@email.com", "이제엠"],
        ])
      ).toEqual(["jason@email.com", "jm@email.com", "mj@email.com"]);
    });
  });
  


function problem6(forms) {
    var answer;
    return answer;
  }
  

  forms = [ ["jm@email.com", "제이엠"], 
        ["jason@email.com", "제이슨"], 
        ["woniee@email.com", "워니"], 
        ["mj@email.com", "엠제이"], 
        ["nowm@email.com", "이제엠"] ]

  module.exports = problem6;

  console.log(problem6(forms))