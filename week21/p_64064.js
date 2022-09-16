// https://velog.io/@jeky22/javascript-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%B6%88%EB%9F%89-%EC%82%AC%EC%9A%A9%EC%9E%90
// 60060 이랑 비교해서 볼 것
function solution(user_id, banned_id) {
    answer = 0
  
    dfs(user_id.slice(), banned_id.slice(), []);
    answer = Array.from(new Set(arr.map(i => i.sort().join()))).length
    return answer;
  }
  var answer
  var arr = []
  
  function dfs(remain_users, banned_id, ban) {
    if (banned_id.length == 0) {
      arr.push(ban)
      return 1
    }
    else {
      for (var idx = 0; idx < remain_users.length; idx++) {
        if (match(remain_users[idx], banned_id[0])) {
          dfs([...remain_users.slice(0, idx), ...remain_users.slice(idx + 1)],
            banned_id.slice(1),
            [...ban, remain_users[idx]]
          )
        }
      }
      return 0
    }
  }
  
  function match(id, pattern) {
    pattern = pattern.replace(/\*/g, ".");
    const regex = RegExp("\^(" + pattern + "\)$")
    // console.log(id, pattern,regex.test(id)) 
    return regex.test(id)
  }

  ////2번 풀이


  // 제재 아이디 후보로 가능한지 확인하는 함수
const isPossible = (uId, bId) => {
    // 1. 문자열 길이 비교
    if (uId.length !== bId.length) return false;
// 2. 값이 '*'이 아닌 자리의 문자가 모두 같은지 확인
    let cnt = 0;
    for (let i = 0; i < uId.length; i++) {
        if (bId[i] !== '*' && uId[i] !== bId[i]) return false;
    }
    return true;
}
function solution(user_id, banned_id) {
    const ch = Array.from({length:user_id.length}, () => 0); //use_id 개수만큼 0으로 채워진 array [0,0,0,0,0]
    console.log(ch)
    const set = new Set();
    
    const DFS = (idx, cnt, possible) => {
        if (cnt === banned_id.length) {
            let arr = possible.split(' ');
            arr.shift(); // 맨 앞에 저장된 '' 값 제거
            arr.sort();
            let newStr = arr.join('');
            set.add(newStr);
        }
        if (idx >= user_id.length) return;
        
        for (let i = idx; i < banned_id.length; i++) {
            for (let j = 0; j < user_id.length; j++) {
                if (ch[j] === 1) continue; //방문체크
                if (!isPossible(user_id[j], banned_id[i])) continue; //둘이 일치하기 어려움
                ch[j] = 1; //방문체크
                DFS(i+1, cnt+1, possible + ' ' + user_id[j]);
                ch[j] = 0;
            }
        }
    }
    DFS(0, 0, '');
    
    return set.size;
}
user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "abc1**"]
solution(user_id, banned_id)