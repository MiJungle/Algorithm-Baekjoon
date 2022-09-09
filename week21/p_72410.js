function solution(new_id) {
    const answer = new_id
      .toLowerCase() // 1
      .replace(/[^\w-_.]/g, "") // 2
    //^not word - _ . 
      .replace(/\.+/g, ".") // 3
    //.+: Matches any string that contains at least one .
      .replace(/^\.|\.$/g, "") // 4
    
      .replace(/^$/, "a") // 5
      .slice(0, 15)
      .replace(/\.$/, ""); // 6
      //A search for "." at the end of a string:
    const len = answer.length;
    return len > 2 ? answer : answer + answer.charAt(len - 1).repeat(3 - len);
  }