import pandas as pd
import tkinter as tk
from tkinter import *
import tkinter.ttk
import plotly.graph_objects as go

def bitcoin():

    df = pd.read_csv(r"C:\Users\IMMENSE\Downloads\BITCOIN.csv")
    fig = go.Figure(go.Candlestick(
        x=df['Date'],
        open=df['Open'],
        high=df['High'],
        low=df['Low'],
        close=df['Close']
    ))
    fig.show()

def litecoin():
    df = pd.read_csv(r"C:\Users\IMMENSE\Downloads\LITECOIN.csv")
    fig = go.Figure(go.Candlestick(
        x=df['Date'],
        open=df['Open'],
        high=df['High'],
        low=df['Low'],
        close=df['Close']
    ))
    fig.show()

def stellar():
    df = pd.read_csv(r"C:\Users\IMMENSE\Downloads\STELLAR.csv")
    fig = go.Figure(go.Candlestick(
        x=df['Date'],
        open=df['Open'],
        high=df['High'],
        low=df['Low'],
        close=df['Close']
    ))
    fig.show()

def ethereum():
    df = pd.read_csv(r"C:\Users\IMMENSE\Downloads\ETHEREUM.csv")
    fig = go.Figure(go.Candlestick(
        x=df['Date'],
        open=df['Open'],
        high=df['High'],
        low=df['Low'],
        close=df['Close']
    ))
    fig.show()

if __name__=='__main__' :

    window = tk.Tk()
    window.title("CRYPTOCURRENCY DATA ANALYSIS")
    window.geometry('700x400')

    bitcoinimage = PhotoImage(file=r"C:\Users\IMMENSE\Downloads\bitcoin.png")
    litecoinimage = PhotoImage(file=r"C:\Users\IMMENSE\Downloads\litecoin.png")
    stellarimage = PhotoImage(file=r"C:\Users\IMMENSE\Downloads\stellar.png")
    ethereumimage = PhotoImage(file=r"C:\Users\IMMENSE\Downloads\stellar.png")

    label = tk.Label(window, text="BITCOIN")
    label.place(relx=0.4, rely=0.2)
    label.grid(row=100, column=1)
    tk.Button(window, text="view", image=bitcoinimage, command=bitcoin).grid(row=100, column=2)

    label = tk.Label(window, text="LITECOIN")
    label.place(relx=0.4,rely=0.2)
    label.grid(row=200, column=1)
    tk.Button(window, text="view", image = litecoinimage, command=litecoin).grid(row=200, column=2)

    label = tk.Label(window, text="STELLAR")
    label.place(relx=0.4,rely=0.2)
    label.grid(row=300, column=1)
    tk.Button(window, text="view", image = stellarimage, command=stellar).grid(row=300, column=2)

    label = tk.Label(window,text="ETHEREUM")
    label.place(relx=0.4,rely=0.2)
    label.grid(row=400, column=1)
    tk.Button(window, text="view", image=ethereumimage, command=ethereum).grid(row=400, column=2)

    window.mainloop()
