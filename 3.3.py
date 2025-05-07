import hashlib

class MerkleTree:
    def __init__(self, files):
        self.files = files
        self.tree = None

    def hash_node(self, data):
        full_hash = hashlib.sha256(data).digest()
        # Truncate the hash to 4 bits
        return full_hash[:1]  # Take only the first byte, which is 8 bits, then truncate to 4 bits

    def hash_file(self, file):
        with open(file, "rb") as f:
            data = f.read()
        return self.hash_node(data)

    def build_merkle_tree(self, files):
        if len(files) == 1:
            return self.hash_file(files[0]), [self.hash_file(files[0])]
        
        mid = len(files) // 2
        left_hash, left_hashes = self.build_merkle_tree(files[:mid])
        right_hash, right_hashes = self.build_merkle_tree(files[mid:])
        root_hash = self.hash_node(left_hash + right_hash)
        all_hashes = [root_hash] + left_hashes + right_hashes
        return root_hash, all_hashes

    def print_merkle_tree(self):
        if not self.tree:
            self.tree = self.build_merkle_tree(self.files)

        root_hash, all_hashes = self.tree
        depth = len(bin(len(all_hashes) - 1)) - 2

        print("Root Hash:")
        print(root_hash.hex())
        print("\nMerkle Tree Structure:")
        for i in range(depth + 1):
            level = "Level {}: ".format(i)
            level_hashes = ["({})".format(hash.hex()[:2]) for hash in all_hashes if hash != None and len(bin(all_hashes.index(hash))) - 2 == i]
            level += " ".join(level_hashes)
            print(level)
        print()

# Function to check for hash collisions
def find_collision(files):
    hashes = set()
    for file in files:
        hash_value = merkle_tree.hash_file(file)
        if hash_value in hashes:
            return True
        hashes.add(hash_value)
    return False

# testing with  four leaf nodes
print("Test with four leaf nodes:")
files_4 = ["file_1.txt", "file_2.txt", "file_3.txt", "file_4.txt"]
merkle_tree = MerkleTree(files_4)
merkle_tree.print_merkle_tree()

# Check for collision
collision_found = find_collision(files_4)
if collision_found:
    print("Collision found!")
else:
    print("No collision found.")

# testing with six leaf nodes
print("\nTest with six leaf nodes:")
files_6 = ["file_1.txt", "file_2.txt", "file_3.txt", "file_4.txt", "file_5.txt", "file_6.txt"]
merkle_tree = MerkleTree(files_6)
merkle_tree.print_merkle_tree()

# Check for collision
collision_found = find_collision(files_6)
if collision_found:
    print("Collision found!")
else:
    print("No collision found.")
