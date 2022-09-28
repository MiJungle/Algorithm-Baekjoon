
export default class Queue{
    constructor(){
        this.item=[];
    }

    enqueue(item){
        this.item.push(item)
    }
    dequeue(){
        return this.item.shift()
    }
    contains(){
        this.item.length;
    }
}