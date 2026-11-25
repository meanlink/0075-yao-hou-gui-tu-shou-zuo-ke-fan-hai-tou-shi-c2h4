from fastapi import HTTPException
from psycopg.types.json import Jsonb
from core import enqueue
from claim.catalog import must_open,workshop
from claim.carrier import all_slips
from claim.pieces import items
from claim.receipt_store import claims
from claim.pivot import summarize

def snapshot(cx,code):
    return cx.execute("SELECT * FROM return_snapshots WHERE workshop=%s",(code,)).fetchone()

def build(cx,course):
    code=course["code"]
    return summarize(course["home"],items(cx,code),all_slips(cx,code),claims(cx,code))

def preview(cx,code):
    course=workshop(cx,code,True)
    saved=snapshot(cx,code)
    return {"published":bool(saved),"pivot":saved["detail"] if saved else build(cx,course)}

def archive(cx,code,staff):
    stats=build(cx,must_open(cx,code))
    if not stats["pieces"]:
        raise HTTPException(409,"该课程没有需要汇总的作品")
    if stats["transit"] or stats["collected"]!=stats["pieces"]:
        raise HTTPException(409,"仍有作品在途或未领取，须先完成返还")
    job=enqueue(cx,"studio-archive",{"course":code})
    return cx.execute("INSERT INTO return_snapshots VALUES (%s,%s,%s,%s) RETURNING *",
                      (code,staff,Jsonb(stats),job)).fetchone()
