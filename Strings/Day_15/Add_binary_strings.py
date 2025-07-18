def add_binary_strings(s1, s2):
    n1=len(s1)
    n2=len(s2)

    first=n1-1
    second=n2-1

    ans=''
    carry=0
    while first>=0 and second>=0:
        if carry==0:
            if s1[first]=='0' and s2[second]=='0':
                ans+='0'
            elif s1[first]=='0' or s2[second]=='0':
                ans+='1'
            else:
                ans+='0'
                carry=1
        else:
            if s1[first]=='0' and s2[second]=='0':
                ans+='1'
                carry=0
            elif s1[first]=='0' or s2[second]=='0':
                ans+='0'
            else:
                ans+='1'
        first-=1
        second-=1
        
    while first>=0:
        if carry==0:
            if s1[first]=='0':
                ans+='0'
            else:
                ans+='1'
        else:
            if s1[first]=='0':
                ans+='1'
                carry=0
            else:
                ans+='0'
        first-=1
    
    while second>=0:
        if carry==0:
            if s2[second]=='0':
                ans+='0'
            else:
                ans+='1'
        else:
            if s2[second]=='0':
                ans+='1'
                carry=0
            else:
                ans+='0'
        second-=1

    ans+=str(carry)

    ans=ans[::-1]

    valid=0
    for i in range(len(ans)):
        if ans[i]=='1':
            valid=i
            break
    
    ans=ans[valid:]

    return ans

s1='1101'
s2='111'

print(add_binary_strings(s1,s2))

