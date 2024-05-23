import os

# print("our directory is: ",os.getcwd())
#this function is used to now where the program is working not the where is the program file occur 
# os.chdir('../')
# print(os.getcwd())
#this function is used to chnge the direcctory
#os.mkdir("data")
# by using this function we can make a new directory or folders and multiple directories

# if(not os.path.exists("data")):
#         os.mkdir("data")
# for i in range(0,100):
#     os.mkdir(f"data/day{i+1}")

print(os.listdir("data"))
os.remove('New Text Document')