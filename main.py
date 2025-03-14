from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
# 문제 1
def read_root():
    a = [1,2,3,4]
    b = [5,6,7,8]
    # TODO 배열 더하기
    result = []
    for i in range(len(a)):
        result.append(a[i]+b[i])
    return {"Hello": result}


@app.get("/two-dimensional-array")
# 문제 2
def two_dimensional_array():
    a = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    b = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ]

    result = []
    for i in range(len(a)):
        c = []
        for j in range(len(a)):
            c.append(a[i][j] + b[i][j])
        result.append(c)
    
    # TODO
    #[[10, 10, 10],
    #[10, 10, 10],
    #[10, 10, 10]]

    return {"result": result}


import random
import time
import numpy as np

# 상수
N = 10**4  # 1만 개 요소

@app.get("/add-count-large-arrays-python")
# 문제 3
def add_large_arrays_python():
    start_creation_time = time.time()
    a, b = gen_r_array_choices(N)
    end_creation_time = time.time()

    add_start_time = time.time()
    plus_py(a,b)
    add_end_time = time.time()
    
    array_creation_time = end_creation_time - start_creation_time
    addition_time = add_end_time - add_start_time
    return array_creation_time, addition_time

@app.get("/add-count-large-arrays-numpy")
def add_large_arrays_numpy():
    start_creation_time = time.time()
    a, b = gen_r_array_numpy(N)
    end_creation_time = time.time()
    
    add_start_time = time.time()
    plus_numpy(a,b)
    add_end_time = time.time()
    
    array_creation_time = end_creation_time - start_creation_time
    addition_time = add_end_time - add_start_time
    return array_creation_time, addition_time
    
# TODO - 고차 함수 이용하기 

def gen_r_array_choices(N):
    a = random.choices(range(101), k=N)
    b = random.choices(range(101), k=N)
    return a, b

def gen_r_array_numpy(N):
    a = np.random.randint(1, 101, size=N)  # 1 이상 100 이하의 정수
    b = np.random.randint(1, 101, size=N)
    return a,b

def plus_py(a, b):
    result = []
    for x, y in zip(a, b):
        result.append(x + y)
    return result

def plus_numpy(a, b):
    return a + b


#def add_arrays(N, fun):
    # 랜덤한 1차원 배열 2개 생성성
    start_creation_time = time.time()
    a, b = fun(N)
    end_creation_time = time.time()
    
    # 실행 시간 측정 시작
    add_start_time = time.time()
    # 요소별 덧셈
    result = []
    for x, y in zip(a, b):
        result.append(x + y)
     
    # 실행 시간 측정 종료
    add_end_time = time.time()
    
    # 수행 시간 리턴
    # 리턴값: 배열 생성 시간(array_creation_time)과 덧셈 수행(addition_time) 시간을 각각 리턴
    array_creation_time = end_creation_time - start_creation_time
    addition_time = add_end_time - add_start_time
    return array_creation_time, addition_time


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
