import mysql.connector
con=mysql.connector.connect(
    user="root",
    password="fumafaith7_",
    host="localhost",
    database="website"
)


from fastapi import FastAPI, Request, Path
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse,RedirectResponse

from fastapi.staticfiles import StaticFiles

from starlette.middleware.sessions import SessionMiddleware

from pydantic import BaseModel
from typing import Annotated


app = FastAPI()

origins = [
    "http://localhost",
    "http://127.0.0.1",
]


app.add_middleware(
    SessionMiddleware,
    secret_key="middleware_secret_key"
)

templates = Jinja2Templates(directory="subfolder_w7")

class acctInfo(BaseModel):
    username: str
    password: str

class newacctInfo(BaseModel):
    newrealname: str
    newusername: str
    newpassword: str

class newMessage(BaseModel):
    msgcontent: str

class deleteMessageId(BaseModel):
    messageId:str

class updateName(BaseModel):
    name:str


# 7-1、7-2
@app.get("/api/member")
async def search(username:str, request:Request): 
    hasSignedin=request.session.get("SIGNED-IN")
    if (not hasSignedin):
        return {"data":None}
    else:
        cursor=con.cursor()  
        cursor.execute("SELECT id,name,username FROM member WHERE username=%s",[username,])
        data=cursor.fetchall()
        hasName=(data!=[])
        
        if hasName:
            result={
                        "data":{
                            "id":data[0][0],
                            "name":data[0][1],
                            "username":data[0][2]
                        }
                    }
            return result
        
        else:
            return {"data":None}


# 7-3
@app.patch("/api/member")
async def search(updateName:updateName,request:Request): 
    hasSignedin=request.session.get("SIGNED-IN")
    if (not hasSignedin):
        return {"error":True}
    else:     
        try:
            input_new_name=updateName.name
            current_username=request.session.get("username")

            cursor=con.cursor()        
            cursor.execute("UPDATE member SET name=%s WHERE username=%s",[input_new_name,current_username])
            con.commit()

            request.session["name"]=input_new_name
            
            result={"ok":True}
        except Exception:
            result={"error":True}
        
        return result    



# 6-2   
@app.post("/signup")
async def signup(newacctInfo:newacctInfo,request:Request):
    cursor=con.cursor()
    cursor.execute("SELECT COUNT(*) FROM member WHERE username=%s" ,[newacctInfo.newusername,])
    data_username=cursor.fetchall()[0][0]
    if data_username>0:  
        return RedirectResponse(url="/error?message=Repeated username",status_code=303)
    else:  
        cursor.execute("INSERT INTO member(name, username, password) VALUES(%s, %s, %s) ",[newacctInfo.newrealname, newacctInfo.newusername,newacctInfo.newpassword])
        con.commit()
        return RedirectResponse(url="/")

# 6-3
@app.post("/signin")
async def signin(acctInfo:acctInfo,request:Request):
    cursor=con.cursor()  
    cursor.execute("SELECT id,name,username FROM member WHERE username=%s and password=%s",[acctInfo.username, acctInfo.password])
    data=cursor.fetchall()
    if data!=[]:
        request.session["id"]=data[0][0]
        request.session["name"]=data[0][1]
        request.session["username"]=data[0][2]

        request.session["SIGNED-IN"]=True 

        return RedirectResponse(url="/member",status_code=303)
        
    else:
        return RedirectResponse(url="/error?message=Username or password is not correct",status_code=303)
   
# 6-4   
@app.get("/signout")
async def signout(request:Request):
    request.session["SIGNED-IN"]=False
    
    request.session["id"]=None
    request.session["name"]=None
    request.session["username"]=None
    
    return RedirectResponse(url="/")

# 6-5
@app.post("/createMessage")
async def CreateMessage(newMessage:newMessage,request:Request):   
    msg_member_id=request.session.get("id")
    cursor=con.cursor()
    cursor.execute("INSERT INTO message(member_id, content) VALUES(%s, %s)", [msg_member_id, newMessage.msgcontent])
    con.commit()    
    return RedirectResponse(url="/member",status_code=303)

# 6-6
@app.post("/deleteMessage")
async def DeleteMessage(deleteMessageId:deleteMessageId,request:Request): 
    msg_member_id=request.session.get("id") 
    cursor=con.cursor()
    cursor.execute("DELETE FROM message WHERE id=%s and member_id=%s",[deleteMessageId.messageId, msg_member_id])
    con.commit()

    return RedirectResponse(url="/member",status_code=303)




@app.get("/backhome")
async def index(request: Request):
    return RedirectResponse(url="/",status_code=303)


@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/error")
async def errorpage(request: Request,message:str):
    return templates.TemplateResponse("error.html", {"request": request})


@app.get("/member", response_class=HTMLResponse)
async def successpage(request: Request):
    if request.session.get("SIGNED-IN"):
        cursor=con.cursor()  
        cursor.execute("SELECT message.id, message.content, member.name, message.member_id FROM member INNER JOIN message ON member.id=message.member_id ORDER BY message.time DESC")
        data_msg=cursor.fetchall()
        messagelist=[]
        for k in data_msg:            
            show_result = (k[3]==request.session.get("id"))
            messagelist.append({"id":k[0],"name":k[2],"content":k[1],"show":show_result}) 
        return templates.TemplateResponse("member.html", {"request": request, "name": request.session["name"],"messagelist":messagelist})
    else:
        return RedirectResponse(url="/")

# 靜態檔案處理
app.mount("/",StaticFiles(directory="subfolder_w7",html=True))



