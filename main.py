from pyscript import document

print("-" * 132)
def imprimir_hola():
    print("Hola desde utilidades")


def translate_english(event):
    input_text = document.querySelector("#english")
    english = input_text.value
    output_div = document.querySelector("#output")
    output_div.innerText = arrr.translate(english)
    print("nose que poner aqui")
