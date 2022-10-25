function solution(babbling) {
    var answer = 0;
    let cansay = ["aya", "ye","woo","ma"]
    babbling.forEach((b)=>{
        let arr = [];

        while(b !== ""){
        if(b.length <2) break
        if(b.slice(0,3)==="aya"&&arr[arr.length-1]!="aya"){
            b=b.replace("aya","")
            arr.push("aya")
            if(arr[-1]=="aya") break
                            }
        else if(b.slice(0,3)==="woo"&&arr[arr.length-1]!="woo"){
            b=b.replace("woo","")
            arr.push("woo")
        if(arr[-1]=="woo") break

        }
        else if(b.slice(0,2)==="ye"&&arr[arr.length-1]!="ye"){
            b=b.replace("ye","")
            arr.push("ye")
        if(arr[-1]=="ye") break
        
        }
        else if(b.slice(0,2)==="ma"&&arr[arr.length-1]!="ma"){
            b=b.replace("ma","")
            arr.push("ma")
        if(arr[-1]=="ma") break
        }
        else break
        }
        if(b=="") answer +=1 
    })
    return answer
    }
