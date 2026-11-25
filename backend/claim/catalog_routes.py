from fastapi import APIRouter,Depends
from core import db,require
from claim import catalog,pieces

router=APIRouter(prefix="/api/studio")

@router.get("/locations")
def locations(_=Depends(require())):
    with db() as cx: return catalog.studios(cx)

@router.get("/workshops")
def schedule(_=Depends(require())):
    with db() as cx: return catalog.workshops(cx)

@router.get("/workshops/{code}/pieces")
def works(code:str,_=Depends(require())):
    with db() as cx:
        catalog.workshop(cx,code)
        return pieces.items(cx,code)
