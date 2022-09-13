const temp = [1,2]
const [x,y,z=3] = temp;
console.log(z)

const vehicle = ['son','avan','bronc']
const [x,y...suv] = vehicle
console.log(suv)