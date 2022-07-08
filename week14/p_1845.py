
nums = [3,1,2,3]
def solution(nums):
    n = len(nums)
    new_nums = set(nums)
    if len(new_nums) >= n//2:
        return(n//2)
    else:
        return len(new_nums)
print(solution(nums))