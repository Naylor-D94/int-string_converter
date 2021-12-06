def ty(no):
    answer=""
    if no==20: answer=" Twenty"
    elif no==30: answer=" Thirty"
    elif no==40: answer=" Forty"
    elif no==50: answer=" Fifty"
    elif no==60: answer=" Sixty"
    elif no==70: answer=" Seventy"
    elif no==80: answer=" Eighty"
    elif no==90: answer=" Ninety"
    return answer

def ones(no):
    answer=""
    if no==1: answer=" One"
    elif no==2: answer=" Two"
    elif no==3: answer=" Three"
    elif no==4: answer=" Four"
    elif no==5: answer=" Five"
    elif no==6: answer=" Six"
    elif no==7: answer=" Seven"
    elif no==8: answer=" Eight"
    elif no==9: answer=" Nine"
    elif no==10: answer=" Ten"
    elif no==11: answer=" Eleven"
    elif no==12: answer=" Twelve"
    elif no==13: answer=" Thirteen"
    elif no==14: answer=" Fourteen"
    elif no==15: answer=" Fifteen"
    elif no==16: answer=" Sixteen"
    elif no==17: answer=" Seventeen"
    elif no==18: answer=" Eighteen"
    elif no==19: answer=" Nineteen"
    return answer

num=int(input("Enter a number:"))
result=""
if num>=1000:
    result=ones(int(num/1000))+" Thousand"
    num%=1000
if num>=100:
    result+=ones(int(num/100))+" Hundred"
    num%=100
if num>=20:
    result+=ty(int(num/10)*10)
    num%=10
if num>=1:
    result+=ones(num)    
print(result)
