const array = [{a:10} , {b:2}, {c:3} ] 

function addToArray(array,element){
    const newArray = [...array]
    newArray.push(element)
    newArray[0].a = 10;
    console.log(newArray);
}
addToArray(array, {d:4})
console.log(array)