# tkinter is used in python to create GUI 
from tkinter import *
from tkinter import ttk
import requests

def data_get( ):
    
# city_name="jodhpur"
    city = city_name.get()
    # api need atleast 2 hours to get activated so after the program just wait for 2hr and then run
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+ "&appid=8082bcada0dd81af899a17a93b16336f").json()
    w_lable1.config(text = data["weather"] [0] ["main"])
    wd_lable1.config(text= data["weather"] [0] ["description"])
    temp_lable1.config(text=str( int(data["main"] ["temp"]-273.15)))
    pre_lable1.config(text=data["main"] ["pressure"])


win = Tk()
#title name
win.title('Weather prediction')

#win means window colour
win.config(bg="light blue") 

#win box 
win.geometry("500x570")

#textbox indside window
name_lable= Label(win,text="Weather App", font =("Time New Roman ",40,"bold"))

#above textbox locating /spacing 
name_lable.place(x=25,y=50,height=50,width=450)
 
city_name= StringVar()

# a variable list_name stores all states name in INDIA
list_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar",
             "Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh",
             "Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh",
             "Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha",
             "Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura",
             "Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands",
             "Chandigarh","Dadra and Nagar Haveli","Daman and Diu",
             "Lakshadweep","National Capital Territory of Delhi","Puducherry"]


com = ttk.Combobox(win,text="Weather App",  values = list_name,font =("Time New Roman ",30,"bold"),textvariable=city_name)
com.place(x=25,y=120,height=50,width=450)

#styling weather climate box and infont text box to get details from api
w_lable= Label(win,text="Weather Climate", font =("Time New Roman ",15))
w_lable.place(x=25,y=260,height=50,width=210)
w_lable1= Label(win,text="", font =("Time New Roman ",15))
w_lable1.place(x=250,y=260,height=50,width=210)

#styling weather description box and infont text box to get details from api
wd_lable= Label(win,text="Weather Description", font =("Time New Roman ",15))
wd_lable.place(x=25,y=330,height=50,width=210)
wd_lable1= Label(win,text="", font =("Time New Roman ",15))
wd_lable1.place(x=250,y=330,height=50,width=210)

#styling temperature box and infont text box to get details from api
temp_lable= Label(win,text="Temperature", font =("Time New Roman ",15))
temp_lable.place(x=25,y=400,height=50,width=210)
temp_lable1= Label(win,text="", font =("Time New Roman ",15))
temp_lable1.place(x=250,y=400,height=50,width=210)

#styling pressure box and infont text box to get details from api
pre_lable= Label(win,text=" Atmospheric Pressure", font =("Time New Roman ",15))
pre_lable.place(x=25,y=470,height=50,width=210)
pre_lable1= Label(win,text="", font =("Time New Roman ",15))
pre_lable1.place(x=250,y=470,height=50,width=210)

#about button atlast call function to get data from api
done_button = Button(win,text="Done",font =("Time New Roman ",20,"bold"),command= data_get)
done_button.place(x=200,y=190,height=50,width=100)

win.mainloop()