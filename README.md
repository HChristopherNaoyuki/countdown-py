# Countdown Timer

This is a simple countdown timer script written in Python. The program takes an input time in seconds from the user and counts down to zero, displaying the remaining time in hours, minutes, and seconds format (HH:MM:SS).

## Features
- Accepts time input in seconds.
- Displays the countdown in a user-friendly HH:MM:SS format.
- Validates input to ensure it’s a positive integer.
- Includes error handling for invalid inputs and unexpected errors.
- Provides a "Time is up" message once the countdown is complete.

## Usage

1. Run the script.
2. Enter the desired time in seconds when prompted.
3. The timer will start counting down, and the remaining time will be displayed in the format `HH:MM:SS`.
4. Once the countdown finishes, the message "Time is up" will be displayed.

Example:
```
Enter the time in seconds: 120
00:02:00
00:01:59
...
00:00:01
Time is up.
```

## Error Handling
- If the input is not a positive integer, the program will raise an error and prompt the user with a message indicating the issue.
- Any unexpected errors during execution will also be caught and displayed to the user.

---
