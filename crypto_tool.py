import os
import hashlib
from cryptography.fernet import Fernet, InvalidToken

KEY_FILE = "secret.key"

def generate_key():
    """Generates a secure key and saves it outside the code repository."""
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)
    print(f"[+] Encryption key successfully generated and saved to {KEY_FILE}")

def load_key():
    """Loads the encryption key from disk, handling missing key errors."""
    if not os.path.exists(KEY_FILE):
        raise FileNotFoundError(f"Error: The key file '{KEY_FILE}' does not exist. Run key generation first.")
    with open(KEY_FILE, "rb") as key_file:
        return key_file.read()

def encrypt_file(input_filename, output_filename):
    """Encrypts a student record file."""
    try:
        key = load_key()
        f = Fernet(key)
        
        if not os.path.exists(input_filename):
            raise FileNotFoundError(f"Error: Input file '{input_filename}' not found.")
            
        with open(input_filename, "rb") as file:
            original_data = file.read()
            
        encrypted_data = f.encrypt(original_data)
        
        with open(output_filename, "wb") as file:
            file.write(encrypted_data)
        print(f"[+] Success: '{input_filename}' encrypted and saved as '{output_filename}'.")
        
    except Exception as e:
        print(f"[-] Encryption Failed: {e}")

def decrypt_file(input_filename, output_filename):
    """Decrypts a file and verifies execution."""
    try:
        key = load_key()
        f = Fernet(key)
        
        if not os.path.exists(input_filename):
            raise FileNotFoundError(f"Error: Encrypted file '{input_filename}' not found.")
            
        with open(input_filename, "rb") as file:
            encrypted_data = file.read()
            
        decrypted_data = f.decrypt(encrypted_data)
        
        with open(output_filename, "wb") as file:
            file.write(decrypted_data)
        print(f"[+] Success: '{input_filename}' decrypted and saved as '{output_filename}'.")
        
    except InvalidToken:
        print("[-] Decryption Failed: Invalid key or corrupted file data.")
    except Exception as e:
        print(f"[-] Decryption Failed: {e}")

def calculate_sha256(filename):
    """Calculates and returns the SHA-256 hash of a file."""
    try:
        if not os.path.exists(filename):
            raise FileNotFoundError(f"Error: File '{filename}' not found for hashing.")
            
        sha256_hash = hashlib.sha256()
        with open(filename, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except Exception as e:
        print(f"[-] Hash Calculation Failed: {e}")
        return None

if __name__ == "__main__":
    # Example workflow demonstration
    sample_file = "student_records.txt"
    encrypted_file = "student_records.enc"
    decrypted_file = "student_records_recovered.txt"

    # Create a dummy sample student record file for testing
    if not os.path.exists(sample_file):
        with open(sample_file, "w") as f:
            f.write("ID: 001, Name: John Doe, Grade: A\nID: 002, Name: Jane Smith, Grade: B")
        print(f"[+] Created sample file: {sample_file}")

    # 1. Generate Key (if not already present)
    if not os.path.exists(KEY_FILE):
        generate_key()

    # 2. Encrypt File
    encrypt_file(sample_file, encrypted_file)

    # 3. Calculate and display SHA-256 hash before/after check
    print(f"[*] SHA-256 Hash of original file: {calculate_sha256(sample_file)}")
    print(f"[*] SHA-256 Hash of encrypted file: {calculate_sha256(encrypted_file)}")

    # 4. Decrypt File
    decrypt_file(encrypted_file, decrypted_file)
