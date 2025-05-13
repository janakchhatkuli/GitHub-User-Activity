from fastapi import FastAPI
from pydantic import BaseModel
from activity import fetch_user_activity

app = FastAPI()

class AddRequest(BaseModel) :
    username: str
    event_type_filter : str | None = None

@app.post("/fetch_user_activity")
def activity(data : AddRequest):
    return{"result": fetch_user_activity(data.username,data.event_type_filter)}

