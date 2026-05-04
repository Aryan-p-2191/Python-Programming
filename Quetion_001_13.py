'''13.Convert bytes into KB, MB and GB.'''
bytes=int(input("enter bytes:"))
kb = bytes/10**3
mb = bytes/10**6
gb = bytes/10**9
print(f"""kb={kb}
mb={mb}
gb={gb}
""")