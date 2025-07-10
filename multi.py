# multithreading을 사용함, 물리적으로 cpu코어를 활용하여 병렬처리

import multiprocessing
import time

if __name__ == "__main__":
    start = time.time() 
    print("=====start")  
    processes = []
    for n in range(5):
        p = multiprocessing.Process(target=long_task)  # 쓰레드 생성
        processes.append(p)  # 쓰레드 목록에 추가

    for P in processes:
        P.start()  # 쓰레드 시작
    for P in processes:
        P.join()  # 쓰레드가 끝날 때까지 기다림
    print("=====end")
    print(f"총 소요 시간: {time.time() - start:.2f}초")
