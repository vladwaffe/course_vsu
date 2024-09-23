file_size_bytes = int(input("Введите размер файла в байтах: "))


full_kilobytes = file_size_bytes // 1024


full_terabytes = file_size_bytes // (1024 ** 4)

print(f"Количество полных килобайт: {full_kilobytes}")
print(f"Количество полных терабайт: {full_terabytes}")
