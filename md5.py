#Padding: Append bits to the input to ensure its length is congruent to 448 modulo 512.
def msg_padding(message):
    message_bytes = bytearray(message, 'utf-8')
    
    org_len = len(message_bytes) * 8
    message_bytes.append(0x80)
    
    while (len(message_bytes) * 8) % 512 != 448:
        message_bytes.append(0)
    
    for i in range(8):
        message_bytes.append(org_len >> (i * 8) & 0xFF)
    
    return message_bytes

message = input("Enter Your Password: ")
preprocessed_message = msg_padding(message)

print(f"Preprocessed message (hex): {preprocessed_message.hex()}")
print(f"Length: {len(preprocessed_message) * 8} bits")
