def get_root(a,b,c):
    r1 = (-b +(b ** 2 - 4 *a *c) ** 0.5) /(2*a)
    r2 = (-b -(b ** 2 - 4 *a *c) ** 0.5) /(2*a)
    return [r1, r2]

# 한번에 전체를 반환받는 법
root1 = get_root(1,5,6)
print(root1)


# 각각을 따로 따로 반환 받는법
root1, root2 = get_root(1,5,6)
print('r1값은', root1)
print('r2값은', root2)




def div(a, b = 2):
    return a / b
print('div(4) =',div(4))
# 위치인자로 넣은 결과
print('div(200 , 5) =',div(200, 5))


#위치인자와키워드 인자를 혼용
print('div(200 , b=5) =',div(200, b=5))
print('div(a=200 , b=5) =',div(a=200, b=5))
print('div(b=5 , a=200) =',div(b=5, a=200))


# div() got an unexpected keyword argument 'bc'
# print('div(bc=5 , ac=200) =',div(bc=5, ac=200))
# SyntaxError: positional argument follows keyword argument
# print('div(b=5 , 200) =',div(b=5, 200))

