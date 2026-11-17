
from data import levels


# MEMBUAT DATA PEMAIN
def create_player():

    print("\n================================")
    print("       CREATE YOUR HERO")
    print("================================")

    while True:

        name = input("Masukkan nama petualang: ").strip()

        # STRING METHOD
        name = name.title()

        if name == "":
            print("Nama tidak boleh kosong!")

        elif len(name) < 3:
            print("Nama minimal 3 karakter!")

        else:
            break

    player = {
        "name": name,

        # HP DAN SP
        "hp": 200,
        "max_hp": 200,
        "sp": 100,
        "max_sp": 100,

        # RESOURCE
        "gold": 100,

        # STATISTIK
        "kills": 0,
        "boss_kills": 0,

        # WEAPON
        "weapon": "Wooden Sword",
        "weapons": ["Wooden Sword"],

        # INVENTORY
        "inventory": [
            {"name": "Health Potion", "qty": 3},
            {"name": "Mana Potion", "qty": 2}
        ],

        # MUSUH YANG SUDAH DIKALAHKAN
        "defeated": set()
    }

    print("\nSelamat datang, {}!".format(name))
    print("Petualanganmu akan segera dimulai!")

    return player


# MENAMPILKAN STATUS PEMAIN
def show_status(player):

    print("\n========== PLAYER STATUS ==========")

    print("Nama       :", player["name"])
    print("Level      :", check_level(player))

    print("HP         :", player["hp"], "/", player["max_hp"])
    print("SP         :", player["sp"], "/", player["max_sp"])

    print("Gold       :", player["gold"])
    print("Weapon     :", player["weapon"])

    print("Musuh kalah:", player["kills"])
    print("Boss kalah :", player["boss_kills"])

    print("===================================")


# MEMERIKSA LEVEL PEMAIN
def check_level(player):

    kills = player["kills"]

    if kills >= 10:
        return levels[3]

    elif kills >= 6:
        return levels[2]

    elif kills >= 3:
        return levels[1]

    else:
        return levels[0]
