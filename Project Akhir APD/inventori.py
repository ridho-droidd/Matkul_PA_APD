
from data import weapons, potions
from ui import pilih_menu


def show_inventory(player):

    print("\n========== INVENTORY ==========")

    # MENAMPILKAN WEAPON
    print("\nWEAPONS:")

    if len(player["weapons"]) == 0:
        print("Tidak memiliki weapon!")

    else:
        for weapon in player["weapons"]:
            print("-", weapon)

    print("\nEquipped Weapon:", player["weapon"])

    # MENAMPILKAN POTION
    print("\nPOTIONS:")

    if len(player["inventory"]) == 0:
        print("Tidak memiliki potion!")

    else:
        for item in player["inventory"]:
            print(item["name"], "x", item["qty"])

    print("===============================")


def use_potion(player):

    show_inventory(player)

    # MENGAMBIL DAFTAR POTION
    potion_list = []

    for item in player["inventory"]:

        if item["name"] in potions and item["qty"] > 0:

            potion_list.append(item["name"])

    if len(potion_list) == 0:

        print("Kamu tidak memiliki potion!")
        return

    potion_name = pilih_menu(
        "Pilih potion yang ingin digunakan:",
        potion_list + ["Kembali"]
    )

    if potion_name == "Kembali":
        return

    for item in player["inventory"]:

        if item["name"] == potion_name:

            # HEALTH POTION
            if potion_name == "Health Potion" or potion_name == "Greater Health Potion":

                if player["hp"] >= player["max_hp"]:

                    print("HP kamu sudah penuh!")
                    return

                heal = potions[potion_name]["heal"]

                player["hp"] += heal

                if player["hp"] > player["max_hp"]:
                    player["hp"] = player["max_hp"]

                print("HP berhasil dipulihkan!")

            # MANA POTION
            elif potion_name == "Mana Potion":

                if player["sp"] >= player["max_sp"]:

                    print("SP kamu sudah penuh!")
                    return

                restore = potions[potion_name]["restore"]

                player["sp"] += restore

                if player["sp"] > player["max_sp"]:
                    player["sp"] = player["max_sp"]

                print("SP berhasil dipulihkan!")

            # MENGURANGI JUMLAH POTION
            item["qty"] -= 1

            if item["qty"] == 0:
                player["inventory"].remove(item)

            return


# MENAMBAHKAN ITEM
def add_item(player, item_name, amount):

    found = False

    for item in player["inventory"]:

        if item["name"] == item_name:

            item["qty"] += amount

            found = True
            break

    if found == False:

        player["inventory"].append({
            "name": item_name,
            "qty": amount
        })
