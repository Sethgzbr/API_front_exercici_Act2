def estudiant_schema(student) -> dict:
    return {"IdAlumne": student[0],
            "IdAula": student[1],
            "nomAlumne": student[2],
            "cicle": student[3],
            "curs": student[4],
            "grup": student[5],
            "createdAt": student[6],
            "updatedAt": student[7]
            }

def alumne_schema(alumne) -> dict:
    return [estudiant_schema(estudiant) for estudiant in alumne] 