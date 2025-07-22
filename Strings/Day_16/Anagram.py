def anagram(st1, st2):
    n1=len(st1)
    n2=len(st2)

    freq=[0]*26

    for i in range(n1):
        char=st1[i]
        freq[ord(char)-ord('a')]+=1

    for i in range(n2):
        char=st2[i]
        freq[ord(char)-ord('a')]-=1

    for i in range(26):
        if freq[i]!=0:
            return False
    
    return True


s1='geeks'
s2='skeeg'

print(anagram(s1,s2))