https://velog.io/@longroadhome/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-LV.4-%ED%8A%B8%EB%A6%AC-%ED%8A%B8%EB%A6%AC%EC%98%A4-%EC%A4%91%EA%B0%84%EA%B0%92-JS
function solution (n, edges) {
    const tree = new Array(n).fill().map(_ => []);
    for(const [e1, e2] of edges) {
      tree[e1-1].push(e2-1);
      tree[e2-1].push(e1-1);
    }
    
    let [leafDist, leafIdx, leafCount] = findLeafnodeWithBFS(tree, 0);
    
    [leafDist, leafIdx, leafCount] = findLeafnodeWithBFS(tree, leafIdx);
    
    let answer = 0;
    
    if (leafCount > 1) answer = leafDist;
    else {
      [leafDist, leafIdx, leafCount] = findLeafnodeWithBFS(tree, leafIdx);
      
      if (leafCount > 1) answer= leafDist;
      else answer = leafDist - 1;
    }
    
    return answer;
  }
  
  const findLeafnodeWithBFS = (tree, node) => {
    const queue = new Queue();
    const dist = new Array(tree.length).fill(Infinity);
    const visited = new Array(tree.length).fill(false);
    
    dist[node] = 0;
    visited[node] = true;
    queue.add(node);
    
    let maxLength = 0;
    let maxIdx = 0;
    let count = 0;
    
    while(queue.size()) {
      const cur = queue.popleft();
      const distance = dist[cur];
      
      for(const next of tree[cur]) {
        if(!visited[next]) {
          const newDistance = distance + 1;
          visited[next] = true;
          dist[next] = newDistance;
          queue.add(next);
          
          if(maxLength < newDistance) {
            maxLength = newDistance;
            maxIdx = next;
            count = 1;
          }
          else if(maxLength === newDistance) {
            count++;
          }
        }
      }
    }
    
    return [maxLength, maxIdx, count];
  }
  
  class Queue {
    constructor() {
      this.storage = {};
      this.front = 0;
      this.rear = 0;
    }
    
    size() {
      if (this.storage[this.rear] === undefined) {
        return 0;
      } else {
        return this.rear - this.front + 1;
      }
    }
    
    add(value) {
      if (this.size() === 0) {
        this.storage['0'] = value;
      } else {
        this.rear += 1;
        this.storage[this.rear] = value;
      }
    }
    
    popleft() {
      let temp;
      if (this.front === this.rear) {
        temp = this.storage[this.front];
        delete this.storage[this.front];
        this.front = 0;
        this.rear = 0;
        return temp;
      } else {
        temp = this.storage[this.front];
        delete this.storage[this.front];
        this.front += 1;
        return temp;
      }
    }
  }
  
  // n으로 나올 수 있는 조합을 구해서, 
  // 몇개의 edge를 거쳐야하는지 구해서 
  // 그거 max값들을 계속 갱신?
  // 거리의 중간값 중 가장 큰 값
  // 