
function solution(s) {
    if(s.length != 4 && s.length != 6) return false;
    for(var i = 0; i < s.length; i++) {
        if(isNaN(s[i])) return false;
    }
    return true;
}


function solution(s) {

    return ((s.length ===4 || s.length===6) && isNaN(s)==false)? true:false;
    
    
}



// isNaN 을 통해 숫자 판별 가능
//두번쨰꺼는 11테케에서 걸림
// function solution(s) {
//     let num = ["0","1", "2","3","4", "5", "6", "7", "8", "9"]
//     var answer = true;
//     let len = s.length
//     let isnum = true
    
//     for (let i = 0; i <s.length ; i++){
//         if ( !(s[i] in num)){
//             isnum = false
//         }
//     }
//     if ((len === 4 || len === 6) && isnum === true){
//     return true}else {
//         return false
//     }
    
// }