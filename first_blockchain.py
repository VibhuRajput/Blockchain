# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import hashlib
# main.py
class VibhutiCoinBlock:
    
    def __init__(self, previous_block_hash, transaction_list):

        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = f"{' - '.join(transaction_list)} - {previous_block_hash}"
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = []
        self.generate_genesis_block()

    def generate_genesis_block(self):
        self.chain.append(VibhutiCoinBlock("0", ['Genesis Block']))
    
    def create_block_from_transaction(self, transaction_list):
        previous_block_hash = self.last_block.block_hash
        self.chain.append(VibhutiCoinBlock(previous_block_hash, transaction_list))

    def display_chain(self):
        for i in range(len(self.chain)):
            print(f"Data {i + 1}: {self.chain[i].block_data}")
            print(f"Hash {i + 1}: {self.chain[i].block_hash}\n")

    @property
    def last_block(self):
        return self.chain[-1]
t1 = "Ujjwal sends 3.1 GC to Sashwat"
t2 = "Shashwat sends 2.5 GC to Shikhar"
t3 = "Shikhar sends 1.2 GC to Snehil"
t4 = "Snehil sends 0.5 GC to Ayush"
t5 = "Ayush sends 0.2 GC to Vaibhav"
t6 = "Vaibhav sends 0.1 GC to Anupam"

myblockchain = Blockchain()

myblockchain.create_block_from_transaction([t1, t2])
myblockchain.create_block_from_transaction([t3, t4])
myblockchain.create_block_from_transaction([t5, t6])

myblockchain.display_chain()