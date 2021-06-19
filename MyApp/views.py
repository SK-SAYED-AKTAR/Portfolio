from django.shortcuts import render
from .models import ProjectTable
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# Create your views here.

def index(request):
    if request.method == "POST":
        clientName = request.POST['name']
        projectName = request.POST['projectName']
        skill = request.POST['skill']
        projectDesc = request.POST['projectDesc']

        obj = ProjectTable(clientName=clientName, projectName=projectName, Skill=skill, projectDesc=projectDesc)
        obj.save()

        sendMail(clientName, projectName, skill, projectDesc)
        return render(request, "index.html", {"onSuccessSend":True})
    else:
        return render(request, "index.html", {"onSuccessSend":False})

def webDev(request):
    return render(request, "webDev.html")

def appDev(request):
    return render(request, "appDev.html")

def webScrapping(request):
    return render(request, "webScrapping.html")

def mySkill(request):
    return render(request, "mySkill.html")

def sendMail(clientName, projectName, skill, projectDesc):
    # Credential
    fromMail = "sayeddevil2@gmail.com"
    password = "sayedisahacker100%TRUE"

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(fromMail, password)
    print("Login successfull ....")


    message = MIMEMultipart("alternative")
    message['Subject'] = "Congratulation! You got a new project."
    html = f'''
        <html>
            <head> </head>
            <body>
                    <b>Client Name: </b>{clientName} <br><br>
                    <b>Project Title: </b>{projectName} <br><br>
                    <b>Required Skills: </b>{skill} <br><br>
                    <b>Description : </b>{projectDesc} <br><br>               
            </body>
        </html>

    '''

    text = MIMEText(html, "html")
    message.attach(text)


    try:
        server.sendmail(fromMail, "sayedacnt123@gmail.com", message.as_string())
        print("Email successfully send !!!!")
    except Exception as e:
        print(e)

    server.quit()
