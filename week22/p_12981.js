
https://velog.io/@sso/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-Javascript-%EC%98%81%EC%96%B4-%EB%81%9D%EB%A7%90%EC%9E%87%EA%B8%B0
function solution(n, words) {
    var answer = [];
    var number = 0;
    var order = 0;

    for(var i=1; i<words.length; i++){
    // 끝말을 잇지 않은 경우   || 중복된 단어가 있는 경우
        var subArr = words.slice(0,i);
    	if((words[i-1].substring(words[i-1].length-1) !== words[i][0])|| (subArr.some(word=> word === words[i]))){
        if((i+1)%n ===0){
          number = n;
        }else{
         number = (i+1)%n ;
      	}
        order = Math.ceil((i+1)/n);
        break;
      }
    }
    if(number===0 && order===0){
        answer = [0,0];
    }else{
        answer = [number,order ];
    }
  
    return answer;
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