# #FileNotFound
# try:
#     file=open("a_file.txt")
#     a_dictionary={"key":"value"}
#     print(a_dictionary["sdsgfsa"])
# except FileNotFoundError:
#     file=open("a_file.txt","w")
#     file.write("Smoozie")
# except KeyError as error_msg:
#     print(f"This key {error_msg} doesn't exist.")
# else:
#     content=file.read()
#     print(content)
# finally:
#     file.close()
#     print("file was closed")
#     raise TypeError("This is an error that i made up")
height=float(input("Height:"))
weight=int(input("Weight:"))
if height>3:
    raise ValueError("Human height can't be higher than 3")
bmi=weight/height**2
print(bmi)