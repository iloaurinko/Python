import qrcode

# URL-ссылка, которую вы хотите закодировать в QR-код
url = "https://github.com/iloaurinko"

# Создание QR-кода
qr = qrcode.QRCode(
    version=1,  # Размер QR-кода
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Уровень коррекции ошибок
    box_size=10,  # Размер каждого квадратика
    border=4,  # Толщина границы
)

# Добавление данных (URL) в QR-код
qr.add_data(url)
qr.make(fit=True)

# Создание изображения QR-кода
img = qr.make_image(fill_color="black", back_color="white")

# Сохранение изображения QR-кода
img.save("qrcode.png")

print("QR-код успешно создан и сохранен как 'qrcode.png'")
