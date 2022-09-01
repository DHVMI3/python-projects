# def two_sum(array, sum):
#     for i in array:
#         if sum - i in array:
#             p = sum - i
#             if array.index(p) != array.index(i):
#                 print('(' + str(array.index(i)) + ',' + str(array.index(p)) + ')')
#copy()
def two_sum(array, sum):
    for i in array:
        if sum - i in array:                        #To make sure that there are 2 sums in the array
            p = sum - i
            if array.count(i) != 1:             #To avoid sumation of the same number if there is more than one of it
                array.remove(i)                     #if there is more than 1 of a number it removes it
                if p in array:                          #checking if sum - i is in the array with i removed
                    return '(' + str(array.index(i)) + ',' + str(array.index(p) + 1) + ')'
            else:
                if p in array and array.index(p) != array.index(i):          #this is for when there is only one of each number
                    return '(' + str(array.index(i)) + ',' + str(array.index(p)) + ')'

list = list(map(int, input('Enter the numbers: ').strip().split()))
target = int(input('Enter your target: '))

print(two_sum(list, target))
