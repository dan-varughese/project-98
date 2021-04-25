def swapFileData():
    fileA = input("Enter the name of the first file you want to swap: ")
    fileB = input("Please enter the name of the second file you want to swap: ")
    with open(fileA, 'r') as a:
        data_a = a.read()
    with open(fileB, 'r') as b:
        data_b = b.read()
    with open(fileA, 'W') as a:
        a.write(data_b)
    with open(fileB, 'W') as a:
        b.write(data_a)

swapFileData()