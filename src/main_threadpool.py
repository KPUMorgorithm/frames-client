from concurrent.futures import ThreadPoolExecutor
from typing import Callable
from client.src.singleton_instance import SingletonInstane

class MainThreadPool(ThreadPoolExecutor, metaclass = SingletonInstane):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print("threadpool 생성됨")
        self.futures = []
        self.closeFuncs = []

    def addThreadPool(self, func : Callable):
        self.futures.append(self.submit(func))

    def addKillThreadFunc(self, func : Callable):
        self.closeFuncs.append(func)
    
    def killAllThread(self):
        for func in self.closeFuncs:
            print(func)
            func()