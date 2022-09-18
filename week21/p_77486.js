
//dfs

function solution(enroll, referral, seller, amount) {
    let graph = Array.from(Array(enroll.length), () => Array());
    let money = Array.from(Array(enroll.length), () => Array());
  
    // 저는 bfs 형식을 사용했지만 단방향 상승밖에 없기 때문에
    // dfs를 사용하여도 전혀 상관 없습니다.
    const upToCenter = (name, amount) => {
      const startIdx = enroll.indexOf(name);
      let queue = [[startIdx, amount]];
  
      while (queue.length) {
        let [next, amount] = queue.shift();
        const tempMoney = Math.floor(amount * 0.1);
  
        money[next] = Number(money[next]) + amount - tempMoney;
  
        /* 중요한건 백트래킹처럼 가지치기를 해야합니다.
         상승하다보면 0원만 주게되는 경우가 생길땐
         탐색을 종료하도록 해야 시간초과가 나지 않습니다. */
        if (tempMoney === 0) break;
  
        if (graph[next].length) {
          queue.push([graph[next][0], tempMoney]);
        }
      }
    };
  
    referral.forEach((el, idx) => {
      const temp = enroll.indexOf(el);
      if (temp >= 0) graph[idx].push(temp);
    });
  
    seller.forEach((el, idx) => {
      upToCenter(el, amount[idx] * 100);
    });
  
    return money.map((el) => (el.length !== undefined ? 0 : el));
  }