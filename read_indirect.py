import os, sys
import mmap
from random import shuffle
from time import time
from streamlit import caching


def read_test(filename, block_size, file_size):

	f = os.open(filename, os.O_RDONLY, 0o777)  # low-level I/O
    # generate random read positions
	offsets = list(range(0, file_size, block_size))
	# print(offsets)
	shuffle(offsets)
	took = []
	for i, offset in enumerate(offsets, 1):
		#caching.clear_cache()
		start = time()
		os.lseek(f, offset, os.SEEK_SET)  # set position
		buff= os.read(f, block_size)  # read from position
		t = time() - start
		if not buff: break  # if EOF reached
		speed = (block_size/t)/1000000
		took.append(speed)
	os.close(f)
	return took

block_size = 4096
file_size = 1048576
filename = "/hdd/file.txt"

took = read_test(filename, block_size, file_size)
#print(took)
print("jumlah: ", len(took))
avg_speed = sum(took)/len(took)
print("reading throughput :", avg_speed, "MB/s")
