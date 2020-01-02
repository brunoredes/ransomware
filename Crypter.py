#módulo que vai ter um método que encripta arquivos
def change_files(filename, cryptoFn, block_size=16):
    with open(filename, 'r+b') as _file:
        raw_value = _file.read(block_size)
        while raw_value:
            cipher_value = cryptoFn(raw_value)
            #compara o tamanho do bloco cifrado e do plain text
            if len(raw_value) != len(cipher_value):
                raise ValueError('O valor cifrado {} tem um tamanho diferente d ovalor plano {}'.format(len(cipher_value), len(raw_value)))
            
            _file.seek(-len(raw_value), 1)
            _file.write(cipher_value)
            raw_value = _file.read(block_size)