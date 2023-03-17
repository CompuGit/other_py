import rsa

pub_key = open('pub_key.pem','rb').read()
priv_key = open('priv_key.pem','rb').read()

pub_key = rsa.PublicKey.load_pkcs1(pub_key)
priv_key = rsa.PrivateKey.load_pkcs1(priv_key)

msg = bytes('hey! hello. how are you.? this is my first rsa encryption.', 'utf-8')


encrypted = rsa.encrypt(msg, pub_key)
print(encrypted)

decrypted = rsa.decrypt(encrypted, priv_key)
print(decrypted)