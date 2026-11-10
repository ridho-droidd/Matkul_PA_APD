from data import petualang, resepsionis, admin
from InquirerPy import inquirer


def register():

    print("\n=== REGISTER PETUALANG ===")

    username = inquirer.text(
        message="Masukkan nama petualang:"
    ).execute()

    if username in petualang or username in resepsionis or username in admin:
        print("Nama sudah digunakan")

    else:
        password = inquirer.secret(
            message="Masukkan password:"
        ).execute()

        petualang[username] = {
            "password": password,
            "role": "Petualang",
            "rank": "C",
            "gold": 100,
            "status": "Menunggu",
            "quest": []
        }

        print("Registrasi berhasil")
        print("Silakan menunggu persetujuan resepsionis.")


def login():

    print("\n=== LOGIN GUILD ===")

    username = inquirer.text(
        message="Masukkan username:"
    ).execute()

    password = inquirer.secret(
        message="Masukkan password:"
    ).execute()

    if username in petualang:

        if petualang[username]["password"] == password:

            if petualang[username]["status"] == "Diterima":
                return username, "Petualang"

            elif petualang[username]["status"] == "Menunggu":
                print("Akun masih menunggu persetujuan")

            else:
                print("Pendaftaran petualang ditolak")

        else:
            print("Password salah")

    elif username in resepsionis:

        if resepsionis[username]["password"] == password:
            return username, "Resepsionis"

        else:
            print("Password salah")

    elif username in admin:

        if admin[username]["password"] == password:
            return username, "Admin"

        else:
            print("Password salah")

    else:
        print("Username tidak ditemukan")

    return None, None


def logout():

    print("\nBerhasil logout")