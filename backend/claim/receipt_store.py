def claims(cx,code):
    return cx.execute("""
      SELECT h.*,c.title FROM claim_checks h JOIN ceramics c ON c.tag=h.tag
      WHERE c.workshop=%s ORDER BY h.local_day DESC,h.tag
    """,(code,)).fetchall()

def sign(cx,tag,data,staff):
    return cx.execute("""
      INSERT INTO claim_checks VALUES (%s,%s,%s,%s,%s) RETURNING *
    """,(tag,data.studio,data.local_day,data.receiver,staff)).fetchone()
