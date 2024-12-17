def msg_padding(message):
    message_bytes = bytearray(message, 'utf-8')
    
    org_len = len(message_bytes) * 8
    message_bytes.append(0x80)
    
    while (len(message_bytes) * 8) % 512 != 448:
        message_bytes.append(0)
    
    for i in range(8):
        message_bytes.append((org_len >> (i * 8)) & 0xFF)
    
    return message_bytes


def initialize_md5_variables():
  
    A = 0x67452301
    B = 0xEFCDAB89
    C = 0x98BADCFE
    D = 0x10325476

    # Per-round shift amounts
    s = [
        7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22,
        5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20,
        4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23,
        6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21,
    ]
    
    return A, B, C, D, s


def md5_update(A, B, C, D, AA, BB, CC, DD):

    A = (A + AA) & 0xFFFFFFFF
    B = (B + BB) & 0xFFFFFFFF
    C = (C + CC) & 0xFFFFFFFF
    D = (D + DD) & 0xFFFFFFFF

    return A, B, C, D


# Main program
message = input("Enter Your Password: ")

# Preprocess the message
preprocessed_message = msg_padding(message)

# Initialize variables
A, B, C, D, s = initialize_md5_variables()
AA, BB, CC, DD = A, B, C, D  # Store initial values for later update

# Update final variables (placeholder for main loop logic)
A, B, C, D = md5_update(A, B, C, D, AA, BB, CC, DD)

# Display results
print(f"Preprocessed message (hex): {preprocessed_message.hex()}")
print(f"Length: {len(preprocessed_message) * 8} bits")
print(f"Final values: A = {A:#010x}, B = {B:#010x}, C = {C:#010x}, D = {D:#010x}")
