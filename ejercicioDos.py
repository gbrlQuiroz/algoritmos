# No se especifica nada de los acentos, así que no lo considero, las palabras con acentos se consideran diferentes:  asi != así

from collections import Counter
import json

texto = """Érase una vez una niñita que lucía una hermosa capa 
de color rojo. Como la niña la usaba muy a menudo, todos la 
llamaban Caperucita Roja. Un día, la mamá de Caperucita Roja la 
llamó y le dijo: — Abuelita no se siente muy bien, he horneado 
unas galletitas y quiero que tú se las lleves. — Claro que sí 
— respondió Caperucita Roja, poniéndose su capa y llenando su 
canasta de galletas recién horneadas. Antes de salir, su mamá 
le dijo: — Escúchame muy bien, quédate en el camino y nunca 
hables con extraños. — Yo sé mamá — respondió Caperucita Roja y 
salió inmediatamente hacia la casa de la abuelita."""

print(f'Texto Original: {texto}')

# limpieza y preparacion del texto
textoMinusculas = texto.lower()
textoSinComas = textoMinusculas.replace(',', '')
textoSinPuntos = textoSinComas.replace('.', '')
textoSinGuiones = textoSinPuntos.replace('—', '')
textoSinSaltos = textoSinGuiones.replace('\n', '')

cadenas = textoSinSaltos.split(' ')

aDict = dict(Counter(cadenas))
aJson = json.dumps(aDict, ensure_ascii=False)

print(f'\n\nTexto Original contando las palabras en Json:\n')
print(aJson)
