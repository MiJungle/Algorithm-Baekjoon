//https://velog.io/@longroadhome/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-LV.3-%EC%8A%A4%ED%8B%B0%EC%BB%A4-%EB%AA%A8%EC%9C%BC%EA%B8%B0-JS
//반례 i 번째 i+1, i+2 번째 비교해서 더해야함. => DP

//초기 접근
//짝수 element 합 홀수 element 합 중 큰 것을 출력

// 채점 결과
// 정확성: 6.0
// 효율성: 0.0
// 합계: 6.0 / 100.0
function solution(sticker) {
    let even = 0
    let odd = 0
    for(let i = 0 ; i < sticker.length ; i++){
        if(i%2 ==0) even += sticker[i]
        else odd += sticker[i]
    }
    if(sticker.length %2 !=0) {
        even= Math.max(even-sticker[0], even-sticker[sticker.length-1])
    }
    return Math.max(even,odd);
}