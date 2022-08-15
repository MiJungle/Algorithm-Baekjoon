
import sys,re
sys.stdin = open('input.txt')
input = sys.stdin.readline

def main():
    li = input()
    new_li = re.sub("\[|\]|\"","",li)
    arr = new_li.split(',')
    arr = [i.strip() for i in arr]

    index = 0
    restore= []
    for i in range(len(input())):
        c = list(map(str,input().split()))
        print(c)
        if c[0] == "move":
            if c[1] =="-u":
                print("-u")
                index -= int(c[2])
                if index< 0:
                    print("작으","Error 100")
            elif c[1] =="-d":
                print("---------_",int(c[2]))
                index += int(c[2])
                if index > len(arr):
                    print("Error 100")

        elif c[0] =="delete":
            try: 
                if len(arr)!= 0 and arr[index]:
                    if index == len(arr)-1:
                        restore.append([index,arr[index]])
                        del arr[index]
                        index -= 1
                    else:
                        restore.append([index,arr[index]])
                        del arr[index]
                        index += 1
            except: 
                continue
        elif c[0] =="restore":
            if restore:
                arr.insert(restore[-1][0], restore[-1][1])
            if not restore:
                print("Error 200")
        elif c[0] =="list":
            for i in range(len(arr)):
                print(arr[i])
        elif c[0] =="q":
            return

print(main())