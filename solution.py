"""Importáljuk a sys modult, hogy elérjük az indító paramétereket"""
import sys
#Szám lista
correct_chars = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

def char_check(int1:str, int2:str):
    """Számvizsgálat"""
    res = []
    i = 0
    while i < len(int1):
        if int1[i] in correct_chars:
            res.append(1)
            i = i + 1
        else:
            res.append(0)
            i = i + 1
    i = 0
    while i < len(int2):
        if int2[i] in correct_chars:
            res.append(1)
            i = i + 1
        else:
            res.append(0)
            i = i + 1
    if 0 in res:
        return False
    return True

def summa(int1:str, int2:str) -> str:
    """Összeadás"""
    res_num = int(int1) + int(int2)
    return str(res_num)

def extract(int1:str, int2:str) -> str:
    """Kivonás"""
    res_num = int(int1) - int(int2)
    return str(res_num)

def compare(int1:str, int2:str) -> str:
    """Összehasonlítás"""
    res_num = None
    if int(int1) < int(int2):
        res_num = 1
    elif int(int1) > int(int2):
        res_num = -1
    elif int(int1) == int(int2):
        res_num = 0
    return str(res_num)

def multiple(int1:str, int2:str) -> str:
    """Szorzás"""
    res_num = int(int1) * int(int2)
    return str(res_num)

def multiple_another_way(int1:str, int2:str) -> str:
    """Másik szorzás"""
    i = 0
    res_num = 0
    while i < int(int2):
        res_num = res_num + int(int1)
        i = i + 1
    return str(res_num)

def string_split(command:str, string:str):
    """Egyben kapott számok bontása"""
    int1 = 0
    int2 = 0
    ints = string.split()
    if len(ints) > 2:
        print("Túl sok érték!")
    elif len(ints) == 2:
        int1 = ints[0]
        int2 = ints[1]
        if char_check(int1, int2) is True:
            if command == "Összeadás":
                print(summa(int1, int2))
            elif command == "Kivonás":
                print(extract(int1, int2))
            elif command == "Szorzás":
                print(multiple(int1, int2))
            elif command == "Szorzás2":
                print(multiple_another_way(int1, int2))
            elif command == "Összehasonlítás":
                print(compare(int1, int2))
            else:
                print("Nem létező funkció.")
        else:
            print("A számokban nem megfelelő karaktert észleltünk.")
    else:
        print("Túl kevés érték.")


def inter_start():
    """Interaktív menü"""
    print("Hello! Funkciók: Összeadás, Kivonás, Szorzás, Szorzás2, Összehasonlítás")
    int1 = input("Első szám: ")
    int2 = input("Második szám: ")
    func = input("Kívánt funkció: ")
    if char_check(int1, int2) is True:
        if func == "Összeadás":
            print(summa(int1, int2))
        elif func == "Kivonás":
            print(extract(int1, int2))
        elif func == "Szorzás":
            print(multiple(int1, int2))
        elif func == "Szorzás2":
            print(multiple_another_way(int1, int2))
        elif func == "Összehasonlítás":
            print(compare(int1, int2))
        else:
            print("Nem létező funkció.")
    else:
        print("A számokban nem megfelelő karaktert észleltünk.")

def main_start(command, int1, int2):
    """Command"""
    if char_check(int1, int2) is True:
        if command == "Összeadás":
            print(summa(int1, int2))
        elif command == "Kivonás":
            print(extract(int1, int2))
        elif command == "Szorzás":
            print(multiple(int1, int2))
        elif command == "Szorzás2":
            print(multiple_another_way(int1, int2))
        elif command == "Összehasonlítás":
            print(compare(int1, int2))
        else:
            print("Nem létező funkció.")
    else:
        print("A számokban nem megfelelő karaktert észleltünk.")

#Start
if __name__ == "__main__":
    if sys.argv[1] == "inter":
        inter_start()
    elif sys.argv[1] == "command":
        if len(sys.argv) < 5 and len(sys.argv) > 3:
            string_split(sys.argv[2],sys.argv[3])
        elif len(sys.argv) > 5:
            print("Túl sok változó lett megadva")
        elif len(sys.argv) == 5:
            main_start(sys.argv[2], sys.argv[3], sys.argv[4])
        else:
            print("A paraméterek nem stimmelnek.")
    else:
        print("Az utasítás nem található, használható: inter, command")
