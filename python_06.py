list_1 = ['h', 'a', 'p', 'p', 'y']
word = 'happy'
list_2 = list(word)
print(list_1)
print(list_2)

country = ['USA', 'Brasil', 'UK', 'Germany', 'Turkey', 'New Zealand']
print(country)

string_1 = 'I quit smoking'
new_list_1 = list(string_1) # we created multi element list
print(new_list_1)
new_list_2 = [string_1] # this is a single element list
print(new_list_2)

mixed_list = [11, 'Joseph', False, 3.14, None, [1, 2, 3]]

my_list = ['Joseph', 'Clarusway', 2020]
new_list1 = list(my_list) # what will be the output?
new_list2 = [my_list]# what will be the output?
print(new_list1)
print(len(new_list1))# what is the length of the variable?
print(new_list2)
print(len(new_list2))

listem = [1,2,3]
len(listem)
list(listem)

a = [[1,2,3], ['ali' , 'ayse'], [True, False]]
len(a)
liste_a = [a]

my_list1 = ["2023's perfect"]
my_list2 = list("2023's perfect")
print(my_list1)
print(my_list2)

city = ['Addis Ababa' , 'Istanbul', 'New York', 'Seoul' , 'Stockholm', 'Sydney' ]
print(len(city))

numbers = [1, 4, 7]
numbers. append(9)
numbers.append('9')
print (numbers)

empty_list = []
empty_list.append(6666)
empty_list. append('Multiverse')
empty_list. append([0])
print(empty_list)

city = ['New York' , 'London' , 'Istanbul' , 'Seoul' , 'Sydney' ]
city. append('Addis Ababa')
print(city)

numbers = []
numbers.append(1)
numbers. append(2)
numbers. append(3)
numbers. append(4)
print(numbers)

numbers = [1, 4, 7]
numbers.insert(2, 9)
print(numbers)
numbers.insert(2, 6)
print (numbers)

city = [ 'New York' , 'London' , 'Istanbul', 'Seoul', 'Sydney', 'Addis Ababa' ]
city. insert(2, 'Stockholm' )
print(city)

listem = ['a', 'b', 'c', 'd']
listem.insert(3,12)

numbers = [1, 2, 3, 4]
numbers.insert(4, 5)
print (numbers)

listem = [1,2,3,4]
listem.insert(-1,5)

numbers = [1, 4, 7, 9]
numbers.remove(7)
print(numbers)
numbers.remove(9)

city = ['New York' , 'London' , 'Stockholm', 'Istanbul' , 'Seoul' , 'Sydney' , 'Addis Ababa' ]
city. remove( 'London' )
print(city) # we have deleted 'London'

listem = [1,2,3,4,2,3,4,3]
listem.remove(2)
listem.pop()

listem = ['a', 'b', 'c', 'd']
listem.remove('c')

a = [1, 4, 7, 9, '9', ['a', 'b', 'c']]

numbers = [4, 1, 9, 7]
numbers.sort()
print(numbers)

city = [ 'New York', 'Stockholm', 'Istanbul', 'Seoul' , 'Sydney', 'Addis Ababa' ]
city.sort() # lists the items in alphabetical order
print(city)

print('Clarus'+"""Way""")

word = 'Clarus'
word += '\tWay'
print(word)

city = 'Chicago'
print(city[ ::- 1])

city = "Chicago"
print(city[-1])

fruit = 'apple'
vegetable = 'spinach'
print('I ate {} and {} ' . format(fruit, vegetable))

fruit1 = 'Banana'
fruit2 = 'Peach'
print(2*fruit1 + '+' + 3*fruit2)

Fruit = 'apple'
vegetable = 'spinach'
output = f"We bought {fruit} and {vegetable}"
print(output)

ord('*')
ord('@')
ord('F')
list_3 = [True, False]

city = ['Addis Ababa' , 'Istanbul', 'New York' , 'Seoul' , 'Stockholm' , 'Sydney' ]
print(len(city))

isimler = ['veli', 'ali', 'ayse', 'kemal' ]
sorted(isimler)
['ali', 'ayse', 'kemal', 'veli']
isimler = sorted(isimler)

word = ['h', 'a', 'p', 'p', 'y']
print(word[1])

colors = ['red', 'purple' , 'blue' , 'yellow', 'green' ]
print(colors[2]) # If we start at zero,
# the second element will be 'blue'.

city = ['New York', 'London', 'Istanbul', 'Seoul' , 'Sydney' ]
city_list = []
city_list. append(city) # we have created a nested list
print(city_list)

city_list = ['New York', 'London' , 'Istanbul' , 'Seoul' , 'Sydney' ]
print(city_list[0]) # access to first and only element

city_list = [ 'New York' , 'London', 'Istanbul' , 'Seoul' , 'Sydney' ]
print(city_list[0][2])