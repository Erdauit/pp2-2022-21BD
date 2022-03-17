import os 

def exists(filename):
    if os.path.exists(filename):
        return True
    else:
        return False


a = r'C:\Users\Админ\Desktop\Python\erdau.txt'
print(exists(a))
print(a)