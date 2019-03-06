#coding:utf-8
import win32com.client as win32
import warnings
import pythoncom
import sys
import smtplib
from email.mime.text import MIMEText
class SendEmail:
      reload(sys)
      warnings.filterwarnings('ignore')
      email_host = "https://owasz.yff.com/ews/exchange.asmx"
      send_user = "nan.wei@yff.com"
      password = "wonder5566"
      def send_mail(self,user_list,sub,content):
         '''
         user = "weinannan"+"<"+self.send_user+">"
         message = MIMEText(content,_subtype='plain',_charset='utf-8')
         message['Subject'] = sub
         message['From'] = user
         message['To'] = ";".join(user_list)
         server = smtplib.SMTP_SSL(self.email_host,443)
         server.connect(self.email_host)
         server.login(self.send_user,self.password)
         server.sendmail(self.send_user,user_list,message.as_string())
         server.close()
         '''
         outlook = win32.Dispatch('outlook.application')
         receivers = user_list
         mail = outlook.CreateItem(0)
         mail.To = receivers[0]
         mail.Subject = sub.decode('utf-8')
         mail.Body = content.decode('utf-8')
         mail.Send()
      def send_main(self,pass_list,fail_list):
         pass_num = float(len(pass_list))
         fail_num = float(len(fail_list))
         count_num = pass_num+fail_num
         #90%
         pass_result = "%.2f%%" %(pass_num/count_num*100)
         fail_result = "%.2f%%" %(fail_num/count_num*100)
         user_list = ['nan.wei@yff.com']
         sub = u"接口自动化测试报告"
         content = u"此次一共运行接口个数为%s个，通过个数为%s个，失败个数为%s,通过率为%s,失败率为%s" %(count_num,pass_num,fail_num,pass_result,fail_result )
         self.send_mail(user_list,sub,content)
if __name__ == '__main__':
     sen = SendEmail()
     sen.send_main([1,2,3,4],[5,6,7,8])