def print_num(n: int):
    # base condition
    if n == 0:
        return
    
    # recurse
    print_num(n-1)
    # after previous function call
    print(n)

def main():
    print_num(3)


if __name__ == "__main__":
    main()
    print("Done")