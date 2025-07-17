from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.schemas import UserRegister, TokenResponse, UserOut
from app.users import get_user, create_user, verify_password
from app.utils import create_access_token, decode_access_token

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

@router.post("/register")
def register(user: UserRegister):
    if get_user(user.username):
        raise HTTPException(status_code=400, detail="Username already exists")
    create_user(user.username, user.password)
    return {"message": "User created successfully"}

@router.post("/login", response_model=TokenResponse)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = get_user(form_data.username)
    if not user or not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"sub": user["username"]})
    return {"access_token": token, "token_type": "bearer"}

@router.get("/me", response_model=UserOut)
def get_me(token: str = Depends(oauth2_scheme)):
    username = decode_access_token(token)
    if not username:
        raise HTTPException(status_code=401, detail="Invalid token")
    user = get_user(username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"username": user["username"]}
