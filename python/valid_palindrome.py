def is_palindrome(word:str):
    l=0
    r=len(word)-1

    while l<r:
        if word[l]==word[r]:
            l=l+1
            r=r-1
        else:
            return False
        
    return True

if __name__ == "__main__":
    print(is_palindrome("noon"))
    print(is_palindrome("civic"))
    print(is_palindrome("madam"))
    print(is_palindrome("racecar"))
    print(is_palindrome("soon"))
