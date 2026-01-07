var1 = 50 # this is a global variable
var2 = 60 # this is a global variable
def myfunction():
   "Change values of global variables"
   global var2
   var1 = 100
   var2 = var2 + 20 + var1
   print ("globals():", globals())
   print ("locals():", locals())

myfunction()
print ("var1:",var1, "var2:",var2) #shows global variables with changed values