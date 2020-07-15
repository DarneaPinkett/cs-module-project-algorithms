'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here

    no_duplicate_lst = []
    for i in arr:
        if i not in no_duplicate_lst:
            no_duplicate_lst.append(i)
        else:
            no_duplicate_lst.remove(i)
    return no_duplicate_lst.pop()


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")