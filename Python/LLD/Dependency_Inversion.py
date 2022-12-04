# def add(arr):
#     return sum(arr)





def wrap_hello(fn):
    def wrapper():
        print("HELLO FROM THE WRAPPER")
        fn()
        return "DONE"
    
    return wrapper

@wrap_hello
def hello():
    print("HELLO FROM MAIN")

improved_hello = wrap_hello(hello)

print(hello())