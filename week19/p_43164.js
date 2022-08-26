let tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"], 'ddd']
let temp = tickets.slice();
for(var i in tickets){
    console.log(i,tickets[i])
}
console.log(temp)