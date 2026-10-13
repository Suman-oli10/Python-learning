# Without walrus
n = len([1, 2, 3])
if n > 2:
    print(n)

# With walrus
if (n := len([1, 2, 3])) > 2:
    print(n)