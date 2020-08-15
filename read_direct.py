import os, sys
import mmap
from random import shuffle
from time import time
def read_test(filename, block_size, file_size):
	f = os.open(filename, os.O_RDONLY | os.O_DIRECT, 0o777)  # low-level I/O
	fo = os.fdopen(f, 'rb', 0)
	took = []
	print(os.stat('/hdd/file.txt'))
	for i in range(100):
		readbuf = mmap.mmap(-1, 4096*2) # read the whole file
		#os.lseek(f, 0, os.SEEK_SET)
		
		start = time()
		p = fo.readinto(readbuf)  # read from position
		t = time() - start
		#print(readbuf.size())
		#print(readbuf.readline())
		print(p)
		speed = (4096*2/t) / 1000000
		#print(t)
		took.append(speed)
		readbuf.close()
	fo.close()
	return took

block_size = 4096
file_size = 1024 * 1024
filename = "/hdd/file.txt"

took = read_test(filename, block_size, file_size)
#print(took)
avg_speed = sum(took) / len(took)

print("reading throughput :", avg_speed, "MB/s")
