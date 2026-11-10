from data import petualang
from prettytable import PrettyTable
from InquirerPy import inquirer


def periksa_pendaftar():

    tabel = PrettyTable()

    tabel.field_names = [
        "Nama", "Rank", "Status"
    ]

    for nama, data in petualang.items():

        if data["status"] == "Menunggu":

            tabel.add_row([
                nama,
                data["rank"],
                data["status"]
            ])

    print(tabel)


def proses_pendaftaran():

    daftar = []

    for nama, data in petualang.items():

        if data["status"] == "Menunggu":
            daftar.append(nama)

    if len(daftar) == 0:
        print("Tidak ada pendaftar baru!")
        return

    username = inquirer.select(
        message="Pilih petualang:",
        choices=daftar
    ).execute()

    keputusan = inquirer.select(
        message="Apakah petualang diterima?",
        choices=[
            "Ya",
            "Tidak"
        ]
    ).execute()

    if keputusan == "Ya":

        petualang[username]["status"] = "Diterima"

        print("Petualang berhasil diterima!")

    else:

        petualang[username]["status"] = "Ditolak"

        print("Petualang ditolak!")


def menu_resepsionis():

    while True:

        pilihan = inquirer.select(
            message="=== MENU RESEPSIONIS ===",
            choices=[
                "Periksa Pendaftar",
                "Proses Pendaftaran",
                "Logout"
            ]
        ).execute()

        if pilihan == "Periksa Pendaftar":

            periksa_pendaftar()

        elif pilihan == "Proses Pendaftaran":

            proses_pendaftaran()

        elif pilihan == "Logout":

            break