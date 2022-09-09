function solution(queue1, queue2) {
    let count = 0
    let sum1, sum2, totalsum
   
    for(let i = 0; i < queue1.length*4; i++){
     sum1 = queue1.reduce((accumulator, value) => {
  return accumulator + value;
    }, 0);
    
     sum2 = queue2.reduce((accumulator, value) => {
  return accumulator + value;
    }, 0);
    
     totalsum = (sum1 + sum2)
    
    if(totalsum % 2!=0) return -1
    else if(sum1 ===totalsum/2 ) return count

        
    else if(sum1 > totalsum/2 ){
       let k = queue1.shift()
       queue2.push(k)
        count += 1
        console.log(queue1,queue2)
    }
    else {
        let m = queue2.shift()
        queue1.push(m)
        count += 1
    }
        
    sum1 = queue1.reduce((accumulator, value) => {
  return accumulator + value;
    }, 0);
    
     sum2 = queue2.reduce((accumulator, value) => {
  return accumulator + value;
    }, 0);
    }
        
    console.log(sum1,totalsum)
    return sum1 ===totalsum/2? count : -1