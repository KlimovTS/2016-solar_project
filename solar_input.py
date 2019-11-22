# coding: utf-8
# license: GPLv3

from solar_objects import Star, Planet


def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов

    Параметры:

    **input_filename** — имя входного файла
    """

    objects = []
    with open(input_filename) as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
            object_type = line.split()[0].lower()
            if object_type == "star":  # FIXME: do the same for planet
                star = Star()
                parse_star_parameters(line, star)
                objects.append(star)
            elif object_type == "planet":  # FIXME: do the same for planet
                planet = Planet()
                parse_planet_parameters(line, planet)
                objects.append(planet)
            else:
                print("Unknown space object")

    return objects


def parse_star_parameters(line, star):
    """Считывает данные о звезде из строки.
    Входная строка должна иметь слеюущий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты зведы, (Vx, Vy) — скорость.
    Пример строки:
    Star 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание звезды.
    **star** — объект звезды.
    """
    str = line
    proc = ''
    star.R = ''
    star.color = ''
    star.m = ''
    star.x = ''
    star.y = ''
    star.vx = ''
    star.vy = ''
    i=0
    while str[i] != ' ':
        proc = proc + str[i]
        i += 1
    i += 1
    while str[i] != ' ':
        star.R = star.R + str[i]
        i += 1
    i += 1
    while str[i] != ' ':
        star.color = star.color + str[i]
        i += 1
    i += 1
    while str[i] != ' ':
        star.m = star.m + str[i]
        i += 1
    i += 1
    while str[i] != ' ':
        star.x = star.x + str[i]
        i += 1
    i += 1
    while str[i] != ' ':
        star.y = star.y + str[i]
        i += 1
    i += 1
    while str[i] != ' ':
        star.vx = star.vx + str[i]
        i += 1
    i += 1
    while str[i] != ' ' and i < len(str)-1:
        star.vy = star.vy + str[i]
        i += 1
    star.vy = star.vy +str[len(str)-1]
    star.R = float(star.R)
    star.m = float(star.m)
    star.x = float(star.x)
    star.y = float(star.y)
    star.vx = float(star.vx)
    star.vy = float(star.vy)
    
    
    

    

def parse_planet_parameters(line, planet):
    """Считывает данные о планете из строки.
    Предполагается такая строка:
    Входная строка должна иметь слеюущий формат:
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты планеты, (Vx, Vy) — скорость.
    Пример строки:
    Planet 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание планеты.
    **planet** — объект планеты.
    """
    str = line
    proc = ''
    planet.R = ''
    planet.color = ''
    planet.m = ''
    planet.x = ''
    planet.y = ''
    planet.vx = ''
    planet.vy = ''
    i=0
    while str[i] != ' ':
        proc = proc + str[i]
        i += 1
    i += 1
    while str[i] != ' ':
        planet.R = planet.R + str[i]
        i += 1
    i += 1
    while str[i] != ' ':
        planet.color = planet.color + str[i]
        i += 1
    i += 1
    while str[i] != ' ':
        planet.m = planet.m + str[i]
        i += 1
    i += 1
    while str[i] != ' ':
        planet.x = planet.x + str[i]
        i += 1
    i += 1
    while str[i] != ' ':
        planet.y = planet.y + str[i]
        i += 1
    i += 1
    while str[i] != ' ':
        planet.vx = planet.vx + str[i]
        i += 1
    i += 1
    while str[i] != ' ' and i < len(str)-1:
        planet.vy = planet.vy + str[i]
        i += 1   
    planet.vy = planet.vy +str[len(str)-1]
    planet.R = float(planet.R)
    planet.m = float(planet.m)
    planet.x = float(planet.x)
    planet.y = float(planet.y)
    planet.vx = float(planet.vx)
    planet.vy = float(planet.vy)


def write_space_objects_data_to_file(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.
    Строки должны иметь следующий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Параметры:

    **output_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
    """
    with open(output_filename, 'w') as out_file:
        for obj in space_objects:
            txt = obj.type + " " + str(obj.R) + " " + obj.color + " " + str(obj.m) + " " + str(obj.x) + " " + str(obj.y) + " " + str(obj.vx) + " " + str(obj.vy) 
            print(out_file, txt)
            
            # FIXME: should store real values

# FIXME: хорошо бы ещё сделать функцию, сохранающую статистику в заданный файл...

if __name__ == "__main__":
    print("This module is not for direct call!")
