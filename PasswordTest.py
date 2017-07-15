passwordFile = open('Malware_Project.docx')
secretPassword = passwordFile.read()
print('Enter your password')
typedPassword = input()
if typedPassword == secretPassword:
    print('Access granted')
    if typedPassword == '12345':
        print('That password is the one that idiot put on their luggage!')
    else:
            print("Access Denied')
 # CHANGES ON WEBSITE
