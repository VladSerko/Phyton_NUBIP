print('-'*50)
String = input("Input your string : ")
Numbers = []
Words = ''
length=len(String)
print('-'*50)
print('String : ' + String)
k=0
for i in range(length):
    j=String[i]
    if '0' <= j <= '9':
        Numbers.append(int(j))
        k+=1
        i+=1
    else:
        Words+=j
        i+=1
Words+=' '
print('-'*50)
print('Numbers : ' + str(Numbers))
print('String without numbers : ' + Words)
i=0
MaxNumber=0
for i in range(len(Numbers)):
        if Numbers[i]>MaxNumber:
            MaxNumber=Numbers[i]
            i+=1
        else:
            i+=1

Numbers2=[]
i=0
for i in range(len(Numbers)):
         if Numbers[i]!=MaxNumber:
              Numbers2.append(Numbers[i]**i)
              i+=1
         else:
              continue

print('-'*50)
print('Max number : ' + str(MaxNumber))
print('Numbers x**i without max : ' + str(Numbers2))
print('-'*50)
StringUpper=''
l=0
i=0
for i in range(len(Words)-1):
    j=Words[i+1]
    if j==' ':
        StringUpper+=Words[l].upper()
        StringUpper+=Words[l+1:i]
        StringUpper+=Words[i].upper()+' '
        l=i+2
        i+=1
    else:
        i+=1
print('String with upper : ' + StringUpper)
print('-'*50)
input()