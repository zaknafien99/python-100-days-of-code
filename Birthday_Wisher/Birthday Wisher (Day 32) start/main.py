import smtplib
import datetime as dt
import random

MY_EMAIL = "ngzervos@gmail.com"
MY_PASSWORD = "ur12talk2"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 6:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=f"Subject: Monday Motivation\n\n{quote}")



# import smtplib
#
# my_email = "ngzervos@gmail.com"
# password = "ur12talk2"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls() #secures the connection
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="zaknafien99@hotmail.com",
#                         msg="Subject:Hello from Python\n\nThis is the body of my email.")
#
#

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day = now.day
#
# day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=1976, month=9, day=20)
# print(date_of_birth)
#
