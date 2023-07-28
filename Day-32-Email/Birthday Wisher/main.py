import datetime as dt
import random
import smtplib
import pandas as pd

BIRTHDAY_FILE = "./birthdays.csv"


def is_someones_birthday(file_path):
    """This function returns True if there is someones birthday."""
    day = dt.datetime.now().day
    month = dt.datetime.now().month
    df = pd.read_csv(file_path, delimiter='\t', header=None)
    return df


email_from = "mateusz.hyla.ff@gmail.com"
password_from = "<app_password>"
is_birthday = is_someones_birthday(BIRTHDAY_FILE)
print(is_birthday)

# with smtplib.SMTP("smtp.gmail.com") as conn:
#     conn.starttls()
#     conn.login(user=email_from, password=password_from)
#     curr_week_day = dt.datetime.now().weekday()
#     if curr_week_day == SEND_WHEN:
#         try:
#             conn.sendmail(from_addr=email_from,
#                           to_addrs="mateusz.hyla.it@gmail.com",
#                           msg=f"Subject:Title.\n\nBody.")
#         except:
#             print("Email not sent. Something went wrong.")
#         else:
#             print("Email sent successfuly.")
