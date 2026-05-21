squares = []
for i in range(1,7):
    squares.append(i*i)
    print(squares)
    my_list = list(range(10))
    print(my_list)

L = [1, 2, 3, 4, 5]
L2 = [x**2 for x in L]
print(L2)

L3 = [ x for x in L if x % 2 == 0]
print(L3)

tuple = (1, 2, 3, "a", "b", "c")
print(len(tuple))
print(tuple[0])
print(tuple[4])


dict ={"name": " markus ", "age": 32, "city": "hamburg"}
print(dict)


new_dict = {**dict, 'country': 'germany'}
print(new_dict)