import sys
import time

def jalankan_lirik():
    lirik = [
        ("Bila habis sudah..... cinta ini", 0.14),
        ("Tak lagi tersisa... untuk dunia", 0.15),
        ("Karena telah ku habiskan sisa cintaku", 0.12),
        ("Hanya untukmuuuu.....:)", 0.15),
        ("Karena telah ku habiskan... sisa cintaku", 0.13),
        ("Hanya untukmu....:)", 0.15),
    ]
    # Delay between lines
    delay = [0.05, 0.5, 0.5, 0.5, 0.5, 0.5]

    print("\n==surat Cinta Untuk Starla==")  # 

    for i, (baris_lagu, delay_karakter) in enumerate(lirik):
        for karakter in baris_lagu:
            print(karakter, end='', flush=True)
            time.sleep(delay_karakter)
        time.sleep(delay[i])
        print('')




# Call the function to run it
jalankan_lirik()
