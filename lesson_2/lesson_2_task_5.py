def month_to_season(nomber):
    if (nomber in (1, 2, 12)):
        print("Зима")
    elif (nomber in (3, 4, 5)):
        print("Весна")
    elif (nomber in (6, 7, 8)):
        print("Лето")
    else:
        print("Осень")


month_to_season(1)
