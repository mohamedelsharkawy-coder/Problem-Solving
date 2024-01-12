# task: get number of emails --> validate them --> sort them 

# email is valide in case of this formate type : username@websitename.extension
# username --> letters, digits, dashes and underscores  
# website_name --> letters and digits 
# extension --> letters / lenght: 3
import re 


def fun(s: str): # s = username@websitename.extension
    pattern = r"\b[A-Z a-z 0-9\-\_]+@[A-Z a-z 0-9]+\.[A-Z a-z]{1,3}\b"
    return bool(re.match(pattern,s))

    
def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)



