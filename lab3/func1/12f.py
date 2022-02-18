def histogram(a):
    for n in a:
        res = ''
        size = n
        while( size > 0 ):
          res += '*'
          size= size - 1
        print(res)

histogram([4, 9, 7])