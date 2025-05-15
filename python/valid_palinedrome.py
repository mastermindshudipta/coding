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
    input="noon"
    print(is_palindrome(input))


##

def is_palindromeOne(wordOne:str):
    l=0
    r=len(wordOne)-1

    while l<r:
        if wordOne[l]==wordOne[r]:
            l=l+1
            r=r-1
        else:
            return False
        
    return True

if __name__ == "__main__":
    inputOne="soon"
    print(is_palindromeOne(inputOne))

##

def is_palindromeTwo(wordTwo:str):
    l=0
    r=len(wordTwo)-1

    while l<r:
        if wordTwo[l]==wordTwo[r]:
            l=l+1
            r=r-1
        else:
            return False
        
    return True

if __name__ == "__main__":
    inputTwo="radar"
    print(is_palindromeTwo(inputTwo))


##

def is_palindromeThree(wordThree:str):
    l=0
    r=len(wordThree)-1

    while l<r:
        if wordThree[l]==wordThree[r]:
            l=l+1
            r=r-1
        else:
            return False
        
    return True

if __name__ == "__main__":
    inputThree="redar"
    print(is_palindromeThree(inputThree))

##

def is_palindromeFour(wordFour:str):
    l=0
    r=len(wordFour)-1

    while l<r:
        if wordFour[l]==wordFour[r]:
            l=l+1
            r=r-1
        else:
            return False
        
    return True

if __name__ == "__main__":
    inputFour="level"
    print(is_palindromeFour(inputFour))
##

def is_palindromeFive(wordFive:str):
    l=0
    r=len(wordFive)-1

    while l<r:
        if wordFive[l]==wordFive[r]:
            l=l+1
            r=r-1
        else:
            return False
        
    return True

if __name__ == "__main__":
    inputFive="civic"
    print(is_palindromeFive(inputFive))




