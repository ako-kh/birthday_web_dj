import datetime


def days_until_birthday(person):
    today = datetime.date.today()
    birthday = datetime.date(today.year, person.date.month, person.date.day)
    days_left = birthday - today
    return days_left.days