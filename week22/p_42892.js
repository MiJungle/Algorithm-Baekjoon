
// https://eunchanee.tistory.com/693


class Node {
    constructor(x, y, num){
        this.x = x;
        this.y = y;
        this.num = num;
        this.left = null;
        this.right = null;
    }
}

function solution(nodeinfo) {
    const answer = [[], []];
    const node = [];
    
    const addNode = (parent, child) => {
        if(child.x < parent.x){
            if(parent.left === null){
                parent.left = child;
            } else{
                addNode(parent.left, child);
            }
        } else{
            if(parent.right === null){
                parent.right = child;
            } else{
                addNode(parent.right, child);
            }
        }
    }
    
    const preorder = (node) => {
        if(node === null){
            return;
        }
        
        answer[0].push(node.num);
        preorder(node.left);
        preorder(node.right);
    }
    
    const postorder = (node) => {
        if(node === null){
            return;
        }
        
        postorder(node.left);
        postorder(node.right);
        answer[1].push(node.num);
    }
    
    for(let i = 0; i < nodeinfo.length; i++){
        const [x, y] = nodeinfo[i];
        const num = i + 1;
        const tmpNode = new Node(x, y, num);
        
        node.push(tmpNode);
    }
    
    node.sort((a, b) => {
        if(a.y === b.y){
            return a.x - b.x;
        }
        
        return b.y - a.y;
    });
    
    const root = node[0];
    
    for(let i = 1; i < node.length; i++){
        addNode(root, node[i]);
    }
    
    preorder(root);
    postorder(root);
    
    return answer;
}