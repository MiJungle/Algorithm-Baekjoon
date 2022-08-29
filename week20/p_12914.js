function solution(n) {
    var answer = 0;
    if(n ==1) return 1
    else if (n==2) return 2
    
    let prev =1
    let next = 2
    let temp = prev
    let result = [1,2]
    for (let i =3; i<=n; i ++){
        prev = next
        next = (temp + next)%1234567
        temp = prev

    }
    
    return next
}
