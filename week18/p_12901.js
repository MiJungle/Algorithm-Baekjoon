function solution(a, b) {
    let  end = [31,29,31,30,31,30,31,31,30,31,30,31]
    let day = ["SUN","MON","TUE","WED","THU", "FRI","SAT"]
    let arr = end.slice(0,a-1)
    const reducer = (accumulator, curr) => accumulator + curr;
    let total
    a==1? total = b: total = arr.reduce(reducer) + b

    if (total %7 === 0){
         return day[4]}
    else if( total % 7 === 1){
        return day[5]}
    else if ( total % 7 === 2){
        return day[6]}
    else if (total % 7 === 3){
        return day[0]}
    else if (total % 7 === 4){
        return day[1] } 
    else if (total % 7 === 5){
        return day[2]}
    else if (total % 7 === 6){
        return day[3]}

}