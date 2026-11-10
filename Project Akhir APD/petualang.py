from data import petualang
from prettytable import PrettyTable
from InquirerPy import inquirer


def lihat_profil(username):

    data = petualang[username]

    tabel = PrettyTable()

    tabel.field_names = [
        "Nama", "Rank", "Gold", "Status"
    ]

    tabel.add_row([
        username,
        data["rank"],
        data["gold"],
        data["status"]
    ])

    print(tabel)


def lihat_quest(username):

    tabel = PrettyTable()

    tabel.field_names = [
        "No", "Nama Quest", "Reward", "Status"
    ]

    daftar_quest = petualang[username]["quest"]

    for i, quest in enumerate(daftar_quest):
        tabel.add_row([
            i + 1,
            quest["nama"],
            quest["reward"],
            quest["status"]
        ])

    print(tabel)


def selesaikan_quest(username):

    daftar_quest = petualang[username]["quest"]

    belum_selesai = []

    for i, quest in enumerate(daftar_quest):

        if quest["status"] == "Belum selesai":
            belum_selesai.append(i)

    if len(belum_selesai) == 0:
        print("Tidak ada quest yang tersedia!")
        return

    pilihan = inquirer.select(
        message="Pilih quest yang ingin diselesaikan:",
        choices=[
            {
                "name": daftar_quest[i]["nama"],
                "value": i
            }
            for i in belum_selesai
        ]
    ).execute()

    quest = daftar_quest[pilihan]

    # Mengubah status quest
    quest["status"] = "Selesai"

    # Menambahkan gold
    petualang[username]["gold"] += quest["reward"]

    # Sistem kenaikan rank
    urutan_rank = ["C", "B", "A", "S"]

    rank_sekarang = petualang[username]["rank"]

    indeks = urutan_rank.index(rank_sekarang)

    if indeks < 3:
        petualang[username]["rank"] = urutan_rank[indeks + 1]

    print("\nQuest berhasil diselesaikan!")
    print("Gold bertambah:", quest["reward"])
    print("Rank sekarang:", petualang[username]["rank"])


def menu_petualang(username):

    while True:

        pilihan = inquirer.select(
            message="=== MENU PETUALANG ===",
            choices=[
                "Lihat Profil",
                "Lihat Quest",
                "Selesaikan Quest",
                "Logout"
            ]
        ).execute()

        if pilihan == "Lihat Profil":
            lihat_profil(username)

        elif pilihan == "Lihat Quest":
            lihat_quest(username)

        elif pilihan == "Selesaikan Quest":
            selesaikan_quest(username)

        elif pilihan == "Logout":
            break