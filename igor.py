import subprocess
import time

def main():
    try:
        # Run the first script and wait for it to finish before proceeding
        print("Starting 2.py...")
        subprocess.run(['python', '2.py'], check=True)
        print("2.py completed.")

        # Sleep for 100 seconds
        print("Waiting for 100 seconds...")
        time.sleep(100)

        # Run the second script with arguments
        print("Starting FrankenKoin.py...")
        subprocess.run(['python', 'FrankenKoin.py', '1BvNwfxEQwZNRmYQ3eno6e976XyxhCsRXj', 'mnemonic.txt'], check=True)
        print("FrankenKoin.py completed.")

    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running the script: {e}")

if __name__ == "__main__":
    main()
