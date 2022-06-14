try:
    with open("fleet.txt", "x") as file:
        file.write("Ships       \t\tLatitude      \t\tLongitude       \tTime\n")

except FileExistsError:
    with open("fleet.txt", "r+") as file:
        lines = file.readlines()

        opc = 0
        while opc != 2:
            print("[1] - Add ship's information \n[2] - Print Information and Exit")
            opc = int(input("Options: "))

            if opc == 1:
                ship = str(input("Ship's name: ")).capitalize()
                latitude = int(input("Latitude: "))
                longitude = input("Longitude like-> [E 10 L]: ")
                hour = int(input("Hour: "))
                minute = int(input("Minute: "))
                file.write(f'{ship:<20}')
                file.write(f'{latitude:<20}')
                file.write(f'{longitude:<20}')
                file.write(f'{hour}:{minute}')
                file.write('\n')

            elif opc == 2:
                with open("fleet.txt", "r") as file:
                    print(file.read())
                break
            else:
                print("\033[31mInvalid option... Try again!\033[m")

