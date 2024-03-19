--------->DAY 8
'''
# ! Eg


def profile(name,age place):
     txt = "My name is {}.Iam {} years old. Iam from {}."
     print(txt.format(name,age,place))
profile("Raj",29,"cbe")    
     

# ! Eg:4
 ? Functions with return statement

# ! return
 1.)A variable declared inside the function can be accessed outside the function using return
 2.)return does not print anything
 3.)we cannot write any code below return  statement



 def f1():
     z = 8
 f1()
 print(z) # error ----> cannot use outside the function


 def f1(a,b):
     c = a*b
     return c
 print(f1(6, 8))
 obj = f1(6, 8)
 obj1 = f1(4, 6)

 def gracemark(object):
     print(output+4)
 gracemark(obj)
 gracemark(obj1)
'''

# ? problem:1 
def palindrome(n):
 string = str(n)
 rev = str(n)[::-1]
 if string==rev:
 print(n, "Palindrome")
else:
    print("Not palindrome")
  a = int(input("Enter the value:")
palindrome(a)

          

# ? Based on the declaration of parameters and args
# ? functions are divided into 5 catagories

 positional args
 keyword args
 default args
 variable length args
 keyword variable lenght args           


# * positional args
  Eg:1
 def profile(name,phone,mark):
     txt = "My name is{}.My phone number is {}.I got {} marks.
     print(txt.format(name, phone, mark))

 profile(9515686875, "raj", 97)# unexpected output


# * keyword args:
 ! Eg:1
 ? To overcome the disadvantages of position args, we use keyword args
 ? It is the process of initialising the parameters with args while callimng the function
 def profile(name, phone,mark))

 profile(name="Raj",123456789,mark=98) # error--> positional args follow keyword
 profile(123456789, name="Raj", mark=98) # error--> name has multiple values
 profile("Raj",mark= 98,phone=9515686875)



 # 1 Defualt args
 ! Eg:2
  def profile(name, photo, place="KADAPA"):
      if place == "Kadapa" or place=="KADAPA" or place=="Kadapa":
  txt = "My name is {}.My phone number is {}.I am from{}.
  print(txt.format(name,phone,place))
 else:
     profile("Yoy are not eligible to signup")
 proflie("Raj",9515686875)


 Exeption
 profile(name, photo, place="KADAPA"): # erroe --->coz default args shopuld not follow
                                        positional parameter
      if place == "Kadapa" or place=="KADAPA" or place=="Kadapa":
  txt = "My name is {}.My phone number is {}.I am from{}.
  print(txt.format(name,phone,place))
 else:
     profile("Yoy are not eligible to signup")
 proflie("Raj",9515686875)



# * Variable lenght params
# ! Eg:1


 To pass more than 1 arg to a parameters means we use variable length args
 To convert normal parameter to variable length param,add * or other paeram

  name = "Raj","name2","name3"
 def profile(*name):
     for val in name:
     print("My name is" ,val)
 profile("Raj",'name2','name3')          



#  Eg:2
 def profile(* name,age):
     for val in name:
         print("My name is",val,"my is age", age)
 profile(28, "Raj",'name2','name3',28) # error ----> age has no args        

 def profile(* age,*name):
     for val in name:
         print("My name is",val,"my is age", age)
 profile(28, "Raj",'name2','name3')        



# * keyword variable length args
  keywords ---> which is used to provide the args in the form of key value pair.
 ! Eg:1
 def price(price_list):
     print(price_list)

 price(shirt=1000, iphone=80000)

 n = 5
 {1:1,2:4, 3:9, 4:16, 5:25}


 n = int(input("Enter the number:"))
 


def dict1(n):
 d1 = {}
 for val in range (1, n+1):
     d1[val] = val**2
     print(d1)

dict1(5)    
     

# !------------> object oriented programming
The panadigms of obejects oriented programming are


# class
  objects
  inheritence
  polymorphism
  abstraction
  encapsulation

# ! Class is a blue print of an object 
  
l1 = [1, 2, 3, 4, 5, 6]



# ? Eg:1
 class c1:
     name = "Raju"

 print(name1)
 


# ? Eg:2
 class person:
     name = "Raju"


 c = person() # c os object
 The process of an object is called as Instatiation
 print(c.name)



# ? Eg:3
 create of a method
 When the functiopn is created with a class is called as method


 class person:
     def display(person): # It is a method
         print("Hello welcome to classes")

 p= person()
 p.display()


# ? Eg:4
# ! Method with parameter
 class person:
     def display(person,name,age):
         print(name,age)
         

 p= person()
 p.display("Raju",28)



 
# ! Eg:5

 class person:
     fname = "Raju" # attribute or static variable
     lname = "T"
     
     def first_name(self):
     
         print(self.fname)

     def full_name(self):
         print(self.fname+""+self.lname)
         
         
 p = person()
 p.display()
 p.full_name()


# ? Eg:6
 constructors --->_init_()
 This is special method wghich has the ebility to excute itself without
 calling it manually through the process of instatiation


 class profile:
     def_init_(self):# constructor method
         print("hey")

 p = profile() #execution of constructor throgh this process         
         




