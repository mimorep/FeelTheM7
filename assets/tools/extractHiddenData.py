import sys

# Append data at the end of the file
# Know the last bytes are D7 44 4F 49
def hiddeData(filePath):
      with open (filePath, 'ab') as f:
            # Write a string or a file inside
            with open (<fileToWrite>, 'rb') as b:
                f.write(b.read())  

# Know the last bytes are D7 44 4F 49
def unHiddeData(filePath):
    print ("IDK how to implement this :)")

if __name__ == '__main__':
    
    option =  input("Type Hidde or Unhidde: \n")

    if (option == "Hidde"):
        hiddeData(str(sys.argv[1]))
    else:
        unHiddeData(str(sys.argv[1]))