# blockchain-sim
A blockchain simulator built over SHA256; useful for modeling mining speeds at varying difficulties, verify the validity of blockchains, and measuring the time needed to forge transactions.

## Using in a Python Script
The file `blockchain.py` is a functional blockchain simulator that you can incorporate into your Python scripts.

### Imports
To import the blockchain module, insert the following code in your script:
```python
import blockchain
```
To import a specific class, like `Blockchain`, use the following code:
```python
from blockchain import Blockchain
```

### The `Block` Class

This class represents a single block of data in the chain as well as a hash to the previous block. To create a `Block`, you need to pass in the data, the hash of the previous block being linked to, and the difficulty (the number of zeros that the hash of this block needs to start with).
```python
genesis_block = Block("Genesis", "000000", 6)
```
The `update_hash()` function updates the hash of the block to confirm that it correctly hashes the block's data and that the hash starts with the correct number of zeros given by the difficulty. This is implemented through the use of a nonce value, the implementation of which has been encapsulated into the class design. Calling the `update_hash()` function will print messages to the screen that will let you track when mining starts and how much time it took to the mine the block. (This message is also created when the block is first made.)
```python
genesis_block.update_hash()
```
The `is_valid()` function returns a boolean. It returns `True` if and only if the value of the block's hash is indeed the hash of the block's data and the hash starts with the correct number of zeros.
```python
if (genesis_block.is_valid()):
    print("Block is valid.")
```
The `Block` can also be printed to the terminal to show the hash of the previous block it links to, its data, and its current hash.
```python
print(genesis_block)
```

### The `Blockchain` Class
This class represents a chain of blocks of data. It can be initialized by passing in a difficulty, which is the number of zeros that the hash of each block in the chain has to start with. Higher difficulties imply more time needed to mine blocks on average. In initializing the object, the class also creates a genesis block.
```python
chain = Blockchain(5)
```
Blocks can be added to the chain using the `add_block` function by passing in the data of the block. The class handles the hash linking.
```python
chain.add_block("$1 from Alice to Bob.")
```
Individual blocks can be accessed by indexing into the blockchain, just as you would with an array. Keep in mind that element 0 is the genesis block, where as element 1 is the first element with non-trivial data in the chain.
```python
transaction = chain[1]
```
The number of blocks, including the genesis block, can be accessed using the `len()` function, just like with arrays.
```python
num_blocks = len(chain)
```
The `is_valid()` function makes sure the hash of each block in the chain is valid, and it also makes sure that each block's record of the previous block's hash matches the previous block's record of it's own hash. Calling it will print a series of messages to the terminal, either the places where invalid data was discovered or a confirmation message that the block is valid. The function also returns a boolean representing the chain's validity.
```python
chain.is_valid()
```
The `Blockchain` can also be printed to the terminal. This prints each individual `Block` which is part of the blockchain.
```python
print(chain)
```

### Examples
The file `terminal.py` is an example of how to use the blockchain module in a Python script. To execute the script, download `terminal.py` and `blockchain.py` and enter `python terminal.py` into a terminal window.

## Using the Dash App
There are plans for the future to implement a Dash web app for increased accessibility with using this module.

## Code Organization
Both `blockchain.py` and `terminal.py` are located in the root directory. `blockchain.py` contains the classes representing blocks and blockchains, whereas `terminal.py` is an example of how to implement the blockchain module into a Python script.
