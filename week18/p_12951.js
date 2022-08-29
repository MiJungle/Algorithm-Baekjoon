function solution(s) {
    var answer = '';
    let arr = s.split(" ")
    for(word of arr){
        let new_word = ""
        for(let i=0 ; i <word.length ; i++){
            if(i==0) {new_word+= word[i].toUpperCase()}
            else {new_word+= word[i].toLowerCase()}
        }
        if(arr.indexOf(word)!= arr.length-1){
            answer += new_word + " "}
        else { answer += new_word}
        
    }
        return answer
}