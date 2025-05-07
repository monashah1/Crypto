import hashlib

class MerkleTree:
    def __init__(self, files):
        self.files = files
        self.tree = None

    def hash_node(self, data):
        return hashlib.sha256(data).digest()

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
            level_hashes = ["({})".format(hash.hex()[:8]) for hash in all_hashes if hash != None and len(bin(all_hashes.index(hash))) - 2 == i]
            level += " ".join(level_hashes)
            print(level)
        print()

# testing with  four leaf nodes
print("Test with four leaf nodes:")
files_4 = ["test_file1.txt", "test_file2.txt", "test_file3.txt", "test_file4.txt"]
merkle_tree_4 = MerkleTree(files_4)
merkle_tree_4.print_merkle_tree()

# testing with six leaf nodes
print("\nTest with six leaf nodes:")
files_6 = ["test_file1.txt", "test_file2.txt", "test_file3.txt", "test_file4.txt", "test_file5.txt", "test_file6.txt"]
merkle_tree_6 = MerkleTree(files_6)
merkle_tree_6.print_merkle_tree()
