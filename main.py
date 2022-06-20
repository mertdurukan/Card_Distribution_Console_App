import random

# Config
display_Preference = 0
cardof_Number = 8

# Program Values
while_Condition = 1
sayac = 0

class Person:
    def __init__(self, name, card_Deck=[[], []]):
        self.Name = name
        self.card_Deck = card_Deck


def Push_Console(player, display_Preference):
    if display_Preference == 0:
        print("\n" + player.Name)
        print(player.card_Deck)
    elif display_Preference == 1:
        print("\n" + player.Name)
        for j in range(7):
            print(player.card_Deck[0][j] + " " + player.card_Deck[1][j])


def Dolu_Kart_Donder(rand_Deste):
    sonuc = []
    match rand_Deste:
        case 0:
            if len(Maca[1]) > 0:
                sonuc.append(Maca[0][0])
                sonuc.append(Maca[1][rand_Deste])
                return sonuc
            else:
                return Dolu_Kart_Donder(random.randint(0, 3))
        case 1:
            if len(Sinek[1]) > 0:
                sonuc.append(Sinek[0][0])
                sonuc.append(Sinek[1][rand_Deste])
                return sonuc
            else:
                return Dolu_Kart_Donder(random.randint(0, 3))
        case 2:
            if len(Kupa[1]) > 0:
                sonuc.append(Kupa[0][0])
                sonuc.append(Kupa[1][rand_Deste])
                return sonuc
            else:
                return Dolu_Kart_Donder(random.randint(0, 3))
        case 3:
            if len(Karo[1]) > 0:
                sonuc.append(Karo[0][0])
                sonuc.append(Karo[1][rand_Deste])
                return sonuc
            else:
                return Dolu_Kart_Donder(random.randint(0, 3))


def Take_Random_Card(player, cardof_Number):
    for i in range(cardof_Number):
        donen_Kart = Dolu_Kart_Donder(random.randint(0, 3))

        match player.Name:
            case "uzay":
                player.card_Deck[0].append(donen_Kart[0])
                player.card_Deck[1].append(donen_Kart[1])
            case "doga":
                player.card_Deck[0].append(donen_Kart[0])
                player.card_Deck[1].append(donen_Kart[1])
            case "evrim":
                player.card_Deck[0].append(donen_Kart[0])
                player.card_Deck[1].append(donen_Kart[1])
            case "damla":
                player.card_Deck[0].append(donen_Kart[0])
                player.card_Deck[1].append(donen_Kart[1])


def Changing_Player_Card(player, kac_Kart=4):
    for i in range(kac_Kart):
        donen_Kart = Dolu_Kart_Donder(random.randint(0, 3))
        match player.Name:
            case "uzay":
                Degisecek_Kart_Indisi = random.randint(0, len(uzay.card_Deck[1]) - 1)
                uzay.card_Deck[0][Degisecek_Kart_Indisi] = donen_Kart[0]
                uzay.card_Deck[1][Degisecek_Kart_Indisi] = donen_Kart[1]
            case "doga":
                Degisecek_Kart_Indisi = random.randint(0, len(doga.card_Deck[1]) - 1)
                doga.card_Deck[0][Degisecek_Kart_Indisi] = donen_Kart[0]
                doga.card_Deck[1][Degisecek_Kart_Indisi] = donen_Kart[1]
            case "evrim":
                Degisecek_Kart_Indisi = random.randint(0, len(evrim.card_Deck[1]) - 1)
                evrim.card_Deck[0][Degisecek_Kart_Indisi] = donen_Kart[0]
                evrim.card_Deck[1][Degisecek_Kart_Indisi] = donen_Kart[1]
            case "damla":
                Degisecek_Kart_Indisi = random.randint(0, len(damla.card_Deck[1]) - 1)
                damla.card_Deck[0][Degisecek_Kart_Indisi] = donen_Kart[0]
                damla.card_Deck[1][Degisecek_Kart_Indisi] = donen_Kart[1]


while (while_Condition):
    sayac += 1
    # Kisiler
    uzay = Person("uzay", [[], []])
    doga = Person("doga", [[], []])
    evrim = Person("evrim", [[], []])
    damla = Person("damla", [[], []])

    # Kartlar
    Maca = [["Maca"], ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]]
    Sinek = [["Sinek"], ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]]
    Kupa = [["Kupa"], ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]]
    Karo = [["Karo"], ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]]

    print("****************************************************************************************************************************************************")
    print("Calıştırılma Sayısı:" + str(sayac))
    Take_Random_Card(uzay, cardof_Number)
    Push_Console(uzay, display_Preference)

    Take_Random_Card(doga, cardof_Number)
    Push_Console(doga, display_Preference)

    Take_Random_Card(evrim, cardof_Number)
    Push_Console(evrim, display_Preference)

    Take_Random_Card(damla, cardof_Number)
    Push_Console(damla, display_Preference)
    print("****************************************************************************************************************************************************")

    input_Islem = input("\nKart dağıtım işlemi tamamlandı, tuşlama yapınız."
                        "\n1: Uzay'ın 4 kartını değiştir"
                        "\n2: Doğa'nın 4 kartını değiştir"
                        "\n3: Evrim'in 4 kartını değiştir"
                        "\n4: Damla'nın 4 kartını değiştir"
                        "\n5: Mevcut kartlar güzel programı bitir. "
                        "\n")
    match input_Islem:
        case "1":
            Changing_Player_Card(uzay, 4)
            Push_Console(uzay, display_Preference)
        case "2":
            Changing_Player_Card(doga, 4)
            Push_Console(doga, display_Preference)
        case "3":
            Changing_Player_Card(evrim, 4)
            Push_Console(evrim, display_Preference)
        case "4":
            Changing_Player_Card(damla, 4)
            Push_Console(damla, display_Preference)
        case "5":
            while_Condition = 0
