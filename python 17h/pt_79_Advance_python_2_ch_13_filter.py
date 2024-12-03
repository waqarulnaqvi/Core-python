# Filter syntax: list(filter(greater_than_5,l))#l=list
# Function can  be a lambda function..
def greater_than_5(num):
    if num>=5:
        return True
    else:
        return False

g10=lambda num:num >10

l=[1,2,3,4,5,6,7,8,89,98]
print(list(filter(greater_than_5,l)))
print(list(filter(g10,l)))
        
