![Static Badge](https://img.shields.io/badge/python-%233776ab?logo=python&logoColor=white)

# License Key Generator

<img width="570" alt="Capture d’écran 2024-12-05 à 10 10 57" src="https://github.com/user-attachments/assets/44645792-1340-4f9f-ade6-2245b81de0de">


## **Description**
This Python script **generates unique license keys**, **hashes them using SHA3-512**, and **saves them to a file**. It also stores user details, including the username and the corresponding hashed license key, in a CSV file.
<br>**The program ensures that each license key is unique by checking against existing keys before generating a new one**.
<br>The script provides logging to track key generation and storage activities.

## **Features**
- **Unique License Key Generation** : Generates a random, unique license key based on a specified length.
- **SHA3-512 Hashing** : The license key is hashed using SHA3-512 for secure storage.
- **User Registration** : Allows users to register with their username and receive a hashed license key.
- **File Storage** : Saves the license key in a text file and user information (username, hashed key) in a CSV file.
- **Logging** : Logs actions, including key generation and file operations, for easy tracking.
- **Error Handling** : Handles errors related to file operations and key generation.

## **Prerequisites**
- **Python 3.11** installed on your machine
- **ShadePy** library

## **Installation Instructions**

Make sure you have [Python](https://www.python.org/downloads/) installed on your system before running the install command.

1. Clone this repository to your machine.

   ```bash
   git clone https://github.com/0x414854/Generate_License_Key.git

2. Run the following command to install **Shadepy** library:

   ```bash
   pip install shadePy
   
3. Once the repository is cloned and dependencies are installed, you're ready to run the program !

   ```bash
   python3 generate_license_key.py

## **Usage Examples**
- Launch the program by running `generate_license_key.py`.
- The program will generate a unique license key, hash it, and display it in the console.
- The hashed license key will be saved in `License_key.txt`.
- You will be prompted to enter a username. Once entered, the username and corresponding hashed license key will be saved in `users.csv`.
- To quit, simply close the program.
  
## Tree Directory

Generate_License_Key/
<br>├── generate_license_key.py
<br>├── README.md
<br>└── LICENSE

## **License**
This project is licensed under the **MIT License**.

## **Author**

[**0x414854**](https://github.com/0x414854)
