from client import db_client

def read():
    try:
        conn = db_client()
        cur = conn.cursor()
        cur.execute("SELECT a.NomAlumne, a.Curs, a.Cicle, a.Grup, aula.DescAula FROM alumne a JOIN aula ON a.IdAula = aula.IdAula;")
    
        students = cur.fetchall()
    
    except Exception as e:
        print("ERROR", se)
        return {"status": -1, "message": f"Error de connexió:{e}" }
    
    finally:
        conn.close()
    
    return students

def read_id(IdAlumne):
    try:
        conn = db_client()
        cur = conn.cursor()
        query = "select * from alumne where IdAlumne = %s;"
        values=(IdAlumne,)
        cur.execute(query,values)

        students = cur.fetchone()
    
    except Exception as e:
        print("ERROR", e)
        return {"status": -1, "message": f"Error de connexió:{e}" }
    
    finally:
        conn.close()
    print(students)
    return students

def create(IdAula,nomAlumne,cicle,curs,grup):
    try:
        conn = db_client()
        cur = conn.cursor()
        query = "insert into alumne (IdAula,nomAlumne,cicle,curs,grup) VALUES (%s,%s,%s,%s,%s);"
        values=(IdAula,nomAlumne,cicle,curs,grup)
        cur.execute(query,values)
    
        conn.commit()
        student_id = cur.lastrowid
    
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}" }
    
    finally:
        conn.close()

    return student_id

def aula_existeix(IdAula):
    conn = db_client()
    cur = conn.cursor()
    query = "SELECT Idaula FROM aula WHERE IdAula = %s"
    cur.execute(query, (IdAula,))
    if cur.fetchone() is None:
        return False
    else:
        return True

def update(IdAula,nomAlumne,cicle,curs,grup):
    try:
        conn = db_client()
        cur = conn.cursor()
        query = "UPDATE AlUMNE SET IdAula = %s, NomAlumne = %s, Cicle = %s, Curs = %s, Grup = %s WHERE NomAlumne = %s;"
        values=(IdAula,nomAlumne,cicle,curs,grup,nomAlumne)
        cur.execute(query,values)
        updated_recs = cur.rowcount
    
        conn.commit()
    
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}" }
    
    finally:
        conn.close()

    return updated_recs

def delete(IdAlumne):
    try:
        conn = db_client()
        cur = conn.cursor()
        query = "DELETE FROM ALUMNE  WHERE IdAlumne = %s;"
        values=(IdAlumne,)
        cur.execute(query,values)
    
        conn.commit()
        student_id = cur.lastrowid
    
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}" }
    
    finally:
        conn.close()

    return student_id

def read_all_with_details():
    try:
        conn = db_client()
        cur = conn.cursor()
        query = """
        SELECT a.NomAlumne, a.Curs, a.Cicle, a.Grup, aula.DescAula
        FROM alumne a
        JOIN aula ON a.IdAula = aula.IdAula;
        """ 
        cur.execute(query)
        result = cur.fetchall()

        alumne_list = []
        for row in result:
            alumne_list.append({
                "IdAlumne": row[0],
                "IdAula": row[1],
                "NomAlumne": row[2],
                "Cicle": row[3],
                "Curs": row[4],
                "Grup": row[5],
                "CreatedAt": row[6],
                "UpdatedAt": row[7],
                "DescAula": row[8],
                "Edifici": row[9],
                "Pis": row[10]
            })

        return alumne_list

    except Exception as e:
        print(f"Error en la función read_all_with_details: {e}")
        return {"status": -1, "message": f"Error de conexión: {e}"}

    finally:
        conn.close()

