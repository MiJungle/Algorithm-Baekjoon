function solution(n, queries) {
    var answer = [];
    let s = {};
    let middle = -2e9
    for (let i = 1; i<=n; i++){
        s[i] = []
    }
    for (q of queries){
        if(q[1]!=-1) {
            if(middle <0) {
                middle = q[1]
            }
            else {s[q[0]].push(q[1]) }
        } 
        else if(q[1]==-1) {
            if(s[q[0]].length!=0) {
                answer.push(s[q[0]].pop())
            }
            else if(s[q[0]].length==0){
                if (middle >=0 ) {
                    answer.push(middle)
                    middle = -2e9
                    for(let i = q[0]+1; i<=n ;i++){
                        if(s[i].length !=0) {
                            middle = s[i].shift()
                            break
                        }
                    } 
                    if(middle <0){
                        for(let i = 1; i<=q[0];i++){
                            if(s[i].length !=0) {
                                middle = s[i].shift()
                                break
                         }
                    } 
                    }                  
                }
                else if (middle <0){
                    answer.push(-1)
                }
            }
        }
    }

    return answer
}
// n개의 q를 만든다
//pop을 해야함
//1) 배열에 수가 없어, 음수밖에 -> middle이 양수면 middle 출력
//시계방향으로 
// 2) 배열에 수가 있으면, 그거 출력 
// 가장 처음 숫자를 중앙숫자로 만들고, [0]queue에 push한다
// [1]이 -1의 경우 pop을 하는데, 원소가 없고 중앙숫자가 양수면 중앙숫자 출력
//그러면 큐.length >=1 인 것중, 가장 가까운 스택의 원소 shift, 하고 그걸 중앙숫자로 설정
// 중앙숫자가 음수면 중앙에 아무숫자가 없음을 의미하고 -1출력
//
n = 2
queries = [[1,2],[1,-1],[1,-1],[1,3],[2,-1],[2,3],[2,4],[2,-1],[1,-1]]
console.log(solution(n,queries))
// n개의 q를 만든다
//pop을 해야함
//1) 배열에 수가 없어, 음수밖에 -> middle이 양수면 middle 출력
//시계방향으로 
// 2) 배열에 수가 있으면, 그거 출력 
// 가장 처음 숫자를 중앙숫자로 만들고, [0]queue에 push한다
// [1]이 -1의 경우 pop을 하는데, 원소가 없고 중앙숫자가 양수면 중앙숫자 출력
//그러면 큐.length >=1 인 것중, 가장 가까운 스택의 원소 shift, 하고 그걸 중앙숫자로 설정
// 중앙숫자가 음수면 중앙에 아무숫자가 없음을 의미하고 -1출력

[3,4,5,6,1,2]
//