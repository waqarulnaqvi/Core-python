# functions and oops implement dry feature or WORA(Write Ones Run Anywhere).
# class memory ni leti hai classes blueprint create karti hai..memory is created only after object instantiation..
# classes name uses PascalNamingConvention in python,java etc
# variable,functions/methods name uses camelCaseNamingConvention in python,java etc
class Number: # class memory ni leti hai classes blueprint create karti hai. memory is allocated only after object instantiation..
    def sum(self):
        return self.a +self.b
num=Number()#object creation/instantiation..
# memory is allocated only after object instantiation..
num.a=23        
num.b=23
s=num.sum()
print(s)        