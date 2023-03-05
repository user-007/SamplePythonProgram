from other.modify import l

email = input("What is your email address").strip()
user = email[:email.index("@")]

domain = email[email.index("@") + l:]
output = "Your username is {} and your domain".format(user, domain)
print(output)
