# email validation using regex

# ---- Approach ----
# ^ start
# [a-z] from a to z all alphabets
# \ for search in regex 
# ? paramerters are present on once or more
# @ special char \w for search
import re

email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"

user_email =input("Enter your email-id : ")

if  re.search(email_condition ,user_email):
    print(" Valid Email ")
else:
    print(" Invalid Email ")