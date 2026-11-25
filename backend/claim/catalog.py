from fastapi import HTTPException

def studios(cx):
    return cx.execute("SELECT * FROM studios ORDER BY code").fetchall()

def workshops(cx):
    return cx.execute("SELECT * FROM workshops ORDER BY end_date DESC,code").fetchall()

def workshop(cx, code, lock=False):
    row=cx.execute("SELECT * FROM workshops WHERE code=%s"+(" FOR UPDATE" if lock else ""),(code,)).fetchone()
    if not row:
        raise HTTPException(404,"课程不存在")
    return row

def must_open(cx, code):
    row=workshop(cx,code,True)
    if cx.execute("SELECT 1 FROM return_snapshots WHERE workshop=%s",(code,)).fetchone():
        raise HTTPException(409,"课程返还进度已归档")
    return row
