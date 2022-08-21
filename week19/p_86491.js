function solution(sizes) {
    let width = [];
    let height = [];
    for(let i = 0 ; i < sizes.length; i++){
        width.push(Math.max(...sizes[i]))
        height.push(Math.min(...sizes[i]))

    }
    let space = Math.max(...width) * Math.max(...height)
    return space;
}

sizes= [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]
console.log(solution(sizes))