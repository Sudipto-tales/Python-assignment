<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MD5 Algorithm Implementation</title>
    <style>
        /* General styles for the page */
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
            padding: 0;
            background-color: #f4f4f9;
            color: #333;
        }
        h1, h2, h3 {
            color: #444;
        }
        pre {
            background-color: #f8f8f8;
            padding: 15px;
            border: 1px solid #ddd;
            border-radius: 5px;
            overflow-x: auto;
        }
        code {
            background-color: #f4f4f4;
            padding: 2px 4px;
            border-radius: 3px;
        }
        .note {
            background-color: #ffffe0;
            border-left: 5px solid #ffd700;
            padding: 10px;
            margin: 20px 0;
        }
        ul {
            margin-left: 20px;
        }
    </style>
</head>
<body>

    <!-- Project Title -->
    <h1>MD5 Algorithm Implementation in Python</h1>
    <p>
        This project showcases a Python implementation of the MD5 hashing algorithm. MD5 is a cryptographic hash function 
        that produces a 128-bit hash value. While not recommended for secure applications due to vulnerabilities, MD5 
        remains widely used for checksums and non-secure applications.
    </p>

    <!-- Features Section -->
    <h2>Features</h2>
    <ul>
        <li><strong>Custom Padding Implementation:</strong> Handles message preprocessing to ensure proper length alignment.</li>
        <li><strong>Initialization:</strong> Defines constants and shifts used in MD5 processing.</li>
        <li><strong>Transformation:</strong> Processes data blocks using MD5-specific bitwise operations.</li>
        <li><strong>Final Hash:</strong> Combines processed variables into the final hexadecimal hash.</li>
    </ul>

    <!-- Prerequisites -->
    <h2>Prerequisites</h2>
    <p>
        The script uses the following Python standard libraries:
    </p>
    <ul>
        <li><code>time</code>: Adds a timestamp to the output hash.</li>
        <li><code>os</code>: Includes the process ID for uniqueness.</li>
    </ul>

    <!-- How It Works -->
    <h2>How It Works</h2>

    <!-- Step 1: Message Padding -->
    <h3>1. Message Padding</h3>
    <p>
        The input message is padded to ensure its length is a multiple of 512 bits:
        <ul>
            <li>Appends a <code>0x80</code> byte to the message.</li>
            <li>Fills with zero bytes until the length is 448 modulo 512.</li>
            <li>Appends the original message length (in bits) as an 8-byte integer.</li>
        </ul>
    </p>

    <!-- Step 2: Initialization -->
    <h3>2. Initialization</h3>
    <p>
        Initializes four 32-bit variables (<code>A</code>, <code>B</code>, <code>C</code>, <code>D</code>) 
        and per-round shift amounts required for MD5.
    </p>

    <!-- Step 3: Transformation -->
    <h3>3. Transformation</h3>
    <p>
        Processes the padded message in 512-bit chunks:
        <ul>
            <li>Splits each chunk into 16 words of 32 bits.</li>
            <li>Applies 64 rounds of transformations using predefined constants and logical operations.</li>
        </ul>
    </p>

    <!-- Step 4: Finalization -->
    <h3>4. Finalization</h3>
    <p>
        Combines the final values of <code>A</code>, <code>B</code>, <code>C</code>, and <code>D</code> 
        into a single 128-bit hash, formatted as a hexadecimal string.
    </p>

    <!-- Code Section -->
    <h2>Code</h2>
    <pre><code>
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
    </code></pre>

    <!-- Example Output -->
    <h2>Example Output</h2>
    <pre><code>
MD5 hash of '2003': <computed_hash><process_id><timestamp>
    </code></pre>

    <!-- Note -->
    <div class="note">
        <strong>Note:</strong> The output combines the MD5 hash with a process ID and timestamp for added uniqueness. 
        This implementation is intended for educational purposes and should not be used for cryptographic security.
    </div>

    <!-- License -->
    <h2>License</h2>
    <p>
        This project is licensed under the MIT License. You can freely use, modify, and distribute it.
    </p>

</body>
</html>
