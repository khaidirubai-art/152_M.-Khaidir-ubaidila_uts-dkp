"""UTS Dasar Komputer dan Pemrograman - Kelompok C (Instrumentasi)
Monitoring Level Tangki

Aturan status:
    Level < 30%          -> LOW
    30% <= Level <= 80%  -> NORMAL
    Level > 80%          -> HIGH
"""

BATAS_BAWAH = 30
BATAS_ATAS = 80

# 15 data inti dari soal + 5 data tambahan (30, 80, 0, 100, 29.5)
data_level = [
    18, 25, 33, 41, 55, 62, 76, 84, 91, 47, 29, 38, 70, 82, 15,
    30, 80, 0, 100, 29.5,
]


def status_level(level):
    """Menentukan status tangki dari level (%). Mengembalikan LOW/NORMAL/HIGH."""
    if level < BATAS_BAWAH:
        return "LOW"
    elif level <= BATAS_ATAS:
        return "NORMAL"
    else:
        return "HIGH"


def hitung_kategori(data):
    """Menghitung jumlah data pada tiap status. Mengembalikan dictionary."""
    jumlah = {"LOW": 0, "NORMAL": 0, "HIGH": 0}
    for level in data:
        jumlah[status_level(level)] += 1
    return jumlah


def rata_rata(data):
    """Menghitung rata-rata dari list angka. Mengembalikan float."""
    total = 0
    for nilai in data:
        total += nilai
    return total / len(data)


def main():
    print("===== MONITORING LEVEL TANGKI =====")
    nomor = 1
    for level in data_level:
        status = status_level(level)
        print(f"{nomor:02d} level = {level:>5}% -> {status}")
        nomor += 1

    jumlah = hitung_kategori(data_level)

    print()
    print("===== RINGKASAN =====")
    print(f"Total data : {len(data_level)}")
    print(f"LOW        : {jumlah['LOW']}")
    print(f"NORMAL     : {jumlah['NORMAL']}")
    print(f"HIGH       : {jumlah['HIGH']}")
    print(f"Rata-rata  : {rata_rata(data_level):.3f}%")
    print(f"Maksimum   : {max(data_level)}%")
    print(f"Minimum    : {min(data_level)}%")


if __name__ == "__main__":
    main()
