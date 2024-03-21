passwordLengths = []
    print("Minimum length of password should be 3")
    for i in range(numPasswords):
        length = int(input("Enter the length of Password #" + str(i+1) + " "))
        length = int(input("Enter the length of Password #" + str(i+1) + " : "))
        if length<3:
            length = 3
        passwordLengths.append(length)
