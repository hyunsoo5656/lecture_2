def kwarg_param(**kwargs):

    print('인자의 개수', len(kwargs)) #len 개수 세기
    print('인자는 :', kwargs)
    print('key값은 : ', kwargs.keys())
    print('key값은 : ', kwargs.values())
kwarg_param(first = 'a', second = 'b', third = 'c')






