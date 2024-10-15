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

def student_schema(studentAll) -> dict:
    return {"IdAlumne": studentAll[0],
            "IdAula": studentAll[1],
            "nomAlumne": studentAll[2],
            "cicle": studentAll[3],
            "curs": studentAll[4],
            "grup": studentAll[5],
            "createdAt": studentAll[6],
            "updatedAt": studentAll[7],
            "DescAula": studentAll[8],
            "edifici": studentAll[9],
            "pis": studentAll[10]
            }

def all_schema(alumne) -> dict:
    return [student_schema(student) for student in alumne] 
