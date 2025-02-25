import time


def square(x):
    return x**2

def double(x):
    return x*2


nums = [1,2,3,4,5]

# TODO
# 함수 2개를 만들어서 num_square(), num_double()
#num_cal(nums, square or double)

def num_cal(nums, fun):
    start_time = time.time()
    print([fun(x) for x in nums])
    end_time = time.time()
    print(end_time - start_time)
    
num_cal(nums, square)
num_cal(nums, double)