# a function that will check whether its time for breakfast, lunch or dinner
def main():
    time_str = input("What Time is it? ")
    meal_time = check_meal_time(time_str)
    if meal_time:
        print(meal_time)

#now define meal time such that it retuns breakfast , lunch or dinner
def convert(time):
    hours,minutes = map(int, time.split(":"))
    return hours + minutes/60

#now we need to combine this convert time or integrate it into check_meal_time function
def check_meal_time(time_str):
    time = convert(time_str)
    if 7 <= time < 8:
     return "breakfast time"
    elif 12 <= time < 13:
       return "lunch time"
    elif 18 <= time < 19:
       return "dinner time"
    else:
       return "none"
main()
