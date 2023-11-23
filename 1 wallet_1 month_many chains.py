#CODE2

# 1 wallet address, multiple chain, 1 month
import firebase_admin
from firebase_admin import credentials, firestore
import matplotlib.pyplot as plt
import random

def initialize_firebase(credpath):
    # Initialize Firebase
    login = credentials.Certificate(credpath)
    firebase_admin.initialize_app(login)
    
    # Initialize Firestore
    db = firestore.client()
    
    return db

def fetch_data(wallet_address, chain, month, db):
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

def create_wallet_bar_chart(wallet_address, month, chains, db):
    chain_labels = []
    total_fees = []

    for chain in chains:
        data = fetch_data(wallet_address, chain, month, db)
        if data:
            chain_labels.append(chain)
            total_fee = sum(data.values())
            total_fees.append(total_fee)

    # Generate random colors for each bar
    bar_colors = [f'#{random.randint(0, 0xFFFFFF):06x}' for _ in range(len(chain_labels))]

    plt.bar(chain_labels, total_fees, color=bar_colors)
    plt.xlabel("Chain")
    plt.ylabel("Total Gas Fees (USD)")
    plt.title(f"Gas Fees for {wallet_address} in {month} Across Chains")
    plt.xticks(rotation=45)
    plt.show()

def main(credpath, wallet_address, month, chains_file):
    # Initialize Firebase
    db = initialize_firebase(credpath)
    
    # Read the list of chains from the "chains.txt" file
    with open(chains_file, 'r') as f:
        chains = [line.strip() for line in f.readlines()]
    
    # Call the create_wallet_bar_chart function
    create_wallet_bar_chart(wallet_address, month, chains, db)

# Define the wallet address, month, and chains.txt file
wallet_address = "0x2209b21F90F52892bf94f7A3D8cC295E8f1B6a04"
month = "October"
credpath = "gasspent-firebase-adminsdk-kht62-2a8e40aed1.json"
chains_file = "chains.txt"

# Call the main function to execute the code
main(credpath, wallet_address, month, chains_file)

import firebase_admin
from firebase_admin import credentials, firestore
import matplotlib.pyplot as plt
import random

def initialize_firebase(credpath):
    # Initialize Firebase
    login = credentials.Certificate(credpath)
    firebase_admin.initialize_app(login)
   
    # Initialize Firestore
    db = firestore.client()
   
    return db


def fetch_data(wallet_address, chain, month, db):
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


def is_valid_wallet(wallet_address):
    # Check if the wallet address is valid by comparing it with entries in "accounts.txt"
    with open("accounts.txt", "r") as accounts_file:
        valid_wallets = [line.strip() for line in accounts_file.readlines()]
    return wallet_address in valid_wallets


def create_wallet_bar_chart(wallet_address, month, chains, db):
    chain_labels = []
    total_fees = []

    for chain in chains:
        data = fetch_data(wallet_address, chain, month, db)
        if data:
            chain_labels.append(chain)
            total_fee = sum(data.values())
            total_fees.append(total_fee)

    # Generate random colors for each bar
    bar_colors = [f'#{random.randint(0, 0xFFFFFF):06x}' for _ in range(len(chain_labels))]

    plt.bar(chain_labels, total_fees, color=bar_colors)
    plt.xlabel("Chain")
    plt.ylabel("Total Gas Fees (USD)")
    plt.title(f"Gas Fees for {wallet_address} in {month} Across Chains")
    plt.xticks(rotation=45)
    plt.show()


def main():
    while True:
        # Get user input for wallet address
        wallet_address = input("Enter your wallet address (type 'exit' to quit): ")
       
        # Check if the user wants to exit
        if wallet_address.lower() == 'exit':
            print("Exiting the program.")
            break

        # Validate wallet address
        if not is_valid_wallet(wallet_address):
            print("Invalid wallet address. Please try again.")
            continue

        # Get user input for month
        month = input("Enter the month (e.g., January, February, etc.): ")

        # Validate month input
        valid_months = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ]
        if month.capitalize() not in valid_months:
            print("Invalid month. Please enter a valid month.")
            continue

        # Initialize Firebase
        credpath = "gasspent-firebase-adminsdk-kht62-2a8e40aed1.json"
        db = initialize_firebase(credpath)
       
        # Read the list of chains from the "chains.txt" file
        chains_file = "chains.txt"
        with open(chains_file, 'r') as f:
            chains = [line.strip() for line in f.readlines()]
       
        # Call the create_wallet_bar_chart function
        create_wallet_bar_chart(wallet_address, month, chains, db)

if __name__ == "__main__":
    main()

# import firebase_admin
# from firebase_admin import credentials, firestore

# def initialize_firebase(credpath):
#     # Initialize Firebase
#     login = credentials.Certificate(credpath)
#     firebase_admin.initialize_app(login)
   
#     # Initialize Firestore
#     db = firestore.client()
   
#     return db

# def fetch_data(wallet_address, chain, month, db):
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

# def calculate_total_fees(wallet_addresses, chains, db):
#     for month in ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]:
#         total_fee = 0
#         for wallet_address in wallet_addresses:
#             for chain in chains:
#                 data = fetch_data(wallet_address, chain, month, db)
#                 if data:
#                     total_fee += sum(data.values())

#         print(f"{month}: {total_fee:.2f} USD")

# def main():
#     # Initialize Firebase
#     credpath = "gasspent-firebase-adminsdk-kht62-2a8e40aed1.json"
#     db = initialize_firebase(credpath)

#     # Read the list of chains from the "chains.txt" file
#     chains_file = "chains.txt"
#     with open(chains_file, 'r') as f:
#         chains = [line.strip() for line in f.readlines()]

#     # Read wallet addresses from "accounts.txt" file
#     wallet_addresses_file = "accounts.txt"
#     with open(wallet_addresses_file, 'r') as f:
#         wallet_addresses = [line.strip() for line in f.readlines()]

#     # Calculate and print total gas fees for each month
#     calculate_total_fees(wallet_addresses, chains, db)

# if __name__ == "__main__":
#     main()
