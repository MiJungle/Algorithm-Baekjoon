s = "cbacdcbc"
ans = ''.join(set(s))
print(ans)


ans = []
ans.append(min(s))
k = s.index(min(s))
print(k)

for i in range(k, len(s)):
    for j in range(len(ans)):
        if s[i] != ans[j]:
            ans.append(s[i])
print(ans)