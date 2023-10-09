message = input('what is your message ')
original = open('sample.bmp', 'rb')
data = []
key = int(input('what is your key '))
bytes = original.read(1)
while bytes:
    data.append(int.from_bytes(bytes, 'little'))
    bytes = original.read(1)
print(data)
for i in range(key, key + len(message)):
    data[i] = ord(message[i-key])
original.close()
coded = open('encoded.bmp', 'wb')
coded.write(bytearray(data))
coded.close()