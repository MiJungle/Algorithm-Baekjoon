function solution(n){
    let bin_n = n.toString(2)
    let count_one = bin_n.split('').filter(n=> n==='1').length
    let target = n +1
    
    while(target > n){
        if(count_one === target.toString(2).split('').filter(n=> n==='1').length) return target
        else target += 1
    }

    return target
}


