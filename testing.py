def generator():
    for i in range(101111):
        yield i

<<<<<<< HEAD
#changes commit

#remote generator changes
=======
#changes commit!

#remote generator changes!
>>>>>>> a013321b4e5cfccdca93092e3b6e6765e2215151

if __name__ == "__main__":
    for i in generator():
        print(i) 
