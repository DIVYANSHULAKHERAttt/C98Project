def swapFileData():
    fileName = input("Enter the file name: ") 
    file=open(fileName, 'r')
    for line in file:
        words = line.split()
        number_of_words = number_of_words + len(words)
    print(number_of_words)
    print(fileName)

swapFileData()