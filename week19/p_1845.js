function solution(nums) {
    const set = new Set(nums)
    const newarr = [...set]
    let answer
    if (parseInt(nums.length/2) > parseInt(newarr.length)){
        answer = parseInt(newarr.length)

    }else {
        answer = parseInt(nums.length/2)
    }
    return answer
}
nums= [3,1,2,3]	
console.log(solution(nums))