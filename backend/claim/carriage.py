from fastapi import HTTPException
from claim import carrier,pieces
from claim.catalog import must_open,studios

def load(cx,tag):
    old=pieces.piece(cx,tag)
    course=must_open(cx,old["workshop"])
    return pieces.piece(cx,tag),course

def depart(cx,tag,transfer,actor):
    row,_=load(cx,tag)
    if row["status"]!="ready":
        raise HTTPException(409,"只有尚在站点且未领取的作品可调拨")
    if row["site"]==transfer.destination or not any(site["code"]==transfer.destination for site in studios(cx)):
        raise HTTPException(409,"须选择不同的有效代收点")
    ticket=carrier.dispatch(cx,tag,row["site"],transfer.destination,actor)
    pieces.move(cx,tag,"moving",row["site"])
    return ticket

def arrive(cx,id,body,user):
    prior=carrier.slip(cx,id)
    item,_=load(cx,prior["tag"])
    if prior["handler"]==user or item["status"]!="moving":
        raise HTTPException(409,"当前调拨必须由另一角色对在途作品验收入点")
    target=prior["destination"] if body.decision=="accepted" else prior["origin"]
    if body.studio!=target:
        raise HTTPException(409,"签收站点必须与到货或退还站点一致")
    result=carrier.acknowledge(cx,id,body.decision,user)
    pieces.move(cx,item["tag"],"ready",target)
    return result
