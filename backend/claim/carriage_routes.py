from fastapi import APIRouter,Depends
from core import db,require
from claim.carriage import depart,arrive
from claim.carrier import all_slips
from claim.forms import Transfer,Arrival

router=APIRouter(prefix="/api/studio")

@router.get("/workshops/{code}/carriage")
def list_carriages(code:str,_=Depends(require())):
    with db() as cx: return all_slips(cx,code)

@router.post("/pieces/{tag}/move",status_code=201)
def carry(tag:str,body:Transfer,user=Depends(require("operator"))):
    with db() as cx: return depart(cx,tag,body,user["email"])

@router.put("/carriage/{id}")
def arrival(id:int,body:Arrival,user=Depends(require("reviewer"))):
    with db() as cx: return arrive(cx,id,body,user["email"])
