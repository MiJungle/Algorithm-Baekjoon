
//초기 접근법 - 그냥 순회하면서 해당 글자를 갖고, 글자 길이도 같으면 count += 1 해서 정답 배열에 넣는다
//반례가 존재: "???o"의 경우 front 도 일치한다고 판단함
//이것또한 trie 푸는게 정석

function Node() {
    this.count = 0;
    this.child = new Map();
  }
  
  function insertTrie (word, root) {
    if (!root.has(word.length)) {
      root.set(word.length, new Node());
    }
    
    let node = root.get(word.length);
  
    for (const ch of word) {
      if (!node.child.has(ch)) {
        node.child.set(ch, new Node());
      }
      node.count++;
      node = node.child.get(ch);
    }
  };
  
  function searchTrie (query, root) {
    if (!root.has(query.length)) {
      return 0;
    }
  
    let node = root.get(query.length);
  
    for (const ch of query) {
      if (ch === '?') {
        return node.count;
      }
      if (!node.child.has(ch)) {
        return 0;
      }
      node = node.child.get(ch);
    }
  };
  
  function solution(words, queries) {
    String.prototype.reverse = function () {
      return this.split('').reverse().join('');
    };
  
    const forwardRoot = new Map();
    const backwardRoot = new Map();
  
    words.forEach((word) => {
      insertTrie(word, forwardRoot);
      insertTrie(word.reverse(), backwardRoot);
    });
  
    const answer = [];
  
    queries.forEach((query, i) => {
      answer[i] = (query[0] !== '?')
        ? searchTrie(query, forwardRoot)
        : searchTrie(query.reverse(), backwardRoot);
    });
  
    return answer;
  }



// function solution(words, queries) {
//     var answer = [];
//     let wordlen = []
//     let count = 0
//     for(let i = 0 ; i <queries.length; i++){
//         wordlen.push(queries[i].length)
//     }
    
//     queries.forEach((element, index) => {
//   queries[index] = queries[index].replace(/\?/g,"") 
// });
//     for (let i =0 ; i <queries.length; i++){
//         count = 0
//         for(let j = 0; j <words.length; j++){
//         if(words[j].includes(queries[i])&& words[j].length == wordlen[i]){
//                 count += 1
//             }
            
//         }
//         answer.push(count)
//     }

//   return answer

// }


//??이것도 trie??
//?앞까지만 잘라서 그게 include 되어있고 글자수가 같으면 count += 1?? 

