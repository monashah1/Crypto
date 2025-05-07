import hashlib

class HashPuzzleSolver:
    @staticmethod
    def hash_with_zero_bits(prefix_zeros):
        nonce = 0
        while True:
            data = str(nonce).encode()
            hash_value = hashlib.sha256(data).digest()
            if hash_value.startswith(b'\x00' * prefix_zeros):  # Check for the required number of leading zero bits
                return nonce, hash_value
            nonce += 1

# Solve hash puzzles with leading 1 zero bit
print("Hashes with leading 1 zero bit:")
nonce, hash_value = HashPuzzleSolver.hash_with_zero_bits(1)
print("Nonce:", nonce)
print("Hash:", hash_value.hex())

# Solve hash puzzles with leading 2 zero bits
print("\nHashes with leading 2 zero bits:")
nonce, hash_value = HashPuzzleSolver.hash_with_zero_bits(2)
print("Nonce:", nonce)
print("Hash:", hash_value.hex())
