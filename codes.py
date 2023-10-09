mode = input('encode or decode? ')
data = []
msage = []
out = ''
if mode == 'encode':
    message = input('what is your message ')
    original = open('sample.bmp', 'rb')
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
elif mode == 'decode':
    file = input('what file would you like to decode? ')
    key = int(input('what is the key? '))
    lenmsg = int(input('how long is the message? '))
    codefile = open(file, 'rb')
    bytes = codefile.read(1)
    while bytes:
        data.append(int.from_bytes(bytes, 'little'))
        bytes = codefile.read(1)
    for i in range(key, key + lenmsg):
        msage.append(chr(data[i]))
    print(''.join(msage))
else:
    print('not a valid mode')