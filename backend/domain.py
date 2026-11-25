from fastapi import APIRouter
from claim import archive_routes,carriage_routes,catalog_routes,collection_routes
from claim.demo import seed
from claim.worker_receipt import close

router=APIRouter()
for section in (catalog_routes,carriage_routes,collection_routes,archive_routes):
    router.include_router(section.router)

def run_job(cx,kind,payload):
    if kind=="studio-archive": return close(cx,payload)
    raise ValueError(f"Unknown studio archive task {kind}")
