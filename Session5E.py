# Keyword Arguments

def fun(**kwargs):
    print(kwargs)
    print(type(kwargs))


fun(a=10, b=20, c=30)
fun(name="John", age=30, email="john@example.com")

# fun(10="John", 20="Fionna", 30="Mike") error