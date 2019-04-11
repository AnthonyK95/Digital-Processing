
import os

if __name__ == "__main__":
    
    for files in os.walk("./cards/"):  
        for filename in files:
            print(filename)