def main(distancia):
    if distancia <= 200:
        preco = distancia * 0.50
    elif distancia <= 400:
        preco = distancia * 0.45
    else:
        preco = distancia * 0.35
    return preco