# -*- coding:utf-8 -*- #
# @time 2019/12/2 17:55
# author:wangpengda
import multiprocessing
import time


def test(x):
    print(x)
    time.sleep(5)


if __name__ == '__main__':

    pool = multiprocessing.Pool(10)
    for i in range(10):
        pool.apply_async(test, args=(i,))  # 异步执行
        # pool.apply(test, args=(i,))  # 同步执行
    pool.close()  # 不在接受新的任务了，异步执行必须要有
    pool.join()   # 阻塞，异步执行必须要有
    print("end")
