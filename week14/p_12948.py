def solution(phone_number):
    answer = ''
    l = len(phone_number)
    m = (l-4) * "*"
    answer = m + phone_number[-4:]
    
    return answer