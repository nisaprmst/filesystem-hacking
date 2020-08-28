# Filesystem Hacking

This is an experiment to hack a linux kernel to make all reading operations direct or indirect, regardless of whether or not the O_DIRECT flag is used in an ext2 filesystem. This experiment was conducted with 100 number of reads and a reading size of 8192 bytes. The file used to test has a size of 1 MB.

## Kernel Modification
1. Always do indirect I/O, regardless of whether or not O_DIRECT flag is present
![diff indirect](/images/diff_with_caching.png)

2. Always do direct I/O, regardless of whether or not O_DIRECT flag is present
![diff direct](/images/diff_without_caching.png)


## Result of the Experiment
1. Reading performance of default kernel
![default kernel](/images/default_kernel.png)
2. Reading performance of hacked kernel with caching
![with caching](/images/with_caching.png)
3. Reading performance of hacked kernel without caching
![without caching](/images/without_caching.png)

## Contributor
Annisa Ayu Pramesti
