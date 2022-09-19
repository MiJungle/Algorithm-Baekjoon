
class Room {
  constructor() {
    this.edges = [];
    this.before = null;
    this.visited = false;
  }
}

function solution(n, path, order) {
  let count = 0;
  const rooms = [...Array(n)].map(() => new Room());
  const save = new Map();
  const stack = [];

  path.forEach(([a, b]) => {
    rooms[a].edges.push(b);
    rooms[b].edges.push(a);
  });
  order.forEach(([a, b]) => {
    rooms[b].before = a;
  });

  stack.push(0);
  while (stack.length > 0) {
    const cur = stack.pop();

    if (rooms[cur].visited) continue;
    if (rooms[cur].before !== null && !rooms[rooms[cur].before].visited) {
      save.set(rooms[cur].before, cur);
      continue;
    }

    count += 1;
    rooms[cur].visited = true;

    stack.push(...rooms[cur].edges);
    if (save.has(cur)) stack.push(save.get(cur));
  }

  return count === n;
}

//초기



function solution(n, path, order) {
    var answer = true;
    return answer;
}
//위상 정렬?dfs? bfs에 조건 추가되는?
// if visited [0]이면 다 돌게끔 
//route = {[]*n}
//for p of path
//p[0].push(p[1])
//p[1].push(p[0])

// que= path[0]
//while que:
// let [from,to] = que.shift()
//order[1]에 해당되지 않으면 q push 