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

'''
def compare(self):
    # Create a new Toplevel window for comparison
    comparison_window = tk.Toplevel(self.window)
    comparison_window.title("Compare Cryptocurrencies")
    comparison_window.geometry('700x400')

    # Add labels and entry widgets for selecting cryptocurrencies
    tk.Label(comparison_window, text="Select Cryptocurrencies to Compare:").grid(row=0, column=0, columnspan=2, pady=10)

    crypto_list = ["Bitcoin", "Litecoin", "Stellar", "Ethereum"]
    selected_cryptos = []

    for i, crypto in enumerate(crypto_list):
        tk.Checkbutton(comparison_window, text=crypto, variable=tk.IntVar(), onvalue=1, offvalue=0,
                       command=lambda c=crypto: self.toggle_crypto_selection(c, selected_cryptos)).grid(row=i + 1, column=0, sticky='w')

    # Button to initiate the comparison
    tk.Button(comparison_window, text="Compare", command=lambda: self.start_comparison(selected_cryptos)).grid(row=len(crypto_list) + 1, column=0, pady=10)

def toggle_crypto_selection(self, crypto, selected_cryptos):
    if crypto in selected_cryptos:
        selected_cryptos.remove(crypto)
    else:
        selected_cryptos.append(crypto)

def start_comparison(self, selected_cryptos):
    if len(selected_cryptos) < 2:
        messagebox.showerror("Error", "Please select at least two cryptocurrencies for comparison.")
    else:
        # Fetch and compare data for selected cryptocurrencies
        comparison_data = []

        for crypto in selected_cryptos:
            file_path = f"C:\\Users\\IMMENSE\\Downloads\\{crypto.upper()}.csv"
            df = self.read_csv(file_path)

            if df is not None:
                comparison_data.append((crypto, df))

        if comparison_data:
            # Plot comparison chart
            fig = go.Figure()

            for crypto, df in comparison_data:
                fig.add_trace(go.Scatter(x=df['Date'], y=df['Close'], mode='lines', name=crypto))

            fig.update_layout(title_text="Cryptocurrency Comparison", xaxis_title="Date", yaxis_title="Closing Price")
            fig.show()
'''
