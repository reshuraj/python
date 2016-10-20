def compose2(f,g):
    return lambda x:f(g(x))
def double(x):
    return x*2
def inc(x):
    return x+1
inc_and_double=compose2(double,inc)
print inc_and_double(10)
