from tokenizers import Tokenizer, models, pre_tokenizers, decoders, trainers, processors

def tokenize_bpe(text, num_iters=3000):
    # Initialize a tokenizer
    tokenizer = Tokenizer(models.WordPiece(unk_token="<unk>"))

    # Customize pre-tokenization and decoding
    tokenizer.pre_tokenizer = pre_tokenizers.Whitespace()
    tokenizer.decoder = decoders.WordPiece()

    # Train the tokenizer
    trainer = trainers.WordPieceTrainer(vocab_size=5000, min_frequency=2)
    tokenizer.train_from_iterator([text], trainer=trainer)

    # Tokenize the text 
    encoding = tokenizer.encode(text)
    tokens = encoding.tokens

    return tokens

def encode_bpe(text, dict):
    text = text.lower()
    tokens = []

    while len(text) != 0:
        aux = text
        for i in range(len(text)):
            if text in dict:
                tk = dict[dict.index(text)]
                text = text.replace(tk, '')
                tokens.append(tk)
                break
            else:
                text = text[:-1]
        text = aux.replace(tokens[-1], '')
    return tokens


with open('poemsv1.txt', 'r', encoding='utf-8') as file:
    text = ''.join(file.readlines()).lower()

bpe = tokenize_bpe(text)
bpe = [c.replace('#', '') for c in bpe]
#bpe = [c for c in bpe if len(c) > 1]
bpe = list(set(bpe))
bpe.append(' ')
#bpe = sorted(bpe, key=len)[::-1]

print('Procesando')
print(len(bpe))
print(bpe)

while True:
    s = input('Ingrese una cadena a tokenizar: ')
    #print(f"tokens encontrados: {[v for k in s.split(' ') for v in encode_bpe(k, bpe)]}")
    print(f"tokens encontrados: {encode_bpe(s, bpe)}")