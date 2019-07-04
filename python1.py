def reversed(s):
 str=" "
 for i in s:
   str=i+str
 return str
s = "phani"
print("The original string  is : ",end="") 
print(s) 
print("The reversed string (using stack)is : ",end="")
print(reversed(s))       
