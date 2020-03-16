import sys
import psycopg2

class Techmodification:
    def __init__(self,data=None):
        self.data=None
        self.host="smtp.neotel.co.za"
        self.port="25"
        self.mail="SanralServiceDesk@liquidtelecom.co.za"
        self.password=""

    def sendmail(self,id ,mail_id):
        try:
            message = "Mail notification of case id {}".format(id)
            subject = "for case id {}".format(id)
            to_addr_list = mail_id
            alarm_id = self.data["event_id"]
            #objmail = OutputConfig.objects.get(name="MAIL")#need to change
            smtpserver = self.host + ":" + self.port
            login = self.username
            password = self.password
            smessage = 'Subject: {}\n\n{}'.format(subject, message)
            server = smtplib.SMTP(smtpserver)
            server.ehlo()
           # server.starttls()
           # server.login(login, password)
            problems = server.sendmail(login, to_addr_list, smessage)
            server.quit()
           # event=Alarms.get(id=alarm_id)
           # obj=mailInfo(sendDate=datetime.datetime.now(),userMailId=to_addr_list,ackNow=message,subject=subject,event=event)
           # obj.save()
            return {"Status":True,"msg":"Mail Send"}
        except Exception as e:
            return {"status":False,"msg":e}


    def techinvolve_user(self):
        try:
            tech=self.data["tech"]
            id=self.data["case_id"]
            conn = psycopg2.connect("dbname = 'public' user = 'client' host = '172.27.63.162' password = 'root123'")
            cursor = conn.cursor()
            cursor.execute("SELECT * from user where tech={};".format(tech))
            record = cursor.fetchall()
            record=Users.objects.filter(tech=tech)
            for data in record:
                email=data.email
                self.sendmail(id,email)
            caseobj=


        except Exception as e:
            return {"status":False,"msg":e}
