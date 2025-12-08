def huffman_encode(msg: str):
    """Кодирует текст с помощью алгоритма Хаффмана"""
    if not msg:
        return "", {}

    # подсчет частоты повтора символов
    freq = {}
    for char in msg:
        freq[char] = freq.get(char, 0) + 1

    # создаем список узлов [частота, символ]
    nodes = [[freq, char] for char, freq in freq.items()]

    # строим дерево хаффмана
    while len(nodes) > 1:
        # сортируем по частоте (сначала наименьшие)
        nodes.sort(key=lambda x: x[0])

        # берём два узла с наименьшей частотой повторения
        left = nodes.pop(0)
        right = nodes.pop(0)

        # создаем новый узел
        new_node = [left[0] + right[0], left, right]
        nodes.append(new_node)

    # строим таблицу кодов
    huffman_table = {}

    def build_codes(node, code=""):
        if len(node) == 2:  # листовой узел
            huffman_table[node[1]] = code

        else:  # внутренний узел
            build_codes(node[1], code + "0")  # левая ветка
            build_codes(node[2], code + "1")  # правая ветка

    if nodes:
        build_codes(nodes[0])

    # если один символ, устанавливаем код "0"
    if len(huffman_table) == 1:
        char = list(huffman_table.keys())[0]
        huffman_table[char] = '0'

    encoded_msg = ''.join(huffman_table[char] for char in msg)

    return encoded_msg, huffman_table


def huffman_decode(encoded: str, table: dict):
    """Декодирует текст с помощью таблицы Хаффмана"""
    if not encoded or not table:
        return ""

    # создаем обратную таблицу (код -> символ)
    reverse_table = {code: char for char, code in table.items()}

    current_code = ""
    decoded_text = []

    for bit in encoded:
        current_code += bit
        if current_code in reverse_table:
            decoded_text.append(reverse_table[current_code])
            current_code = ""

    return ''.join(decoded_text)


def encode_to_file(msg: str, filename: str):
    """Кодирует текст и сохраняет в файл (простой текстовый формат)"""
    encoded, table = huffman_encode(msg)

    with open(filename, 'w', encoding='utf-8') as f:
        # сохраняем таблицу в формате "символ:код\n"
        for char, code in table.items():
            # записываем специальные символы, чтобы не ломался формат
            if char == '\n':
                char_escaped = '\\n'
            elif char == '\t':
                char_escaped = '\\t'
            elif char == '\\':
                char_escaped = '\\\\'
            else:
                char_escaped = char
            f.write(f"{char_escaped}:{code}\n")

        # создаём разделитель между таблицей и закоддированным текстом
        f.write("---\n")

        f.write(encoded)


def decode_from_file(filename: str):
    """Декодирует текст из файла"""
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    table = {}
    i = 0
    while i < len(lines) and lines[i].strip() != '---':
        line = lines[i].strip()
        if ':' in line:
            char_escaped, code = line.split(':', 1)
            # восстанавливаем специальные символы
            if char_escaped == '\\n':
                char = '\n'
            elif char_escaped == '\\t':
                char = '\t'
            elif char_escaped == '\\\\':
                char = '\\'
            else:
                char = char_escaped
            table[char] = code
        i += 1

    encoded = ''.join(lines[i + 1:]).strip()

    return huffman_decode(encoded, table)


# Простая бинарная версия
def encode_to_file_bin(msg: str, filename: str):
    """Кодирует текст и сохраняет в бинарный файл"""
    encoded, table = huffman_encode(msg)

    with open(filename, 'wb') as f:
        table_data = ""
        for char, code in table.items():
            # кодируем символ через unicode (чтобы избежать проблем со спец. символами и т.д.)
            char_code = ord(char)
            table_data += f"{char_code}:{code};"

        # записываем длину таблицы и саму таблицу
        table_bytes = table_data.encode('utf-8')
        f.write(len(table_bytes).to_bytes(4, 'big'))
        f.write(table_bytes)

        # преобразуем биты в байты
        padding = 8 - len(encoded) % 8
        if padding != 8:
            encoded += '0' * padding

        # записываем закодированные данные
        encoded_bytes = bytearray()
        for i in range(0, len(encoded), 8):
            byte = encoded[i:i + 8]
            encoded_bytes.append(int(byte, 2))

        f.write(len(encoded).to_bytes(4, 'big'))
        f.write(encoded_bytes)


def decode_from_file_bin(filename: str):
    """Декодирует текст из бинарного файла"""
    with open(filename, 'rb') as f:

        table_length = int.from_bytes(f.read(4), 'big')
        table_data = f.read(table_length).decode('utf-8')

        # восстанавливаем таблицу
        table = {}
        for item in table_data.split(';'):
            if ':' in item:
                char_code, code = item.split(':', 1)
                if char_code:
                    char = chr(int(char_code))
                    table[char] = code

        bit_length = int.from_bytes(f.read(4), 'big')
        encoded_bytes = f.read()

    # преобразуем байты в биты
    encoded_bits = ""
    for byte in encoded_bytes:
        encoded_bits += format(byte, '08b')
    encoded_bits = encoded_bits[:bit_length]  # обрезаем до исходной длины

    return huffman_decode(encoded_bits, table)
