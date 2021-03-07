#A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
#Following are the criteria for checking the password:
#1. At least 1 letter between [a-z]
#2. At least 1 number between [0-9]
#3. At least 1 letter between [A-Z]
#4. At least 1 character from [$#@]
#5. Minimum length of transaction password: 6
#6. Maximum length of transaction password: 12
#Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
#Example
#If the following passwords are given as input to the program:
#ABd1234@1,a F1#,2w3E*,2We3345
#Then, the output of the program should be:
#ABd1234@1

#Hints:
#In case of input data being supplied to the question, it should be assumed to be a console input.


#Here is the code for the above problem.


a=input().split(',')
s=''
Alp=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
small=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
num=['1','2','3','4','5','6','7','8','9']
symbols=['`','~','!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','[','}','}','|',':',';','"','<','>','.','?','/']
for i in a:
  for j in Alp:
    for k in small:
       for m in num:
          for n in symbols:
             if j in str(i) and k in str(i) and m in str(i) and n in str(i) and len(i)>=6 and len(i)<=12:
                 if i not in s:
                    s+=i+'\n'
print(s)                
