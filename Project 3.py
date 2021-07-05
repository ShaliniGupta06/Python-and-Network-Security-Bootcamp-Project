# PROJECT 3:
# Python code to generate hashes of string data using MD5
# and adding salting to it

#importing hashlib library
import hashlib

#inputting data
data = input('Enter data:\t')
temp = data

# Adding Salting:
data = data+'123'
data = 'abc'+data

ans = hashlib.md5(data.encode())

# printing the output
print('The MD5 Hash of ',temp,' after salting is : ', ans.hexdigest())

# End of Program

# NOTE: Iteration part not done
