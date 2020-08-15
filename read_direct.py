import os, sys
import mmap
from random import shuffle
from time import time
def read_test(filename, block_size, file_size):
	'''
        Performs read speed test by reading random offset blocks from
        file, at maximum of blocks_count, each at size of block_size
        bytes until the End Of File reached.
        Returns a list of read times in sec of each block.
        '''
	f = os.open(filename, os.O_RDONLY | os.O_DIRECT, 0o777)  # low-level I/O
    # generate random read positions
	offsets = list(range(0, file_size, block_size))
	# print(offsets)
	shuffle(offsets)
	took = []
	for i, offset in enumerate(offsets, 1):
		m = mmap.mmap(-1, block_size) # read the whole file
		start = time()
		os.lseek(f, offset, os.SEEK_SET)  # set position
		m.read(f)  # read from position
		t = time() - start
		took.append(t)
	os.close(f)
	return took

block_size = 4096
file_size = 1048576
filename = "/hdd/file.txt"

took = read_test(filename, block_size, file_size)
print(took)
time_spent = sum(took)
print("reading throughput :", 1/time_spent, "MB/s")
