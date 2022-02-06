<h1> List sorting and search using custom functions </h1>

This program takes a sequence of numbers separated by a space from user input #1.

It also asks for any number from user input #2.

It checks whether user entries are valid and raises errors in case of invalid entries.

The algorithm works as follows:
1.	It transforms user input #1 (sequence of numbers) into a list of numbers (floats)
2.	It sorts the list in ascending order using a custom sort function which uses merge sorting method
3.	It finds indices for numbers in the sorted list which are lesser and greater than user input #2.
4.	In case user input #2 is out of range of the sorted list, or it is it’s minimum or maximum value, the user gets a proper message about this.

Custom function for binary search is used here.
