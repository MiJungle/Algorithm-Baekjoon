let a = [1,2,3,4,5,6,7]
let m = a.slice(0,3)
let d = [...m]
console.log(m,a)
console.log(d)
let b = [1,3,5]
d = [...d,...b]
console.log(d)

let dd = [1,2]
let md = dd.slice(0,3)
console.log(md)

let length = 9
let n = 4
console.log(Math.ceil(length/n))