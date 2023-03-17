import rsa
pubkey, privkey = rsa.newkeys(1024)

pubkey = pubkey.save_pkcs1().decode('utf-8')
privkey = privkey.save_pkcs1().decode('utf-8')

open('pub_key.pem','wb').write(bytes(pubkey,'utf-8'))
open('priv_key.pem','wb').write(bytes(privkey, 'utf-8'))
