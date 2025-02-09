from fastapi import FastAPI,Request,Path
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse,RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()

origins = [
    "http://localhost",
    "http://127.0.0.1",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(
    SessionMiddleware,
    secret_key="middleware_secret_key"
)

templates = Jinja2Templates(directory="folder_a")

class acctInfo(BaseModel):
    username: str
    password: str


@app.get("/square/{squ}")
async def square(squ:Annotated[int,Path(ge=1)], request:Request):
    calculateResult = squ **2
    return RedirectResponse(url="/square?result="+str(calculateResult),status_code=303)
   
@app.get("/square")
def squarepage(calculateResult:str):
    return "square.html?result="+calculateResult

@app.post("/signin")
async def signin(acctInfo:acctInfo,request:Request):
    if acctInfo.username=='' or acctInfo.username==' ' or acctInfo.password=='' or acctInfo.password==' ':
        return RedirectResponse(url="/error?message=Please enter username and password",status_code=303)
    else:
        if acctInfo.username =='test' and acctInfo.password=='test':
            request.session["SIGNED-IN"]=True
            return RedirectResponse(url="/member",status_code=303)
        else:
            return RedirectResponse(url="/error?message=Username or password is not correct",status_code=303)

@app.get("/signout")
async def signout(request:Request):
    request.session["SIGNED-IN"]=False
    return "/"

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/member")
def successpage(request:Request):
    if request.session.get("SIGNED-IN"):
        return "member.html"
    else:
        return "/"
    

@app.get("/error")
def errorpage(message:str):
    return "error.html?message="+message


# 靜態檔案處理
app.mount("/",StaticFiles(directory="folder_a",html=True))