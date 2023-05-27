from django.shortcuts import render,HttpResponse,redirect
from clientadminapp.dowellconnection import dowellconnection
import requests
import json
def home(request):
    redirect_url=request.GET.get('session_id',None)
    if redirect_url is not None:
        request.session["session_id"]=redirect_url
        return redirect('homepage')
    else:
        return redirect("https://100014.pythonanywhere.com/?redirect_url=http://127.0.0.1:8000")
def MainPage(request):
    if request.session.get("session_id"):
        context={}
        session=request.session["session_id"]
        url="https://100014.pythonanywhere.com/api/userinfo/"
        resp=requests.post(url,data={"session_id":session})
        try:
            user=json.loads(resp.text)
        except:
            return HttpResponse('<style>body{background-color: rgba(0,0,0, 0.4);}.close-btn {position: absolute;bottom: 12px;right: 25px;}.content {position: absolute;width: 250px;height: 200px;background: #fff;top: 0%;left: 50%;transform: translate(-50%, -50%)scale(0.1);visibility: hidden;transition: transform 0.4s, top 0.4s;}.open-popup {visibility: visible;top: 50%;transform: translate(-50%, -50%)scale(1);}.header {height: 50px;background: #efea53;overflow: hidden;text-align: center;}p {padding-top: 40px;text-align: center;}</style><div class="content open-popup" id="popup"><div class="header"><h2>Alert!</h2></div><p>Some thing went wrong pl <a href="logout" >logout </a> <a href="/">login</a> again</p><div><button type="button" onclick="history.back();" class="close-btn">close</button></div></div>')
        context["login"]=user["userinfo"]
        field={"document_name":user["userinfo"]["username"]}
        forg=dowellconnection("login","bangalore","login","client_admin","client_admin","1159","ABCDE","fetch",field,"nil")
        client_admin_res=json.loads(forg)
        ls=[client_admin_res["data"][0]["organisations"][0]["org_name"]]
        
        for ii in client_admin_res["data"][0]["other_organisation"]:
            ls.append(ii["org_name"])
        context["org"]=[*set(ls)]
        context["profile"]=client_admin_res["data"][0]["profile_info"]
        return render(request,"header.html",context)
def HomePage(request):

    if request.session.get("session_id"):
        context={}
        if request.method=="POST":

           return render(request,"index.html",context)
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
