
function solution(n) {
    var answer = 0;
    if(n==0) return 0
    if(n==1) return 1
 
    if(n >1){
        let a =0
        let b = 1
        let temp
       for(i = 2; i<=87; i++){
        if (i >=80)  console.log(a,b,temp)
            temp = a+b
            a = b
            b = temp
       }

    }

}
console.log(solution(43))


// function solution(n) {
//     var answer = 0;
//     if(n==0) return 0
//     if(n==1) return 1
//     let a =0
//     let b = 1
//     let temp 
//     if(n >1){
//        for(i = 2 ; i<=n; i++){
//            temp = a+b
//            a = b
//            b = temp 
//        }
//         return (b % 1234567)
//     }

// }