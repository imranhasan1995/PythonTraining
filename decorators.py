def my_function(x):
   print("The number is=",x)

def my_decorator(some_function,num):
   def wrapper(num):
      print("Inside wrapper to check odd/even")
      if num%2 == 0:
         ret= "Even"
      else:
         ret= "Odd!"
      some_function(num)
      return ret
   print ("wrapper function is called")
   return wrapper

no=10
my_function = my_decorator(my_function, no)
print ("It is ",my_function(no))

###    @classmethod Decorator    ####
class counter:
   count=0
   def __init__(self):
      print ("init called by ", self)
      counter.count=counter.count+1
      print ("count=",counter.count)
   @classmethod
   def showcount(cls):
      print ("called by ",cls)
      print ("count=",cls.count)

c1=counter()
c2=counter()
print ("class method called by object")
c1.showcount()
print ("class method called by class")
counter.showcount()


###   @staticmethod Decorator   ### 
class StaticCounter:
   count=0
   def __init__(self):
      print ("init called by ", self)
      StaticCounter.count=StaticCounter.count+1
      print ("count=",StaticCounter.count)
   @staticmethod
   def showcount():
      print ("count=",StaticCounter.count)

c1=StaticCounter()
c2=StaticCounter()
print ("class method called by object")
c1.showcount()
print ("class method called by class")
StaticCounter.showcount()

### @property Decorator ####

class car:
   def __init__(self, speed=40):
      self._speed=speed
      return
   @property
   def get_speed(self):
      return self._speed
   @get_speed.setter
   def speed(self, speed):
      if speed<0 or speed>100:
         print ("speed limit 0 to 100")
         return
      self._speed=speed
      return

c1=car()
print (c1.get_speed) #calls getter
c1.speed=60 #calls setter