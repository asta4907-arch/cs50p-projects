def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")  
    else:
        print("Invalid")   

def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if not s[0].isalpha() or not s[1].isalpha():
        return False
    if not s.isalnum():
        return False
    if any(char.isdigit() for char in s[2:]) and s[2] == '0':
        return False
    return True

main()
