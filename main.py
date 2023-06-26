import json
from typing import List

import uvicorn
from fastapi import FastAPI
from fastapi import Query

from app.utils.tlearning_ai import ai_request

app = FastAPI()

@app.get('/')
def home():
    return {"Hello": "I'm in a container from AWS"}

@app.get('/ai')
def get_corricular_grid(
    type_skills: List[str] = Query(
        ...,
        description= "Describe una o más habilidades"
        ),
    sector_company: str = Query(
        ...,
        description= "Agro | Industria | Servicios"
        )
):  
    
    skills = {type_skills[0] if len(type_skills)==1 else " y ".join(type_skills)}

    prompt_b = f"""Eres un experto en formación corporativa, con más de 30 años de experiencia potenciando las habilidades de {skills} para el capital humano
                de cientos de empresas del sector {sector_company}. Recientemente fuiste contratado por una empresa de este sector,  
                en la cual se te asignó la responsabilidad de crear una malla curricular de cursos enfocados en {skills} para sus empleados.
                Entonces, crea una malla curricular de cursos teniendo en cuenta las competencias de {skills} y organízala por niveles de cargo.
                Escribe el resultado en notación JSON."""
    
    response = ai_request(prompt_b)
    response = response["choices"][0]["text"]
    json_resp = json.loads(response)
    print(f"OUTPUT TYPE{type(json_resp)}")
    print(json_resp)
    return json_resp


if __name__=='__main__':
    uvicorn.run(app, port=8888, host="127.0.0.1")