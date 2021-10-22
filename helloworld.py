import time

print('\n\nHello World!\n\n')
t = 5
while t:
    timer = 'This window will close in ' + str(t) + ' seconds'
    print(timer, end="\r")
    t -= 1
    time.sleep(1)
