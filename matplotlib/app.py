import smbus
import time

# ADXL345 adresi
DEVICE_ADDRESS = 0x53

# I2C otobüs numarası (Orange Pi PC Plus'ta I2C-1 kullanılır)
bus = smbus.SMBus(1)

# ADXL345'e başlatma komutu gönderme
bus.write_byte_data(DEVICE_ADDRESS, 0x2D, 0x08)

# ADXL345 veri formatını ayarlama (tam çözünürlük)
bus.write_byte_data(DEVICE_ADDRESS, 0x31, 0x08)

# Ölçek faktörü
SCALE_FACTOR = 3.9  # 3.9 mg/LSB

try:
    while True:
        # X ekseninden veri okuma
        x0 = bus.read_byte_data(DEVICE_ADDRESS, 0x32)
        x1 = bus.read_byte_data(DEVICE_ADDRESS, 0x33)
        x = (x1 << 8) | x0
        if x > 0x7FFF:
            x = x - 0xFFFF

        # Y ekseninden veri okuma
        y0 = bus.read_byte_data(DEVICE_ADDRESS, 0x34)
        y1 = bus.read_byte_data(DEVICE_ADDRESS, 0x35)
        y = (y1 << 8) | y0
        if y > 0x7FFF:
            y = y - 0xFFFF

        # Z ekseninden veri okuma
        z0 = bus.read_byte_data(DEVICE_ADDRESS, 0x36)
        z1 = bus.read_byte_data(DEVICE_ADDRESS, 0x37)
        z = (z1 << 8) | z0
        if z > 0x7FFF:
            z = z - 0xFFFF

        # Ivme hesaplama
        x_g = x * SCALE_FACTOR
        y_g = y * SCALE_FACTOR
        z_g = z * SCALE_FACTOR

        # Okunan verileri ekrana yazdırma
        print("X (g):", x_g)
        print("Y (g):", y_g)
        print("Z (g):", z_g)
        print("---------")

        # 0.1 saniye bekleme
        time.sleep(0.1)

except KeyboardInterrupt:
    pass
Bu güncellenmiş kodda, X, Y ve Z eksenlerinden veri okurken eksi değerler doğru bir şekilde işlenir. Okunan verileri hesaplama ve ekrana yazdırma aşamaları da güncellenmiştir.

Dikkat edilmesi gereken bir nokta, ölçek faktörünün değiştiği ve 3.9 mg/LSB olarak güncellendiği noktadır. Bu, ADXL345 ivmeölçer tarafından sağlanan hassasiyeti temsil eder. Ölçek faktörünü kullanarak okunan verileri doğru bir şekilde ivme birimine dönüştürebilirsiniz.

Bu güncellenmiş kodda eksi değerleri doğru bir şekilde işlemleyerek istediğiniz sonuçları elde etmeniz gerektiğini umuyorum.






