from claim.archives import snapshot

def close(cx,payload):
    data=snapshot(cx,payload["course"])["detail"]
    return {"preserved":sum(row["collected"] for row in data["sites"])==data["pieces"],
            "offsite_share":round(100*data["away"]/data["pieces"],2)}
