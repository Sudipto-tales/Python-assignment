# MD5 Algorithm Implementation

This project demonstrates the implementation of the MD5 hashing algorithm in Python. MD5 is a cryptographic hash function that produces a 128-bit hash value from an input message. Although MD5 is no longer recommended for cryptographic security due to vulnerabilities, it remains widely used for purposes like checksums and non-critical data verification.

---

## Features

- **Custom Padding Implementation**: Handles message preprocessing to ensure proper length alignment.
- **MD5 Initialization**: Sets up constants and shift amounts used in the hashing process.
- **Transformation Rounds**: Applies the core logic of MD5 using bitwise operations on 512-bit chunks.
- **Final Hash Computation**: Produces a 128-bit hash formatted as a hexadecimal string.

---

## Prerequisites

Ensure you have Python installed. This script uses the following Python standard libraries:

- `time`: Adds a timestamp to the output hash.
- `os`: Includes the process ID for uniqueness.

---

## How It Works

### 1. Message Padding
The input message is padded to ensure its length is a multiple of 512 bits:
- Appends a `0x80` byte to the message.
- Adds zero bytes until the length is congruent to 448 modulo 512.
- Appends the original message length (in bits) as an 8-byte little-endian integer.

### 2. Initialization
The algorithm initializes four 32-bit variables (`A`, `B`, `C`, `D`) with predefined constants and sets up shift amounts for the transformation rounds.

### 3. Transformation
The padded message is processed in 512-bit chunks:
- Each chunk is split into 16 32-bit words.
- Applies 64 rounds of transformations using constants and logical operations.

### 4. Finalization
The final values of `A`, `B`, `C`, and `D` are combined to produce the final 128-bit hash as a hexadecimal string.

---

## Code Example

```python
import time
import os

def msg_padding(message):
    # Padding the message to align to 512-bit length
    pass

def initialize_md5_variables():
    # Initialize MD5-specific constants and shift values
    pass

def md5_transform(A, B, C, D, block, s):
    # Core MD5 processing on each 512-bit block
    pass

def md5(message):
    # Full MD5 hash computation
    pass

# Testing the MD5 function with the input "2003"
hash_result = md5("2003") + f"{os.getpid()}" + f"{time.time()}"
print("MD5 hash of '2003':", hash_result)
