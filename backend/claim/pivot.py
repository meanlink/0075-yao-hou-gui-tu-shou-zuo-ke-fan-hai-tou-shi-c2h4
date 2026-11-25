from collections import defaultdict

def summarize(home,pieces,slips,claims):
    sites=defaultdict(lambda:{"shelf":0,"in_transit":0,"collected":0,"collected_away":0})
    next_site={row["tag"]:row["destination"] for row in slips if row["state"]=="out"}
    got={row["tag"]:row["studio"] for row in claims}
    for piece in pieces:
        tag=piece["tag"]
        if tag in got:
            pickup=got[tag]
            sites[pickup]["collected"]+=1
            sites[pickup]["collected_away"]+=int(pickup!=home)
        elif tag in next_site:
            sites[next_site[tag]]["in_transit"]+=1
        else:
            sites[piece["site"]]["shelf"]+=1
    return {"sites":[{"studio":key,**row} for key,row in sorted(sites.items())],"pieces":len(pieces),
            "collected":len(got),"away":sum(value!=home for value in got.values()),"transit":len(next_site)}
