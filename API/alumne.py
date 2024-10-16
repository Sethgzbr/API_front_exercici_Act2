def estudiant_schema(student) -> dict:
     return {"NomAlumne": fetchAlumnes[0],
            "Cicle": fetchAlumnes[1],
            "Curs": fetchAlumnes[2],
            "Grup": fetchAlumnes[3],
            "DescAula": fetchAlumnes[4]
            }


def alumne_schema(alumne) -> dict:
    return [estudiant_schema(estudiant) for estudiant in alumne] 