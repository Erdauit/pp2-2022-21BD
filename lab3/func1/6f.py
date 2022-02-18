text = input()

def  to_reverse(text): 
    return ' '.join(text.split()[::-1])

result = to_reverse(text)
print(result)