def is_palindrome(string):
    a = word[::-1]
    if a==string:
        return "palindrome"
    else:
        return "not a palindrome"
    
    
if __name__=="__main__":
    word = "dsaasd"
    print(is_palindrome(word))
