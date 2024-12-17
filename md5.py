number = 2003

def padding(number):
 binary_representation = bin(number)[2:]
 return binary_representation.zfill(512)

print(f"512-bit binary representation of {number} is:\n{padding(number)}")
print(f"Length: {len(padding(number))} bits")
