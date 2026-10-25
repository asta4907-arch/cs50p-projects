"""Identify whether a time falls within a typical meal window."""


def convert(time):
    hours_text, minutes_text = time.split(":")
    hours, minutes = int(hours_text), int(minutes_text)
    if not 0 <= hours <= 23 or not 0 <= minutes <= 59:
        raise ValueError("Invalid 24-hour time.")
    return hours + minutes / 60


def check_meal_time(time_str):
    time = convert(time_str)
    if 7 <= time < 8:
        return "breakfast time"
    if 12 <= time < 13:
        return "lunch time"
    if 18 <= time < 19:
        return "dinner time"
    return None


def main():
    meal_time = check_meal_time(input("What time is it? "))
    if meal_time:
        print(meal_time)


if __name__ == "__main__":
    main()
