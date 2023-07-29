import datetime as dt
import random
import smtplib
import pandas as pd
import os

BIRTHDAY_FILE = "./birthdays.csv"
LETTERS_DIR = "./letter_templates"


def get_letter_content(letters_dir_path):
    """This function returns a random letter content from a list of letters."""

    letters_no = len(os.listdir(letters_dir_path))
    letter_no = random.randrange(1, letters_no)
    file_name = f"letter_{letter_no}.txt"
    file_path = os.path.join(letters_dir_path, file_name)

    with open(file_path, "r") as f:
        return f.read()


def get_birthday_data(file_path):
    """This function returns True if there is someones birthday."""
    day = dt.datetime.now().day
    month = dt.datetime.now().month
    recipients_data = []

    df = pd.read_csv(file_path)
    for index, row in df.iterrows():
        df_day = row['day']
        df_month = row['month']
        df_name = row['name']
        df_year = row['year']
        df_email = row['email']

        if day == df_day and month == df_month:
            recipients_data.append((df_name, df_email, df_year))

    return recipients_data


email_from = "mateusz.hyla.ff@gmail.com"
password_from = "<app_pass>"
recipients_data = get_birthday_data(BIRTHDAY_FILE)

for idx, recipient in enumerate(recipients_data):
    idx += 1
    email_to = recipient[1]
    name_to = recipient[0]
    year_to = recipient[2]

    message = get_letter_content(LETTERS_DIR).replace("[NAME]", name_to)
    subject = "Happy Birthday Wishes!"

    with smtplib.SMTP("smtp.gmail.com") as conn:
        conn.starttls()
        conn.login(user=email_from, password=password_from)
        try:
            conn.sendmail(from_addr=email_from,
                          to_addrs=email_to,
                          msg=f"Subject:{subject}\n\n"
                              f"{message}.")
        except:
            print(f"Email not sent. Something went wrong with email no_{idx}.")
        else:
            print(f"[{idx}]Email sent successfuly.")
