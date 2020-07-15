def greet(*names):
    print(names)
    for name in names:
        print('안녕하세요', name, '씨')

greet('홍길동', '양만춘', '이순신')  #인자 3개
greet('James', 'Thomas')  #인자 2개