# PROJECT 1:
# Python code to generate MD5 of string data

# importing hashlib library
import hashlib

# inputting data
data = input('Enter data:\t')

# generating MD5 Hash of data
ans = hashlib.md5(data.encode())

# printing the MD5 Hash
print('The MD5 Hash of ',data,'is : ', ans.hexdigest())

# End of Program
