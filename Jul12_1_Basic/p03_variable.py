
a=10
print(a)
print(type(a))
print(id(a))

a = 20  
print(a)
print(type(a))
print(id(a))

p_str = 'Beaver'
print (p_str, type(p_str))
p_int = 10
print(p_int, type(p_int))
p_float=1.234
print(p_float, type(p_float))
p_bool = True
print(p_bool, type(p_bool))

p_list = [3,7,5]
print(p_list, type(p_list))

p_dict = {
    'name' : 'Beaver',
    'age' : 100
    }
print(p_dict, type(p_dict))
p_set = {6,7,4}
print(p_set, type(p_set))
p_tuple=(5,7,6)
print(p_tuple,type(p_tuple))

# 형 변환 (Type Casting)

d = 1
print(type(d), id(d))

d = str(d)
print(type(d), id(d))

e = False
e = int(e)
print(e)        # False = 0 / True = 1

# 키보드 입력받기 (keyboard input)
ki = input('키 : ')
print(ki,type(ki)) # input으로 가져오면 기본적으로 str

ki = float(ki)
print(ki,type(ki)) 

ki2 = float(input('몸무게 : '))
print(ki2, type(ki2))

a = 10
b = 10
print("==========")
print(id(a))
print(id(b))

