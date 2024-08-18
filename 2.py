import random

# Load the BIP39 wordlist
def load_bip39_wordlist(filename='bip.txt'):
    with open(filename, 'r') as f:
        words = f.read().splitlines()
    return words

# Create a function to generate a mnemonic phrase
def generate_mnemonic_phrase(wordlist, num_words=12):
    return ' '.join(random.choice(wordlist) for _ in range(num_words))

# Load the BIP39 wordlist
bip39_wordlist = load_bip39_wordlist()

# Initialize an empty list to store the mnemonics
mnemonics = []

# Loop 1,000,000 times
for _ in range(1000000):
    # Generate a 12-word mnemonic phrase
    mnemonic = generate_mnemonic_phrase(bip39_wordlist)
    # Add the mnemonic to the list
    mnemonics.append(mnemonic)

# Save the mnemonics to a file
with open("mnemonic.txt", "w") as f:
    for mnemonic in mnemonics:
        f.write(mnemonic + "\n")
