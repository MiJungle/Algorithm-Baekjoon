// describe("problem2", () => {
//     test("case1", () => {
//       expect(problem2("browoanoommnaon")).toEqual("brown");
//     });
//     test("case2", () => {
//       expect(problem2("zyelleyz")).toEqual("");
//     });
//   });


function problem2(cryptogram) {
    var answer=""
    let word = cryptogram
    while(true){
      let first = 0
      let second = first + 1
      for(let i =0 ; i< word.length+1; i++){
        if(word[first]==word[second]){
          first += 2
          second = first + 1
          continue
        }
        answer += word[first]
        first += 1
        second = first + 1
      }
      if(word === answer) break
      word = answer
      answer = "" 
    }
    return answer;
  }
  
  module.exports = problem2;
  cryptogram = "browoanoommnaon"

  console.log(problem2(cryptogram))