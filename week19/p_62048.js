
function solution(w, h) {
    
    function gcd(w,h){
        a= Math.max(w,h)
        b = Math.min(w,h)
        while(a){
            r= a% b
            if (r ===0){
                return b
            }else {
                a = b
                b = r
            }
        }
        
    }
    let answer = (w*h) -(w+h-gcd(w,h) )
    return answer;
}