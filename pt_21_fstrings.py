letter="Hey my name is {} and I am from {}"
country="India"
name="Waqarul"
print(letter.format(name,country))
print(letter.format(name,334))

letter="Hey my name is {1} and I am from {0}"
country="India"
name="Waqarul"
print(letter.format(country,name))
print(letter.format(3434,name))

# f string:
print(f"Hey my name is {name} and I am from {country}")
txt="For only {price:.2f} dollars!"
print(txt.format(price =49.09999999))

p=49.099999
txt=f"For only {p:.22f} dollars!" #it is newly inserted in python 3.6 onwards.
print(txt)
print(f"{2*38}")
print(type(f"{2*38}"))

print(f"We use f-strings like this: Hey my name is {name} and I am from {country}")
print(f"We use f-strings like this: Hey my name is {{name}} and I am from {{country}}")


