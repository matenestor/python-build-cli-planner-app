import csv

from src.deadlined_reminders import DeadlinedReminder


def list_reminders():
    f = open("reminders.csv", "r")

    with f:
        reader = csv.reader(f)

        for row in reader:
            print()
            for e in row:
                print(e.ljust(32), end=' ')
        print()


def add_reminder(text, date, ReminderClass):
    reminder = ReminderClass(text, date)

    # Check whether an instance of a ReminderClass class is valid,
    # as opposed to the class itself done with 'issubclass()'.
    # Thus, do not make an assumption about the parameters taken by the
    # constructor ReminderClass(). Using 'isinstance()' would allow the
    # add_reminder() function to TODO? receive the instance directly, thus
    # delegating its construction to a code that knows how to do it better.
    if not isinstance(reminder, DeadlinedReminder):
        raise TypeError("Invalid Reminder Class")

    with open('reminders.csv', 'a+', newline='\n') as file:
        writer = csv.writer(file)
        writer.writerow(reminder)

