from blockchain import Blockchain

chain = Blockchain(5)
chain.add_block("$1 from Alice to Bob.")
chain.add_block("$2 from Bob to Carol.")

print("Complete Chain:\n")
print(chain)
print()

chain.is_valid()
print()

print("Changing block 1's data.")
chain[1].data = "$100 from Alice to Bob."
chain.is_valid()
print()

print("Updating Block 1's hash.")
chain[1].update_hash()
chain.is_valid()
print()

print("Updating Block 2's prev_hash and curr_hash.")
chain[2].prev_hash = chain[1].curr_hash
chain[2].update_hash()
chain.is_valid()
print()
