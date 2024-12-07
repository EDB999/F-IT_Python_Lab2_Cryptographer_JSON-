import json
from cryptography.fernet import Fernet


def write_key():
    # Создаем ключ и сохраняем его в файл
    crypto_key = Fernet.generate_key()
    with open('crypto.key', 'wb') as key_file:
        key_file.write(crypto_key)


def load_key():
    # Загружаем ключ 'crypto.key' из текущего каталога
    return open('crypto.key', 'rb').read()


def encrypt(filename, key_enc):
    # Зашифруем файл и записываем его
    f_enc = Fernet(key_enc)

    with open(filename, 'rb') as file_enc:
        # прочитать все данные файла
        file_data = file_enc.read()

    encrypted_data = f_enc.encrypt(file_data)

    # записать зашифрованный файл
    with open(filename, 'wb') as file_enc:
        file_enc.write(encrypted_data)


def decrypt(filename, key_dec):
    # Расшифруем файл и записываем его
    f_dec = Fernet(key_dec)

    with open(filename, 'rb') as file_dec:
        # читать зашифрованные данные
        encrypted_data = file_dec.read()
    # расшифровать данные
    decrypted_data = f_dec.decrypt(encrypted_data)
    # записать оригинальный файл
    with open(filename, 'wb') as file_dec:
        file_dec.write(decrypted_data)


def createDataJSON(filename):
    with open(filename, 'rb') as file_json:
        data = file_json.read().decode('utf-8')

    with open('data.json', 'w') as file_json:
        json.dump({"content": data}, file_json)


if __name__ == '__main__':
    write_key()
    # загрузить ключ
    key = load_key()
    # имя шифруемого файла
    file = 'For the Lab2.txt'

    # зашифровать файл
    encrypt(file, key)

    # Проверка содержимого файла после шифрования
    with open(file, 'rb') as f:
        encrypted_content = f.read()
        print("Encrypted content:", encrypted_content)

    # дешифровать файл
    decrypt(file, key)

    # Проверка содержимого файла после дешифрования
    with open(file, 'rb') as f:
        decrypted_content = f.read()
        print("Decrypted content:", decrypted_content)

    # Создать JSON файл с содержимым расшифрованного файла
    createDataJSON(file)
