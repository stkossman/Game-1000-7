def main():
    num = 1000
    decr = 7

    print("Subtract 7 from number and enter result")

    while num >= -1:
        correct = num - decr
        user_input = int(input(f"Enter the result of {num} - {decr}: "))

        while user_input != correct:
            print("Incorrect result. Try again")
            user_input = int(input(f"Enter the result of {num} - {decr}: "))

        print("good")
        num = correct
    print("the end")


if __name__ == "__main__":
    main()
