#wap to open 3 files 1.txt,2.txt,3.txt.If any of these files are not present ,a message wihtout exiting the program must be printed prompting the same
def readfile(filename):
    try:
        with open(filename,'r') as f:
            print(f.read())
    except FileNotFoundError:
        print(f'File {filename} is not found')

readfile('1.txt')
readfile('2.txt')
readfile("3.txt")

#after deleting 2.txt file
readfile('1.txt')
readfile('2.txt')
readfile("3.txt")

