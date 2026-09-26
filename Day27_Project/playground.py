def add(*args):
    sum=0
    for n in args:
        sum+=n
    print(sum)

add(1,2,3,4,5,6,7,8)

def calc(n,**kwargs):
    for key,value in kwargs.items():
        print(key)
        print(value)
    print(kwargs["add"])
    n+=kwargs["add"]
    n*=kwargs["multiply"]
    print(n)

calc(2,add=3,multiply=5)

class car:
    def __init__(self,**kw):
        self.make=kw.get("make")#get function return none instead of error
        self.model=kw.get("model")

my_car=car(make="KIA",model="Cerato")
print(my_car.make)