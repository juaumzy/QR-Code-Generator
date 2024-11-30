import qrcode
while True:
    url = input("Digite uma Url para converter em Qrcode \n")
    if url.startswith("https") or url.startswith("http"):
        qr = qrcode.make(url)
        qr.save("qrcode.png")
        print("Qrcode Gerado com Sucesso! ")
        break
    else:
        print ("insira um link valido (https,http) ")