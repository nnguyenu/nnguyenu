file  = open("addin.txt", "r")
a, b = file.readline().split()
file.close()
s = int(a) +int(b)
file = open("addout.txt", "w")
file.write(str(s))
file.close()