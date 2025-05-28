def generator():
    for i in range(101):
        yield i

if __name__ == "__main__":
    for i in generator():
        print(i) 