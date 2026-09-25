# Countdown Timer

import time

print("===== COUNTDOWN TIMER =====")

seconds = int(input("Enter countdown time in seconds: "))

if seconds < 0:
    print("Time cannot be negative.")

else:
    print("\nCountdown Started!")

    while seconds > 0:
        minutes = seconds // 60
        remaining_seconds = seconds % 60

        print(
            f"\rTime Remaining: {minutes:02d}:{remaining_seconds:02d}",
            end=""
        )

        time.sleep(1)
        seconds -= 1

    print("\rTime Remaining: 00:00")
    print("⏰ Time's Up!")