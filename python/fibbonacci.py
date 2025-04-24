def fibbonacci(n:int):
    if n==0:
        return 0
    if n==1:
        return 1
    
    res=fibbonacci(n-2) + fibbonacci(n-1)
    return res



if __name__ == "__main__":
    total = fibbonacci(4)
    print(total)