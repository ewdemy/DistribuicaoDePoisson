from tkinter import *

def fat(n):
    for i in range(n -1):
        n += n * i
    if n > 0:
        return n
    else:
        return 1
   
x = 2
m = 10

#p = ((m**x) * (2.7183**(-m))) / fat(x)
#p = ((m**x) * (2.7183**(-m))) / fat(x)
#print("A probabilidade é: %.4f"%p)


def bt_click():
      x = int(ent1.get())
      m = float(ent2.get())
      p = ((m**x) * (2.7183**(-m))) / fat(x)
      #print("A probabilidade é: %.4f"%p)
      lb3["text"] = ("A probabilidade é: %.4f"%p)
      lb3["bg"] ="green"

def limpar():
      ent1.delete(0,10)
      ent2.delete(0,10)


janela = Tk()
janela.title("Distribuição de Poissson")
lb = Label(janela, text="Distribuição de Poisson", font=("Verdana",12,"bold"))
lb.place(x=45, y=30)

lb1 = Label(janela, text="Valor(X):")
lb1.place(x=30, y=75)

lb2 = Label(janela, text="Média:")
lb2.place(x=30, y=120)

lb3 = Label(janela, text="",font=("bold"))
lb3.place(x=60, y=160)

ent1 = Entry(janela)
ent1.place(x=85, y=75)

ent2 = Entry(janela)
ent2.place(x=85, y=120)


btcalc = Button(janela, width=15, text="Calcular", command=bt_click)
btcalc.place(x=30,y=200)

btlimpar = Button(janela, width=15, text="Limpar", command=limpar)
btlimpar.place(x=155,y=200)





janela.geometry("300x250+600+300")
janela.mainloop()

