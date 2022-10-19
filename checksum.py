# Caleb Knight
# Small project to mimic checksums
# CS 372


import socket
import sys


# Read in .txt files


# Split line into two (source & dest)


# Function to convert dots and numbers (IP Addys) to bytestrings


# Read in .dat files


# Function to generate IP psuedoheader bytes from the IP Address given from .txt & the TCP header length from .dat


# Build replica of TCP data with checksum set to 0 (16 and 17th byte is checksum)


# Concat pseudoheader and TCP data with zeroed checksum


# Compute the checksum of the concat


# Get the checksum from the original data (.dat)


# Compare the two
	# If they match: success
	# Else: fail