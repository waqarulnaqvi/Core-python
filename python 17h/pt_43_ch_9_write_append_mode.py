"NOTE :write and append mode can create a file but read does not.."
"Opening a file in write mode:"
# f = open('another.txt','w')
# f.write("Please2 write this to the file:\n")
# f.close()
f = open('this.txt','w')
f.write("Please2 write this to the file:\n")
f.write("Please2 write this to the file:\n")
f.write("Please2 write this to the file:\n")
f.write("Please2 write this to the file:\n")
f.close()

"Opening a file in append mode:"
# f = open('another.txt','a')
# f.write("I am appending\n")
# f.close()
# f = open('this.txt','a')
# f.write("I am appending\n")
# f.close()