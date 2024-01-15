def encrypt(msg, key, index=0):
    if index >= len(msg):
        return msg

    e_ch = ord(msg[index]) + key
    if e_ch > 90:  # is key less than 26?
        e_ch -= 26
    e_ch = chr(e_ch)

    msg = msg[:index] + e_ch + msg[index + 1 :]

    # calling print after before change output
    encrypt(msg, key, index + 1)
    print(e_ch, end="")


if __name__ == "__main__":
    msg = "AXZ"
    key = 8
    encrypt(msg, key, 0)
    print()
