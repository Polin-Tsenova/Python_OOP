def type_check(type):
    def decorator(func):
        def wrapper(args):
            if isinstance(args, type):
                return func(args)
            else:
                return 'Bad Type'
        return wrapper
    return decorator


@type_check(int)
def times2(num):
    return num*2
print(times2(2)) # 4
print(times2('Not A Number')) #Bad Type


@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World')) #H
print(first_letter(['Not', 'A', 'String']))#Bad Type

