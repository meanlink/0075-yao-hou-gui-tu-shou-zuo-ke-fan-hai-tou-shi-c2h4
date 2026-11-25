from fastapi import HTTPException

def all_slips(cx,code):
    return cx.execute("""
      SELECT s.*,c.title FROM carrier_slips s JOIN ceramics c ON c.tag=s.tag
      WHERE c.workshop=%s ORDER BY s.id DESC
    """,(code,)).fetchall()

def slip(cx,id):
    row=cx.execute("SELECT * FROM carrier_slips WHERE id=%s",(id,)).fetchone()
    if not row:
        raise HTTPException(404,"调拨票找不到")
    return row

def dispatch(cx,tag,origin,dest,email):
    return cx.execute("""
      INSERT INTO carrier_slips(tag,origin,destination,handler)
      VALUES (%s,%s,%s,%s) RETURNING *
    """,(tag,origin,dest,email)).fetchone()

def acknowledge(cx,id,decision,actor):
    row=cx.execute("""
      UPDATE carrier_slips SET state=%s,accepted_by=%s WHERE id=%s AND state='out' RETURNING *
    """,(decision,actor,id)).fetchone()
    if not row:
        raise HTTPException(409,"调拨票已处理")
    return row
