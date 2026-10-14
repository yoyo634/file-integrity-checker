import hashlib
import sys

def calculate_sha256(file_path):
    """Calculate the SHA-256 hash of a file."""
    sha256_hash = hashlib.sha256()
    
    try:
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(65536), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    
    except FileNotFoundError:
        print(f"[!] Error: File '{file_path}' not found.")
        return None
    
def main():
    if len(sys.argv) < 2:
        print("Usage: python Security.py <file_path> [expected_hash]")
        sys.exit(1)
    
    target_file = sys.argv[1]
    current_hash = calculate_sha256(target_file)
    
    if not current_hash:
        return

    print(f"\n[+] Target File: {target_file}")
    print(f"[+] SHA-256 Hash: {current_hash}\n")
        
    if len(sys.argv) == 3:
        expected_hash = sys.argv[2].strip().lower()
        if current_hash == expected_hash:
            print("[SUCCESS] File integrity verified! The file has NOT been modified.")
        else:
            print("[WARNING] Hash mismatch! The file may have been tampered with.")

if __name__ == "__main__":
    main()