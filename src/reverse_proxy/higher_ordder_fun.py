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

# Main.py 내용 고차 함수 만들기 

def generate_random_array_with_radint(N):
    return [random.randint(0, 100) for _ in range(N)]
    
def generate_random_array_with_choices(N):
    return random.choices(range(101), k=N)

    
def add_arrays(N, generate_random_array):
    #N = 10**6  # 100만 개 요소
    # 배열열 실행 시간 측정 시작
    array_start_time = time.time()
    
    # 랜덤한 1차원 배열 2개 생성
    array1 = generate_random_array(N)
    array2 = generate_random_array(N)
    
    # 배열 실행 시간 측정 종료료
    array_end_time = time.time()
    
    # 연산 실행 시간 측정 시작
    add_start_time = time.time()
    
    # 요소별 덧셈
    result = []
    for i in range(N):
        result.append(array1[i] + array2[i])
        
    # 연산 실행 시간 측정 종료
    add_end_time = time.time()
    
    # 수행 시간 리턴
    print(f"array_creation_time: {array_end_time - array_start_time}, execution_time: {add_end_time - add_start_time}")

add_arrays(10**6, generate_random_array_with_radint)
add_arrays(10**6, generate_random_array_with_choices)
