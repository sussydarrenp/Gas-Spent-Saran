
# #CODE1

# # 1 wallet address, 1 chain, 1 month


# import firebase_admin
# from firebase_admin import credentials, firestore
# import matplotlib.pyplot as plt
# import random
# import numpy as np

# # Initialize Firebase (if not initialized)
# credpath = "gasspent-firebase-adminsdk-kht62-2a8e40aed1.json"
# login = credentials.Certificate(credpath)
# firebase_admin.initialize_app(login)

# # Initialize Firestore
# db = firestore.client()

# def fetch_data(wallet_address, chain, month):
#     doc_ref = db.collection("accounts").document(wallet_address)
    
#     try:
#         doc = doc_ref.get()
#         data = doc.to_dict()
#         if data:
#             if "chains" in data and chain in data["chains"]:
#                 chain_data = data["chains"][chain]
#                 if month in chain_data:
#                     month_data = chain_data[month]
#                     return month_data
#     except Exception as e:
#         print(f"Error fetching data: {e}")
    
#     return None

# def create_bar_chart(wallet_address, chain, month):
#     data = fetch_data(wallet_address, chain, month)
#     if data:
#         days = list(data.keys())
#         fees = [data[day] for day in days]
        
#         # Generate random colors for each bar
#         num_bars = len(days)
#         bar_colors = [np.random.rand(3,) for _ in range(num_bars)]
        
#         plt.bar(days, fees, color=bar_colors)
#         plt.xlabel("Day of Month")
#         plt.ylabel("Gas Fees (USDT)")
#         plt.title(f"Gas Fees for {wallet_address} on {chain} in {month}")
#         plt.show()
#     else:
#         print("Data not found for the selected wallet address, chain, and month.")

# wallet_address = "0x14880Ab225cF9d2Fda3F95Ce0B983267A241247e"
# chain = "arbitrum-mainnet"
# month = "July"

# create_bar_chart(wallet_address, chain, month)

# CODE1

# 1 wallet address, 1 chain, 1 month

import firebase_admin
from firebase_admin import credentials, firestore
import matplotlib.pyplot as plt
import random
import numpy as np

# Initialize Firebase (if not initialized)
credpath = "gasspent-firebase-adminsdk-kht62-2a8e40aed1.json"
login = credentials.Certificate(credpath)
firebase_admin.initialize_app(login)

# Initialize Firestore
db = firestore.client()

def fetch_data(wallet_address, chain, month):
    doc_ref = db.collection("accounts").document(wallet_address)
    
    try:
        doc = doc_ref.get()
        data = doc.to_dict()
        if data:
            if "chains" in data and chain in data["chains"]:
                chain_data = data["chains"][chain]
                if month in chain_data:
                    month_data = chain_data[month]
                    return month_data
    except Exception as e:
        print(f"Error fetching data: {e}")
    
    return None

def check_wallet_address(wallet_address, accounts_file):
    # Check if the entered wallet address is in the "accounts.txt" file
    with open(accounts_file, 'r') as f:
        valid_wallet_addresses = [line.strip() for line in f.readlines()]
        if wallet_address not in valid_wallet_addresses:
            print(f"The entered wallet address {wallet_address} is not valid. Please try again.")
            return False
    return True

def check_chain(chain, chains_file):
    # Check if the entered chain is in the "chains.txt" file
    with open(chains_file, 'r') as f:
        valid_chains = [line.strip() for line in f.readlines()]
        if chain not in valid_chains:
            print(f"The entered chain {chain} is not valid. Please try again.")
            return False
    return True

def create_bar_chart(wallet_address, chain, month):
    data = fetch_data(wallet_address, chain, month)
    while data is None:
        print(f"No data found for {wallet_address} on {chain} in {month}. Please try again.")
        
        # Get user input for wallet address and month
        wallet_address = input("Enter your wallet address (type 'exit' to quit): ")
        
        # Check if the user wants to exit
        if wallet_address.lower() == 'exit':
            print("Exiting the program.")
            return

        # Check if the entered wallet address is valid
        if not check_wallet_address(wallet_address, "accounts.txt"):
            continue

        month = input("Enter the month (e.g., January, February, etc.): ")
        
        # Get user input for chain
        chain = input("Enter the specific chain: ")
        
        # Check if the entered chain is valid
        if not check_chain(chain, "chains.txt"):
            continue

        data = fetch_data(wallet_address, chain, month)

    days = list(data.keys())
    fees = [data[day] for day in days]
    
    # Generate random colors for each bar
    num_bars = len(days)
    bar_colors = [np.random.rand(3,) for _ in range(num_bars)]
    
    plt.bar(days, fees, color=bar_colors)
    plt.xlabel("Day of Month")
    plt.ylabel("Gas Fees (USD)")
    plt.title(f"Gas Fees for {wallet_address} on {chain} in {month}")
    plt.show()

# Run the script in a loop
while True:
    # Get user input for wallet address and month
    wallet_address = input("Enter your wallet address (type 'exit' to quit): ")
    
    # Check if the user wants to exit
    if wallet_address.lower() == 'exit':
        print("Exiting the program.")
        break

    # Check if the entered wallet address is valid
    if not check_wallet_address(wallet_address, "accounts.txt"):
        continue

    month = input("Enter the month (e.g., January, February, March, April, May, June, July, August, September, October, November, December): ")
    
    # Get user input for chain
    chain = input("Enter the specific chain 'eth-mainnet', 'matic-mainnet', 'bsc-mainnet', 'avalanche-mainnet', 'arbitrum-mainnet', 'optimism-mainnet', 'zksync-mainnet': ")
    
    # Check if the entered chain is valid
    if not check_chain(chain, "chains.txt"):
        continue

    # If all checks pass, proceed with creating the bar chart
    create_bar_chart(wallet_address, chain, month)
