'''
Stephan and Sophia forget about security and use simple passwords for everything. 
Help Nikola develop a password security check module. 
The password will be considered strong enough if its length is greater than or equal to 10 symbols, it has at least one digit, as well as containing one uppercase letter and one lowercase letter in it. 
The password contains only ASCII latin letters or digits.

Input: A password as a string.
Output: Is the password safe or not as a boolean or any data type that can be converted and processed as a boolean. In the results you will see the converted results.
Precondition:
re.match("[a-zA-Z0-9]+", password)
0 < len(password) ≤ 64
'''

def checkio(data: str) -> bool:
    cond1 = True if len(data) >= 10 else False
    cond2 = any(char.isdigit() for char in data)
    cond3 = any(char.isupper() for char in data)
    cond4 = any(char.islower() for char in data)
    
    return cond1 and cond2 and cond3 and cond4

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")