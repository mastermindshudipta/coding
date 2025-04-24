# N multiplication factorial

def mul_num(n: int):
    if n == 1:
        return 1
    
    res = n * mul_num(n-1)
    return res


def main():
    res = mul_num(4)
    print(res)

if __name__ == "__main__":
    main()


# N summation

def sum_rec(n:int):
    if n==1:
        return 1
    total=n + sum_rec(n-1)
    return total


def main():
    total=sum_rec(4)
    print(total)

if __name__ == "__main__":
    main()

