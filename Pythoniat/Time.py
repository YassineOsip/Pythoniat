import time
tt = time.time()
t = time.ctime(tt)
print(t)

time = time.localtime()
t = "%s / %s / %s" %(time[0],time[1], time[2])
print(t)
