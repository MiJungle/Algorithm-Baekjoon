students = ["PPPPPPPPPP", "LLPPPPPPPP", "PPPPPPPPPP"]

function solution(students) {
    var answer = [];
    let arr = []
    if (students.length == 1) return [1]

    for(let i = 0 ; i <students.length; i++){
        let defaultscore = 10
        let scoreA = [...students[i]].filter(a=> a=="A").length
        let scoreL = Math.floor([...students[i]].filter(a=> a=="L").length/2)
        let scoreP = [...students[i]].filter(a=> a=="P").length
        scoreL + scoreP >= 3?defaultscore = 0 : defaultscore = defaultscore +scoreA - scoreL - scoreP
        arr.push([defaultscore, i+1])     
    }
    arr.sort((a,b)=> b[0]-a[0]||a[1]-b[1])
    for (a of arr){
        answer.push(a[1])
    }
    return answer
}

//for student of students - > let default = 10
// for letter.length - > 
// "A" -> +1 [...string].filter(a=>a==="A").length 
// .filter ("L").length /2 (-1)
//. filter ("P") (-1)
// answer.push([default,i] )
// sort by [0], sort by [i] 해서 i출력

// 10점에서 출석 +1 , 결석 -1, 3 결석: 0, 지각 2번은 결석 1번, -1
//학생들의 번호 나열
//점수가 같으면 index 순으로 나열 
console.log(solution(students))
//for student of students - > let default = 10
// for letter.length - > 
// "A" -> +1 [...string].filter(a=>a==="A").length 
// .filter ("L").length /2 (-1)
//. filter ("P") (-1)
// answer.push([default,i] )
// sort by [0], sort by [i] 해서 i출력

// 10점에서 출석 +1 , 결석 -1, 3 결석: 0, 지각 2번은 결석 1번, -1
//학생들의 번호 나열
//점수가 같으면 index 순으로 나열 