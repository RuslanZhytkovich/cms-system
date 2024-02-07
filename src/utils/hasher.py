import hashlib


class Hasher:
    @staticmethod
    def get_password_hash(password: str) -> str:
        # Генерируем соль
        salt = hashlib.sha256().hexdigest()[:16]

        # Хешируем пароль с использованием соли
        password_hash = hashlib.pbkdf2_hmac(
            "sha256",  # Используем алгоритм хеширования SHA-256
            password.encode("utf-8"),  # Преобразуем пароль в байтовую строку
            salt.encode("utf-8"),  # Преобразуем соль в байтовую строку
            100000,  # Количество итераций хеширования
        ).hex()

        # Возвращаем хеш пароля и соль в формате "хеш:соль"
        return f"{password_hash}:{salt}"

    @staticmethod
    def verify_password(password: str, hashed_password: str) -> bool:
        # Разделяем хеш пароля и соль
        password_hash, salt = hashed_password.split(":")

        # Вычисляем хеш пароля для введенного пароля и сохраненной соли
        calculated_hash = hashlib.pbkdf2_hmac(
            "sha256",  # Используем алгоритм хеширования SHA-256
            password.encode("utf-8"),  # Преобразуем пароль в байтовую строку
            salt.encode("utf-8"),  # Преобразуем соль в байтовую строку
            100000,  # Количество итераций хеширования
        ).hex()

        # Сравниваем полученный хеш пароля с сохраненным хешем пароля
        return calculated_hash == password_hash
