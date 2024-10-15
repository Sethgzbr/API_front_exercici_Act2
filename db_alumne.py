from client import db_client

def read():
    try:
        conn = db_client()
        cur = conn.cursor()
        cur.execute("select * from alumne")
    
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

def readAll():
    try:
        conn = db_client()
        cur = conn.cursor()
        cur.execute("SELECT a.IdAlumne, a.IdAula, a.NomAlumne, a.Cicle, a.curs, a.grup, au.DescAula, au.Edifici, au.Pis FROM alumne a JOIN aula au ON a.IdAula = au.IdAula;")
    
        students = cur.fetchall()
    
    except Exception as e:
        print("ERROR", e)
        return {"status": -1, "message": f"Error de connexió:{e}" }
    
    finally:
        conn.close()
    
    return students