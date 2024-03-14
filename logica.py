import os

def verificar_pasta_salvar(caminho_base=""):
  pasta_salvar = os.path.join(caminho_base, "save-location")

  # Verifica se a pasta existe
  if not os.path.isdir(pasta_salvar):
    os.makedirs(pasta_salvar)
    return []

  # Lista os nomes das pastas dentro de "save-location"
  lista_pastas = os.listdir(pasta_salvar)

  return lista_pastas
