import hmac
from Crypto.Hash import SHA3_256

def read_file_content(path):
    try:
        with open(path, 'rb') as f:
            return f.read()
    except FileNotFoundError:
        print("❌ File not found. Please check the path.")
        return None

def create_hmac():
    file_path = input("Enter the path to the local file: ").strip()
    file_data = read_file_content(file_path)
    if file_data is None:
        return
    secret_key = input("Enter a secret key: ")
    hmac_gen = hmac.new(secret_key.encode(), file_data, SHA3_256)
    print("✅ Generated HMAC (hex):", hmac_gen.hexdigest())

def verify_hmac():
    file_path = input("Enter the path to the local file: ").strip()
    file_data = read_file_content(file_path)
    if file_data is None:
        return
    secret_key = input("Enter the secret key: ")
    received_hmac = input("Enter the received HMAC (hex): ").strip()
    recalculated_hmac = hmac.new(secret_key.encode(), file_data, SHA3_256)

    if recalculated_hmac.hexdigest() == received_hmac:
        print("✅ File is authentic and untampered.")
    else:
        print("⚠️ File was altered or key mismatch.")

def main():
    print("=== Garuda File Integrity Checker ===")
    print("1. Create HMAC for a file")
    print("2. Verify file integrity")
    choice = input("Enter your choice (1 or 2): ").strip()

    if choice == '1':
        create_hmac()
    elif choice == '2':
        verify_hmac()
    else:
        print("❌ Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
