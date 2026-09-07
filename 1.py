//sum of digits of a number
n=int(input("enter any number:"))
s=0
while n>0:
    ld=n%10
    s=s+ld
    n=n//10
print("sum of digits of a number:",s)

armstrong number
n=int(input("enter any number:"))
l=len(str(n))
s=0
temp=n
while temp>0:
    d=temp%10
    s+=d**l
    temp=temp//10
if n==s:
    print("entered number is a armstrong number",s)
else:
    print("not a armstrong number")

perfect number
num=int(input("enter any number:"))
sod=0
for i in range(1,num):
    if num%i==0:
        sod+=i
if sod==num:
    print(f"sum of digits of a {num} is {sod} and it is perfect number")
else:
    print("not a perfect number")

lcm and gcd
import math
a=int(input("enter a value:"))
b=int(input("enter b value:"))
gcd=math.gcd(a,b)
lcm=(a*b)/gcd
print("gcd of two numbers is",gcd)
print("lcm of two numbers is",lcm)

a=int(input("enter a value:"))
b=int(input("enter b value:"))
print(f"before swaapping of a and b is {a},{b}")
a,b=b,a
print(f"after swapping of a nd b is {a},{b}")

n=int(input("enter any number:"))
for i in range(1,21):
    print(f"{n} X {i} = {n*i}")
    
n=int(input("enter any number:"))
if n<=1:
    print("not a prime number")
else:
    for i in range(2,n):
        if n%i==0:
            print("not a prime number")
    else:
        print("prime number",n)
        
start=int(input("enter the starting value:"))
end=int(input("enter the ending value:"))
for num in range(start,end):
    if num>1:
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                # print("there a no prime numbers you entered from the range of numbers!")
                break
        else:
            print(num,end=" ")




1. ATM GENERATOR

balance=6000
pin=7323
entered_pin=int(input("enter your atm pin:"))
if entered_pin==pin:
    while True:
        print("\n ---ATM MENU----")
        print("1.check balance")
        print("2.deposit money")
        print("3.withdraw money")
        print("4.exit")
        choice=int(input("enter your choice:"))
        if choice==1:
            print("your current balance amount is",balance)
        elif choice==2:
            deposit=int(input("enter how much money you want to deposit:"))
            balance=balance+deposit
            print("your amount succesfully credited to the account",balance)
        elif choice==3:
            amount=int(input("enter how much amount you want to withdraw:"))
            if amount<balance:
                print("please collect your cash:",balance)
            else:
                print("insufficient funds!")
        else:
            print("THANK YOU for visiting atm")




numbers = [10, 20, 30]
numbers.append([40])

print(len(numbers))






1. linear search
def linear(arr,target):
    f=False
    for i in range(len(arr)):
        if arr[i]==target:
            print("target element found at index",i)
            f=True
            break
    if not f:
        print("not found in the array")

a=list(map(int,input("enter any numbers:").split()))
t=int(input("enter target value:"))
print(linear(a,t))




def linear(arr,target):
    count=0
    for i in range(len(arr)):
        if arr[i]==target:
            count+=1
    return count

a=list(map(int,input("enter any numbers:").split()))
t=int(input("enter target value:"))
print(linear(a,t))




def linear(arr,target):
    f=False
    for i in range(len(arr)):
        if arr[i]==target:
            print("target element found at index",i)
            f=True
            break
    if not f:
        print("not found in the array")

a=list(map(int,input("enter any numbers:").split()))
t=int(input("enter target value:"))
print(linear(a,t))



l=list(map(int,input("enter:").split()))
target=int(input("enter target value:"))
k=-1
for i in range(len(l)):
    if l[i]==target:
        k=i
if k!=-1:
    print("the element of the index is",k)
else:
    print("not found in the list")

reverse string
s=list(map(int,input("enter any list:").split()))
i=0
j=len(s)-1
while i<j:
    s[i],s[j]=s[j],s[i]
    i+=1
    j-=1
print(s)

product of array except self
li=[1,2,3,4]
res=[]
for i in range(len(li)):
    p=1
    for j in range(len(li)):
        if i!=j:
            p*=li[j]
    res.append(p)
print(res)

k=[2,7,11,15]
target=int(input("enter target element to find:"))
i=0
j=len(k)-1
while i<j:
    if k[i]+k[j]==target:
        print(i,j)
        break
    elif k[i]+k[j]<target:
        i+=1
    else:
        j-=1


s=input("enter string:")/
s="loonbalxballpoon"
d={}
for i in s:
    d[i]=d.get(i,0)+1
