# def outer_func(msg):
#     def inner_func():
#         print(msg)
#
#     return inner_func

def decorator_function(original_func):
    def wrapper_func():
        print(f'wrapper function before {original_func.__name__}')
        original_func()

    return wrapper_func

def decorator_func(original_func):
    def wrapper_func(*args, **kwargs):
        print(f'wrapper function before {original_func.__name__}')
        original_func(*args, **kwargs)

    return wrapper_func

class decorator_class(object):
    def __init__(self, original_func):
        self.original_func = original_func

    def __call__(self, *args, **kwargs):
        print(f'wrapper function before {self.original_func.__name__}')
        return self.original_func(*args, **kwargs)

@decorator_class
def display():
    print('Display function') 

@decorator_class
def display_info(name, age):
    print(f'The name and age are {name} and {age}')


display_info('John', 34)

display()



# decorated_display = decorator_function(display)
# decorated_display()


# hi_func = outer_func('Hi')
# bye_func = outer_func('Bye')
# hi_func()
# bye_func()
