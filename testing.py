def generator():
    for i in range(101111):
        yield i

#changes commit!!!~~!

#remote generator changes!!!~~!

if __name__ == "__main__":
    for i in generator():
        print(i) 
