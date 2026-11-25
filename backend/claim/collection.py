from secrets import compare_digest
from fastapi import HTTPException
from claim.carriage import load
from claim.pieces import move
from claim.receipt_store import sign

def deliver(cx,tag,data,staff):
    row,course=load(cx,tag)
    if row["status"]=="moving":
        raise HTTPException(409,"作品在途，须先确认收货")
    if row["status"]=="collected":
        raise HTTPException(409,"作品已领取")
    if data.studio!=row["site"]:
        raise HTTPException(409,"应在实物所在的站点签收")
    if not compare_digest(row["claim_code"],data.code):
        raise HTTPException(409,"课程领件码不匹配")
    if not course["end_date"]<=data.local_day<=course["pickup_through"]:
        raise HTTPException(409,"领件日期不在课程允许时段")
    row=sign(cx,tag,data,staff)
    move(cx,tag,"collected",data.studio)
    return row
