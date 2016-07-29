#########################
# UNI:yl3433
# Name: Yuxuan Liu
#
#######################

import os

# Create a directory
if not os.path.exists("D:\pythonHW"):
    os.makedirs("D:\pythonHW")

# Create this_file
with open("D:\\pythonHW\\thisFile.txt", 'w+') as this_file:
    this_file.write("Mickey Mouse\n")
    this_file.write("David Hume\n")
    this_file.write('Edmund Burke\n')
    this_file.write('Joe Lion\n')
    
# Read this_file 
this_file = open("D:\\pythonHW\\thisFile.txt",'r')
# Create and get read to write on that_file
that_file= open('D:\\pythonHW\\thatFile.txt', 'w')  

def write_every_other_line(in_file, out_file):
    '''Write every other line into that_file, starting from the first line'''
    count_of_line = 0
    for line in this_file:
        count_of_line += 1
        if count_of_line % 2 == 1:    
            that_file.write(line)
            
write_every_other_line(this_file, that_file)
        
this_file.close()
that_file.close()




    
