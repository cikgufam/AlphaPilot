from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health():
    return {
        "status": "OK",
        "version": "0.1",
        "owner": "Fam CK"
    }