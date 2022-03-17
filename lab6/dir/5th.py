list = ['erdauit', 'aliyar', 'nurbek', 'riza']
a = open('listappender.txt', 'w')
for i in list:
    a.write('\n'+i)

a.close()
