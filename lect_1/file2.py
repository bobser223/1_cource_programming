class InitDekTest():

    def __init__(self):
        print("InitDelTest: __init__")

    def __del__(self):
        print("InitDelTest: __del__")

initDel = InitDekTest()