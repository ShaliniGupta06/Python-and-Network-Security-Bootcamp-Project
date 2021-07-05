# PROJECT 2:
# Python code to generate hashes of string data using 3 algorithms
# from hashlib

#importing hashlib library
import hashlib

#inputting data
data = input('Enter data:\t')

# generating SHA-256 hash of data
ans = hashlib.sha256(data.encode())

# printing the output
print('The SHA-256 Hash of ',data,'is : ', ans.hexdigest())

# generating SHA-512 hash of data
ans = hashlib.sha512(data.encode())

# printing the output
print('The SHA-512 Hash of ',data,'is : ', ans.hexdigest())

# generating Blake2 hash of data
ans = hashlib.blake2s(data.encode())

# printing the output
print('The Blake 2c Hash of ',data,'is : ', ans.hexdigest())

# End of Program
