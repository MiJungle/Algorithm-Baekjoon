name = "JEROEN"
def solution(name):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    answer = len(name)-1

    for str in name:
        k= alphabet.index(str)
        answer += min(k, 26-k)
        
    return answer
print(solution(name))