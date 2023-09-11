import datetime


def get_n_days_date_before_excluding_weekends(n):
    date_now = datetime.datetime.now()
    delta = datetime.timedelta(days=n)
    n_day_before_day = (date_now - delta).date().weekday()
    n_day_before_date = (date_now - delta).date()

    # for weekends
    if n == 1:
        # if is saturday
        if n_day_before_day == 5:
            n += 1
            delta = datetime.timedelta(days=n)
            n_day_before_date = (date_now - delta).date()
        elif n_day_before_day == 6:
            n += 2
            delta = datetime.timedelta(days=n)
            n_day_before_date = (date_now - delta).date()
    elif n == 2:
        # if is sunday
        if n_day_before_day == 5:
            n += 2
            delta = datetime.timedelta(days=n)
            n_day_before_date = (date_now - delta).date()
        elif n_day_before_day == 6:
            n += 3
            delta = datetime.timedelta(days=n)
            n_day_before_date = (date_now - delta).date()

    return str(n_day_before_date)


print(get_n_days_date_before_excluding_weekends(2))
