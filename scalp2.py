from Crypto.Cipher import AES
from binascii import unhexlify

# 1. The target ciphertext flag from the U-Boot environment block
ciphertext_hex = "419828e807072c659513b999ceb30c63d4254366e9111aae92c3d5fd174232e8"

# 2. Your verified 64-character Key and 32-character IV hex strings
AES_KEY_HEX = "25571639f3e7829a021f08955f65c0b8ca10600a077e7aa1916ef53117014e98" 
AES_IV_HEX  = "aa15e6b979b4644edae55377c26d9205"

try:
    # Convert hexadecimal configurations into raw binary bytes
    ciphertext = unhexlify(ciphertext_hex)
    key = unhexlify(AES_KEY_HEX)
    iv = unhexlify(AES_IV_HEX)
    
    # Initialize the AES-CBC Cipher
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    
    # Decrypt the 32-byte block
    decrypted_bytes = cipher.decrypt(ciphertext)
    
    # Attempt to handle standard PKCS#7 padding if present
    padding_len = decrypted_bytes[-1]
    if 1 <= padding_len <= 16 and all(x == padding_len for x in decrypted_bytes[-padding_len:]):
        plaintext_bytes = decrypted_bytes[:-padding_len]
    else:
        plaintext_bytes = decrypted_bytes

    print("=== DECRYPTION SUCCESSFUL ===")
    print(f"Raw Decrypted (Hex): {decrypted_bytes.hex()}")
    print(f"Plaintext String:    {plaintext_bytes.decode('utf-8', errors='ignore')}")
    print("=============================")

except ValueError as ve:
    print(f"Configuration Error: Ensure parameters are valid hex characters. Details: {ve}")
except Exception as e:
    print(f"An unexpected error occurred during decryption: {e}")
