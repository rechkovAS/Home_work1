def test_function(x):
    a = x ** 3
    def inner_function():
        return print("Я в области видимости функции test_function")
    inner_function()
    inner_function()
    inner_function()
    return print(a)

test_function(2)
#inner_function()
# Traceback (most recent call last):
#   File "C:\Users\Алексей\PycharmProjects\Project2_prostranstvo_name\main.py", line 15, in <module>
#     inner_function()
#     ^^^^^^^^^^^^^^
# NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?