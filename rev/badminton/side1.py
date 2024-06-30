import socket
import sys

offset = int(sys.argv[1])

flag = b"0CTF{r3v3rs1ng_1s_7he_art_0f_pred1ct1ng_patt3rns}"

messages = [c for c in "asjdjsahdiusadasudoiadoisandoisaudoiadoisauoiduasoiduiasnudoiaidisanudoinsnu"]

for i in range(0 + offset, len(flag), 2):
    # s.bind("127.0.0.1", 6900 + flag[i])
    port = 6900

    
