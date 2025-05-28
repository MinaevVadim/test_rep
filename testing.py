def generator():
<<<<<<< HEAD
    for i in range(101111):
=======
    for i in range(1000000):
>>>>>>> a0e2b98 (changes)
        yield i

#changes commit

if __name__ == "__main__":
    for i in generator():
        print(i) 
