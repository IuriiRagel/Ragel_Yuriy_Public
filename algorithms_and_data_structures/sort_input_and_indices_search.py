""" This algorithm takes array of numbers from the user input separated by a space
Then it creates a list of numbers from the input provided and sorts them in ascending order into a new array.
It then asks for user to enter a single number. It then searches and displays indices of the lesser and greater
number in the array. In case the entered number is out of range of the array, it displays the message accordingly.
In the first block of code we define our functions for list sorting and binary search
Fist two functions -- merge_sort and merge use merge sort method to sort array in ascending order"""
def merge_sort(array):
    if len(array) < 2:
        return array[:]
    else:
        middle = len(array) // 2
        left = merge_sort(array[:middle])
        right = merge_sort(array[middle:])
        return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result

"""We use binary search method to look for a particular number in the SORTED list and return
index of left (or smaller) and right (greater) element from it.
We will be working with two cases:
a) number is in the sorted list (for example number '5' is in the list [1,3,5,8]
in this case we will be using function indices_search which will return indices of left
and right elements (1 and 4 respectively)

b) number is not in the sorted list, but within its range (for example number '4' and list [1,3,5,8]
in this case in order to find the indices of numbers which are less or more than '4', we would plug
the '4' into the list, and return index from the left and index of the plugged number (as it replaced the index
of the number greater than itself). For this case we will use function indices_search_2
"""

def indices_search(array, element, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if array[middle] == element:
        return middle-1, middle+1

    elif element < array[middle]:
        return indices_search(array, element, left, middle - 1)
    else:
        return indices_search(array, element, middle + 1, right)

def indices_search_2(array, element, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if array[middle] == element:
        return middle-1, middle

    elif element < array[middle]:
        return indices_search_2(array, element, left, middle - 1)
    else:
        return indices_search_2(array, element, middle + 1, right)

"""
Now to the fun part! Let's ask for the input and find the indices!
"""
a = input("Enter numbers separated by a space")
array = a.split()
# This will convert our input into a list of strings, which we need to convert into numbers
# We convert our list of strings into numbers using the 'for' loop
# We add try - except to raise an error message if the entry is incorrect

try:
    for i in range(len(array)):
        array[i] = float(array[i])

    print("The range entered is", array)

except:
    raise ValueError("Incorrect input")

array_sorted = merge_sort(array)
print("The sorted array is", array_sorted)

x = input("Enter number")

# Same for the number input -- we try to convert to float and raise an error if it occurs

try:
    x = float(x)
except:
    raise ValueError("This is not a number")

"""There are several scenarios we are working with:
1) Entered number x is out of range of the list -- we need to raise an error
2) Entered number x is maximum value in the list -- we need to notify and return the left index only
3) Entered number x is minimum value in the list -- we need to notify and return the left index only
4) Number x is within the list values -- search the number and return the indices
5) Number x is within the range, but not in the values -- we need to find and return indices of numbers
in the list which are smaller and larger than x
"""

#checking if number is out of range
if x > array_sorted[-1] or x < array_sorted[0]:
    print("Number is out of range")

#checking if number is max value
elif x == array_sorted[-1]:
    result = indices_search(array_sorted, x, 0, len(array_sorted))[0]
    print("This is the max number in the list, its left index is {}".format(result))

#checking if number is min value
elif x == array_sorted[0]:
    result = indices_search(array_sorted, x, 0, len(array_sorted))[1]
    print("This is the min number in the list, its right index is {}".format(result))

#if number is in the list
elif x in array_sorted:
    result = indices_search(array_sorted,x,0,len(array_sorted))
    print("The number is in the list, the left index is {}, the right index is {}".format(result[0],result[1]))

#if number is not in the list, but within its range:
else:
    array_sorted.append(x)
    array_sorted = merge_sort(array_sorted)
    result=indices_search_2(array_sorted,x,0,len(array_sorted))
    print("The number is not in the list, but within its range. The index of lesser number is {}, the index of greater number is {}".format(result[0],result[1]))