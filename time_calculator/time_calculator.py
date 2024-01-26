# --Time Calculator--


def add_time(start, duration, starting_day=""):
    days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]

    start_hour, start_minutes, start_period = start.replace(" ", ":").split(":")

    start_hour, start_minutes = int(start_hour), int(start_minutes)

    duration_hour, duration_minutes = [int(time) for time in duration.split(":")]

    new_time_minutes = str((start_minutes + duration_minutes) % 60)

    new_time_minutes = (
        "0" + new_time_minutes if len(new_time_minutes) == 1 else new_time_minutes
    )

    extra_hours = (start_minutes + duration_minutes) // 60

    new_time_hour = (start_hour + duration_hour + extra_hours) % 12

    new_time_hour = "12" if new_time_hour == 0 else str(new_time_hour)

    extra_days = (start_hour + duration_hour + extra_hours) // 24

    elapsed_periods = (start_hour + duration_hour + extra_hours) // 12

    if start_period == "AM":
        new_time_period = start_period if elapsed_periods % 2 == 0 else "PM"
    else:
        new_time_period = start_period if elapsed_periods % 2 == 0 else "AM"
        extra_days += 1 if elapsed_periods % 2 == 1 else 0

    new_time = f"{new_time_hour}:{new_time_minutes} {new_time_period}"

    if starting_day:
        starting_day = starting_day[0].upper() + starting_day[1:].lower()

        starting_day_number = days.index(starting_day) + 1

        new_time_day = days[((starting_day_number + extra_days) % 7) - 1]

        new_time += f", {new_time_day}"

    if extra_days > 0:
        new_time += " (next day)" if extra_days == 1 else f" ({extra_days} days later)"

    return new_time


if __name__ == "__main__":
    print(add_time("10:00 PM", "12:00"))
