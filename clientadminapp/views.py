from django.shortcuts import render,HttpResponse,redirect
from clientadminapp.dowellconnection import dowellconnection
import requests
from datetime import datetime, date
import json
from django.http import JsonResponse
def home(request):
    redirect_url=request.GET.get('session_id',None)
    if redirect_url is not None:
        request.session["session_id"]=redirect_url
        return redirect('dashboard')
    else:
        return redirect("https://100014.pythonanywhere.com/?redirect_url=http://127.0.0.1:8000")
def MainPage(request):
    if request.session.get("session_id"):
        context={}
        
        return render(request,"header.html",context)
def HomePage(request):
    session=request.session["session_id"]
    if session:
        if request.method=="POST":
            
            org=request.POST["org_name"]
            request.session["selected_wspace"]=org
            return JsonResponse({"msg":f"Wait workspace changing to {org} ..."})
        context={}
        url="https://100014.pythonanywhere.com/api/userinfo/"
        resp=requests.post(url,data={"session_id":session})
        try:
            user=json.loads(resp.text)
            request.session["username"]=user["userinfo"]["username"]
            #print(user)
        except:
            return HttpResponse('<style>body{background-color: rgba(0,0,0, 0.4);}.close-btn {position: absolute;bottom: 12px;right: 25px;}.content {position: absolute;width: 250px;height: 200px;background: #fff;top: 0%;left: 50%;transform: translate(-50%, -50%)scale(0.1);visibility: hidden;transition: transform 0.4s, top 0.4s;}.open-popup {visibility: visible;top: 50%;transform: translate(-50%, -50%)scale(1);}.header {height: 50px;background: #efea53;overflow: hidden;text-align: center;}p {padding-top: 40px;text-align: center;}</style><div class="content open-popup" id="popup"><div class="header"><h2>Alert!</h2></div><p>Some thing went wrong pl <a href="logout" >logout </a> <a href="https://100014.pythonanywhere.com">login</a> again</p><div><button type="button" onclick="history.back();" class="close-btn">close</button></div></div>')
        if user["userinfo"]:
            context["login"]=user["userinfo"]
            field={"document_id":user["userinfo"]["userID"]}
            forg=dowellconnection("login","bangalore","login","organization","organization","1084","ABCDE","find",field,"nil")
            client_admin_res=json.loads(forg)
            context["products"]=client_admin_res["data"]["products"]
            if client_admin_res["data"] is None:
                with open('organisation.json') as json_file:
                    data = json.load(json_file)
                    data["document_id"]=user["userinfo"]["userID"]
                    data["username"]=user["userinfo"]["username"]
                    data["first_name"]=user["userinfo"]["first_name"]
                    data["last_name"]=user["userinfo"]["last_name"]
                    data["email"]=user["userinfo"]["email"]
                    orgs={"owner": user["userinfo"]["username"], "username": user["userinfo"]["username"], "workspace_name": user["userinfo"]["username"], "logo": ""}
                    data["myworkspaces"].append(orgs)
                    field1=data
                    dowellconnection("login","bangalore","login","organization","organization","1084","ABCDE","insert",field1,"nil")
                    field={"document_id":user["userinfo"]["userID"]}
                    forg=dowellconnection("login","bangalore","login","organization","organization","1084","ABCDE","find",field,"nil")
                    client_admin_res=json.loads(forg)
                    context["products"]=client_admin_res["data"]["products"]
            try:
                request.session["selected_wspace"]
            except:
                request.session["selected_wspace"]=client_admin_res["data"]["myworkspaces"][0]["workspace_name"]
            context["org"]=client_admin_res["data"]
            request.session["own_wspace"]=client_admin_res["data"]["myworkspaces"][0]["workspace_name"]
            request.session["owner_name"]=client_admin_res["data"]["myworkspaces"][0]["owner"]
            request.session["userID"]=user["userinfo"]["userID"]
            request.session["admin_id"]=client_admin_res["data"]["_id"]
            context["org"]=client_admin_res["data"]
            datetime_object = datetime.strptime(user["userinfo"]["dowell_time"], '%d %b %Y %H:%M:%S')
            totalsec=(datetime.now() - datetime_object).total_seconds()
            totalmin=totalsec//60
            totalhr=int(totalmin//60)
            totalmin1=int(totalmin%60)
            context["duration"] = f'{totalhr} hours {totalmin1} minutes'
            return render(request,"layout.html",context)
        else:
            return redirect("logout")
    
        return render(request,"index.html",context)
        
def ProductPage(request):
    if request.session.get("session_id"):
        context={}

        return render(request,"product.html",context)
def PortfolioPage(request):
    if request.session.get("session_id"):
        if request.method=="POST":
            pass
        context={}
        return render(request,"portfolio.html",context)
def MembersPage(request):
    if request.session.get("session_id"):
        context={}
        return render(request,"members.html",context)
def RolesPage(request):
    if request.session.get("session_id"):
        context={}
        return render(request,"roles.html",context)
def LevelsPage(request):
    if request.session.get("session_id"):
        if request.POST["form"]=="getlevels":
            context={}
            admin_id=request.session["admin_id"]
            own_wspace=request.session["own_wspace"]
            username=request.session["username"]
            owner=request.session["owner_name"]
            field={"admin_id":admin_id,"wspace_name":own_wspace}
            resp=dowellconnection("login","bangalore","login","department","department","1085","ABCDE","find",field,"nil")
            admin_res=json.loads(resp)
            if admin_res["data"] is None:
                field={"admin_id":admin_id,"username":username,"wspace_name":own_wspace,"level1":{"name":"level1","items":[]},"level2":{"name":"level2","items":[]},"level3":{"name":"level3","items":[]},"level4":{"name":"level4","items":[]},"level5":{"name":"level5","items":[]}}
                dowellconnection("login","bangalore","login","department","department","1085","ABCDE","insert",field,"nil")
                field={"admin_id":admin_id,"wspace_name":own_wspace}
                resp=dowellconnection("login","bangalore","login","department","department","1085","ABCDE","find",field,"nil")
                admin_res=json.loads(resp)
            return JsonResponse(admin_res['data'])
        if request.POST["form"]=="levelnames":
            level=request.POST["level"]
            levelname=request.POST["level_name"]
            field={"admin_id":request.session["admin_id"],"wspace_name":request.session["own_wspace"]}
            resp=dowellconnection("login","bangalore","login","department","department","1085","ABCDE","find",field,"nil")
            admin_res=json.loads(resp)
            admin_res["data"][level]["name"]=levelname
            update={level:admin_res["data"][level]}
            resp=dowellconnection("login","bangalore","login","department","department","1085","ABCDE","update",field,update)
            
            return JsonResponse({"name":levelname,"msg":"updated Successfully"})
def LayersPage(request):
    if request.session.get("session_id"):
        context={}
        return render(request,"layers.html",context)
def LogoutPage(request):
    d=request.session.get("session_id")
    #return HttpResponse(d)
    #equest.session.modified = True
    if d:
        try:
            del request.session["username"]
            del request.session["selected_wspace"]
            # del request.session["orgname"]
            del request.session["session_id"]
            return redirect("https://100014.pythonanywhere.com/sign-out")
        except:
            return redirect("https://100014.pythonanywhere.com/sign-out")
    else:
        return redirect("https://100014.pythonanywhere.com/sign-out")
