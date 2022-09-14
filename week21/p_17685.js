// https://velog.io/@young_pallete/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%9E%90%EB%8F%99-%EC%99%84%EC%84%B1%EC%9E%90%EB%B0%94%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%8A%B8

class Node {
    constructor(value = '') {
      this.value = value;
      this.children = new Map();
      this.cnt = 0;
    }
  }
  
  class Trie {
    constructor() {
      this.root = new Node();
    }
    insert(string) {
      let currentNode = this.root;
      currentNode.cnt += 1;
  
      for (const char of string) {
        if (!currentNode.children.has(char)) {
          currentNode.children.set(char, new Node(currentNode.value + char));
        }
  
        currentNode = currentNode.children.get(char);
        currentNode.cnt += 1;
      }
    }
  
    getCount(string) {
      let cnt = 0;
      let currentNode = this.root;
      for (const char of string) {
        cnt += 1;
  
        currentNode = currentNode.children.get(char);
        if (currentNode.cnt === 1) break;
      }
  
      return cnt;
    }
  }
  
  const solution = (words) => {
    let result = 0;
    const trie = new Trie();
  
    for (let i = 0; i < words.length; i += 1) {
      trie.insert(words[i]);
    }
  
    for (let i = 0; i < words.length; i += 1) {
      result += trie.getCount(words[i]);
    }
  
    return result;
  };

