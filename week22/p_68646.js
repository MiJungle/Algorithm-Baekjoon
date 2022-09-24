//완전탐색
https://velog.io/@jeky22/javascript-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%92%8D%EC%84%A0-%ED%84%B0%ED%8A%B8%EB%A6%AC%EA%B8%B0


function solution(a) {
    var p = []
    var j = []
    var left_min = a[0]
    var right_min = a[a.length - 1]
    
    for (var i = 1; i < a.length - 1; i++) {
      if (left_min > a[i]) {
        left_min = a[i]
        p.push(a[i])
  
      }
      if (right_min > a[a.length - i - 1]) {
        right_min = a[a.length - i - 1]
        j.push(a[a.length - i - 1])
  
      }
    }
      
    return [...new Set([...p, ...j])].length + 2
  }
  