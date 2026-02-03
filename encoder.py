# Input Payload

payload = "malicious_payload_test"

print("Original Payload:")
print(payload)


# Base64 Encoding

import base64
import random
import string

encoded_payload = base64.b64encode(payload.encode()).decode()

print("\nBase64 Encoded Payload:")
print(encoded_payload)

# XOR Encoding

key = "K"        # user-defined key


xor_encoded = ""
for i in range(len(payload)):
    xor_encoded += chr(ord(payload[i]) ^ ord(key[i % len(key)]))

print("\nXOR Encoded Payload:")
print(xor_encoded)


# ROT13 Encoding

def rot13(text):
    result = ""
    for char in text:
        if 'a' <= char <= 'z':
            result += chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
        elif 'A' <= char <='Z':
            result += chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
        else:
            result += char
    return result
rot13_encoded = rot13(payload)

print("\nROT13 Encoded Payload:")
print(rot13_encoded)

# Random Character Insertion Obfuscation
def random_insertion(text):
    obfuscated = ""
    for char in text:
        obfuscated += char
        if random.choice([True, False]):
           obfuscated += random.choice(string.ascii_letters)
    return obfuscated

random_obfuscated = random_insertion(payload)

print("\nRandom Character Obfuscated Payload:")
print(random_obfuscated)


# Charater Splitting & Concatenation Obfuscation
def split_and_concatenate(text, split_size=3):
    parts = []
    for i in range(0, len(text), split_size):
        parts.append(text[i:i+split_size])
    return "".join(parts)

split_concat_payload = split_and_concatenate(payload)

print("\nSplit & Concatenated Payload:")
print(split_concat_payload)


# Reversible Transformation (String Reversal)
def reversible_transform(text):
    return text[::-1]

reversed_payload = reversible_transform(payload)

print("\nReversibly Transformed Payload:")
print(reversed_payload)


# Escape-Sequence Obfuscation

def escape_sequence_obfuscation(text):
    escaped = ""
    for char in text:
        escaped += "\\x" + format(ord(char), "02x")
    return escaped

escaped_payload = escape_sequence_obfuscation(payload)

print("\nEscape-Sequence Obfuscated Payload:")
print(escaped_payload)


# Evasion Testing Module (Simulated Detection)
def simulated_detection(payload_data):
    signatures = ["malicious", "payload", "attack"]
    for sig in signatures:
        if sig in payload_data.lower():
           return "Detected"
    return "Bypassed"

print("\n--- Evasion Testing Results ---")

print("Original Payload:", simulated_detection(payload))
print("Base64 Encoded Payload:", simulated_detection(encoded_payload))
print("XOR Encoded Payload:", simulated_detection(xor_encoded))
print("ROT13 Encoded Payload:", simulated_detection(rot13_encoded))
print("Random Obfuscated Payload:", simulated_detection(random_obfuscated))
print("Split & Concatenated Payload:", simulated_detection(split_concat_payload))
print("Reversed Payload:", simulated_detection(reversed_payload))
print("Escape-Sequence Payload:", simulated_detection(escaped_payload))


# STEP 7: Output Summary

print("\n--- Payload Comparison Summary ---")
print("Original Payload        :", payload)
print("Base64 Encoded          :", encoded_payload)
print("XOR Encoded             :", xor_encoded)
print("ROT13 Encoded           :", rot13_encoded)
print("Random Obfuscated       :", random_obfuscated)
print("Split & Concatenated    :", split_concat_payload)
print("Reversed Payload        :", reversed_payload)
print("Escape-Sequence Payload :", escaped_payload)


            