
from data import enemies, boss
from player import create_player
from battle import battle, preparation
from leaderboard import leaderboard_menu, add_leaderboard
from ui import pilih_menu


# MEMULAI PETUALANGAN
def start_adventure():

    player = create_player()

    result = "Defeat"

    print("\n================================")
    print("       ADVENTURE BEGINS.")
    print("================================")

    # MELAWAN MUSUH BIASA
    for enemy in enemies:

        won = battle(player, enemy)

        # JIKA PEMAIN KALAH
        if not won:

            result = "Defeat"
            break

        # MENU PERSIAPAN
        lanjut = preparation(player)

        # JIKA PEMAIN MENYERAH
        if not lanjut:

            result = "Abandoned"
            break

    # JIKA SEMUA MUSUH BIASA BERHASIL DIKALAHKAN
    else:

        print("\nSemua musuh berhasil dikalahkan.")
        print("Bersiaplah menghadapi FINAL BOSS.")

        won = battle(player, boss, True)

        if won:

            result = "Victory"

            print("\n================================")
            print("       YOU ARE A LEGEND.")
            print("================================")

        else:

            result = "Defeat"

    # MENYIMPAN HASIL PETUALANGAN
    add_leaderboard(player, result)

    # LAPORAN PETUALANGAN
    print("\n========== ADVENTURE REPORT ==========")

    print("Nama       :", player["name"])
    print("Hasil      :", result)
    print("Musuh kalah:", player["kills"])
    print("Boss kalah :", player["boss_kills"])
    print("Gold       :", player["gold"])

    print("======================================")


# MENU UTAMA
def main():

    print("\n========================================")
    print("      LEGENDS OF THE LOST KINGDOM")
    print("========================================")

    while True:

        print("\nSelamat datang, petualang.")
        print("Dunia menantikan kisah kepahlawananmu.")

        choice = pilih_menu(
            "Pilih menu utama:",
            [
                "Mulai Petualangan Baru",
                "Lihat Leaderboard",
                "Keluar"
            ]
        )

        if choice == "Mulai Petualangan Baru":

            start_adventure()

        elif choice == "Lihat Leaderboard":

            leaderboard_menu()

        elif choice == "Keluar":

            print("\nTerima kasih telah bermain.")
            print("Sampai jumpa, petualang.")

            break


# MENJALANKAN PROGRAM
if __name__ == "__main__":

    main()
