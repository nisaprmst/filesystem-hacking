import os, sys
import mmap
from random import shuffle
from time import time
import numpy as np
import matplotlib.pyplot as plt
def read_test(filename, block_size, direct):
	# low level I/O
	if (direct):
		f = os.open(filename, os.O_RDONLY | os.O_DIRECT, 0o777)
	else:
		f = os.open(filename, os.O_RDONLY, 0o777)
	fo = os.fdopen(f, 'rb', 0)
	took = []
	for i in range(100):
		readbuf = mmap.mmap(-1, block_size) # read the whole file
		#os.lseek(f, 0, os.SEEK_SET)
		
		start = time()
		p = fo.readinto(readbuf)  # read from position
		t = time() - start
		#print(readbuf.size())
		#print(readbuf.readline())
		#print(p)
		speed = (block_size/t) / 1000000
		#print(t)
		took.append(speed)
		readbuf.close()
	fo.close()
	return took

block_size = 4096*2
#file_size = 1024*1024
filename = "/hdd/file.txt"
print(os.stat(filename))

direct = read_test(filename, block_size, True)
indirect = read_test(filename, block_size, False)

avg_direct = sum(direct) / len(direct)
avg_indirect = sum(indirect) / len(indirect)

print("reading throughput direct:", avg_direct, "MB/s")
print("reading throughput indirect:", avg_indirect, "MB/s")

plt.title("Reading performance with caching")
plt.plot(direct, label="direct read")
plt.plot(indirect, label="indirect read")
plt.xlabel("number of readings")
plt.ylabel("reading throughput (MB/s)")
plt.legend(loc="upper left")
plt.savefig("with_caching.png")
plt.show()
