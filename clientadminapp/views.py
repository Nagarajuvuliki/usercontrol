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
            if request.session["selected_wspace"]:
                pass
            else:
                request.session["selected_wspace"]=client_admin_res["data"]["myworkspaces"][0]["workspace_name"]
            context["org"]=client_admin_res["data"]
            
            datetime_object = datetime.strptime(user["userinfo"]["dowell_time"], '%d %B %Y %H:%M:%S')
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
        context={}
        return render(request,"levels.html",context)
def LayersPage(request):
    if request.session.get("session_id"):
        context={}
        return render(request,"layers.html",context)
