"""Complete the function/method (depending on the language) to return False/True when its argument is an array that has the same nesting structures and same corresponding length of nested arrays as the first array.

For example:

# should return True
same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] )

# should return False
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] )

# should return True
same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] )

# should return False
same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] )"""

original = [ 1, [ 1, 1 ] ]
other = [ 2, [ 2, 2 ] ]

original_tuple = tuple(original)
other_tuple = tuple(other)
answer = True
for_ex = []
for_ex_t = ()
for_ex_str = "dsad"

counter = 0
while counter != len(original_tuple):
    if type(original_tuple[counter]) == type(other_tuple[counter]):

        # Проверка каждого элемента в исходном значении на то, что это либо словарь, либо list, либо строка
        if type((original_tuple[counter])) == type(for_ex):
            if len(original_tuple[counter]) != len(other_tuple[counter]):
                answer = False
                break

        if type((original_tuple[counter])) == type(for_ex_t):
            if len(original_tuple[counter]) != len(other_tuple[counter]):
                answer = False
                break

        if type((original_tuple[counter])) == type(for_ex_str):
            if len(original_tuple[counter]) != len(other_tuple[counter]):
                answer = False
                break

                # print(1)
    else:
        answer = False
        break
    counter += 1
print(answer)
