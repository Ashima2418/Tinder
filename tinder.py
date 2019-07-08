from tkinter import *
import mysql.connector

class login():

#initiates the connection bitweem sql and python intrepretor

        def __init__(self):

            try:
                self.conn=mysql.connector.connect(host='localhost',user='root',password='',database='tinder')
                self.mycursor=self.conn.cursor()
            except Exception as  ProgrammingError:
                print('Cant connect to database. Try again')
                self.conn='Undefined'
                self.mycursor='Undefined'
                self.Login()



#login screen main frame

        def Login(self):

            self.root=Tk()
            self.root.wm_iconbitmap("tinder.ico")
            x=StringVar()
            y=StringVar()

            self.lable=Label(self.root,text='WELCOME TO TINDER ').grid(row=0,column=1)

            self.blank=Label(self.root, text='-------------------------').grid(row=1, column=1)

            self.email_label=Label(self.root,text='Email').grid(row=2,sticky=W,padx=4)

            self.email_input1=Entry(self.root,textvariable=x).grid(row=2,column=1,sticky=E,padx=4)

            self.password_label = Label(self.root, text='Password').grid(row=3,column=0,sticky=W,padx=4)

            self.password_input1 = Entry(self.root,textvariable=y).grid(row=3,column=1,sticky=E,padx=4)

            self.button=Button(self.root,text='Login',fg='white',bg='Green',command=lambda :self.checklogin(x.get(),y.get())).grid(row=4,padx=4)

            self.notregister = Label(self.root, text='Not Registered !!!').grid(row=5,column=1)

            self.rbutton = Button(self.root, text='Register', fg='white', bg='black', command=lambda: self.register()).grid(row=6,column=1)


            self.root.title('Tinder')
            self.root.minsize(220,190)
            self.root.maxsize(220,190)

            self.root.mainloop()



