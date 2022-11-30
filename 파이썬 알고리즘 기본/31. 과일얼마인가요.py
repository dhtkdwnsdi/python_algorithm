fruits={'사과':1200, '배':2000, '감':800, '망고':1500, '귤':2500}
a = input()
if a in fruits :
    print('{}:{}원'.format(a, fruits[a]))
else :
    print('판매하지 않습니다.')