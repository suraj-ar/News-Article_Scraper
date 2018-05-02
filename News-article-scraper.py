from tkinter import *
import tkinter.messagebox
from newspaper import Article
from bs4 import BeautifulSoup
import urllib.request
from urllib.request import urlopen

import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
import pandas as pd

arr=[]
arr1=[]

def changeLabel():


    master = Tk()
    Label(master, text="Article Number").grid(row=0)
    e1 = Entry(master)
    e1.grid(row=0, column=1)

    def printval():
        st=e1.get()
        list_comma=st.split(",")
        list_of_articles=list(map(int, list_comma))
        print("Article Number %s" % (e1.get()))
        arrstore.append(e1.get())
        #print (list_of_articles)
        for i in list_of_articles:
            a = Article(arr1[i], language='en')
            a.download()
            a.parse()
            print(a.title)
            print(a.text)
            print("----------------------------")
            
""" def linear():
        dataset1 = pd.read_csv("C:\\Users\\Suraj\\Desktop\\rainfall.csv")

        npMatrix1 = np.matrix(dataset1)
        X,Y = npMatrix1[:,0],npMatrix1[:,1]

        regression1 = linear_model.LinearRegression()
        regression1.fit(X,Y)
        x = [int(X[0]),int(X[3])]
        y = [int(regression1.predict(X[0])),int(regression1.predict(X[3]))]

        plt.scatter(X,Y)
        plt.plot(x,y)
        plt.show()

        #print(regression1.predict(0))

        dataset2 = pd.read_csv("C:\\Users\\Suraj\\Desktop\\days_of_rainfall.csv")

        npMatrix2 = np.matrix(dataset2)
        U,V = npMatrix2[:,0],npMatrix2[:,1]

        regression2 = linear_model.LinearRegression()
        regression2.fit(U,V)
        u = [int(U[0]),int(U[3])]
        v = [int(regression2.predict(U[0])),int(regression2.predict(U[3]))]

        plt.scatter(U,V)
        plt.plot(u,v)
        plt.show()


        
    
    Button(master, text='Get Article', command=printval).grid(row=3, column=0, sticky=W, pady=4)
    Button(master, text = 'regression model',command = linear).grid(row=4, column=0, sticky=W, pady=4)"""




def change_dropdown():
    app2 = Tk()
    app2.title("Select the Articles")
    
   #with open("C:\\Users\\Suraj\\v.csv") as f:
                    
 #arr.append(line.split()[0])
    
    with open('C:\\Users\\Suraj\\k.csv', 'r') as rf:
        reader = csv.reader(rf, delimiter=',')
        for row in reader:
              arr.append(row[1])
    with open('C:\\Users\\Suraj\\k.csv', 'r') as rf:
        reader = csv.reader(rf, delimiter=',')
        for row in reader:
              arr1.append(row[0])

    length=len(arr)
    for x in range(len(arr)):
        q = Label(app2, text=x, textvariable=x)
        w = Label(app2, text=arr[x], textvariable=arr[x])
        #r = Label(app2)
        
 #       q.pack(side="left")
#        w.pack(side="left")


        q.grid(column=0, row=x)
        w.grid(column=1, row=x)


        
    button1 = Button(app2, text="Click Here", width=20,command=changeLabel)
    button1.grid(column=3,padx=15,pady=15)



def int_window(*args):
    app3 = Tk()
    app3.title("initiate Scraping")
    
    button1 = Button(app3, text="Scrape articles", width=20,command=change_dropdown)
    button1.grid(column=3,padx=15,pady=15)









app = Tk()
app.title("Self Study")

arrstore=[]

copyright_symbol = u"\u00A9"
w = Label(app, text="Hello user. \n Welcome to Dengone %s \n Please select from the list below. \n" % copyright_symbol)
w.pack(pady=0)
w.configure(background='#33B0F5')
w.pack()

mainframe = Frame(app)
#mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.pack(pady = 100, padx = 100)
app.configure(background="#000000")

# Create a Tkinter variable
tkvar = StringVar(app)
 
# Dictionary with options
choices = { 'dengue'}
tkvar.set('dengue') # set the default option
 
popupMenu = OptionMenu(mainframe, tkvar, *choices)
Label(mainframe, text="Choose a disease").grid(row = 1, column = 1)
popupMenu.grid(row = 2, column =1)

z = Label(app, text="Rohitraj Hindupur \n Krishna Sridhar \n Suraj AR \n")
z.pack(pady=0, anchor='e')
z.configure(background='#33B0F5')
z.pack()

# link function to change dropdown
tkvar.trace('w', int_window)
app.mainloop()
