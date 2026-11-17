
import json
import os

from ui import pilih_menu, input_teks


# NAMA FILE JSON
FILE_LEADERBOARD = "leaderboard.json"


# MEMBACA DATA LEADERBOARD
def load_data():

    if not os.path.exists(FILE_LEADERBOARD):
        return []

    try:
        with open(FILE_LEADERBOARD, "r") as file:
            data = json.load(file)

        return data

    except (json.JSONDecodeError, OSError):
        print("Gagal membaca data leaderboard!")
        return []


# MENYIMPAN DATA LEADERBOARD
def save_data(data):

    try:
        with open(FILE_LEADERBOARD, "w") as file:
            json.dump(data, file, indent=4)

    except OSError:
        print("Gagal menyimpan data leaderboard!")


# MENAMBAHKAN PEMAIN BARU
def add_leaderboard(player, result):

    data = load_data()

    score = (
        player["kills"] * 100
        + player["boss_kills"] * 500
        + player["gold"]
    )

    pemain = {
        "name": player["name"],
        "kills": player["kills"],
        "boss_kills": player["boss_kills"],
        "gold": player["gold"],
        "score": score,
        "result": result
    }

    data.append(pemain)

    save_data(data)


# MENAMPILKAN LEADERBOARD
def show_leaderboard():

    data = load_data()

    if len(data) == 0:
        print("\nBelum ada data leaderboard!")
        return

    # MENGURUTKAN SKOR TERTINGGI
    data.sort(key=lambda x: x["score"], reverse=True)

    print("\n========== LEADERBOARD ==========")

    for i, player in enumerate(data, start=1):

        print("\nPeringkat:", i)
        print("Nama:", player["name"])
        print("Score:", player["score"])
        print("Kills:", player["kills"])
        print("Boss Kills:", player["boss_kills"])
        print("Gold:", player["gold"])
        print("Result:", player["result"])

    print("\n================================")


# MENCARI PEMAIN
def search_player():

    data = load_data()

    if len(data) == 0:
        print("\nBelum ada data pemain!")
        return

    nama = input_teks("Masukkan nama pemain yang dicari:").lower()

    ditemukan = False

    for player in data:

        if nama in player["name"].lower():

            print("\n=== DATA PEMAIN DITEMUKAN ===")
            print("Nama:", player["name"])
            print("Score:", player["score"])
            print("Kills:", player["kills"])
            print("Boss Kills:", player["boss_kills"])
            print("Gold:", player["gold"])
            print("Result:", player["result"])

            ditemukan = True

    if ditemukan == False:
        print("\nPemain tidak ditemukan!")


# MENGUBAH NAMA PEMAIN
def update_player():

    data = load_data()

    if len(data) == 0:
        print("\nBelum ada data pemain!")
        return

    nama = input_teks("Masukkan nama pemain yang ingin diubah:").lower()

    daftar_pemain = []

    for i, player in enumerate(data):

        if nama in player["name"].lower():
            daftar_pemain.append(i)

    if len(daftar_pemain) == 0:
        print("\nPemain tidak ditemukan!")
        return

    pilihan = []

    for i in daftar_pemain:
        pilihan.append(data[i]["name"] + " | Score: " + str(data[i]["score"]))

    pemain_pilihan = pilih_menu(
        "Pilih pemain yang ingin diubah:",
        pilihan + ["Kembali"]
    )

    if pemain_pilihan == "Kembali":
        return

    indeks = daftar_pemain[pilihan.index(pemain_pilihan)]

    nama_baru = input_teks("Masukkan nama baru:")

    if nama_baru == "":
        print("Nama tidak boleh kosong!")
        return

    data[indeks]["name"] = nama_baru.title()

    save_data(data)

    print("\nNama pemain berhasil diubah!")


# MENGHAPUS DATA PEMAIN
def delete_player():

    data = load_data()

    if len(data) == 0:
        print("\nBelum ada data pemain!")
        return

    nama = input_teks("Masukkan nama pemain yang ingin dihapus:").lower()

    daftar_pemain = []

    for i, player in enumerate(data):

        if nama in player["name"].lower():
            daftar_pemain.append(i)

    if len(daftar_pemain) == 0:
        print("\nPemain tidak ditemukan!")
        return

    pilihan = []

    for i in daftar_pemain:
        pilihan.append(data[i]["name"] + " | Score: " + str(data[i]["score"]))

    pemain_pilihan = pilih_menu(
        "Pilih data pemain yang ingin dihapus:",
        pilihan + ["Kembali"]
    )

    if pemain_pilihan == "Kembali":
        return

    indeks = daftar_pemain[pilihan.index(pemain_pilihan)]

    konfirmasi = pilih_menu(
        "Apakah kamu yakin ingin menghapus data ini?",
        ["Ya", "Tidak"]
    )

    if konfirmasi == "Ya":

        data.pop(indeks)

        save_data(data)

        print("\nData pemain berhasil dihapus!")

    else:
        print("\nPenghapusan dibatalkan!")


# MENU LEADERBOARD
def leaderboard_menu():

    while True:

        print("\n========== LEADERBOARD MENU ==========")

        choice = pilih_menu(
            "Pilih menu leaderboard:",
            [
                "Lihat Leaderboard",
                "Cari Pemain",
                "Ubah Nama Pemain",
                "Hapus Data Pemain",
                "Kembali"
            ]
        )

        if choice == "Lihat Leaderboard":

            show_leaderboard()

        elif choice == "Cari Pemain":

            search_player()

        elif choice == "Ubah Nama Pemain":

            update_player()

        elif choice == "Hapus Data Pemain":

            delete_player()

        elif choice == "Kembali":

            break
