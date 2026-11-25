from fastapi import APIRouter,Depends
from core import db,require
from claim.collection import deliver
from claim.forms import Claim
from claim.receipt_store import claims

router=APIRouter(prefix="/api/studio")

@router.get("/workshops/{code}/claims")
def receipts(code:str,_=Depends(require())):
    with db() as cx: return claims(cx,code)

@router.post("/pieces/{tag}/claim",status_code=201)
def collect(tag:str,body:Claim,user=Depends(require("operator"))):
    with db() as cx: return deliver(cx,tag,body,user["email"])
