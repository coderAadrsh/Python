# f=open("sample.txt","w")#file object
# # #read file
# # #data=f.read()#print all the text in sample file.
# # data=f.readline()#when we want to read a file line by line.
# # print(data)
# # data=f.readline()
# #write file
# f.write("text to overwrite\n the complete data.")

# f.close()
# #modes in file I/O.


# # w-write, truncates file first.
# f=open("sample.txt","w")
# f.write("he llo this is new line\n and all old text deleted.")
# f.close()

# # # x-create new and open for writing .
# # f=open("story.txt","x")
# # f.write("Twinkle, twinkle, little star,\n How I wonder what you are!\nUp above the world so high,\nLike a diamond in the sky.\nTwinkle, twinkle, little star,\nHow I wonder what you are!\n")
# # f.close()
# # a-writing, append at end.
# f=open("sample.txt","a")
# f.write("\n this is python.")
# f.close()
# # b-binary Mode 

# # t-text mode(default)

# # +-open disk file for update(r & w)
# #r+ mode
# f=open("sample.txt","a+")
# f.write("123")
# print(f.read())
# f.close()


# # r-read(default)
# files=("sample.txt","story.txt")
# for file in files:
#   f=open(file,"r")
#   data=f.read()
#   print(data)
#   print ("\n ---------------START NEW FILE----------------------\n")
#   f.close()

# #with key word :we do not close file explicitly,it done by automatically after exuction of program.
# with open("sample.txt","r") as f:
#     data=f.read()
#     print("length of data is {} and content in file:\n {}".format(len(data),data))
# #delete file:-import module os(operating system).
# import os
# os.remove("story.txt")
# x-create new and open for writing .
with open("story.txt","w") as f:
   f.write("Twinkle, twinkle, little star,\n How I wonder what you are!\nUp above the world so high,\nLike a diamond in the sky.\nTwinkle, twinkle, little star,\nHow I wonder what you are!\n")

data=True
with open("story.txt","rt") as f:
   find=input("Find words:")
   line=1
   while data:
      data=f.readline()

      if(find in data):
         print("found line no.",line)
         break
      else:
         line+=1
      
   
  


