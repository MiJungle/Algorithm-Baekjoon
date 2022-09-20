// https://kyun2da.github.io/2020/07/16/lockandKey/

const rotationKey = (key) => {
    const len = key.length;
    const ret = Array.from(Array(len), () => Array(len).fill(null));
    for (let i = 0; i < len; ++i) {
      for (let j = 0; j < len; ++j) {
        ret[i][j] = key[len - j - 1][i];
      }
    }
    return ret;
  };
  
  //답인지 검사하는 함수
  const isAnswer = (newLock, len) => {
    for (let i = len; i < len * 2; i++) {
      for (let j = len; j < len * 2; j++) {
        if (newLock[i][j] !== 1) {
          return false;
        }
      }
    }
    return true;
  };
  const solution = (key, lock) => {
    let answer = true;
    const len = lock.length;
    const arr = Array.from(Array(len * 3), () => Array(len * 3).fill(null));
  
    for (let i = len; i < len * 2; i++) {
      for (let j = len; j < len * 2; j++) {
        arr[i][j] = lock[i - len][j - len];
      }
    }
    //키를 회전 시키면서 탐색
    for (let i = 0; i < 4; i++) {
      key = rotationKey(key, i);
      //키를 이동시키면서 탐색
      for (let j = 0; j <= arr.length - key.length; j++) {
        for (let k = 0; k <= arr[0].length - key[0].length; k++) {
          const newLock = arr.map(function (arr) {
            return arr.slice();
          });
          for (let m = 0; m < key.length; m++) {
            for (let n = 0; n < key.length; n++) {
              if (newLock[j + m][k + n] === 1 && key[m][n] === 1) {
                //키가 둘다 1이면 2로바꿈 -> 답이 될수 없음
                newLock[j + m][k + n] = 2;
              } else if (newLock[j + m][k + n] === 1 && key[m][n] === 0) {
                newLock[j + m][k + n] = 1;
              } else {
                newLock[j + m][k + n] = key[m][n];
              }
            }
          }
          if (isAnswer(newLock, len)) {
            return true;
          }
        }
      }
    }
    return false;
  };
  //큐스택? X 완전탐색을 이용해야한다
  //영역을 벗어난 부분에 있는 것은 문을 여는 데 영향을 주지 않음
  // 딱 그 열쇠 구멍 만큼만 열쇠가 나와져있어야한다. 
  // nx ny 만큼 옮겼을 때 그 구멍 좌표와 일치하고, 나머지가 0 이면 된다
  // 1) lock을 돌면서 0의 좌표를 구한다 
  // 2) key 좌표 중 1인것들을 담아서 
  // 3) 나올 수 있는 가능성 중 lock 좌표와 일치하는게 있으면 출력?
  