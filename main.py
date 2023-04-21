'''
1. Inicialmente, cada caracter en el corpus de entrenamiento se trata como una subpalabra única.
2. Se calcula la frecuencia de cada par de subpalabras adyacentes (por ejemplo, "corri" y "endo") en el corpus de entrenamiento.
3. Los pares de subpalabras más frecuentes se combinan en una nueva subpalabra, que se agrega al vocabulario.
4. El proceso se repite para cada nueva subpalabra agregada al vocabulario, hasta que se alcanza el tamaño deseado del vocabulario.
'''

def tokenize_bpe(text, num_iterations):
    # Paso 1: Inicializar el vocabulario con los caracteres únicos del texto
    vocab = set(text)
    #vocab = set()
    
    # Paso 2: Iterar para crear los tokens
    for i in range(num_iterations):
        # Contar las frecuencias de los pares de subpalabras
        freq = {}
        for j in range(len(text)-1):
            pair = (text[j], text[j+1])
            if pair in freq:
                freq[pair] += 1
            else:
                freq[pair] = 1
        
        # Seleccionar el par de subpalabras más frecuente
        most_common_pair = max(freq, key=freq.get)
        
        # Reemplazar el par de subpalabras más frecuente por un nuevo token
        new_token = "".join(most_common_pair)
        text = text.replace("".join(most_common_pair), new_token)
        
        # Agregar el nuevo token al vocabulario
        vocab.add(new_token)
    
    # Paso 3: Devolver el vocabulario ordenado alfabéticamente
    return sorted(vocab)

with open('poemsv1.txt', 'r', encoding='utf-8') as file:
    text = ''.join(file.readlines())

print('Procesando')
print(tokenize_bpe(text, 1024))