def greet():
    print("こんにちは")


def print_name(name):
    print(f"私の名前は{name}です")


def get_greet():
    return "おはようございます"


def add(a, b):
    if type(a) != int or type(b) != int:
        return "数値を入れてください"
    else:
        return a + b


print("Hello world")
greet()
print_name("やすお@58期")
print(get_greet())
print(add(1, 1))
