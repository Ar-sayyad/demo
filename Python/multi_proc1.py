import time
import multiprocessing

square_result=[]
def cal_square(numbers):
    global square_result
    for n in numbers:
        #time.sleep(5)
        #print("square "+ str(n*n))
        square_result.append(n*n)
    print("Within a Process Result: " + str(square_result))
#
# def cal_cube(numbers):
#     for n in numbers:
#         #time.sleep(5)
#         print("cube "+ str(n*n*n))


if __name__ == "__main__":
    arr = [2,3,8,9]
    p1 = multiprocessing.Process(target=cal_square, args=(arr,))
    # p2 = multiprocessing.Process(target=cal_cube, args=(arr,))

    p1.start()
    # p2.start()

    p1.join()
    # p2.join()
    print("Result: "+str(square_result))
    #print("Done!")