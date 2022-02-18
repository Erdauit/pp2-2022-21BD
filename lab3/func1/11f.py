word = input()
def is_palindrome(word):
    if word == word[::-1]:
        print('YES')
        
    else:
        print('NO')
        

is_palindrome(word)