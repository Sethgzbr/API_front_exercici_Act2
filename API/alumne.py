def estudiant_schema(fetchAlumnes) -> dict:
     return {"NomAlumne": fetchAlumnes[0],
            "Curs": fetchAlumnes[1],
            "Cicle": fetchAlumnes[2],
            "Grup": fetchAlumnes[3],
            "DescAula": fetchAlumnes[4]
            }


def alumne_schema(alumne) -> dict:
    return [estudiant_schema(estudiant) for estudiant in alumne] 