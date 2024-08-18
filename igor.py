import subprocess
import time

def main():
    try:
        # Run the first script and wait for it to finish before proceeding
        print("Starting ThrowTheSwitch.py...")
        subprocess.run(['python', 'ThrowTheSwitch.py'], check=True)
        print("YeSsSs MaStEr...")

        # Sleep for 30 seconds
        print("IGOR! Throw The Switch in 30 seconds!...")
        time.sleep(30)

        # Run the second script with arguments
        print("Starting FrankenKoin.py...")
        subprocess.run(['python', 'FrankenKoin.py', '1BvNwfxEQwZNRmYQ3eno6e976XyxhCsRXj', 'mnemonic.txt'], check=True)
        print("DAMN-IT IGOR! ATTEMPT TO BRUTE-FORCE THE KEY-SPACE INSTEAD!!!")

        # Run the third script with arguments
        print("YeSsSs MaStEr.....")
        time.sleep(5)
        subprocess.run(['python', 'FRANKENKOIN.py', '1BvNwfxEQwZNRmYQ3eno6e976XyxhCsRXj', 'mnemonic.txt'], check=True)
        print("Do it Or Die...")

    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running the script: {e}")

if __name__ == "__main__":
    main()
