#  pip install pywhatkit

import pywhatkit as kit

texto = '''
Herald Fortunato Sebastião

e

Bellanires Jimenez Soto!
'''

#  Gera imagem com texto escrito
kit.text_to_handwriting(texto, save_to='texto_a_mao.png')