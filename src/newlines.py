def find_min_max_widths(words):
    # Calcola la larghezza minima e massima
    min_width = max_width = current_width = 0
    line_lengths = []

    for word_length in words:
        if word_length == -1:  # Carattere "a capo"
            line_lengths.append(current_width - 1)  # Toglie l'ultimo spazio
            current_width = 0
        else:
            current_width += word_length + 1  # Aggiunge la parola e uno spazio

    # Aggiunge l'ultima riga se non finisce con un "a capo"
    if current_width > 0:
        line_lengths.append(current_width - 1)

    min_width = min(line_lengths)
    max_width = max(line_lengths)

    return min_width, max_width

# Lettura da file di input e scrittura su file di output
with open('input/newlines_input_1.txt', 'r') as input_file, open('output/newlines_output_1.txt', 'w') as output_file:
    T = int(input_file.readline().strip())  # Numero di casi di test

    for t in range(1, T + 1):
        input_file.readline()  # Ignora la riga vuota
        N = int(input_file.readline().strip())  # Numero di parole/caratteri
        W = list(map(int, input_file.readline().strip().split()))  # Lunghezze delle parole e "-1" per gli acapi

        K1, K2 = find_min_max_widths(W)
        output_file.write(f"Case #{t}: {K1} {K2}\n")

