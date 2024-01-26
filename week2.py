lucky_number = 13
# 13 is an integer
price = 2.99
# float is an approximate number it is not an integer

print('lucky number is:', type(lucky_number))
print('price is:', type(price))

# boolean True or False
likes_carrots = True
likes_broccoli = False
likes_new_veggie = None
# None is equivalent of null
print('likes carrot is a:', type(likes_carrots))
print('likes new veggie is a:', type(likes_new_veggie))

# augmented assignment
# shorthand arithmetic

stein = 1
pint = 1
print('original value of stein', stein)
# regular long hand syntax
stein = stein + pint
print('new value of stein', stein)

# shorthand syntax
stein += pint
print('newest value of stein', stein)

stein -= 2
print('newest value of stein', stein)

# operator overloading is language specific

lucky_number = 13
remainder = lucky_number % 2
print(remainder)

if remainder == 0:
    print('your lucky number is even')
    # print('your lucky number is', lucky_number)
else:
    print('your lucky number is odd')
    # print('your lucky number is', lucky_number)
print('your lucky number is', lucky_number)
# DRY do not repeat yourself

# python data types
# strings

first_name = "Yulianna"
last_name = 'Garcia'
full_name = first_name + " " + last_name
print(full_name)

sentence = "mr khan's bike"
sentence2 = 'bart shouted "boo"'
sentence3 = """bart's shouted "boo"""""

# collection types
# tuples, lists and dictionary
# tuples
name_tuple = 'abiola', 'anagha', 'jen'
print(name_tuple)
print(type(name_tuple))

# list
name_list = ['bec', 'jiya', 'cherina']
print(type(name_list))

# sets collection of unique things no duplication
name_set = {'cally', 'katy', 'leticia'}
print(name_set)
print(type(name_set))

name_set = {'cally', 'katy', 'leticia', 'katy'}
print(name_set)
print(type(name_set))

lucky_number_dictionary = {'minahil': 17, 'rana': 8, 'shuje': 7}
print(lucky_number_dictionary)
print(type(lucky_number_dictionary))

# sequence remembers the order of its items

# immutable unchangeable
# mutable changeable


# concatenating string and integer
# print('minahils lucky number is' + 17)
print('minahils lucky number is' + str(17))

# conditional statement
# if
# elif
# else
print(lucky_number)

if lucky_number > 20:
    print("your lucky number is not greater than 20")
elif lucky_number > 10:
    print("your lucky number is greater than 10")
else:
    print("your lucky number is not greater than 10")


if 'Yulianna' in name_list:
    print("she is in the list")
else:
    print("she is not in the list")

list_a = ['one','two', 'three']
list_b = ['four', 'five']
list_c = ['one','two', 'three']

if list_a == list_b:
    print('(a and b) they are the same')
elif  list_a == list_c:
    print('(a and c) they are the same')

    if list_a is list_c:
        print('(a and c with "is") they are the same')
    else:
        print('they are different')

# is is reference equality
# == is value equality
number = 5
distance = 20
if 0 < number < 42 < distance:
    print(" number and distance are within range")
else:
    print("number and distance are out of range")

if 0 < number and number < 42 and   42 < distance:
    print(" number and distance are within range")
else:
    print("number and distance are out of range")

if 0 < number < 42 and distance !=20:
    print(" number and distance are within range")
else:
    print("number and distance are out of range")