import time
import multiprocessing

def cal_square(numbers,q):
    for n in numbers:
        q.put(n*n)


if __name__ == "__main__":
    numbers = [2,3,8,9]
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=cal_square, args=(numbers,q))

    p.start()
    p.join()

    while q.empty() is False:
        print(q.get())