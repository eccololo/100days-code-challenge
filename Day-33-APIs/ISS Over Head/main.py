import requests
import smtplib
from datetime import datetime
from tkinter import messagebox
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from time import sleep

MY_LAT = 50.064651  # Your latitude
MY_LONG = 19.944981  # Your longitude
EMAIL_TO = "mateusz.hyla.it@gmail.com"
EMAIL_FROM = "mateusz.hyla.ff@gmail.com"
APP_PASS = "<app_pass>"
ISS_IMAGE = "iss_image_small.jpg"
HOST = "smtp.gmail.com"


def send_html_email_with_image_attachment():
    """This function sends email in HTML format with birthday card as attachment."""
    msg = MIMEMultipart('alternative')
    msg['From'] = EMAIL_FROM
    msg['To'] = EMAIL_TO
    msg['Subject'] = "ISS is above. You can see it on the sky :-)!"

    try:
        with open(ISS_IMAGE, 'rb') as f:
            img_data = f.read()
    except FileNotFoundError as err_msg:
        messagebox.showerror("ISS image error!", "ISS image file was not found.\n"
                                                 "Contact app support to solve this problem.")
        print(f"Error message: {err_msg}")
    else:
        image = MIMEImage(img_data, name="ISS Image!")
        image.add_header('Content-ID', '<image1>')
        msg.attach(image)

    message = "The ISS is above you. You can observe it on the sky tonight. Have a nice time!"
    html = """<html>
      <head></head>
      <body>
        <h3>ISS is above!</h3>
        <p>You can observe it on the sky.</p>
        <p>Lots of love,</p>
        <p>Mateusz</p>
        <p><img src="cid:image1"></p>
      </body>
    </html>"""

    part1 = MIMEText(message, 'plain', 'utf-8')
    part2 = MIMEText(html, 'html', 'utf-8')

    msg.attach(part1)
    msg.attach(part2)

    try:
        with smtplib.SMTP(HOST, port=587) as conn:
            conn.starttls()
            conn.login(user=EMAIL_FROM, password=APP_PASS)
            conn.sendmail(from_addr=EMAIL_FROM,
                          to_addrs=EMAIL_TO,
                          msg=msg.as_string())

    except smtplib.SMTPConnectError as err_msg:
        print(f"Email not sent. Something went wrong with sending email.")
        print(f"Error message: {err_msg}")
        print("-" * 7)
        return False
    else:
        print(f"Email sent successfuly.")
        return True


def is_iss_above_my_head():
    """This function returns True is ISS is above my head and False if is not."""
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    diff_lat = abs(iss_latitude - MY_LAT)
    diff_long = abs(iss_longitude - MY_LONG)
    return diff_lat <= 5 and diff_long <= 5


def is_still_day():
    """This function returns True if it is still day and False if it is already night."""
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now_hour = datetime.now().hour
    return sunset > time_now_hour > sunrise


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

while True:
    if is_iss_above_my_head():
        if not is_still_day():
            if send_html_email_with_image_attachment():
                print("Notification email send. ISS is now visible on the ske.")
        else:
            print("Unfortunately ISS is above me but I am unable to see it because it is still day.")
    else:
        print("I have to still wait to see ISS on the sky.")

    sleep(60)
