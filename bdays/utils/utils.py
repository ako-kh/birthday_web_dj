import datetime


def days_until_birthday(person):
    today = datetime.date.today()
    birthday = datetime.date(today.year, person.date.month, person.date.day)
    n_birthday = datetime.date(today.year + 1, person.date.month, person.date.day)

    return ((birthday if birthday > today else n_birthday) - today).days