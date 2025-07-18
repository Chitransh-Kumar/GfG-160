def atoi(st):
    n=len(st)

    flag=False
    started=False

    ans=0
    for i in range(n):
        char=st[i]

        if char==' ' and not started:
            continue
        elif char=='-' and not started:
            flag=True
            started=True
        elif char.isdigit():
            started=True
            num=ord(char)-ord('0')
            ans=ans*10+num
        else:
            break
    
    if flag==True:
        ans=-ans

    int_max=2**31-1
    if ans>int_max:
        ans=int_max
    
    int_min=-(2**31)
    if ans<int_min:
        ans=int_min

    return ans

st='-999999999999'

print(atoi(st))