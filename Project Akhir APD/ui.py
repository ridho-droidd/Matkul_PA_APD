
from InquirerPy import inquirer


# MENU PILIHAN
def pilih_menu(pesan, pilihan):

    hasil = inquirer.select(
        message=pesan,
        choices=pilihan,
        instruction="(Gunakan tombol panah dan Enter)"
    ).execute()

    return hasil


# INPUT TEKS
def input_teks(pesan):

    hasil = inquirer.text(
        message=pesan
    ).execute()

    return hasil.strip()
