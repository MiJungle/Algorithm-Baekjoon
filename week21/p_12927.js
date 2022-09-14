function solution(n, works) {
    works.sort((a,b)=>(b-a))
    let big = works[0]
    
    while(n>0){
        for (let i= 0; i < works.length; i++){
            if(big === works[i]){
                works[i]-= works[i]>0? 1: 0
                n-=1
            }
            if(!n) break
        }
        big -= 1
        if(!big) break
    }
    return sumsquare(works)
}
const sumsquare = (arr)=> arr.reduce((accum,val)=> {return accum+ val**2},0)


// https://velog.io/@longroadhome/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-LV.3-%EC%95%BC%EA%B7%BC-%EC%A7%80%EC%88%98-JS
//
//a*2 + b*2 + c*2 가 최소가 되기위해서는 ac + bc + ab 가 최대가 되어야한다고 생각. 
//sort한다음 계속 1씩 빼주고 그걸 다 제곱해서 더한다?

// 채점 결과
// 정확성: 26.7
// 효율성: 0.0
// 합계: 26.7 / 100.0

// function solution(n, works) {
//     var answer = 0;
//     works.sort((a,b)=>(b-a))
    
//     while(n!==0){
//         for (let i= 0; i < works.length; i++){
//             works[i]-= 1
//             n-=1
//             if(works.filter(a=> a==0).length === works.length) return sum1(works)
//             if(n==0 ) return sum1(works)
                
//         }

//         }      
// }
// const sum1 = (arr)=> arr.reduce((accum,val)=> {return accum+ val**2},0)


// works = [1,1]
// n = 3
// console.log(solution(n,works))