import multiprocessing

def cal_square(numbers, result, v):
    v.value = 5.67
    for idx,n in enumerate(numbers):
        result[idx]=n*n


if __name__ == "__main__":
    numbers = [2,3,8,9]
    result = multiprocessing.Array('i',4)
    v = multiprocessing.Value('d',0.0)
    p = multiprocessing.Process(target=cal_square, args=(numbers, result, v))

    p.start()
    p.join()
    print(result[:])
    print(v.value)