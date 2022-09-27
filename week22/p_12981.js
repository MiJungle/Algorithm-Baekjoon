
function solution(n, words) {
    let idx;
    for (let i = 0; i < words.length; i++) {
      // 끝말잇기 틀린 경우
      if (i !== 0 && words[i][0] !== words[i - 1][words[i - 1].length - 1]) {
        idx = i + 1;
        return [idx % n === 0 ? n : idx % n, Math.ceil(idx / n)];
      }
      // 중복 단어 말한 경우
      for (let j = i - 1; j >= 0; j--) {
        if (words[i] === words[j]) {
          idx = i + 1;
          return [idx % n === 0 ? n : idx % n, Math.ceil(idx / n)];
        }
      }
    }
    return [0, 0];
  }
  



function solution(n, words) {
    var answer = [];
    let allround = []
    let total = words.length
    for(let i = 1 ; i <= Math.ceil(total/n); i++){
        let round = words.slice(3*(i-1), 3*(i-1)+n)
        let end = round[0][round[0].length-1]
        for(let k = 0; i<round.length; k++){
            if (allround.includes(round[k])){
                answer=[i*k + n,i]
            }
        }
        for(let j = 1; j < round.length; j++){
            if(round[j][0]===end){
                end = round[j][round[j].length-1]
            }else {
                answer=[j,i]
            }
        
        } 
        allround = [...allround, ...round]
    
    }
    

    return answer;
}
//n씩 잘라서, 문자 앞뒤를 확인?
//slice 해서 [...복사하고]
// [n-1]을 end에 담고, 그게 [0]이랑 같은지 계속 갱신하면서 확인
// 