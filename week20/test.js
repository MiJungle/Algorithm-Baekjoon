const person = {
    name:'Lee',
    getName(){
        return this.name;
    }
}

const anotherPerson = {
    name: 'Kim'
}
anotherPerson.getName = person.getName;
console.log(anotherPerson.getName())





