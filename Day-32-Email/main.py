import smtplib
import random
import datetime as dt

QUOTES_FILE = "./quotes.txt"
SEND_WHEN = 4


def get_random_motivational_quote(file_path):
    """This function returns one motivational quote from the file."""
    with open(file_path, "r") as f:
        return random.choice(f.readlines())


email_from = "mateusz.hyla.ff@gmail.com"
password_from = "<app_pass>"
random_quote = get_random_motivational_quote(QUOTES_FILE).replace("\n", "")

Days = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
}

with smtplib.SMTP("smtp.gmail.com") as conn:
    conn.starttls()
    conn.login(user=email_from, password=password_from)
    curr_week_day = dt.datetime.now().weekday()
    if curr_week_day == SEND_WHEN:
        try:
            conn.sendmail(from_addr=email_from,
                        to_addrs="mateusz.hyla.it@gmail.com",
                        msg=f"Subject:Motivational Quote From Mateusz Hyla.\n\n"
                            f"Here is your {Days[SEND_WHEN]} motivational quote:\n\n{random_quote}.")
        except:
            print("Email not sent. Something went wrong.")
        else:
            print("Email sent successfuly.")