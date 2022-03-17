import os

print('Testing:', 'erdauit.txt')
print('Exists:', os.access('erdauit.txt', os.F_OK))
print('Readable:', os.access('erdauit.txt', os.R_OK))
print('Writable:', os.access('erdauit.txt', os.W_OK))
print('Executable:', os.access('erdauit.txt', os.X_OK))