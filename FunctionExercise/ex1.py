def convert_to_days():
    global hours, minutes, seconds
    hours = int(input("Enter number of hours:"))
    minutes = int(input("Enter number of minutes:"))
    seconds = int(input("Enter number of seconds:"))
    get_days()

def get_days ():
    num = (hours/24) + (minutes/1440) + (seconds/86400)
    print(round(num, 4))

convert_to_days()