b=d.get("b",0)
a=d.get("a",0)
l=d.get("l",0)//2
o=d.get("o",0)//2
n=d.get("n",0)
k=min(b,a,l,o,n)
print(k)
nums1=[1,2,3]
nums2=[0,0]
print(nums1+nums2)

s="pandduu"
d={}
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for i in d:
    print(i,":",d[i])


class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        d={'}':'{',      ']':'[',    ")":'('}
        for i in range(len(s)):
            if stack and s[i] in d and stack[-1]==d[s[i]]:
                stack.pop()
            else:
                stack.append(s[i])
        if stack:
            return False
        else:
            return True
        

  {   [    ]    }



product of array except self
s=input("enter any parenthesis:")
l=[]
d={']'   :'[',    '}'    :'{'    ,')'    :'('}
for i in range(len(s)):
    if l and s[i] in d and l[-1]==d[s[i]]:
        l.pop()
    else:
        l.append(s[i])
if l:
    print("not valid ")
else:
    print("valid parenthesis")   
    
product of array except self
l=[1,2,3,4,5]
res=[]
for i in range(len(l)):
    p=1
    for j in range(len(l)):
        if i!=j:
            p*=l[j]
    res.append(p)
print(res)

checking wheather the number is palindrome or not
n=int(input("enter :"))
rev=0
original=n
while n>0:
    d=n%10
    rev=rev*10+d
    n=n//10
print(rev)
if rev==original:
    print("palindrome number",rev)
else:
    print("not a palindrome number")
    
count of digits
n=int(input("enter any number:"))
if n==0:
    c=1
else:
    c=0
    while n>0:
        n=n//10
        c+=1
    print(c)

sum of digits
n=int(input("enter any number:"))
s=0
while n>0:
    k=n%10
    s=s+k
    n=n//10
print(s)


