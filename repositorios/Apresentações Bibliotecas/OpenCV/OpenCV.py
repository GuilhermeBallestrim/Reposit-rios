import cv2

# Carrega uma imagem (substitua 'caminho/para/imagem.jpg' pelo caminho real)
imagem = cv2.imread('C:/Users/Aluno 02/Pictures/images.jpg')

# Verifica se a imagem foi carregada
if imagem is None:
    print("Erro ao carregar a imagem.")
    exit()

# Converte para escala de cinza
imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)

# Mostra a imagem original
cv2.imshow('Imagem Original', imagem)

# Mostra a imagem em escala de cinza
cv2.imshow('Imagem Cinza', imagem_cinza)

# Espera até que alguma tecla seja pressionada
cv2.waitKey(0)

# Fecha todas as janelas
cv2.destroyAllWindows()
