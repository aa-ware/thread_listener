import vk, vk_api

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup

from kivy.graphics import Color

class Groups(object):
    def getGroupNames(self):
        group_info_list=api.groups.getById(group_ids=api.groups.get())
        return group_info_list

class Login():
    parent=Widget()
    login=''
    password=''
    token=''
    code=''

    def two_step_auth_handler(self):
        '''TODO: GUI input'''
        self.code=input('input SMS-code:')
        return self.code, False

    def trylogin(self,email,password):
        vk_session = vk_api.VkApi(email, password, auth_handler=self.two_step_auth_handler())
        try:
            vk_session.authorization(True)
        except vk_api.AuthorizationError as error_msg:
            print(error_msg)
            return ''
        return vk_session.token

    def loginScreen(self):
        login_label=Label(text='Login/Phone number:',center_x=Window.width/6,center_y=Window.height/1.1)
        self.parent.add_widget(login_label)
        loginForm = TextInput(multiline=False,
                              center_x=Window.width/2,
                              center_y=Window.height/1.3,
                              width=Window.width/1.1,
                              height=Window.height/10)
        loginForm.bind(text=self.loginInput)
        self.parent.add_widget(loginForm)
        password_label=Label(text='Password:',
                             center_x=Window.width/8.2,
                             center_y=Window.height/1.7)
        self.parent.add_widget(password_label)
        passwordForm = TextInput(password=True,
                                 multiline=False,
                                 center_x=Window.width/2,
                                 center_y=Window.height/2,
                                 width=Window.width/1.1,
                                 height=Window.height/10)
        passwordForm.bind(text=self.passwordInput)
        self.parent.add_widget(passwordForm)
        submit_button=Button(text='Submit' ,
                             center_x=Window.width/2,
                             center_y=Window.height/4,
                             width=Window.width/1.1,
                             height=Window.height/10)
        submit_button.bind(on_press=self.checkLogin)
        self.parent.add_widget(submit_button)
        return self.parent

    def loginInput(self,instance,value):
        self.login=value

    def passwordInput(self,instance,value):
        self.password=value

    def codeInput(self,instance,value):
        self.code=value

    def checkLogin(self,instance):
        self.token=self.trylogin(self.login,self.password)
        if self.token=='':
            print('fail')
        else:
            print('success')

class MyApp(App):
    def build(self):
        parent=Login().loginScreen()
        return parent

def main():
    aGroups=Groups()
    aApp=MyApp()
    aApp.run()

if __name__ == '__main__':
    main()