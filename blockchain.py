from hashlib import sha256
from time import time

# This class represents a single block of data in the chain as well as a hash to the
# previous block.
class Block:

    # Defines the block with a data and the hash of the previous block.
    def __init__(self, data, prev_hash, difficulty):
        self.data = data
        self.prev_hash = prev_hash
        self.curr_hash = None
        self.__nonce = 0
        self.difficulty = difficulty

        self.update_hash()

    # Updates the hash of this block to contain the data, the previous hash, and find
    # a nonce value so that the hash stars with the number of zeros indicated by
    # difficulty.
    def update_hash(self):
        print("Mining for block \"" + self.data + "\"...")
        start_time = time()
        while (self.curr_hash == None or not self.is_valid()):
            self.__nonce += 1
            self.curr_hash = sha256((self.data + self.prev_hash + str(self.__nonce))
                .encode()).hexdigest()
        print("Mining complete after " + str(time() - start_time) + " seconds.\n")
    
    # Checks the current hash of the block and makes sure it is actually equal to the
    # hash of the block's data, and makes sure the hash starts with the right number
    # of zeros.
    def is_valid(self):
        return (self.curr_hash == sha256((self.data + self.prev_hash + str(self.__nonce))
                .encode()).hexdigest()) and self.curr_hash[:self.difficulty] == self.difficulty * "0"
    
    # For formatted printing to the terminal.
    def __str__(self):
        return "From: " + self.prev_hash+ "\nData: " + self.data + "\nHash: " + self.curr_hash

# This class represents a chain of blocks of data.
class Blockchain:

    # Creates a genesis block.
    def __init__(self, difficulty):
        self.difficulty = 5
        self.blocks = [Block("Genesis", difficulty * "0", difficulty)]

    # Adds a new block and correctly assigns it's previous hash to the hash of the
    # current last node.
    def add_block(self, data):
        self.blocks.append(Block(data, self.blocks[len(self.blocks) - 1].curr_hash,
                                 self.difficulty))

    # Checks the validity of each block's hash, and also makes sure that the hashes
    # that point to the previous block is consistant.
    def is_valid(self):
        res = True
        print("Checking blockchain validity...\n")
        
        if (not self.blocks[0].is_valid()):
            print("Block 0's hash is not valid.\n")
            res = False

        for i in range(1, len(self.blocks)):
            if (self.blocks[i].prev_hash != self.blocks[i - 1].curr_hash):
                print("Block " + str(i) + "'s record of the previous hash is not valid.")
                res = False
            if (not self.blocks[i].is_valid()):
                print("Block " + str(i) + "'s hash is not valid.\n")
                res = False
        
        if (res):
            print("Validity confirmed.")
        return res

    # Allows for indexing into the blockchain and retrieving a specific block.
    def __getitem__(self, index):
        return self.blocks[index]
    
    # Returns the number of blocks.
    def __len__(self):
        return len(self.blocks)
    
    # For formatted printing to the terminal.
    def __str__(self):
        res = ""
        for i in range(len(self.blocks)):
            res += str(self.blocks[i])
            res += "\n\n"
        return res[:-2]