from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Fake in-memory user database
fake_users_db = {}

def get_user(username: str):
    return fake_users_db.get(username)

def create_user(username: str, password: str):
    hashed_password = pwd_context.hash(password)
    user = {"username": username, "hashed_password": hashed_password}
    fake_users_db[username] = user
    return user

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)
