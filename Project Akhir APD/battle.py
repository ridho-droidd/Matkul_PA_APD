
from data import skills, weapons
from inventori import show_inventory, use_potion, add_item
from player import show_status
from ui import pilih_menu


def battle(player, enemy, is_boss=False):

    enemy_hp = enemy["hp"]

    print("\n================================")
    print("         BATTLE START.")
    print("================================")

    print(enemy["name"], "muncul.")

    while enemy_hp > 0 and player["hp"] > 0:

        print("\n--------------------------------")
        print(player["name"], "HP:", player["hp"])
        print(player["name"], "SP:", player["sp"])
        print(enemy["name"], "HP:", enemy_hp)
        print("--------------------------------")

        choice = pilih_menu(
            "Pilih tindakan:",
            [
                "Attack",
                "Skill",
                "Open Inventory",
                "Give Up"
            ]
        )

        # ATTACK
        if choice == "Attack":

            weapon_name = player["weapon"]

            if weapon_name not in weapons:
                print("Weapon tidak ditemukan.")
                continue

            damage = 20 + weapons[weapon_name]["damage"]

            enemy_hp -= damage

            print("\nKamu menyerang", enemy["name"])
            print("Damage:", damage)

        # SKILL
        elif choice == "Skill":

            skill_names = list(skills.keys())

            skill_choice = pilih_menu(
                "Pilih skill:",
                skill_names + ["Kembali"]
            )

            if skill_choice == "Kembali":
                continue

            skill = skills[skill_choice]

            if player["sp"] < skill["cost"]:

                print("SP kamu tidak cukup.")
                continue

            player["sp"] -= skill["cost"]

            enemy_hp -= skill["damage"]

            print("\nKamu menggunakan", skill_choice)
            print("Damage:", skill["damage"])

        # INVENTORY
        elif choice == "Open Inventory":

            use_potion(player)

        # GIVE UP
        elif choice == "Give Up":

            print("\nYou can't escape brochacho.")

        # CEK MUSUH KALAH
        if enemy_hp <= 0:

            print("\n", enemy["name"], "BERHASIL DIKALAHKAN!")

            player["kills"] += 1

            if is_boss:
                player["boss_kills"] += 1

            player["defeated"].add(enemy["name"])

            player["gold"] += enemy["gold"]

            print("Gold diperoleh:", enemy["gold"])

            add_item(player, "Health Potion", 1)

            print("Reward: 1 Health Potion")

            return True

        # MUSUH MENYERANG
        print("\n", enemy["name"], "menyerang.")

        player["hp"] -= enemy["damage"]

        if player["hp"] < 0:
            player["hp"] = 0

        print("Kamu menerima damage:", enemy["damage"])

        if player["hp"] <= 0:

            print("\nGAME OVER!")

            return False

    return False


def preparation(player):

    while True:

        print("\n================================")
        print("       PREPARATION WINDOW")
        print("================================")

        choice = pilih_menu(
            "Apa yang ingin kamu lakukan?",
            [
                "Lanjut",
                "Cek Inventory",
                "Cek Status",
                "Give Up"
            ]
        )

        if choice == "Lanjut":

            player["hp"] += 20
            player["sp"] += 15

            if player["hp"] > player["max_hp"]:
                player["hp"] = player["max_hp"]

            if player["sp"] > player["max_sp"]:
                player["sp"] = player["max_sp"]

            print("\nHP dan SP berhasil dipulihkan.")

            return True

        elif choice == "Cek Inventory":

            inventory_choice = pilih_menu(
                "Pilih tindakan inventory:",
                [
                    "Gunakan Potion",
                    "Ganti Weapon",
                    "Kembali"
                ]
            )

            if inventory_choice == "Gunakan Potion":

                use_potion(player)

            elif inventory_choice == "Ganti Weapon":

                weapon_names = player["weapons"]

                if len(weapon_names) == 0:

                    print("Kamu belum memiliki weapon")

                    continue

                weapon_choice = pilih_menu(
                    "Pilih weapon:",
                    weapon_names + ["Kembali"]
                )

                if weapon_choice != "Kembali":

                    if weapon_choice in weapons:

                        player["weapon"] = weapon_choice

                        print("Weapon berhasil digunakan.")

                    else:

                        print("Weapon tidak terdaftar.")

            elif inventory_choice == "Kembali":

                continue

        elif choice == "Cek Status":

            show_status(player)

        elif choice == "Give Up":

            print("\nPetualangan telah diakhiri.")

            return False
