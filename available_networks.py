# importing the subprocess module
import subprocess, time

###
### Currently connected network details
###
 
# using the check_output() for having the network term retrieval
devices = subprocess.check_output(['netsh','wlan','show','network'])

# decode it to strings
devices = devices.decode('ascii')
devices = devices.replace("\r","")
 
# displaying the information
print(devices)

###
### Getting all the Wifi Devices the system has connected
###

# getting meta data of the wifi network
meta_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])
 
# decoding meta data from byte to string
data = meta_data.decode('utf-8', errors ="backslashreplace")
 
# splitting data by line by line
# string to list
data = data.split('\n')
 
# creating a list of wifi names
names = []
 
# traverse the list
for i in data:
     
    # find "All User Profile" in each item
    # as this item will have the wifi name
    if "All User Profile" in i :
         
        # if found split the item
        # in order to get only the name
        i = i.split(":")
         
        # item at index 1 will be the wifi name
        i = i[1]
         
        # formatting the name
        # first and last chracter is use less
        i = i[1:-1]
         
        # appending the wifi name in the list
        names.append(i)
 
# printing the wifi names
print("All wifi that system has connected to are ")
print("-----------------------------------------")
for name in names:
    print(name)


time.sleep(5)