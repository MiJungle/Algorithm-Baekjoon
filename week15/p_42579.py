genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

from collections import defaultdict
def solution(genres, plays):
    arr = defaultdict(int)
    for i in range(len(genres)):
        arr[genres[i]] += plays[i]

    sorted_arr = sorted(arr.items(),key=lambda item:-item[1])
    max_arr = []

    for i , key in enumerate(sorted_arr ):
        for j in range(len(genres)):
            if genres[j] == key[0]:
                max_arr.append([i,key[0],j,plays[j]])
    max_arr  = sorted(max_arr,key=lambda item:(item[0],-item[3]))
    print(max_arr)

    ans = []
    for i in range(len(max_arr)-1):
        if len(ans)<2:
            ans.append(max_arr[i])
        else:
            if ans[-1][1] == ans[-2][1]and max_arr[i][1]== ans[-1][1]:
                continue
            else:
                ans.append(max_arr[i])
    final = []

    for i in range(len(ans)):
        final.append(ans[i][2])

    return final
    # print(max_arr)
    # real =[]
    # for i , key in enumerate(sorted_arr):

    #     for j in range(len(genres)):
    #         if genres[j] == key[0]:
    #             if len(real) < 2:
    #                 real.append([i,key[0],j,plays[j]])
    #             else:
    #                 if real[-1][1] == key[0] and real[-2][1] == key[0]:
    #                     continue
    #                 else: 
    #                     real.append([i,key[0],j,plays[j]])
    # answer = []
    # for i in max_arr:
    #     answer.append(i[1])
    # return answer
    

    # print(max_arr)

        # print(i,key[0])
    #     if genres[i] == key:
    #         max_arr.append(key,i)
    # print(max_arr)



print(solution(genres,plays))