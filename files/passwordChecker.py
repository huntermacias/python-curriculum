#take user input (uname & pword)

username = input("Please enter your username: ")
password = input("Please enter your password: ")

pwordlen = len(password)
encrypted_password = "*" * pwordlen


print(f"{username}, your password is {encrypted_password} and has a length of {pwordlen}")