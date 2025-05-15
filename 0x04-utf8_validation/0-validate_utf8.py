#!/usr/bin/python3
def validUTF8(data):
    num_following = 0
    for byte in data:
        # Ensure we only consider the 8 least significant bits
        byte = byte & 0xFF
        if num_following == 0:
            # Determine the number of bytes for this character
            if (byte >> 7) == 0b0:
                # 1-byte character
                num_following = 0
            elif (byte >> 5) == 0b110:
                # 2-byte character
                num_following = 1
            elif (byte >> 4) == 0b1110:
                # 3-byte character
                num_following = 2
            elif (byte >> 3) == 0b11110:
                # 4-byte character
                num_following = 3
            else:
                # Invalid leading byte
                if (byte >> 6) != 0b10:
                    return False
        else:
            # check if continuation byte starts with 10
            if (byte >> 6) != 0b10:
                return False
                num_following -= 1
        # All characters must be complete
        return num_following == 0
