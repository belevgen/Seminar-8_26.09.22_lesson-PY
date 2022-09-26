def read_file(title):
    src = input(title)
    f = open(src, "r")
    data = f.read()
    f.close()

    return data


def write_file(title, data):
    dst = input(title)
    f = open(dst, "w")
    f.write(data)
    f.close()


command = input("Введите команду : ")

if command == "1":
    n = input('Вас интересует справочник учеников?')
    data = read_file("Файл с входными данными для сжатия: ")
    print(f"Сейчас мы будем сжимать данные: {data}")
    compressed = compress(data)
    print(f"Сжатые данные: {compressed}")
    write_file("Файл для сжатых данных: ", compressed)

elif command == "decompress":
    data = read_file("Файл с сжатыми данными: ")
    print(f"Сейчас мы будем разжимать данные: {data}")
    decompressed = decompress(data)
    print(f"Разжатые данные: {decompressed}")
    write_file("Файл для разжатых данных: ", decompressed)

else:
    print("Команда не найдена")