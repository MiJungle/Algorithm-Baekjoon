function gcd(n,m){
    let a = Math.max(n,m) 
    let b = Math.min(n,m)
    let r = a%b
    while (a){
        r = a%b
        if (r ==0){
            return b
        } else{
                a = b
                b = r
            }
        }        
    }
    

function solution(n, m) {
    let gcnum = gcd(n,m)
    let answer = [gcnum, (n*m)/gcnum]
    return answer

}
n= 2
m= 5
console.log(solution(n,m))