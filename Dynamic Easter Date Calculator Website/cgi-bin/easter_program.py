#!/usr/bin/python3
import cgi, cgitb

def verbose(d, m, year):
    month = ""
    superscript = ""

    if m == 3:
        month = "March"
    elif m == 4:
        month = "April"

    if d == 1 or d == 21 or d == 31:
        superscript = "<sup>st</sup>"
    elif d == 2 or d == 22:
        superscript = "<sup>nd</sup>"
    elif d == 3 or d == 23:
        superscript = "<sup>rd</sup>"
    else:
        superscript = "<sup>th</sup>"

    print("Content-Type: text/html; charset=utf-8")
    print("")
    print("<!Doctype html>")
    print("<html>")
    print("<head> <title>When is Easter?</title> </head>")
    print("<body>")
    print("<p>")
    print("The date of easter for the year is: %s %s %s" % (d, month, year))
    print("</p>")
    print("</body>")
    print("</html>")




def numeric(d, m, year):
    day_date = ""
    month_date = ""
    if d >= 10:
        day_date = str(d)
    elif d < 10:
        day_date = "0" + str(d)

    if m < 10:
        month_date = "0" + str(m)
    elif m >= 10:
        month_date = str(m)

    print("Content-Type: text/html; charset=utf-8")
    print("")
    print("<!Doctype html>")
    print("<html>")
    print("<head> <title>When is Easter?</title> </head>")
    print("<body>")
    print("<p>")
    print("The date of easter for the year is: %s %s %s" % (day_date, month_date, year))
    print("</p>")
    print("</body>")
    print("</html>")


def Easter(y, f):
    a = y % 19
    b = y // 100
    c = y % 100
    d = b // 4
    e = b % 4
    g = (8 * b + 13) // 25
    h = (19 * a + b - d - g + 15) % 30
    j = c // 4
    k = c % 4
    m = (a + 11 * h) // 319
    r = (2 * e + 2 * j - k - h + m + 32) % 7
    n = (h - m + r + 90) // 25
    p = (h - m + r + n + 19) % 32

    day = p
    month = n

    if f == "verbose":
        verbose(day, month, y)
    elif f == "numeric":
        numeric(day, month, y)
    else:
        verbose(day, month, y), numeric(day, month, y)


form = cgi.FieldStorage()
user_input = form.getvalue("year")
user_input = int(user_input)
format_type = form.getvalue("format")

Easter(user_input, format_type)
