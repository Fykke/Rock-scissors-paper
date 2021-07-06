from tkinter import *
import random
#loga izmērs, krase
rpc = Tk() #pats logs
rpc.title('Rock scissors paper')
rpc.geometry('298x246')
rpc.resizable(width=False, height=False)
rpc['bg'] = '#d6eaf8'

#StringVar() - Ļauj izveidot enkuru virknei.

var = StringVar()
comp_var = StringVar()
won_var = StringVar()
my_points = StringVar()
comp_points = StringVar()
winner = StringVar()

n = 5 #spēļu skaits

computer_score = 0
your_score = 0

turns = ['Rock', 'Paper', 'Scissors']

def restart():

    global computer_score #piemērot vērtību visa kodā
    global your_score #piemērot vērtību visa kodā

    computer_score = 0
    your_score = 0
    var.set('')
    comp_var.set('')
    won_var.set('') 
    my_points.set('') 
    comp_points.set('')
    winner.set('')

#funkcija, kura tiek aktivizēta pēc pogas “Rock” nospiešanas
def rock():

    var.set('Rock') #apstiprina manu izvēli "Rock"
    computer_choice = random.choice(turns)  #izvēlieties datoram nejaušu vērtību
    comp_var.set(computer_choice) #apstiprina datora gadījuma izvēli

    global computer_score #piemērot vērtību visa kodā
    global your_score #piemērot vērtību visa kodā

    if computer_choice == 'Rock':
        won_var.set('Tie!') #iestatīt tekstu rpc_won uz “Tie”

    if computer_choice == 'Scissors':
        won_var.set('+1 to You!') #iestatīt tekstu rpc_won uz “You won”
        your_score += 1
        my_points.set(your_score)

    if computer_choice == 'Paper':
        won_var.set('+1 to Computer!') #iestatīt tekstu rpc_won uz “You lose!”
        computer_score += 1
        comp_points.set(computer_score)

    if computer_score == n:
        winner.set('Computer won!') #iestatīt tekstu winner uz “Computer won!”

    if your_score == n:
        winner.set('You won!') #iestatīt tekstu winner uz “You won!”


#funkcija, kura tiek aktivizēta pēc pogas “Scissors” nospiešanas
def scissors():

    var.set('Scissors')
    computer_choice = random.choice(turns)
    comp_var.set(computer_choice)

    global computer_score
    global your_score

    if computer_choice == 'Scissors':
        won_var.set('Tie!')

    if computer_choice == 'Paper':
        won_var.set('+1 to You!')
        your_score += 1
        my_points.set(your_score)


    if computer_choice == 'Rock':
        won_var.set('+1 to Computer!')
        computer_score += 1
        comp_points.set(computer_score)

    if computer_score == n:
        winner.set('Computer won!')

    if your_score == n:
        winner.set('You won!')

#funkcija, kura tiek aktivizēta pēc pogas “Paper” nospiešanas
def paper():

    var.set('Paper')
    computer_choice = random.choice(turns)
    comp_var.set(computer_choice)

    global computer_score
    global your_score

    if computer_choice == 'Paper':
        won_var.set('Tie!')

    if computer_choice == 'Rock':
        won_var.set('+1 to You!')
        your_score += 1
        my_points.set(your_score)

    if computer_choice == 'Scissors':
        won_var.set('+1 to Computer!')
        computer_score += 1
        comp_points.set(computer_score)

    if computer_score == n:
        winner.set('Computer won!')

    if your_score == n:
        winner.set('You won!')

rock_photo = PhotoImage(file = r"rock.png")
scissors_photo = PhotoImage(file = r"scissors.png")
paper_photo = PhotoImage(file = r"paper.png")
restart_photo = PhotoImage(file = r"restart.png")

'''
izvēles pogas
'command=' darbība, kas aktivizē funkciju pēc noklikšķināšanas uz pogas
'(rpc)' parāda, kuram logam pieder logrīks
'''

rpc_rock = Button(rpc, text='Rock', image = rock_photo, font='Helvetica 14 bold', bg='#837B71', width=7, borderwidth=5, command=rock)
rpc_scissors = Button(rpc, text='Scissors', image = scissors_photo, font='Helvetica 14 bold', bg='#56768B', width=8, borderwidth=5, command=scissors)
rpc_paper = Button(rpc, text='Paper', image = paper_photo, font='Helvetica 14 bold', bg='#C2C9CE', width=7, borderwidth=5, command=paper)
rpc_restart = Button(rpc, text='Play Again!', image = restart_photo, compound = TOP, font='Helvetica 10 bold', bg='#1b4f72', width=7, borderwidth=5, command=restart)

