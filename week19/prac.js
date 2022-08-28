let array = [[1,2,3]]

console.log(array)


let runners = new Map();
for (let i=0;i <3 ; i++){
    runners.set("p", (runners.get("p")||0)+1);

}
console.log(runners.get("p"))

console.log(runners)




v = [1,2,3,4,5]

result = v.reduce((acc, cur, i) => {
    console.log(acc, cur, i);
    return acc + cur;
  }, v[2]);


console.log(result)


let sum
for (let i =2; i<=v.length; i++){
sum = v.reduce((a,b)=>(a[i]+b))

}

console.log("sum======",sum)



let nums = new Map()
for (let i =0 ; i <v.length; i++){
    nums.set(i, v[i])
}

nums.set(2,8)
console.log(nums)

// 테스트
// 테스트 1 〉 통과 (3.37ms, 33.2MB)
// 테스트 2 〉 통과 (3.22ms, 32.9MB)
// 테스트 3 〉 통과 (0.67ms, 30.3MB)
// 테스트 4 〉 통과 (0.62ms, 30.3MB)
// 테스트 5 〉 통과 (0.67ms, 30.6MB)
// 테스트 6 〉 통과 (0.66ms, 30.5MB)
// 테스트 7 〉 통과 (0.62ms, 30.6MB)
// 테스트 8 〉 통과 (4.32ms, 35.5MB)
// 테스트 9 〉 통과 (4.28ms, 35.4MB)
// 테스트 10 〉 통과 (4.27ms, 35.4MB)
// 테스트 11 〉 통과 (4.49ms, 35.7MB)
// 테스트 12 〉 통과 (4.34ms, 35.4MB)


// 테스트 1 〉 통과 (4.95ms, 33.4MB)
// 테스트 2 〉 통과 (1.04ms, 30.5MB)
// 테스트 3 〉 통과 (1.07ms, 30.5MB)
// 테스트 4 〉 통과 (0.87ms, 30.6MB)
// 테스트 5 〉 통과 (0.93ms, 30.6MB)
// 테스트 6 〉 통과 (1.24ms, 30.6MB)
// 테스트 7 〉 통과 (1.01ms, 30.6MB)
// 테스트 8 〉 통과 (13.54ms, 35.4MB)
// 테스트 9 〉 통과 (11.05ms, 34.6MB)
// 테스트 10 〉 통과 (11.12ms, 35.1MB)
// 테스트 11 〉 통과 (11.97ms, 34.4MB)
// 테스트 12 〉 통과 (11.4




let y = [1,2]
let x = [3,2]
let z= [3,2]
let answer = [[...y], [...x], [...z]]
answer = new Set(answer)
console.log(answer, answer.size)