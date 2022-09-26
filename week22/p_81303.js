
// insert 할때 [2,3,5,6]이 있으면 [2,1,3,5,6 ]으로 insert 됨
//https://dev-note-97.tistory.com/291
//linked list로 구현할 생각을 어떠헥 했지?
function solution(n, k, cmd) {
    let answer = new Array(n);
    for(let i = 0; i < n; i++){
        answer[i] = 'O';
    }
    
    let root = new Node(0);
    let curNode = root;
    let prevNode = root;
    for(let i = 1; i < n; i++){
        const newNode = new Node(i, prevNode);
        prevNode.next = newNode;
        prevNode = newNode;
        
        if(i === k){
            curNode = newNode;
        }
    }
    
    const history = [];
    cmd.map((commandLine) => {
        const [command, count] = commandLine.split(' ');
        let i = 0;
        switch(command){
            case 'U':
                while(i < count && curNode.prev){
                    curNode = curNode.prev;
                    i++;
                }
                break;
            case 'D':
                while(i < count && curNode.next){
                    curNode = curNode.next;
                    i++;
                }
                break;
            case 'C':
                history.push(curNode);
                const prev = curNode.prev;
                const next = curNode.next;
                if(prev && next){
                    prev.next = next;
                    next.prev = prev;
                    curNode = next;
                }else if(prev){
                    prev.next = null;
                    curNode = prev;
                }else if(next){
                    next.prev = null;
                    curNode = next;
                }
                break;
            case 'Z':
                const node = history.pop();
                const prevNode = node.prev;
                const nextNode = node.next;
                if(prevNode){
                    prevNode.next = node;
                }
                if(nextNode){
                    nextNode.prev = node;
                }
                break;
        }
    })
    
    history.map(node => {
        answer[node.idx] = 'X';
    })
    return answer.join('');
}

const Node = function(idx, prevNode){
    this.idx = idx;
    this.prev = prevNode;
    this.next;
}




function solution(n, k, cmd) {
    var answer = '';
    let origin = []
    for(let i = 0 ; i<n ; i++){
        origin.push(i)
    }
    let zstack = []
    for(c of cmd){
        if(c[0]=="D") {
            let a = c.split(" ")
            k += Number(a[1])
            }
        else if(c[0]=="C"){
            let m = origin.splice(k,1)
            zstack.push(m[0])
        }
        else if(c[0]==="U"){
            let a,b = c.split(" ")
            k -= Number(b)
        }
        else if(c[0]==="Z"){
            let goback = zstack.pop()
            origin.splice(goback, 0,  goback);

        }      
        console.log('origin',origin)
        console.log('zstack',zstack)
        
    }
    

   for(let i = 0; i< n ; i++){
       if(zstack.includes(i)){
           answer += "X"
       }
       else {
           answer += "O"
       }
   }
        
    return answer;
}

n= 8
k=2
cmd =["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
console.log(solution(n,k,cmd))