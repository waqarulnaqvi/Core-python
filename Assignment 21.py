# Assignmet 21 (Dictionary)
# 6 28
# 7 14
# Problem:1
# dict1={'abc': 49, 1: 36, 2: 25, 4: 16, 3: 9, 5: 4, 6: 1, 7: 1}
# mul=1
# for i in dict1:
#     mul*=dict1.get(i)
#
# print(mul)

# Problem:2
# dict={'Red': 10, 'Green': 41, 'White': 22, 'Black': 3, 'Pink': 14, 'Yellow': 5}
# mykeys=list(dict.keys())
# mykeys.sort()
#
# sorted_dict={i:dict[i] for i in mykeys}
# print(sorted_dict)

# Problem:3
# dict1={'abc': 49, 1: 36, 2: 25, 4: 16, 3: 933, 5: 4, 6: -111, 7: 1}
# max_value=max(dict1.values())
# print("The maximum value in a dictionary is :",max_value)
# min_value=min(dict1.values())
# print("The minimum value in a dictionary is :",min_value)


# Problem:4
# dict1={'abc': 49, 1: 36, 2: 25, 4: 16, 3: 933, 5: 4, 6: 111, 7: 1}
# max=-121212121
# for i in dict1:
#     if dict1[i]>max:
#         max=dict1[i]
#
# print("The maximum value in a dictionary is :",max)
# min=121212121
# for i in dict1:
#     if dict1[i]<min:
#         min=dict1[i]
#
# print("The minimum value in a dictionary is :",min)

# Problem:5
# dict1={'abc': 49, 1: 36, 2: 25, 4: 16, 3: 933, 5: 4, 6: -111, 7: 1}
# if not dict1:
#     print("The dictioanry is empty")
# else:
#     print("The dictionary is not empty")
#
# # empty=not bool(dict1)
# # print(empty)
# # empty=not dict1
# # print(empty)

# Problem:6
# dict1={'a':200,'b':300,"c":400}
# dict2={'a':300,'b':500,"c":100}
# dict3={}
# for key1,key2 in zip(dict1,dict2):
#     if key1==key2:
#         dict3[key1]=dict1[key2]+dict2[key1]
# print(dict3)

# Problem:7
SampleData = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
output=set()
for i in SampleData:
    output.update(i.values())

print(output)

# Problem:8
import itertools

def generate_combinations(dictionary):
    keys = list(dictionary.keys())
    combinations = list(itertools.product(*(dictionary[key] for key in keys)))
    for combination in combinations:
        print(''.join(combination))

# Problem:9
data = {'1': ['a', 'b'], '2': ['c', 'd']}
generate_combinations(data)
def find_highest_values(dictionary, n):
    sorted_items = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    highest_values = sorted_items[:n]
    for key, value in highest_values:
        print(key, value)

# Example usage
scores = {'Alice': 85, 'Bob': 72, 'Charlie': 92, 'David': 68, 'Eve': 91}
find_highest_values(scores, 3)

# Problem:10
# from collections import Counter
# Sample= [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# result=Counter()
# for i in Sample:
#     result[i['item']]+=i['amount']
# print(result)
#
#

