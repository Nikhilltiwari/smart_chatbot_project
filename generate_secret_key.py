
import secrets

def generate_secret_key():
    return secrets.token_hex(24)

if __name__ == '__main__':
    print("Your secret key is:", generate_secret_key())
