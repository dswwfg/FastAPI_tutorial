# https://wizardforcel.gitbooks.io/practical-cryptography-for-developers-book/content/asymmetric-key-ciphers/rsa-encrypt-decrypt-examples.html


from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

key_pair = RSA.generate(2048)
public_key = key_pair.publickey()
public_key_pem = public_key.exportKey()

# print('pubkey : ', public_key_pem)

private_key_pem = key_pair.exportKey()
# print('private key : ', private_key_pem)

# #  RSA Encryption
msg = b'{"user_id" = "gavin@hanafn.com"}'
#
encryptor = PKCS1_OAEP.new(public_key)
encrypted = encryptor.encrypt(msg)
print(encrypted)


decryptor = PKCS1_OAEP.new(key_pair)
decrypted = decryptor.decrypt(encrypted)

print(decrypted.decode('utf-8'))