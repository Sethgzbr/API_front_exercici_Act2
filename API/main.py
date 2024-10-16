from typing import List, Union
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

import alumne
import db_alumne

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class student(BaseModel):
    IdAlumne: int
    IdAula: int
    nomAlumne:str
    cicle: str
    curs: int
    grup: str

class tablaAlumne(BaseModel):
    NomAlumne:str
    Cicle: str
    Curs: int
    Grup: str
    DescAula: int

@app.get("/")
def read_root():
    return {"Students API"}

@app.get("/alumne", response_model=List[tablaAlumne])
def read_alumne():

    return alumne.alumne_schema(db_alumne.read())


@app.get("/alumne/show/{IdAlumne}", response_model=List[dict])
def read_id(IdAlumne:int):
    print(IdAlumne)
    if db_alumne.read_id(IdAlumne) is not None:
        student = alumne.alumne_schema(db_alumne.read_id(IdAlumne))
    else:
        raise HTTPException(status_code=404, detail="Item not found")
    return student 

@app.post("/create_estudiant")
async def create_student(data: student):
    IdAula = data.IdAula
    nomAlumne = data.nomAlumne
    cicle = data.cicle
    curs = data.curs
    grup = data.grup
    if db_alumne.aula_existeix(IdAula):
        l_student_id = db_alumne.create(IdAula, nomAlumne,cicle,curs,grup)
    else:
        raise HTTPException(status_code = 404, detail = "Aula no trobada, sisplau afegeix un que existeixi,")
    
    return {
        "msg": "“S’ha afegit correctement",
        "id student": l_student_id,
        "Nom Alumne": nomAlumne
    }

@app.put("/update/{id}")
def update(IdAula: int,nomAlumne: str,cicle: str,curs: int,grup: str):
    updated_records = db_alumne.update(IdAula,nomAlumne,cicle,curs,grup)
    if updated_records == 0:
       raise HTTPException(status_code=404, detail="Items to update not found") 


@app.post("/delete_estudiant/{id}")
async def delete_student(IdAlumne: int):
    IdAlumne = IdAlumne

    if db_alumne.aula_existeix(IdAula):
        l_student_id = db_alumne.create(IdAula, nomAlumne,cicle,curs,grup)
    else:
        raise HTTPException(status_code = 404, detail = "Aula no trobada, sisplau afegeix un que existeixi,")
    
    return {
        "msg": "“S’ha eliminat correctement",
        "id student": l_student_id,
    }

@app.get("/alumne/listAll")
def read_all_alumne():
    return db_alumne.read_all_with_details()