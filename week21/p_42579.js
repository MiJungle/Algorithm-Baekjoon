

// https://nakzyu.tistory.com/32

function solution(genres, plays) {
    // {[genre:string]:{
    //   played: number,
    //   songs:  song{index:number, played:number}[] }
    const genreData = {};
  
    for (let i = 0; i < genres.length; i++) {
      const genre = genres[i];
      const play = plays[i];
  
      if (!(genre in genreData)) {
        genreData[genre] = { played: 0, songs: [] };
      }
      genreData[genre].played += play;
  
      genreData[genre].songs.push({ index: i, played: play });
    }
  
    Object.values(genreData).forEach((genre) => {
      genre.songs.sort((a, b) => b.played - a.played);
      genre.songs.sort((a, b) => {
        if (a.played === b.played) {
          return a - b;
        }
        return 0;
      });
    });
    const sortByPlayed = Object.values(genreData).sort(
      (a, b) => b.played - a.played
    );
  
    const answer = [];
  
    sortByPlayed.forEach((genre) => {
      genre.songs.some((item, i) => {
        if (i > 1) return true;
        answer.push(item.index);
      });
    });
    return answer;
  }





//채점 결과
// 정확성: 53.3
// 합계: 53.3 / 100.0

function solution(genres, plays) {
    var answer = [];
    let gen = {}
    for(let i =0; i < plays.length; i++){
        gen[genres[i]]= (gen[genres[i]]||0)+ plays[i]
    }
    const sorted = Object.fromEntries(
    Object.entries(gen).sort(([, a], [, b]) => b - a)
)
   
    let all = []
    for (let i = 0; i <genres.length; i++){
        let arr = []
        arr.push(genres[i], plays[i], i)
        all.push(arr)
    }
    for (let key in sorted){
        let arr1 = all.filter(word => word[0]===key)
        arr1.sort((a,b)=> b[1]-a[1])
        for(let i=0; i <2 ; i++){
            answer.push(arr1[i][2])
        }
    }
    return answer
}


//장르 순으로 2개씩 가장 많이 재생된 노래
// 횟수가 같으면 index가 작은 순서대로

//장르별로 plays 수를 더한다, 
//{classic : 1240 pop: 234}
// [classic 500 index, pop 600 index, classic 150, ...]
//객체 for문돌리면서 classic에 해당하는걸로 filter후 sort를 [1]로한다음에 
// index를 추가함-  2개까지만
//