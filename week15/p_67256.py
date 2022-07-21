numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"

def solution(numbers, hand):
    for i in range (len(numbers)):
        if numbers[i] == 1 or  numbers[i] == 4 or  numbers[i] == 7:
            numbers[i]="L"

        elif numbers[i] == 3 or  numbers[i] == 6 or  numbers[i] == 9:
            numbers[i]="R"
        print(numbers)

    L = [3,0]
    R = [0,3]
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    for i in range(len(numbers)):
        if numbers[i].isalpha() == 0:
            if numbers[i] == 2:
                
print(solution(numbers,hand))