from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Ability(BaseModel):
    name: str
    description: str

class CharacterRole(BaseModel):
    name: str
    description: str
    abilities: list[Ability]
    equipment: list[str]

class Scene(BaseModel):
    name: str
    description: str
    characters: list[CharacterRole]

@app.get("/knight")
async def get_knight():
    knight = CharacterRole(
        name="Knight",
        description="A noble warrior with a strong sense of justice.",
        abilities=[
            Ability(name="Swordsmanship", description="Expertise in wielding swords."),
            Ability(name="Shield Defense", description="Ability to defend with shields.")
        ],
        equipment=["Sword", "Shield", "Armor"]
    )
    return knight

@app.get("/wizard")
async def get_wizard():
    wizard = CharacterRole(
        name="Wizard",
        description="A wise and powerful mage with mastery over the elements.",
        abilities=[
            Ability(name="Magic Casting", description="Ability to cast powerful spells."),
            Ability(name="Elemental Resistance", description="Resistance to elemental attacks.")
        ],
        equipment=["Staff", "Tome", "Robes"]
    )
    return wizard

@app.get("/scene")
async def get_scene():
    scene = Scene(
        name="The Dark Forest",
        description="A dense and mysterious forest filled with ancient secrets and hidden dangers.",
        characters=[
            CharacterRole(
                name="Knight",
                description="A noble warrior with a strong sense of justice.",
                abilities=[
                    Ability(name="Swordsmanship", description="Expertise in wielding swords."),
                    Ability(name="Shield Defense", description="Ability to defend with shields.")
                ],
                equipment=["Sword", "Shield", "Armor"]
            ),
            CharacterRole(
                name="Wizard",
                description="A wise and powerful mage with mastery over the elements.",
                abilities=[
                    Ability(name="Magic Casting", description="Ability to cast powerful spells."),
                    Ability(name="Elemental Resistance", description="Resistance to elemental attacks.")
                ],
                equipment=["Staff", "Tome", "Robes"]
            )
        ]
    )
    return scene
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)