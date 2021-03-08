# Our program starts from here

# accepting the number of students or inputs
n=int(input())

# Initialising empty lists and one dictionary, which we use in later stages
a=[]
b=[]
l=[]
m=[]
t={}
c=[]

# Using for loops in order to accept the n students with n marks scored
for i in range(n):
  for j in range(0,2):
    b.append(input())
  a.append(b)
  b=[]
# Defining a function to remove nested lists and make one flat list
def reemovNestings(a): 
    for i in a: 
        if type(i) == list: 
            reemovNestings(i) #reemovNestings() function used to remove the nesting
        else: 
            b.append(i) 
reemovNestings(a) # here 'a' list consists of all student names and scores respectively.


# Using for loops to append student name and student marks in two different lists from 'a' list
for j in range(0,len(b)):
    if j%2==0:
       l.append(b[j])
    else:
       m.append(int(b[j]))
# Making a copy of the list which is required in later stage
c=m.copy()

c.sort(reverse= False) # Sorting a copied list of scores in assending order,So that the 2nd lowest score will be in [1] position of the list


# Using for loop in order to convert two above lists into one dictionary
for p in range(0,len(l)):
    t[l[p]]=m[p]
    
#Using for loop to iterate through the dictionary
for x,y in t.items():
    y=int(y)
    if y==c[1]:
       print(x)


#Thank You
