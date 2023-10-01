from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List
from uuid import uuid4

app = FastAPI()

class Animal(BaseModel):
    id: Optional[str] = None
    nome: str
    idade: int
    sexo: str
    cor: str

banco : List[Animal] = []

@app.get('/animais')
def listar_animais() -> List[Animal]:
    return banco

@app.get('/animais/{animal_id}')
def obter_animal(animal_id: str):
    for animal in banco:
        if animal.id == animal_id:
            return animal
    return {'error': 'Animal não encontrado...'}

@app.delete('/animais/{animal_id}')
def remover_animal(animal_id: str):
    posicao = -1
    # buscar o posicao do animal
    for index, animal in enumerate(banco):
        if animal.id == animal_id:
            posicao = index
            break

    if posicao != -1:
        banco.pop(posicao)
        return {'mensagem': 'Animal removido com sucesso'}
    else:
        return {'erro': 'Animal não localizado'}
    
@app.post('/animais')
def criar_animal(animal: Animal) -> None:
    animal.id = str(uuid4())
    banco.append(animal)
    return None
