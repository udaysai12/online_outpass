from django.shortcuts import render
from online_outpass.settings import BASE_DIR, MEDIA_URL, STATIC_URL
from .models import Outpassform, Outpassformaccepted
from django.http import HttpResponseRedirect
from datetime import datetime
from django.contrib.auth import authenticate, login
from django.urls import reverse
from datetime import datetime

# Create your views here.
def index(request):
    return render(request, "online_outpass_api/home_page.html")

def outpass_form(request):
    if request.method == 'POST':
        studentname = request.POST["studentname"]
        sklmid = request.POST["sklmid"]
        email = request.POST["email"]
        studentph = request.POST["studentph"]
        parentname = request.POST["parentname"]
        parentph = request.POST["parentph"]
        year = request.POST["year"]
        rclass = request.POST["rclass"]
        outdate = request.POST["outdate"]
        reportingdate = request.POST["reportingdate"]
        reason = request.POST["reason"]
        address = request.POST["address"]
        proofletter = request.FILES.get("proofletter")
        form = Outpassform(studentname=studentname, sklmid=sklmid, email=email, studentph=studentph, parentph=parentph,parentname=parentname, year=year, rclass=rclass, reason=reason, address=address, outdate=outdate, reportingdate=reportingdate, proofletter=proofletter)
        
        #phone number check
        if (len(studentph) == 10) or (len(parentph) == 10):

            #id check
            try:
                checkid = int(sklmid[-6:])
            except:
                return render(request, "online_outpass_api/outpass_form.html", {
                    "message": "Details not submitted ,Entered id is not valid."
                })
            else:

                #email check
                if email.endswith("@rguktsklm.ac.in"):
                    
                    #date check
                    if datecheck(outdate, reportingdate):

                        #reason check
                        if len(reason) <= 30:
                            form.save()
                            return render(request, "online_outpass_api/outpass_form.html", {
                                "success": "sucessfully your request summitted."
                            })
                        else:
                            return render(request, "online_outpass_api/outpass_form.html", {
                                "message": "Details not submitted ,reason must be below 30 characters"                            })
                    else:
                        return render(request, "online_outpass_api/outpass_form.html", {
                            "message": "Details not submitted ,Entered reporting date is not valid."
                        })
                else:
                    return render(request, "online_outpass_api/outpass_form.html", {
                        "message": "Details not submitted ,Entered email is not college mail."
                    })
        else:
            return render(request, "online_outpass_api/outpass_form.html", {
                "message": "Details not submitted ,Entered phone number is not vlaid."
            })

    return render(request, "online_outpass_api/outpass_form.html")

def admin_login_page(request):
    if request.method == 'POST':
        adminname = request.POST["adminname"]
        adminpassword = request.POST["adminpassword"]
        user = authenticate(request, username=adminname, password=adminpassword)

        #logining
        if user is not None:
            login(request, user)
            return HttpResponseRedirect("/onlineoutpass/adminpage")
        else:
            return render(request, "online_outpass_api/admin_login_page.html", {
                "message":"Incorrect password or username.Try Again..."
            })
    return render(request, "online_outpass_api/admin_login_page.html")

def admin_page(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("adminlogin"))
    applications = Outpassform.objects.all()
    return render(request, "online_outpass_api/admin_page.html", {
        "applications": applications
    })

def details_page(request, applicant_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("adminlogin"))

    applicant = Outpassform.objects.get(id=applicant_id)

    context = {
        "outpassformaccepted": Outpassformaccepted,
        "applicant":applicant,
        "accepted":f"Your request for outpass was accepted.\nNAME: {applicant.studentname}\nYEAR: {applicant.year}\nID: {applicant.sklmid}\nREASON: {applicant.reason}\nTODAY: {datetime.today().date()}\nOUTING DATE: {applicant.outdate}\nREPORTING DATE: {applicant.reportingdate}\nGo safe return happily.",
        "rejected":f"Your request for outpass was rejected for your reason({applicant.reason}) for queries message to {request.user.email}."
    }

    if request.method == 'POST':
        btnvalue = request.POST["submit"]
        print(btnvalue)
        if btnvalue == 'accept':
            form = Outpassformaccepted(studentname=applicant.studentname, sklmid=applicant.sklmid, email=applicant.email, studentph=applicant.studentph, parentph=applicant.parentph,parentname=applicant.parentname, year=applicant.year, rclass=applicant.rclass, reason=applicant.reason, address=applicant.address, outdate=applicant.outdate, reportingdate=applicant.reportingdate, proofletter=applicant.proofletter)
            form.save()
            applicant.delete()

    
    return render(request, "online_outpass_api/detail-view-page.html", context)

#check higher date
def datecheck(out, report):
    out = out.split("-")
    report = report.split("-")
    out = datetime(int(out[0]), int(out[1]), int(out[2]))
    report = datetime(int(report[0]), int(report[1]), int(report[2]))
    if out>report:
        return False
    else:
        return True