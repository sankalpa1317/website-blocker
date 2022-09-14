#import module
from tkinter import*

host_path='C:\Windows\System32\drivers\etc\hosts'
ip_address='127.0.0.1'

def block():
    website_list=enter_Website.get(1.0,END)
    Website = list(website_list.split(','))
    with open (host_path,'r+')as host_file:
        file_content=host_file.read()
        for web in Website:
            if web in file_content:
                display=Label(window,text='Already Blocked',font='arial')
                display.place(x=200,y=200)
                # display.after(10,display.Label(window,text='omm',font='arial'))
                # display.place(x=200,y=200)
                
            else:
                host_file.write(ip_address+' '+web)
                Label(window,text='Blocked',font='arial').place(x=200,y=200)

def unblock():
    website_list=enter_Website.get(1.0,END)
    #print(website_un)
    Website = list(website_list.split(','))
    temp_f=''
    with open (host_path,'r+')as host_file:
        file_content=host_file.read()
        #print(file_content)
        for web in Website:
            if web in file_content:
                Label(window,text=web+'UnBlocked\n',font='arial').place(x=350,y=200)
                with open(host_path,'r+') as website_un:
                    for line in website_un:
                        print('Line1 :-'+line)
                        if web in line:
                            temp_un=ip_address+' '+web
                            line=line.replace(temp_un,'')
                        print('line2 :- '+line)     
                        temp_f=temp_f+line

                with open(host_path,'w') as new_file:
                    new_file.write(temp_f);
                    print(temp_f)                    
            else:
                display=Label(window,text='Already UnBlocked',font='arial')
                display.place(x=350,y=200)
        
        # for web in Website:
        #     if web in file_content:
        #         with open (host_path,'r+')as f:
        #             for line in file_content:
        #                 if line.strip(',')!=website_list:
        #                     f.write(line)
    
def close():
    window.destroy()

#to make a window
window=Tk()

#set size of window
window.geometry('650x400')
window.maxsize(750,600)
window.minsize(550,300)

#set title of window
window.title('WEBSITE BLOCKER')

#set Header
Label(window,text='WEBSITE BLOCKER',font=('bold',15),fg='purple').pack()
Label(window,text='Developed By Sankalpa@13',font=('bold',12),fg='purple').pack(side=BOTTOM)

Label(window,text='Enter website :').place(x=100,y=50)
enter_Website = Text(window,font=(10),width=30,height=1)
enter_Website.place(x=200,y=48)

Button(window,text='Block',font=('bold',10),bg='red',fg='white',command=block).place(x=150,y=100)
Button(window,text='Un Block',font=('bold',10),bg='green',fg='white',command=unblock).place(x=270,y=100)
Button(window,text='Exit',font=('bold',10),bg='blue',fg='white',command=close).place(x=400,y=100)
window.mainloop()