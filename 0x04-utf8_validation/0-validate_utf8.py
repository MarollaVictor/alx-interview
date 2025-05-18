#!/usr/bin/python3
"""Validates if a given data set represents a valid UTF-8 encoding."""

def validUTF8(data):
    """Check if a list of integers represents valid UTF-8 bytes."""
    n_bytes = 0
    for byte in data:
        byte = byte & 0xFF  # Ensure we only use the 8 least significant bits
        if n_bytes == 0:
            # Determine the number of continuation bytes
            if (byte >> 7) == 0b0:
                continue
            elif (byte >> 5) == 0b110:
                n_bytes = 1
            elif (byte >> 4) == 0b1110:
                n_bytes = 2
            elif (byte >> 3) == 0b11110:
                n_bytes = 3
            else:
                return False
        else:
            # Check continuation byte
            if (byte >> 6) != 0b10:
                return False
            n_bytes -= 1
    return n_bytes == 0
