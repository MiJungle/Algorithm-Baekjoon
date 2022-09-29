function solution(n) {
    var answer = 0;
    let arr = [1,2]
    
    for(i=2; i<n ; i++){
        let a = arr[i-2]
        let b = arr[i-1]
        let c = (a+b)%1000000007
        arr.push(c)
    }    
    return arr[n-1]
    
}