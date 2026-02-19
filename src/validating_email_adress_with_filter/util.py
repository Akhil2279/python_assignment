
import re

def fun(s):
    pattern = r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$'
    return bool(re.match(pattern, s))

def filter_mail():
    n = int(input())

    emails = []

    for _ in range(n):
        emails.append(input().strip())

    valid_emails = list(filter(fun, emails))
    valid_emails.sort()
    return valid_emails

if __name__ == "__main__":
    result = filter_mail()
    print(result)