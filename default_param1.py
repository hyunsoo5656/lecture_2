def div(a, b =2):
    return a/b


print('div() =', div(0))
# 위치인자로 넣은 결과
print('div(200, 5) =', div(200, 5))
print('div(6,3) =', div(6,3))

#위치인자 와 키워드 인자를 혼용
print('div(200, b=5) = ', div(200, b=5)) 
print('div(200, b=5) = ', div(a = 200, b=5))
print('div(b=5, a=200) = ', div(b=5, a=200))




#positional argument follows keyword argument
#print('div(b=5, 200) = ', div(b=5, 200))



print('div(b=6, a=3 =', div(b=6, a=3))



