# Caleb Knight
# Small project to mimic checksums
# CS 372


import socket
import sys


# Read in .txt files
file_name = sys.argv[1]
file = open(file_name) # ==> If we print this, it will give us file type and encoding (for capstone)

txt = file.read()
print(txt)

# Split line into two (source & dest)
source_addr = txt.split()[0]
destination_addr = txt.split()[1]
print("Source Address: ", source_addr)
print("Destination Address: ", destination_addr)

# Function to convert dots and numbers (IP Addys) to bytestrings
def ip_to_bytestring(ip_addr):
	array_of_bytes = ip_addr.split('.')
	print("Array of Bytes", array_of_bytes)

# Read in .dat files


# Function to generate IP psuedoheader bytes from the IP Address given from .txt & the TCP header length from .dat


# Build replica of TCP data with checksum set to 0 (16 and 17th byte is checksum)


# Concat pseudoheader and TCP data with zeroed checksum


# Compute the checksum of the concat


# Get the checksum from the original data (.dat)


# Compare the two
	# If they match: success
	# Else: fail
ip_to_bytestring(source_addr)