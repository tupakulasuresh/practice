def format_license(license_key, size):
    license_key = license_key.replace("-","").upper()
    prefix_len =  len(license_key) % size
    new_str = []
    if prefix_len > 0:
         new_str.append(license_key[:prefix_len])
         license_key = license_key[prefix_len:]
    while license_key:
        new_str.append(license_key[:size])
        license_key = license_key[size:]
    return "-".join(new_str)

print format_license("5F3Z-2e-9-w", 4)
print format_license("2-5g-3-J", 2)
print format_license("2-4A0r7-4k", 4)
