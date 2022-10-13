function solution(fees, records) {
    var answer = [];
    let in_record = [];
    let out_record = [];
    records.forEach(r=> {
        let re = r.split(' ')
        if(re[2]==="IN") in_record.push(re)
        else out_record.push(re)
    })
    let fin = []
    in_record.forEach(i => {
        let time = i[0].split(":")
        let car_num = i[1]
        let money
        out_record.forEach(o => {
            if(o[1] === car_num) {
                let out_time = o[0]
                let spent = o[0].split(":")
                let t1 = Number(spent[0]) * 60 + Number(spent[1])
                let t2 = Number(time[0])*60 + Number(time[1])
                if (t1>= t2 && (t1- t2 >= fees[0])){
                     money = fees[1] + ((t1-t2-fees[0])/fees[2])*600
                }
                else if (t1< t2){
                    t1 = 11*60 + 59
                    money = fees[1] + ((t1-t2-fees[0])/fees[2])*600
                }
                else if  (t1>= t2 && (t1- t2 < fees[0])){money = fees[1]}
            }
        })
                        fin.push([car_num, money])

    })
    
    console.log(fin)
}


//fees: 기본 시간 / 기본 요금/ 단위 시간/ 단위 요금
//records: 시간 / 차량 / In or Out

//in out으로 나눠 
