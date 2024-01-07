import hashlib


class Hasher:
    @staticmethod
    def get_password_hash(password: str) -> str:
        # generate salt
        salt = hashlib.sha256().hexdigest()[:16]

        # hashing password using salt
        password_hash = hashlib.pbkdf2_hmac(
            'sha256',                             # use SHA-256
            password.encode('utf-8'),                        # Convert password (str) to bytes
            salt.encode('utf-8'),                            # Convert salt (str) to bytes
            100000                                 # count of hashing iterations
        ).hex()

        return f"{password_hash}:{salt}"                     # return hash and salt in  "hash:salt" format

    @staticmethod
    def verify_password(password: str, hashed_password: str) -> bool:
        password_hash, salt = hashed_password.split(":")     # divide into salt, hash

        calculated_hash = hashlib.pbkdf2_hmac(               # calculate hash for password
            'sha256',
            password.encode('utf-8'),
            salt.encode('utf-8'),
            100000
        ).hex()

        return calculated_hash == password_hash              # compare current hash with hash in DB
