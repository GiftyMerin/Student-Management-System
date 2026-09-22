'''
x=13
print(x)
g='gifty'
print(g)

#data structures - list, tuple, set, dictionary

#list=['a','b','c','d','e',2]
print(list) 

#list operations
# 1. append()- adds an item to an already existing list
fruits=['apple','orange','banana']
fruits.append('grapes')
print(fruits) 

# 2. insert()- inserts an item according to the index number
fruits=['apple','orange','banana']
fruits.insert(1,'avocado')
print(fruits)   

# 3. extend()- extends another list to an already existing list
fruits=['apple','orange','banana']
fruits.extend(['pear','kiwi','mango'])
print(fruits)   

# 4. remove()- removes an item from the list
fruits=['apple','orange','banana']
fruits.remove('orange')
print(fruits)   

# 5. pop()- removes the last item from the list
fruits=['apple','orange','banana']
fruits.pop()
print(fruits)  

# 6. count()- gives the index number of the value 
fruits=['apple','orange','banana']
print(fruits.count('apple'))     

# 7. slicing()- slices the list
fruits=['apple','orange','banana']
print(fruits[0:2])  

tuple=(1,2,3,4,5)
print(tuple)
#len()- finds the length of the tuple
print(len(tuple))
#max()- finds the max value of the tuple
print(max(tuple))
#min()- finds the min value of the tuple
print(min(tuple))
#sum()- finds the sum of the total mathematical elements in the tuple
print(sum(tuple))    

dict={"colour":"red", "div":"A", "car":"Suzuki"}
print(dict)
dict["colour"]="green"
print(dict)    

#access-values
#access using keys
dict={"colour":"red", "div":"A", "car":"Suzuki"}
print(dict["colour"])
#access using get()- avoids KeyErrors
print(dict.get("colour"))
print(dict.get("city"))   

dict={"colour":"red", "div":"A", "car":"Suzuki"}

#adding new key-value pair
dict["city"]="Tokyo"
print(dict)

#update existing key
dict["city"]="New York"      

#remove existing key
dict={'colour': 'red', 'div': 'A', 'car': 'Suzuki', 'city': 'Tokyo'}
del dict["city"]
print(dict)

#remove last inserted item
dict.popitem()
print(dict)

#clear all items
dict.clear()
print(dict)     

set={'a','bulb','is','on','top','of','the','ladder'}
print(set)     

age=int(input("Enter your age: "))
if age>=18:
    print("You can vote.")
else:
    print("You cannot vote.")    
for i in range(10):
    print(i,end=" ")
    print()


def name():
    print("grrrr")
name()
li=[1,2,3,4,5,6]
print(li)       '''

#class li:
def Num(avg):
    if not avg:
        return 0
    return sum(avg)/len(avg)
li=[1,2,3,4,5,6,7,8,9]
result=Num(li)
print("The average of the list is: ",result)


