w="Hello world"
encode_utf8=w.encode('utf-8')
encode_utf16=w.encode('utf-16')
encode_utf32=w.encode('utf-32')
print("UTF-8")
print("encode UTF-8 : ",encode_utf8)
print("encode UTF-8 : ",encode_utf8.decode('utf-8'))
print("UTF-16")
print("encode UTF-16 : ",encode_utf16)
print("encode UTF-16 : ",encode_utf16.decode('utf-16'))
print("UTF-32")
print("encode UTF-32 : ",encode_utf32)
print("encode UTF-32 : ",encode_utf32.decode('utf-32'))