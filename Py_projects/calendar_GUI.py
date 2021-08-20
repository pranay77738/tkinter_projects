from tkinter import *
from calendar import calendar

# fuction to show the calender of the year
def showCalendar():
    cal=Tk()
    cal.config(background='grey')
    cal.title('Calendar of the year')
    # cal.geometry("550x600")
    year=int(year_field.get())
    cal_content=calendar(year)
    calYear=Label(cal,text=cal_content,font='Consolas 10 bold')
    calYear.grid(row=5,column=1,padx=20)
    cal.mainloop()




if __name__ == "__main__":
    new=Tk()
    new.config(background='grey')
    new.title('Calendar')
    new.geometry("250x140")
    new_cal = Label(new, text="Calender",bg='grey',font=("times", 28, "bold"))
    new_year = Label(new, text="Enter year", bg='dark grey')
    year_field=Entry(new)
    button = Button(new, text='Show Calender',
                    fg='Black',bg='Blue',command=showCalendar)
    Exit= Button(new, text="Exit", command=new.destroy)

    #putting widgets in position
    new_cal.grid(row=1, column=1)
    new_year.grid(row=2, column=1)
    year_field.grid(row=3, column=1)
    button.grid(row=4, column=1)
    Exit.grid(row=6, column=1)
    new.mainloop()


