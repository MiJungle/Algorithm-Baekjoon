function solution(s) {
    var answer = [];
    let zerocount = 0
    let count = 0
    let new_s, bin
    while(s!="1"){
        [...s].forEach (char => {
        if(char =="0") zerocount +=1})
        new_s = s.replaceAll("0",'').length
        bin = new_s.toString(2)
        s = bin
        count += 1

    }
 return [count, zerocount]
    
}

