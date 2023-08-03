def compose_function(*functions):
    def inside_func(arg,i=0):
        if i >= len(functions):
            return arg
        new_arg = functions[i](arg)
        return inside_func(new_arg,i+1)
    return inside_func

#тестовые функции

def f(n):
    return n + 1
def g(n):
    return n + 2
def h(n):
    return n + 3

new_func = compose_function(f,g,h)

print(new_func(1))
