'''
We have given a string and a patterns to search in string
Search operation should be in O(n+m)
'''

def KMP(s: str, p: str):
    lps = [0 for i in range(len(p))] #store the info of longest prefix which is also a suffix where len(pref) < len(p)
    prevlpsLen = 0
    i = 1
    while i < len(p): 
        if p[prevlpsLen] == p[i]:
            lps[i] = lps[prevlpsLen] + 1
            prevlpsLen+=1
        else:
            if prevlpsLen == 0:
                i+=1
            else:
                prevlpsLen = lps[prevlpsLen-1]
    
    '''Find the pattern in string using lps'''
    i = 0
    j = 0
    while i < len(s):
        if s[i] == p[j]:
            i+=1
            j+=1
        else:
            if j == 0:
                i+=1
            else:
                j = lps[j-1]
        if j == len(p):
            break
    print(i-j)


s="abhcabhd"
p="abhd"
KMP(s,p)