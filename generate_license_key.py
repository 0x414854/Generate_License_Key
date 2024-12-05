import os
import csv
import secrets
import string
import hashlib
import logging
from shadePy import Colors

GREEN = Colors.GREEN
RED = Colors.RED
GREY = Colors.GREY
YELLOW = Colors.YELLOW
RESET = Colors.RESET

BASE_DIR = 'users'
LICENSE_KEY_FILE = os.path.join(BASE_DIR, 'License_key.txt')
USERS_CSV_FILE = os.path.join(BASE_DIR, 'users.csv')

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)

class LicenseManager:
    def __init__(self):
        self.existing_keys = set()
        self._load_existing_keys()

    def _load_existing_keys(self):
        if os.path.exists(USERS_CSV_FILE):
            try:
                with open(USERS_CSV_FILE, 'r', encoding='utf-8') as csvfile:
                    reader = csv.reader(csvfile)
                    next(reader, None)
                    for row in reader:
                        self.existing_keys.add(row[1].strip())
                logging.info(f"{GREEN}License keys loaded from {USERS_CSV_FILE}{RESET}")
            except Exception as e:
                logging.error(f"{RED}Error loading license keys: {e}{RESET}")

    def generate_license_key(self, length=64):
        characters = string.ascii_letters + string.digits + string.punctuation.replace('"', '').replace("'", "")
        while True:
            key = ''.join(secrets.choice(characters) for _ in range(length))
            hashed_key = self._hash_license_key(key)
            if hashed_key not in self.existing_keys:
                self.existing_keys.add(hashed_key)
                return hashed_key
            else:
                logging.warning(f"{YELLOW}License key already exists. Generating a new key...{RESET}")

    @staticmethod
    def _hash_license_key(key):
        return hashlib.sha3_512(key.encode('utf-8')).hexdigest()[:64]

    def _save_to_file(self, file_path, content):
        os.makedirs(BASE_DIR, exist_ok=True)
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content + '\n')
            logging.info(f"{GREEN}Content saved to {file_path}{RESET}")
        except Exception as e:
            logging.error(f"{RED}Error saving content to {file_path}: {e}{RESET}")

    def save_license_key(self, hashed_key):
        self._save_to_file(LICENSE_KEY_FILE, hashed_key)

    def save_user_license(self, username, hashed_key):
        try:
            os.makedirs(BASE_DIR, exist_ok=True)
            file_exists = os.path.exists(USERS_CSV_FILE)
            with open(USERS_CSV_FILE, 'a', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                if not file_exists:
                    writer.writerow(['Username', 'License Key'])
                writer.writerow([username, hashed_key])
            logging.info(f"{GREEN}User saved to {USERS_CSV_FILE}{RESET}")
        except Exception as e:
            logging.error(f"{RED}Error saving user to CSV: {e}{RESET}")

def main():
    manager = LicenseManager()
    license_key = manager.generate_license_key()
    print(f"{GREY}License Key : {RESET}{license_key}")
    manager.save_license_key(license_key)
    
    while True:
        username = input(f"{GREY}Enter username : {RESET}").strip()
        if username:
            break
        else:
            print(f"{YELLOW}Username cannot be empty. Please try again.{RESET}")
    
    manager.save_user_license(username, license_key)

if __name__ == "__main__":
    main()
