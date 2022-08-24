function solution(begin, target, words) {
    const visited = [];
    const queue = [[begin, 0]];
    //첫 단어와, 몇번을 거쳐야하는지 수를 더할 0을 배열에 넣음

    while(queue.length){
        let [w, c] = queue.shift();
        if(w === target) return c; //단어가 target에 해당되면 c,즉 계속 더해왔던 숫자를 return

        words.forEach(word => {//각각의 단어마다 visited를 안했으면, 1단어만 바꿔도 되는 경우에한해서만 push
            if(!visited.includes(word)){
                if(checked(w, word)){
                    queue.push([word, ++c]);
                    visited.push(word);
                }
            }
        });
    }

    return 0;
}

function checked(str1, str2){
    let check = 0;
    for(let i = 0; i < str1.length ; i++){
        if(str1[i] !== str2[i]) check++;
    }
    return check === 1;
}
