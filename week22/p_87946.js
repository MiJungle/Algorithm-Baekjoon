
//sort 잘못 생각함



function solution(k, dungeons) {
    var answer = 0;
    dungeons.sort((a,b)=> a[1]-b[1]||b[0]-a[0])
    console.log(dungeons)
    for(dungeon of dungeons){
        if(k >= dungeon[0]){
            k-=dungeon[1]
            answer += 1
        }
    }
    // return answer;
}