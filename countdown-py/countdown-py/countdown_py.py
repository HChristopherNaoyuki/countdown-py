import time

try:
    MY_TIME = int(input("Enter the time in seconds: "))

    if MY_TIME < 0:
        raise ValueError("Time must be a positive integer.")

    for x in range(MY_TIME, 0, -1):
        seconds = x % 60
        minutes = int(x / 60) % 60
        hours = int(x / 3600)
        print(f"{hours:02}:{minutes:02}:{seconds:02}")
        time.sleep(1)

    print("Time is up.")

except ValueError as ve:
    print(f"Invalid input: {ve}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
