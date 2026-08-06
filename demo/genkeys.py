from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.hazmat.primitives.serialization import Encoding, PrivateFormat, PublicFormat, NoEncryption
import os

os.makedirs('keys', exist_ok=True)
key = Ed25519PrivateKey.generate()

with open('keys/issuer_private.pem', 'wb') as f:
    f.write(key.private_bytes(Encoding.PEM, PrivateFormat.PKCS8, NoEncryption()))

with open('keys/issuer_public.pem', 'wb') as f:
    f.write(key.public_key().public_bytes(Encoding.PEM, PublicFormat.SubjectPublicKeyInfo))

print('keys 생성 완료!')