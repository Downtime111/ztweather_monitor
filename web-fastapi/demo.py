from fastapi import FastAPI,Cookie
from fastapi.responses import HTMLResponse
from starlette.requests import Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")
'''
#@app.get('/')
#async def main(request:Request):
#    return templates.TemplateResponse('index.html',{'request':request,"hello":"hahhaha"})

#@app.get('/{item_id}/')
#async def main(request:Request,item_id):
#    return templates.TemplateResponse('index.html',{'request':request,"hello":"hahhaha","item_id":item_id})

@app.post("/")
async def create_upload_files(request:Request,username:str=Form(...),password:str=Form(...)):
    print(username)
    print(password)
    return templates.TemplateResponse("index.html",{"request":request,"username":username,"password":password})

@app.get('/')
async def main(request:Request):
    return templates.TemplateResponse('post.html', {'request': request})
'''

@app.get('/items/')
async def get_cookie(cookie:int = Cookie(None)):
    return {"id":1,"cookie":cookie}
if __name__ == '__main__':
   import uvicorn
   uvicorn.run(app, host="127.0.0.1", port=8000)