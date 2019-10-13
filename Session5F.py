# Variable Arguments(tuple) and KeywordArguments(dictionary)
def fun(*args, **kwargs):
    print(args)
    print(kwargs)



a = int(input("Enter a"))

fun(a, 20, 30, 40, 50, "hello", a=10, b=20, c=30)

