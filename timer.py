import tkinter as tk
import time

window=tk.Tk()
window.title("인터벌 타이머")
window.geometry("640x400+100+100")

setting = tk.Frame(window)
counter = tk.Frame(window)

setting.place(relx=0, rely=0, relwidth=1, relheight=1)
counter.place(relx=0, rely=0, relwidth=1, relheight=1)
setting.tkraise()

#세트 표시
set_hmc = 0

def setcount_up():
    global set_hmc
    set_hmc += 1
    set.config(text=set_hmc)
    #setting.after(100, setcount_up)

def setcount_down():
    global set_hmc
    if set_hmc != 0:
        set_hmc -= 1
        set.config(text=set_hmc)
        #setting.after(100, setcount_down)

set_exp = tk.Label(setting, text="세트", width=10, height=5)
set = tk.Label(setting, text=set_hmc, width=10, height=5)
set_up = tk.Button(setting, text="+", command=setcount_up)
set_down = tk.Button(setting, text="-", command=setcount_down)

set_exp.place(x=320,y=50)
set.place(x=320,y=100)
set_up.place(x=50,y=100)
set_down.place(x=590,y=100)


#운동 시간 표시
exz_sec = 0

def exzcount_up():
    global exz_sec
    global exz_hmc
    exz_sec += 1
    exz_hmc = f'{exz_sec//60:02d}:{exz_sec%60:02d}'
    exz.config(text=exz_hmc)
    #setting.after(100, exzcount_up)

def exzcount_down():
    global exz_sec
    global exz_hmc
    if exz_sec != 0:
        exz_sec -= 1
        exz_hmc = f'{exz_sec//60:02d}:{exz_sec%60:02d}'
        exz.config(text=exz_hmc)
        #setting.after(100, exzcount_down)

exz_hmc = f'{exz_sec//60}:{exz_sec%60}'

exz_exp = tk.Label(setting, text="운동", width=10, height=5)
exz = tk.Label(setting, text=exz_hmc, width=10, height=5)
exz_up = tk.Button(setting, text="+", command=exzcount_up)
exz_down = tk.Button(setting, text="-", command=exzcount_down)

exz_exp.place(x=320,y=150)
exz.place(x=320,y=200)
exz_up.place(x=50,y=200)
exz_down.place(x=590,y=200)

#휴식 시간 표시
rest_sec = 0
rest_hmc = f'{rest_sec//60}:{rest_sec%60}'

def restcount_up():
    global rest_sec
    global rest_hmc
    rest_sec += 1
    rest_hmc = f'{rest_sec//60:02d}:{rest_sec%60:02d}'
    rest.config(text=rest_hmc)
    #setting.after(100, restcount_up)

def restcount_down():
    global rest_sec
    global rest_hmc
    if rest_sec != 0:
        rest_sec -= 1
        rest_hmc = f'{rest_sec//60:02d}:{rest_sec%60:02d}'
        rest.config(text=rest_hmc)
        #setting.after(100, restcount_down)


rest_exp = tk.Label(setting, text="휴식", width=10, height=5)
rest = tk.Label(setting, text=rest_hmc, width=10, height=5)
rest_up = tk.Button(setting, text="+", command=restcount_up)
rest_down = tk.Button(setting, text="-", command=restcount_down)

rest_exp.place(x=320,y=250)
rest.place(x=320,y=300)
rest_up.place(x=50,y=300)
rest_down.place(x=590,y=300)

#실행 버튼
def execute():
    set_count = set_hmc
    cur_set.config(text=set_count)
    counter.tkraise()
    counting()


exct = tk.Button(setting, text="실행", command=execute)
exct.place(x=320,y=350)

###############################################counter로 시간재기##########################################
set_count = 0
cur = 5


cur_set = tk.Label(counter, text=set_count, width=10, height=5)
cur_what = tk.Label(counter, text='준비', width=10, height=5)
cur_time = tk.Label(counter, text=f'{cur//60}:{cur%60}', width=10, height=5)

cur_set.place(x=320,y=50)
cur_what.place(x=320,y=100)
cur_time.place(x=320,y=200)

def counting():
    global set_count
    global cur

    if set_count > 0:
        cur_set.config(text=set_count)

        if set_count == set_hmc:  # give user time to get ready on the first set
            countdown()

        cur = exz_sec
        cur_what.config(text='exercise')
        countdown()

        cur = rest_sec
        cur_what.config(text='rest')
        countdown()

        set_count -= 1

        window.after(1000, counting)  # schedule the counting function after 1000 milliseconds

    if set_count == 0:
        setting.tkraise()

def countdown():
    global cur
    if cur > 0:
        cur_time.config(text=f'{cur//60:02d}:{cur%60:02d}')
        cur -= 1
        window.after(1000, countdown)

window.mainloop()