factorial number
n=int(input("enter any number:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)


fibonaci series
n=int(input("enter any number:"))
a=0
b=1
# count=0
for i in range(n):
    print(a,end=" ")
    c=a+b
    a=b
    b=c
    count+=1



prime number
n=int(input("enter any number:"))
prime=True
for i in range(2,int(n**0.5)+1):
    if n%i==0:
        prime=False
        break
if prime:
    print("given number is prime number",n)
else:
    print("not")



s=input("enter any string:").split()
stack=[]
for i in s:
    if i.isdigit():
        stack.append(int(i))
    else:
        b=stack.pop()
        a=stack.pop()
        if i=="+":
            k=a+b
            stack.append(k)
        elif i=="-":
            k=a-b
            stack.append(k)
        elif i=="*":
            k=a*b
            stack.append(k)
        else:
            k=a//b
            stack.append(k)
print(stack.pop())

great string
s=input("enter any str:")
stack=[]
for i in s:
    if stack and abs(ord(stack[-1])-ord(i))==32:
        stack.pop()
    else:
        stack.append(i)
k="".join(stack)
print("great string",k)
        
        
res=""
o=""
for i in s:
    if i.isalnum():
        res=res+i
    else:
        o=i+o
print(res+o)

buble sort
l=[32,11,45,63,77,1,42]
for i in range(len(l)):
    for j in range(len(l)-i-1):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
print(l)



merge sort
l1=[1,2,3,4]
l2=[5,6,7,8]
i=0
j=0
res=[]
while i<len(l1) and j<len(l2):
    if l1[i]<l2[j]:
        res.append(l1[i])
        i+=1
    else:
        res.append(l2[j])
        j+=1
while i<len(l1):
    res.append(l1[i])
    i+=1
while j<len(l2):
    res.append(l2[j])
    j+=1
print(res)




selection sort
arr=[9,4,1,3,2]
for i in range(len(arr)):
    mid_index=i
    for j in range(i+1,len(arr)):
        if arr[j]<arr[mid_index]:
            mid_index=j
    arr[i],arr[mid_index]=arr[mid_index],arr[i]
print(arr)



s=list(map(int,input("enter any number:").split()))
stack=[]
d={"}":"{",")":"(","]":"["}
for i in s:
    stack.append(i)
rev=""
while stack:
    k=stack.pop()
    rev=rev+k
print(rev)

for i in range(len(s)):
    if stack and s[i] in d and stack[-1]==d[s[i]]:
        stack.pop()
    else:
        stack.append(s[i])
if stack:
    print("not valid")
else:
    print("valid")


for i in range(len(s)):
    found=False
    for j in range(i+1,len(s)):
        if s[j]>s[i]:
            stack.append(s[j])
            found=True
            break
    if not found:
        stack.append(-1)
print(stack)


s=input("enter any expression:")
stack=[]
for i in s:
    if i.isdigit():
        stack.append(int(i))
    else:
        b=stack.pop()
        a=stack.pop()
        if i=="+":
            k=a+b
        elif i=="-":
            k=a-b
        elif i=="*":
            k=a*b
        else:
            k=a//b
        stack.append(k)
print(stack.pop())


s=input("enter")
rev=""
for i in s:
    rev=i+rev
print(rev)


s=input("enter:")
vowels=0
consonants=0
for i in s.lower():
    if i.isalpha():
        if i in "aeiou":
            vowels+=1
        else:
            consonants+=1
print(vowels)
print(consonants)

s=input("enter any str:")
d={}
for i in s:
    d[i]=d.get(i,0)+1
for i in d:
    # print(i,":",d[i])
    # if d[i]==1:
    #     print(i)
    #     break
    # print(f"{i}{d[i]}",end="")
    if d[i]==1:
        print(i)
        break


s=input("enter:")
k=input("enter:")
# d_s=""
# for i in s:
#     if i not in d_s:
#         d_s+=i
# print(d_s)
if sorted(s)==sorted(k):
    print("anagram")
else:
    print("not")


s=input("enter:")
longest=""
for i in range(len(s)):
    k=""
    for j in range(i,len(s)):
        if s[j] in k:
            break
        k=k+s[j]
    if len(k)>len(longest):
        longest=k
print("longest substring",longest)


l=[3,2,1,5,6,4]
for i in range(len(l)):
    for j in range(len(l)-i-1):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
print(l)



l1=[1,3,5,7]
l2=[2,4,6,8]
i=0
j=0
stack=[]
while i<len(l1) and j<len(l2):
    if l1[i]<l2[j]:
        stack.append(l1[i])
        i+=1
    else:
        stack.append(l2[j])
        j+=1
while i<len(l1):
    stack.append(l1[i])
    i+=1
while j<len(l2):
    stack.append(l2[j])
    j+=1
print(stack)


l=[4,5,2,25]
for i in range(len(l)):
    mid_val=i
    for j in range(i+1,len(l)):
        if l[j]<l[mid_val]:
            mid_val=j
            
    l[i],l[mid_val]=l[mid_val],l[i]
    
print(l)



n1=int(input("enter"))
n2=int(input("enter"))
while n2!=0:
    n1,n2=n2,n1%n2
# print()
print(n1)



l=[4,5,2,25]
res=[]
for i in range(len(l)):
    found=False
    for j in range(i+1,len(l)):
        if l[j]>l[i]:
            res.append(l[j])
            found=True
            break
    if not found:
        res.append(-1)
print(res)

arr=[1,5,3,9,7,8]
arr.sort()
print(arr[-2])



arr=list(map(int,input("enter any elements:").split()))
current_sum=0
max_sum=arr[0]
for i in arr:
    current_sum+=i
    if current_sum>max_sum:
        max_sum=current_sum
    if current_sum<0:
        current_sum=0
print(max_sum)



arr=list(map(int,input("enter any:").split()))
count=0
max_count=0
for i in arr:
    if i==1:
        count+=1
        if count>max_count:
            max_count=count
    else:
        count=0
print(max_count)
    
    
    
    
arr=list(map(int,input("enter:").split()))
prefix=[0]*len(arr)
prefix[0]=arr[0]
for i in range(1,len(arr)):
    prefix[i]=prefix[i-1]*arr[i]
print(prefix)
suffix=[0]*len(arr)
suffix[n-1]=arr[n-1]
for i in range(-2,-1,-1):
    suffix[i]=suffix[i+1]+arr[i]
print(suufox)


arr=[1,2,3,4]
res=[]
for i in range(len(arr)):
    p=1
    for j in range(i,len(arr)):
        if i!=j:
            p=p*arr[j]
    res.append(p)
print(res)


arr=list(map(int,input("enter any elements:").split()))
for i in range(len(arr)):
    leader=True
    for j in range(i+1,len(arr)):
        if arr[j]>arr[i]:
            leader=False
            break
    if leader:
        print(arr[i],end=" ")



arr=list(map(int,input("enter any elements:").split()))
arr.sort()
res=[]
for i in range(len(arr)-1):
    if i>0 and arr[i]==arr[i-1]:
        continue
    else:
        l=i+1
        r=len(arr)-1
        while l<r:
            val=arr[i]+arr[l]+arr[r]
            if val==0:
                res.append([arr[i],arr[l],arr[r]])
                l+=1
                while arr[l]==arr[l-1] and l<r:
                    l+=1
            elif val>0:
                r-=1
            else:
                l+=1
print(res)





