 # N addition factorial .............
def add_res(n:int):
    if n == 1:
        return 1
    
    total = n + add_res(n-1)
    return total

def main():
    res = add_res(5)
    print(res)



if __name__ == "__main__":
    main()


###

# N multiplication factorial ................


def mul_res(n:int):
    if n==1:
        return 1
    
    total = n * mul_res(n-1)
    return total


def main():
    res=mul_res(5)
    print(res)

if __name__ == "__main__":
    main()




