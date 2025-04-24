def recursion(n: int):
    if n == 0:
        return
    # total = recursion(n-1) ###
    recursion(n-1)
    print(n)   ####

def main():
    recursion(4)  ###

if __name__ == "__main__":
    main()