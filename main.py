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
#import numpy as np

@app.get("/add-large-arrays")
# 문제 3
def add_large_arrays():
    N = 10**6  # 100만 개 요소
    # 배열열 실행 시간 측정 시작
    array_start_time = time.time()
    
    # 랜덤한 1차원 배열 2개 생성
    array1 = [random.randint(0, 100) for _ in range(N)]
    array2 = [random.randint(0, 100) for _ in range(N)]
    # random.choice 로 바꿔서 속도 비교
    
    # numpy 이용 속도 비교
    #array1 = np.random.randint(0, 100, size=N)
    #array2 = np.random.randint(0, 100, size=N)

    # 배열 실행 시간 측정 종료료
    array_end_time = time.time()
    
    # 연산 실행 시간 측정 시작
    add_start_time = time.time()
    
    # 요소별 덧셈
    result = []
    for i in range(N):
        result.append(array1[i] + array2[i])
    #result = array1 + array2

    # 연산 실행 시간 측정 종료
    add_end_time = time.time()
    
    # 수행 시간 리턴
    return {
        "array_creation_time": array_end_time - array_start_time, 
        "execution_time": add_end_time - add_start_time
        }


@app.get("/add-large-arrays-choices")
def add_large_arrays_choices():
    N = 10**6  # 100만 개 요소
    # 배열열 실행 시간 측정 시작
    array_start_time = time.time()
    
    # 랜덤한 1차원 배열 2개 생성
    # random.choice 로 바꿔서 속도 비교
    array1 = random.choices(range(101), k=N)
    array2 = random.choices(range(101), k=N)
    
    # 배열 실행 시간 측정 종료료
    array_end_time = time.time()
    
    # 연산 실행 시간 측정 시작
    add_start_time = time.time()
    
    # 요소별 덧셈
    result = []
    for i in range(N):
        result.append(array1[i] + array2[i])
    #result = array1 + array2

    # 연산 실행 시간 측정 종료
    add_end_time = time.time()
    
    # 수행 시간 리턴
    return {
        "array_creation_time": array_end_time - array_start_time, 
        "execution_time": add_end_time - add_start_time
        }

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}