def fuel_check():
    while True:
        try:
            fraction = input("Fraction: ")
            Numerator, Denominator = fraction.split("/")
            Numerator = int(Numerator)
            Denominator = int(Denominator)
            if Denominator == 0:
                raise ZeroDivisionError
            if Numerator > Denominator or Denominator < 0 or Numerator < 0:
                raise ValueError
            
            return round((Numerator / Denominator) * 100)
        except (ValueError, ZeroDivisionError):
            pass
            
def main():
    percentage = fuel_check()
    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage}%")


main()