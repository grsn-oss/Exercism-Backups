def is_valid(isbn):
# make the string into an array to make things easier to work with. Ignore "-" and any other letter except "X"
    arr_isbn = []
    for index in range(0,len(isbn)):
        if isbn[index].isdigit():
            arr_isbn.append(int(isbn[index]))
    
        if isbn[index] == 'X':
            arr_isbn.append(10)
# If there a letter other than X then cancel the process
        if isbn[index].isalpha() and not isbn[index] == 'X':
            return False

#To make a valid ISBN check, I need 10 digits.
    if len(arr_isbn) < 10 or len(arr_isbn)> 10:
        return False
#X can only exist as a check digit
    if 10 in arr_isbn[0:-1]:
        return False
        

#ISBN Calculation
    isbn_sum = 0
    count = 10
    for index2 in range(0,len(arr_isbn)):
        isbn_sum += arr_isbn[index2] * count
        count -= 1

    return isbn_sum % 11 == 0

