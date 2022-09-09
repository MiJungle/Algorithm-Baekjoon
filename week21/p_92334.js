function solution(id_list, report, k) {
    let userId = new Array(id_list.length).fill(0)
    let target = [];
    let result = {};
    new Set(report).forEach(f => {
        const r = f.split(' ');
        const to = r[1];
        target.push(r);
        result[to] = (result[to] || 0) + 1;
    })
    Object.keys(result).forEach(f => {
        if (result[f] >= k) {
            target.filter(a => a[1] == f).forEach(m => userId[id_list.indexOf(m[0])]++)
        }
    })

    return userId;
}