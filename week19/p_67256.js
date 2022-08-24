function solution(numbers, hand) {
    
    // 위치 찾아주는 함수
    function findKey(key) {
        let keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']];
        for (let i = 0; i < 4; i++) {
            for (let j = 0; j < 3; j++) {
                if (keypad[i][j] === key) {
                    return [i, j];
                }
            }
        }
    }
    
    var answer = '';
    let left = '*';
    let right = '#';
    for (let i of numbers) {
        if (i === 1 || i === 4 || i === 7) {
            answer += 'L';
            left = i;
        }else if (i === 3 || i === 6 || i === 9) {
            answer += 'R';
            right = i - 2;
        }else {
            let r = findKey(right);
            let l = findKey(left);
            let middle = findKey(i);
            // 손위치와 눌러야할 키패드 거리 구하기
            let rr = Math.abs(r[0] - middle[0]) + Math.abs(r[1] - middle[1]);
            let ll = Math.abs(l[0] - middle[0]) + Math.abs(l[1] - middle[1]);
            if (rr === ll) { // 거리가 같다면 오른손잡이 -> 'R', 왼손잡이 -> 'L'
                hand === 'right' ? (right = i, answer += 'R') : (left = i, answer += 'L');
            }else if(rr > ll) { // 오른손의 거리가 더 멀다면
                answer += 'L';
                left = i;
            }else { // 왼손의 거리가 더 멀다면
                answer += 'R';
                right = i;
            }
        }
    }
    
    return answer;
}

// 만약 147의 경우에는 L
// 369의 경우에는 R
// 2580을 입력할 때는 가까운 손가락을 사용한다. 위치가 똑같으면 무슨 손잡인지에 따라서 출력
// -> 가까운것을 어떻게 판단할 것인가?
//     L, R에 위치를 저장해놓는다
//     1) 두번째 숫자가 2580 중 하나일 때- 손가락이 * #에 있는 경우
//     -> 무슨손잡인지에 따라 출력을 한다
//     2) 손가락이 *#에 없는 경우 중 2580 수가 나오면 
//     -> 오른손이 1,4,7에 있을 수 있고
//     -> 왼손이 3,6,9에 있을 수 있는데
//       -> 같은 줄에 있는 경우 무슨 손잡인지에 따라 출력
//       -> 다른 줄에 있는 경우, 줄의 차이가 같으면 무슨 손잡인지에 따라 출력
//             -> 아닌 경우 줄의 차이가 작은 걸 출력 
//     R=[1,4,7] L= 3,6,9 M= 2,5,8 -> M의 index와 R 과 L의 index를 비교한다

    
// 123
// 456
// 789
// *0#