'''
logi, kas parāda izvēlēto atbildi, pašreizējo rezultātu un uzvarētāju
'textvariable' saista StringVar objektu ar tekstu vizuala elementa
'padx', 'pady' - atribūti ievilkumam
'Label' - logrīks paredzēts jebkura uzraksta parādīšanai
'''

rpc_computer_score = Label(rpc, width=7, bg='#1f618d', textvariable=comp_var, font='Helvetica 14 bold', padx=5, pady=5, borderwidth=3)
rpc_my_score = Label(rpc, width=7, bg='#1f618d', textvariable=var, font='Helvetica 14 bold', padx=5, pady=5, borderwidth=3)
rpc_won = Label(rpc, width=8, bg='#7fb3d5', textvariable=won_var, font='Helvetica 10 bold', padx=5, pady=5, borderwidth=3) #победитель раунда
rpc_who_won = Label(rpc, width=10, bg='#7fb3d5', textvariable=winner, font='Helvetica 10 bold', padx=5, pady=5, borderwidth=5) #окончательный победитель
rpc_my_points = Label(rpc, width=5, bg='#1f618d', textvariable=my_points, font='Helvetica 18 bold', padx=5, pady=5, borderwidth=5)
rpc_computer_points = Label(rpc, width=5, bg='#1f618d', textvariable=comp_points, font='Helvetica 18 bold', padx=5, pady=5, borderwidth=5)

#vienkāršs teksts, kas palīdzēs jums saprast spēli

you_text = Label(rpc, width=8, bg='#d6eaf8', text='Your answer', font='Helvetica 10 bold', padx=11, pady=5, borderwidth=1)
comp_text = Label(rpc, width=7, bg='#d6eaf8', text='Comps answer', font='Helvetica 10 bold', padx=18, pady=5, borderwidth=1)
score_text = Label(rpc, width=7, bg='#d6eaf8', text='Score', font='Helvetica 10 bold', padx=11, pady=5, borderwidth=1)

#parādot visu logā: pogas, tekstu (rinda='', sleja='') (ряд, ячейка/столб)
#1. rinda
you_text.grid(row = 0, column = 0)
score_text.grid(row = 0, column = 1)
comp_text.grid(row = 0, column = 2)
#2. rinda
rpc_won.grid(row=1, column=1, sticky='nsew')
rpc_my_score.grid(row=1, column=0)
rpc_computer_score.grid(row=1, column=2)
#3 rinda
rpc_rock.grid(row = 2, column=0, sticky='nsew')
rpc_scissors.grid(row = 2, column=1, sticky='nsew')
rpc_paper.grid(row = 2, column=2, sticky='nsew')
#4. rinda
rpc_my_points.grid(row = 3, column = 0, sticky='nsew')
rpc_who_won.grid(row = 3, column = 1, sticky='nsew')
rpc_computer_points.grid(row = 3, column = 2, sticky='nsew')
#5. rinda
rpc_restart.grid(row = 4, column = 0, columnspan=3, sticky='nsew')

#funkcijas un pogu iesiešana, lai pievienotu krāsu
#rodas, kad kursors ienāk vai atstāj logrīka robežas

def on_enterrock(color):
    rpc_rock['background'] = '#A49D94'
def on_leaverock(color):
    rpc_rock['background'] = '#837B71' 
rpc_rock.bind('<Enter>', on_enterrock) #piesaistiet pogu funkcijai
rpc_rock.bind('<Leave>', on_leaverock) #funkcija divu dažādu notikumu apstrādei: '<Enter>', '<Leave>' 

def on_enterscissors(color):
    rpc_scissors['background'] = '#799AAF'
def on_leavescissors(color):
    rpc_scissors['background'] = '#56768B'
rpc_scissors.bind('<Enter>', on_enterscissors)
rpc_scissors.bind('<Leave>', on_leavescissors)

def on_enterpaper(color):
    rpc_paper['background'] = '#E8E9EB'
def on_leavepaper(color):
    rpc_paper['background'] = '#C2C9CE'
rpc_paper.bind('<Enter>', on_enterpaper)
rpc_paper.bind('<Leave>', on_leavepaper)

def on_enterrestart(color):
    rpc_restart['background'] = '#347098'
def on_leaverestart(color):
    rpc_restart['background'] = '#1b4f72'
rpc_restart.bind('<Enter>', on_enterrestart)
rpc_restart.bind('<Leave>', on_leaverestart)

#atvērt spēles logu
rpc.mainloop()