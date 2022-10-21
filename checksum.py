# Caleb Knight
# Small project to mimic checksums
# CS 372


import socket
import sys
import re


# Read in .txt files
if ".txt" in sys.argv[1] or ".txt" in sys.argv[2]:
	text_file_name = sys.argv[1]
	txt_file = open(text_file_name) # ==> If we print this, it will give us file type and encoding (for capstone)
	
	txt = txt_file.read()
	print(txt)

	# Split input into two (source & dest)
	source_addr = txt.split()[0]
	destination_addr = txt.split()[1]
	print("Source Address: ", source_addr)
	print("Destination Address: ", destination_addr)

# Read in .dat files
if ".dat" in sys.argv[2] or ".dat" in sys.argv[1]:
	data_file_name = sys.argv[1]
	with open(data_file_name, "rb") as fp:
		tcp_data = fp.read()
		tcp_length = len(tcp_data)  # <-- length
		print("TCP Data: ", tcp_data)


# Function to convert dots and numbers (IP Addys) to bytestrings
def ip_to_bytestring(ip_addr):

	array_str = ip_addr.split('.') # ==> Split on the period to get an array of numbers in str format
	string_of_bytes = b''

	print("Array of Numbers in String Format", array_str)

	# For loop that iterates the array of str nums and converts them to bytes and stores them in a bytestring
	for s in array_str:
		get_int = int(s)
		print("Int: ", get_int)
		byte = get_int.to_bytes(1, 'big')
		print("Bytes: ", byte)
		string_of_bytes += byte 
		print("String of Bytes: ", string_of_bytes)
	return string_of_bytes


# Function to generate IP psuedoheader bytes from the IP Address given from .txt & the TCP header length from .dat
def gen_pseudoheader(source_addr, destination_addr, tcp_length):

	# Covert all to bytes
	zero = 1
	ptcl = 6
	tcp_new_length = tcp_length
	zero_byte = zero.to_bytes(1, 'big')
	ptcl_bytes = ptcl.to_bytes(1, 'big')
	tcp_length_bytes = tcp_new_length.to_bytes(2, 'big')
	source_len = ip_to_bytestring(source_addr)
	dest_len = ip_to_bytestring(destination_addr)

	# Check for type of vars (need bytes)
	# print("PTCL len type: ", type(ptcl_bytes))
	# print("Zero type: ", type(zero_byte))
	# print("IP addr Len type: ", type(byte_len_ip))
	# print("TCP Len type: ", type(tcp_length_bytes))

	print("Zero len: ", zero_byte)
	print("PTCL len: ", ptcl_bytes)
	print("TCP len: ", tcp_length_bytes)
	print("Source len: ", source_len)
	print("Dest len: ", dest_len)


	byte_len_ip = source_len + dest_len
	psuedoheader = byte_len_ip + zero_byte + ptcl_bytes + tcp_length_bytes
	print("Pseduoheader: ", psuedoheader)
	print("Length of psuedoheader: ", len(psuedoheader))

# Get the checksum from the tcp data
def get_checksum(tcp_data):
    checksum = int.from_bytes(tcp_data[16:18], 'big')
    print ("Checksum: ", checksum)
    return checksum

# Build replica of TCP data with checksum set to 0 (16 and 17th byte is checksum)
def gen_zero_checksum(tcp_data):
	tcp_zero_cksum = tcp_data[:16] + b'\x00\x00' + tcp_data[18:]
	print("Zeroed checksum: ", tcp_zero_cksum)
	return tcp_zero_cksum

# Concat pseudoheader and TCP data with zeroed checksum
def mathing(psuedoheader, tcp_zero_cksum):
	if len(tcp_zero_cksum) % 2 == 1:
    	tcp_zero_cksum += b'\x00'

    our_data = psuedoheader + tcp_zero_cksum

    offset = 0

    while offset < len(our_data)
    	word = int.from_bytes(data[offset:offset + 2], "big")
   		offset += 2   # Go to the next 2-byte value


# Compute the checksum of the concat


# Get the checksum from the original data (.dat)


# Compare the two
	# If they match: success
	# Else: fail



ip_to_bytestring(source_addr)
gen_pseudoheader(source_addr, destination_addr, tcp_length)
get_checksum(tcp_data)
gen_zero_checksum(tcp_data)