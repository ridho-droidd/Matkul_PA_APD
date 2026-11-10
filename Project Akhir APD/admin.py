from data import petualang
from prettytable import PrettyTable
from InquirerPy import inquirer


# READ DATA
def lihat_data():

    tabel = PrettyTable()

    tabel.field_names = [
        "Nama", "Rank", "Gold", "Status"
    ]

    for nama, data in petualang.items():

        tabel.add_row([
            nama,
            data["rank"],
            data["gold"],
            data["status"]
        ])

    print(tabel)


# CREATE DATA
def tambah_petualang():

    nama = inquirer.text(
        message="Nama petualang baru:"
    ).execute()

    if nama in petualang:
        print("Nama sudah tersedia!")

    else:

        password = inquirer.secret(
            message="Password:"
        ).execute()

        petualang[nama] = {
            "password": password,
            "role": "Petualang",
            "rank": "C",
            "gold": 100,
            "status": "Diterima",
            "quest": []
        }

        print("Data petualang berhasil ditambahkan!")


# DELETE DATA
def hapus_petualang():

    if len(petualang) == 0:
        print("Tidak ada data!")
        return

    nama = inquirer.select(
        message="Pilih petualang yang ingin dihapus:",
        choices=list(petualang.keys())
    ).execute()

    konfirmasi = inquirer.confirm(
        message=f"Yakin menghapus {nama}?"
    ).execute()

    if konfirmasi:

        del petualang[nama]

        print("Data berhasil dihapus!")

    else:
        print("Penghapusan dibatalkan!")


# UPDATE DATA / MENAMBAHKAN QUEST
def tambah_quest():

    if len(petualang) == 0:
        print("Tidak ada petualang!")
        return

    nama = inquirer.select(
        message="Pilih petualang:",
        choices=list(petualang.keys())
    ).execute()

    nama_quest = inquirer.text(
        message="Masukkan nama quest:"
    ).execute()

    reward = inquirer.number(
        message="Masukkan reward gold:",
        min_allowed=1
    ).execute()

    petualang[nama]["quest"].append({
        "nama": nama_quest,
        "reward": int(reward),
        "status": "Belum selesai"
    })

    print("Quest berhasil ditambahkan!")


# MENU ADMIN
def menu_admin():

    while True:

        pilihan = inquirer.select(
            message="=== MENU ADMIN ===",
            choices=[
                "Lihat Data Petualang",
                "Tambah Petualang",
                "Hapus Petualang",
                "Tambah Quest",
                "Logout"
            ]
        ).execute()

        if pilihan == "Lihat Data Petualang":

            lihat_data()

        elif pilihan == "Tambah Petualang":

            tambah_petualang()

        elif pilihan == "Hapus Petualang":

            hapus_petualang()

        elif pilihan == "Tambah Quest":

            tambah_quest()

        elif pilihan == "Logout":

            break