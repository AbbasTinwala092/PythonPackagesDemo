"""
Open file in appropriate mode: read(r), write(w), append(a)
Enter/Read data
Close file
"""
myFile = open("text.txt","w")
myFile.writelines("Hello, My name is Abbas Tinwala.")
text = input("Enter your mobile number: ")
myFile.writelines(text)
myFile.readline(myFile)