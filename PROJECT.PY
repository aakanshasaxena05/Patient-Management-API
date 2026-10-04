from fastapi import FastAPI,HTTPException
app=FastAPI()
from pydantic import BaseModel,Field
from typing import Annotated,Optional,Literal
patient = {
    "P101": {
        "name": "Aakansha",
        "age": 22,
        "gender": "Female",
        "disease": "Diabetes",
        "city": "Jaipur"
    },
    "P102": {
        "name": "Rahul",
        "age": 35,
        "gender": "Male",
        "disease": "Fever",
        "city": "Delhi"
    },
    "P103": {
        "name": "Priya",
        "age": 28,
        "gender": "Female",
        "disease": "Asthma",
        "city": "Mumbai"
    },
    "P104": {
        "name": "Amit",
        "age": 45,
        "gender": "Male",
        "disease": "Hypertension",
        "city": "Pune"
    },
    "P105": {
        "name": "Neha",
        "age": 31,
        "gender": "Female",
        "disease": "Migraine",
        "city": "Jaipur"
    },
    "P106": {
        "name": "Rohan",
        "age": 40,
        "gender": "Male",
        "disease": "Asthma",
        "city": "Delhi"
    },
    "P107": {
        "name": "Sneha",
        "age": 26,
        "gender": "Female",
        "disease": "Anemia",
        "city": "Kolkata"
    },
    "P108": {
        "name": "Vikas",
        "age": 52,
        "gender": "Male",
        "disease": "Diabetes",
        "city": "Mumbai"
    },
    "P109": {
        "name": "Pooja",
        "age": 29,
        "gender": "Female",
        "disease": "Thyroid",
        "city": "Lucknow"
    },
    "P110": {
        "name": "Arjun",
        "age": 33,
        "gender": "Male",
        "disease": "Fever",
        "city": "Jaipur"
    },
    "P111": {
        "name": "Kavita",
        "age": 47,
        "gender": "Female",
        "disease": "Hypertension",
        "city": "Delhi"
    },
    "P112": {
        "name": "Manish",
        "age": 38,
        "gender": "Male",
        "disease": "Cholesterol",
        "city": "Pune"
    },
    "P113": {
        "name": "Anjali",
        "age": 24,
        "gender": "Female",
        "disease": "Migraine",
        "city": "Mumbai"
    },
    "P114": {
        "name": "Suresh",
        "age": 56,
        "gender": "Male",
        "disease": "Heart Disease",
        "city": "Delhi"
    },
    "P115": {
        "name": "Meena",
        "age": 42,
        "gender": "Female",
        "disease": "Diabetes",
        "city": "Jaipur"
    },
    "P116": {
        "name": "Karan",
        "age": 30,
        "gender": "Male",
        "disease": "Back Pain",
        "city": "Kolkata"
    },
    "P117": {
        "name": "Riya",
        "age": 27,
        "gender": "Female",
        "disease": "Asthma",
        "city": "Lucknow"
    },
    "P118": {
        "name": "Deepak",
        "age": 49,
        "gender": "Male",
        "disease": "Kidney Stone",
        "city": "Pune"
    },
    "P119": {
        "name": "Simran",
        "age": 34,
        "gender": "Female",
        "disease": "Thyroid",
        "city": "Delhi"
    },
    "P120": {
        "name": "Nikhil",
        "age": 41,
        "gender": "Male",
        "disease": "Hypertension",
        "city": "Mumbai"
    }
}
app=FastAPI()
@app.get("/display/{id}")
#get 
def display(id:str):
    return{
          "record":patient[id]
    } 
@app.get("/dis")
def dis(id:str):
    return{
        "record":patient[id]
    }
class create(BaseModel):
    id:str
    name:str
    age:int
    gender:str
    disease:str
    city:str
@app.post("/add/{id}")
def create(id:str,data:create):
    if id in patient:
        raise HTTPException(status_code=400,detail="already exists")
    patient[id]={
        "name":data.name,
        "age":data.age,
        "gender":data.gender,
        "disease":data.disease,
        "city":data.city
    }
    return{
        "Data added":patient[id]

    }
class Update(BaseModel):
    id: Annotated[Optional[str], Field(description="Enter ID")] = None

    name: Annotated[Optional[str], Field(description="Enter name")] = None

    age: Annotated[Optional[int], Field(gt=0, description="Enter age")] = None

    gender: Annotated[
        Optional[Literal["Male", "Female"]],
        Field(description="Enter gender: Male or Female")
    ] = None

    disease: Annotated[Optional[str], Field(description="Enter disease")] = None

@app.put("/update/{id}")
def update(id:str,d:Update):
    if id not in patient:
        raise HTTPException(status_code=404,detail="not found")
    if d.name is not None:
        patient[id]["name"]=d.name
    if d.age is not None:
        patient[id]["age"] = d.age

    if d.gender is not None:
        patient[id]["gender"] = d.gender

    if d.disease is not None:
        patient[id]["disease"] = d.disease

    return {
        "message": "Patient updated successfully",
        "patient": patient[id]
    }
@app.delete("/delete/{id}")
def dele(id: str):

    if id not in patient:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    deleted_patient = patient.pop(id)

    return {
        "message": "Patient deleted successfully",
        "patient": deleted_patient
    }