def malicious_function():
    print("I am malicious!")
    i = 0
    while True:
        i = i + 1
    
def main():
    malicious_function()

if __name__ == "__main__":
    main()
