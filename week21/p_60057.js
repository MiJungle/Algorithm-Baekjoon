function solution(s) {  
    let answer = s;  
    const HALF = s.length/2;   
    for (let i = 1; i <= HALF; i++) {    
        let slice = s.slice(0, i);    
        let count = 1;     
        const str = compare(s, i, slice, count);     
        if (answer.length > str.length) {      
            answer = str;    }  
        }   return answer.length;} 
        
        
function compare(s, i, slice, count) {  
    let temp = '';   
    for (let j = i; j < s.length; j += i) {
            const target = s.slice(j, j + i);     
            if (slice === target) {      
                count++;    } 
            else {      count === 1 ? (temp += slice) : (temp += count + slice);      
                slice = target;      
                count = 1;    }  }   
    count === 1 ? (temp += slice) : (temp += count + slice);  
    return temp;
    }

















//초기 접근
//몇개씩 반복되는지는 찾았지만
// 반복되는 문자열을 숫자로 어떻게 처리해야할지를 모르곘음

// function solution(s) {
//     var answer = 0;
//     let len = s.length
//     let mid = parseInt(0+len/2)

//     while (mid != 0){
//         let s1 = s.slice(0,mid)
//         let s2 = s.slice(mid,s.length)
//         if (s1.length ===1) {return len}
//         else {
//             mid = parseInt(mid/2)
//             s = s1
//         }
//         }
//     return answer;
// }
//몇개씩 반복되는지를 찾는다
//
// 반복횟수만큼 압축시킨 문자의 길이를 출력한다
