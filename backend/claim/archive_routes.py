from fastapi import APIRouter,Depends
from core import db,require
from claim.archives import archive,preview

router=APIRouter(prefix="/api/studio/workshops")

@router.get("/{code}/pivot")
def report(code:str,_=Depends(require())):
    with db() as cx: return preview(cx,code)

@router.post("/{code}/archive",status_code=201)
def freeze(code:str,user=Depends(require("reviewer"))):
    with db() as cx: return archive(cx,code,user["email"])
