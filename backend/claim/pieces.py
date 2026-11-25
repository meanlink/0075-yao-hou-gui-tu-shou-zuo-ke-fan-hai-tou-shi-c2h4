from fastapi import HTTPException

def items(cx,workshop):
    return cx.execute("SELECT tag,title,site,status,workshop FROM ceramics WHERE workshop=%s ORDER BY tag",(workshop,)).fetchall()

def piece(cx,tag):
    row=cx.execute("SELECT * FROM ceramics WHERE tag=%s",(tag,)).fetchone()
    if not row:
        raise HTTPException(404,"作品标签不存在")
    return row

def move(cx,tag,status,site):
    row=cx.execute("""
      UPDATE ceramics SET status=%s, site=%s WHERE tag=%s RETURNING tag,title,site,workshop,status
    """,(status,site,tag)).fetchone()
    return row
