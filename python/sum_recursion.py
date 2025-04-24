# N summation

def sum_calculate(n:int):
    if n==1:
        return 1
    total=n+ sum_calculate(n-1)
    return total



def main():
    total=sum_calculate(10)
    print(total)


if __name__ == "__main__":
    main()


# N _ division.

def div_res(n:int):
    if n==1:
        return 1
    result= n / div_res(n-1)
    return result


def main():
    result=div_res(10)
    print(result)
if __name__ == "__main__":  
    main()
