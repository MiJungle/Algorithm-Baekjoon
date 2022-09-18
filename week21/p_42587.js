

 

const solution = (priorities, location) => {
    let counter = 0;
    const mapped = priorities.map((num, index) => {
      if (index === location) return [num, true];
      return [num, false];
    });
  
    while (mapped.length > 0) {
      const cur = mapped.shift();
      if (mapped.some((num) => num[0] > cur[0])) {
        mapped.push(cur);
      } else {
        counter++;
        if (cur[1]) return counter;
      }
    }
  };


//초기

function solution(priorities, location) {
    var answer = 0;
    
    let locnum = priorities[location]
    let indexnum = location
    for (priority of priorities){
        if (Math.max(...priorities) !== priority) {
            let k = priorities.shift() 
            priorities.push(k)
        }
        else {
            priorities.shift()
            answer += 1
        }
        
    }
    return answer
}