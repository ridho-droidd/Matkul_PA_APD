
from auth import register, login, logout
from petualang import menu_petualang
from resepsionis import menu_resepsionis
from admin import menu_admin

from prettytable import PrettyTable
from InquirerPy import inquirer

def menu_awal():

    while True:

        pilihan = inquirer.select(
            message="=== GUILD PETUALANG ===",
            choices=[
                "Register",
                "Login",
                "Keluar"
            ]
        ).execute()

        if pilihan == "Register":

            register()

        elif pilihan == "Login":

            username, role = login()

            if role == "Petualang":

                menu_petualang(username)
                logout()

            elif role == "Resepsionis":

                menu_resepsionis()
                logout()

            elif role == "Admin":

                menu_admin()
                logout()

        elif pilihan == "Keluar":

            print("Terima kasih")
            break


menu_awal()