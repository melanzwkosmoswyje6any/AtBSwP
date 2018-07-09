
# Write a function that takes a list value as argument and returns a string with all the items separated by comma
# and a space, with and inserted before the last item.


def func(param):
    a = ''
    for i in range(len(param)):
        if i != 0:
            a = a + ', ' + str(param[i])
        else:
            a = str(param[0])

    return str(a)


b = func(['A', 'B', 'C', 'D'])