#checks for login credentials shows up the logged in page and if wrong credentials shows error

        def checklogin(self,email,password):
            self.mycursor.execute("""SELECT * FROM `users` WHERE `email` LIKE '{}' AND `password` LIKE '{}'""".format(email, password))
            user_list = self.mycursor.fetchall()

            if (len(user_list) > 0):
                self.current_user_id = user_list[0][0]
                self.user_menu()
            else:
                self.wrongcredentials()


        def wrongcredentials(self):
            self.root.destroy()
            root5=Tk()
            root5.title('Tinder')
            invalid = Label(root5, text='   Invalid Credentials !!').grid(row=0)
            empty = Label(root5, text='').grid(row=1)
            backbutton = Button(root5, text='Try Again', fg='White', bg='Red',
                    command=lambda: self.back1(root5)).grid(row=2, padx=4)
            root5.wm_iconbitmap("tinder.ico")
            root5.maxsize(130, 80)
            root5.minsize(130, 80)





        def user_menu(self):

            self.root.destroy()
            self.root6=Tk()
            self.root6.title('Tinder')
            self.root6.wm_iconbitmap("tinder.ico")
            u = StringVar()
            name_label = Label(self.root6, text='How would you like to proceed  ').grid(row=0, padx=4)
            empty = Label(self.root6, text='').grid(row=1)

            alluser = Label(self.root6, text='1. View All Users').grid(row=3)
            alluser = Label(self.root6, text='2. View requested').grid(row=4)
            alluser = Label(self.root6, text='3. View proposals').grid(row=5)
            alluser = Label(self.root6, text='4. View matches').grid(row=6)
            alluser = Label(self.root6, text='5. Logout').grid(row=7)
            empty = Label(self.root6, text='').grid(row=8)
            empty = Label(self.root6, text='-----------------------------------------------------').grid(row=9)
            user_input1 = Entry(self.root6, textvariable=u).grid(row=10,sticky=E, padx=4)
            submitbutton=Button(self.root6,text='Proceed',fg='white',bg='green',command=lambda:
                                                self.user_menu_input(u.get())).grid(row=11, sticky=E, padx=4)

        def user_menu_input(self,user_input):
            if user_input == '1':
                self.view_users()
            elif user_input == '2':
                self.view_requested()
            elif user_input == '3':
                self.view_proposals()
            elif user_input == '4':
                self.view_matches()
            elif user_input=='5':
                self.current_user_id = 0
                self.root6.destroy()
                root7=Tk()
                root7.title('Tinder')
                root7.wm_iconbitmap("tinder.ico")
                blank1 = Label(root7, text='Successfully Logged Out', fg='white', bg='black').grid(row=0, padx=20)
                submitbutton = Button(root7, text='OKAY', fg='black', bg='yellow',command=lambda :self.back1(root7)).grid(row=1, padx=4)





        def view_users(self):
            self.root6.destroy()
            root8=Tk()
            root8.title('Tinder')
            root8.wm_iconbitmap("tinder.ico")
            option=StringVar()
            self.mycursor.execute("""SELECT * FROM `users` WHERE `user_id` NOT LIKE '{}'""".format(self.current_user_id))
            all_users = self.mycursor.fetchall()
            blank1 = Label(root8, text='ALL USERS', fg='white', bg='orange').grid(row=0,column=2,sticky=E,padx=20)
            empty = Label(root8, text='').grid(row=1)
            empty = Label(root8, text='USER-ID').grid(row=2,column=0)
            empty = Label(root8, text='NAME').grid(row=2,column=1)
            empty = Label(root8, text='GENDER').grid(row=2,column=2)
            empty = Label(root8, text='AGE').grid(row=2,column=3)
            empty = Label(root8, text='PLACE').grid(row=2, column=4)
            j=4
            for i in all_users:
                if i[0]!=self.current_user_id:
                    userlabel=Label(root8,text=i[0]).grid(row=j,column=0)
                    userlabel = Label(root8, text=i[1]).grid(row=j, column=1)
                    userlabel = Label(root8, text=i[4]).grid(row=j, column=2)
                    userlabel = Label(root8, text=i[5]).grid(row=j, column=3)
                    userlabel = Label(root8, text=i[6]).grid(row=j, column=4)
                j=j+1

            empty = Label(root8, text='').grid(row=j + 1)
            empty = Label(root8, text='Propose id : ').grid(row=j+2, column=2)
            name_input = Entry(root8, textvariable=option).grid(row=j+2, column=3, sticky=E, padx=4)
            empty = Label(root8, text='').grid(row=j+4)
            backbutton=Button(root8,text='Back',bg='green',fg='white',command=lambda :self.back2(root8)).grid(row=j+5,column=0)
            submitbutton=Button(root8,text='Propose',bg='green',fg='white',command=lambda :self.propose(self.current_user_id, option.get(),root8)).grid(row=j+5,column=4)






        def propose(self, romeo_id, julliet_id,root8):
            root8.destroy()
            root9=Tk()
            root9.title('Tinder')
            root9.wm_iconbitmap("tinder.ico")
            self.mycursor.execute(
                """SELECT * FROM `proposals` WHERE `romeo_id` LIKE '{}' AND `julliet_id` LIKE '{}'""".format(romeo_id,
                                                                                                     julliet_id))
            lista = self.mycursor.fetchall()

            if len(lista) != 0:
                label_ca=Label(root9,text="You've already proposed this user.....").grid(row=0)
                button=Button(root9,text="OKAY",fg='white',bg='yellow',command=lambda :self.back2(root9)).grid(row=1)

            else:
                self.mycursor.execute(
                    """INSERT INTO `proposals` (`proposal_id`,`romeo_id`,`julliet_id`) VALUES (NULL ,'{}','{}')"""
                    .format(romeo_id, julliet_id))
                self.conn.commit()

                label_ca=Label(root9,text="Proposal sent successfully..... Fingers Crossed!!").grid(row=0)
                button=Button(root9,text="OKAY",fg='white',bg='yellow',command=lambda :self.back2(root9)).grid(row=1)





        def back2(self,root8):
            root8.destroy()
            self.root=Tk()
            self.user_menu()




        def view_requested(self):
            self.root6.destroy()
            root8 = Tk()
            root8.title('Tinder')
            root8.wm_iconbitmap("tinder.ico")
            option = StringVar()
            self.mycursor.execute("""SELECT * FROM `proposals` p JOIN `users` u ON p.`julliet_id`=u.`user_id`
                                                            WHERE p.`romeo_id` LIKE '{}'""".format(
                self.current_user_id))

            requested_user_list = self.mycursor.fetchall()
            blank1 = Label(root8, text='REQUESTED USERS', fg='white', bg='orange').grid(row=0, column=2, sticky=E, padx=20)
            empty = Label(root8, text='').grid(row=1)
            empty = Label(root8, text='USER-ID').grid(row=2, column=0)
            empty = Label(root8, text='NAME').grid(row=2, column=1)
            empty = Label(root8, text='GENDER').grid(row=2, column=2)
            empty = Label(root8, text='AGE').grid(row=2, column=3)
            empty = Label(root8, text='PLACE').grid(row=2, column=4)
            j = 4
            for i in requested_user_list:
                userlabel = Label(root8, text=i[3]).grid(row=j, column=0)
                userlabel = Label(root8, text=i[4]).grid(row=j, column=1)
                userlabel = Label(root8, text=i[7]).grid(row=j, column=2)
                userlabel = Label(root8, text=i[8]).grid(row=j, column=3)
                userlabel = Label(root8, text=i[9]).grid(row=j, column=4)
                j = j + 1

            empty = Label(root8, text='').grid(row=j + 1)
            backbutton = Button(root8, text='Back', bg='green', fg='white', command=lambda: self.back2(root8)).grid(
                                    row=j + 5, column=0)


        def view_proposals(self):
            self.root6.destroy()
            root8 = Tk()
            root8.title('Tinder')
            root8.wm_iconbitmap("tinder.ico")
            option = StringVar()
            self.mycursor.execute("""SELECT * FROM `users` u JOIN `proposals` p ON p.`romeo_id`=u.`user_id`
                            WHERE p.`julliet_id` LIKE '{}'""".format(self.current_user_id))

            proposals_list = self.mycursor.fetchall()
            blank1 = Label(root8, text='USERS PROPOSED', fg='white', bg='orange').grid(row=0, column=2, sticky=E,
                                                                                        padx=20)
            empty = Label(root8, text='').grid(row=1)
            empty = Label(root8, text='USER-ID').grid(row=2, column=0)
            empty = Label(root8, text='NAME').grid(row=2, column=1)
            empty = Label(root8, text='GENDER').grid(row=2, column=2)
            empty = Label(root8, text='AGE').grid(row=2, column=3)
            empty = Label(root8, text='PLACE').grid(row=2, column=4)
            j = 4
            for i in proposals_list:
                userlabel = Label(root8, text=i[0]).grid(row=j, column=0)
                userlabel = Label(root8, text=i[1]).grid(row=j, column=1)
                userlabel = Label(root8, text=i[4]).grid(row=j, column=2)
                userlabel = Label(root8, text=i[5]).grid(row=j, column=3)
                userlabel = Label(root8, text=i[6]).grid(row=j, column=4)
                j = j + 1

            empty = Label(root8, text='').grid(row=j + 1)
            backbutton = Button(root8, text='Back', bg='green', fg='white', command=lambda: self.back2(root8)).grid(
                row=j + 5, column=0)


        def view_matches(self):
            self.root6.destroy()
            root8 = Tk()
            root8.title('Tinder')
            root8.wm_iconbitmap("tinder.ico")
            option = StringVar()

            self.mycursor.execute(
                """SELECT `julliet_id` FROM `proposals` WHERE `romeo_id` LIKE '{}'""".format(self.current_user_id))
            requested_list = self.mycursor.fetchall()
            self.mycursor.execute(
                """SELECT `romeo_id` FROM `proposals` WHERE `julliet_id` LIKE '{}'""".format(self.current_user_id))
            asked_list = self.mycursor.fetchall()
            match_id = []

            for i in requested_list:
                for j in asked_list:
                    if i == j:
                        match_id.append(i[0])

            match_list = []
            for i in match_id:
                self.mycursor.execute("""SELECT * FROM `users` WHERE `user_id` LIKE '{}'""".format(i))
                x = self.mycursor.fetchall()
                match_list.append(x[0])

            blank1 = Label(root8, text='USERS MATCHES', fg='white', bg='orange').grid(row=0, column=2, sticky=E,
                                                                                       padx=20)
            empty = Label(root8, text='').grid(row=1)
            empty = Label(root8, text='USER-ID').grid(row=2, column=0)
            empty = Label(root8, text='NAME').grid(row=2, column=1)
            empty = Label(root8, text='GENDER').grid(row=2, column=2)
            empty = Label(root8, text='AGE').grid(row=2, column=3)
            empty = Label(root8, text='PLACE').grid(row=2, column=4)
            j = 4
            for i in match_list:
                userlabel = Label(root8, text=i[0]).grid(row=j, column=0)
                userlabel = Label(root8, text=i[1]).grid(row=j, column=1)
                userlabel = Label(root8, text=i[4]).grid(row=j, column=2)
                userlabel = Label(root8, text=i[5]).grid(row=j, column=3)
                userlabel = Label(root8, text=i[6]).grid(row=j, column=4)
                j = j + 1

            empty = Label(root8, text='').grid(row=j + 1)

            backbutton = Button(root8, text='Back', bg='green', fg='white', command=lambda: self.back2(root8)).grid(
                row=j + 5, column=0)




        def check(self,email,password):
            self.mycursor.execute("""SELECT * FROM `users` WHERE `email` LIKE '{}' AND `password` LIKE '{}'""".format(email,password))
            user_list=self.mycursor.fetchall()

            if(len(user_list)>0):
                return 1
            else:
                return 0



        def register(self):
            self.root.destroy();
            self.root1 = Tk()
            self.root1.wm_iconbitmap("tinder.ico")
            name = StringVar()
            email = StringVar()
            password = StringVar()
            gender = StringVar()
            age = StringVar()
            city = StringVar()

            blank1 = Label(self.root1, text='Registration', fg='white', bg='black').grid(row=0, column=0, padx=20)

            name_label = Label(self.root1, text='Enter your Name : ').grid(row=1, column=0, sticky=W, padx=4)
            name_input = Entry(self.root1, textvariable=name).grid(row=1, column=1, sticky=E, padx=4)

            email_label = Label(self.root1, text='Enter your Email : ').grid(row=2, column=0, sticky=W, padx=4)
            email_input = Entry(self.root1, textvariable=email).grid(row=2, column=1, sticky=E, padx=4)

            password_label = Label(self.root1, text='Enter your Password : ').grid(row=3, column=0, sticky=W, padx=4)
            password_input = Entry(self.root1, textvariable=password).grid(row=3, column=1, sticky=E, padx=4)

            gender_label = Label(self.root1, text='Enter your Gender : ').grid(row=4, column=0, sticky=W, padx=4)
            gender_input = Entry(self.root1, textvariable=gender).grid(row=4, column=1, sticky=E, padx=4)

            age_label = Label(self.root1, text='Enter your Age : ').grid(row=5, column=0, sticky=W, padx=4)
            age_input = Entry(self.root1, textvariable=age).grid(row=5, column=1, sticky=E, padx=4)

            city_label = Label(self.root1, text='Enter your City : ').grid(row=6, column=0, sticky=W, padx=4)
            city_input = Entry(self.root1, textvariable=city).grid(row=6, column=1, sticky=E, padx=4)

            registerbutton = Button(self.root1, text='Register', fg='white', bg='black', command=lambda:
            self.userregister(name.get(), email.get(), password.get(), gender.get(), age.get(), city.get())).grid(row=7,column=1,padx=4)

            notregister = Label(self.root1, text='Registered !!!').grid(row=8)

            backbutton=Button(self.root1,text='Login Now !!!',fg='White',bg='Green',command=lambda :self.back(self.root1)).grid(row=9,padx=4)

            self.root1.title('Tinder')
            self.root1.minsize(270, 230)
            self.root1.minsize(270, 230)
            self.root1.mainloop()




        def check_email(self, email):
            self.mycursor.execute("""SELECT * FROM `users` WHERE `email` LIKE '{}'""".format(email))
            already_user_list = self.mycursor.fetchall()
            if (len(already_user_list) == 1):
                return 1
            else:
                return 0




        def userregister(self, name, email, password, gender, age, city):
            if (self.check_email(email) == 1):
                self.root1.destroy()
                root4=Tk()
                root4.maxsize(210,80)
                root4.minsize(210,80)
                root4.wm_iconbitmap("tinder.ico")
                root4.title('Tinder')
                blank1 = Label(root4, text='  Try login OR use anther email id !! :) ', fg='white', bg='black').grid(row=0)
                empty = Label(root4, text='').grid(row=1)
                backbutton = Button(root4, text='Back to Login Now !!!', fg='White', bg='Green',
                                    command=lambda: self.back1(root4)).grid(row=2, padx=4)


            else:
                self.mycursor.execute("""INSERT INTO `users`(`user_id`,`name`,`email`,`password`,`gender`,`age`,`city`)
                                  VALUES(NULL ,'{}','{}','{}','{}','{}','{}')""".format(name, email, password,
                                                                                        gender,
                                                                                        age, city))
                self.conn.commit()
                self.root1.destroy()
                root4 = Tk()
                root4.maxsize(150, 80)
                root4.minsize(150, 80)
                root4.wm_iconbitmap("tinder.ico")
                root4.title('Tinder')
                blank1 = Label(root4, text='Registration Successful', fg='white', bg='black').grid(
                    row=0)
                backbutton = Button(root4, text='Back to Login Now !!!', fg='White', bg='Green',
                                    command=lambda: self.back1(root4)).grid(row=2, padx=4)




        def back1(self,root4):
            root4.destroy()
            self.Login()




        def back(self,root1):
            self.root1.destroy()
            self.Login()






obj=login()
obj.Login()
