from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from presentation.routers.user_router import router as user_router
from presentation.routers.auth_router import router as auth_router
from presentation.routers.ghibli_router import router as ghibli_router
from infrastructure.database import SessionLocal
from domain.entities.user import User
from domain.enums.role_enum import RoleEnum
from infrastructure.security.password_handler import hash_password

app = FastAPI(title="Users API", version="1.0.0")


@app.on_event("startup")
def seed_admin_user():
    db = SessionLocal()
    try:
        existing = db.query(User).filter(User.username == "admin").first()
        if not existing:
            admin = User(
                username="admin",
                password=hash_password("admin"),
                role=RoleEnum.ADMIN,
            )
            db.add(admin)
            db.commit()
    finally:
        db.close()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router, prefix="/api")
app.include_router(auth_router, prefix="/api")
app.include_router(ghibli_router, prefix="/api")
