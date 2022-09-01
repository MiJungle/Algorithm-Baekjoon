function solution(n) {
    let new_n = n.toString(2)
    
    var count = [...new_n].filter(x => x === "1").length;

    for (let i = n+1; i<2*n ; i++){
        let n_count = [...i.toString(2)].filter(x=>x ==="1").length;
        if(n_count === count){
            return i
        }
    }

}