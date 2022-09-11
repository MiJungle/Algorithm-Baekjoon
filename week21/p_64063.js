function solution(k, room_number) {
    const rooms = new Map();
    const assignRooms = (num)=> {
        if(!rooms.has(num)){
            rooms.set(num,num+1);
            return num;
        }
        const nearestRoom = assignRooms(rooms.get(num));
        rooms.set(num,nearestRoom+1);
        return nearestRoom;
    }
    return room_number.map(assignRooms)
}

// o// function solution(k, room_number) {
//     var answer = [];
//     let room = []
//     for (let i = 1; i<=k ; i++){
//         room.push(i)
//     }

//     for (let r of room_number){
//         if( room.includes(r) ===true){
//             let index = room.indexOf(r)
//             room.splice(index,1)
//             console.log(room)
//             answer.push(r)
//         }
//         else {
//             let k = room.shift()
//             answer.push(k)
//         }
        
//     }
    
//     return answer;
// }