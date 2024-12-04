"""WELCOME TO THE SLOT MACHINE GAME SAMPLE"""
#source that been reorganized: https://www.youtube.com/watch?v=f5J3YiZ3XX8
import random

def spin_row():
    symbols = ['💕', '❤️', '😍', '😘','😊','yo te amo', 'estas mejor', 'ven', 'amor']
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print(" ".join(row))

def get_payout(row, bet):
    if row[0] == row[1] == row [2]:
        if row[0] == '💕':
            print("Amazing! Corazons!")
            return bet * 3

        elif row[0] == '❤️':
            print("Wow!! Corazon!")
            return bet * 2

        elif row[0] == '😍️':
            print("Estas millionario")
            return bet * 4

        elif row[0] in ['yo te amo', 'estas mejor', 'ven','amor'] :
            print("More phrases - more love")
            return bet * 1

    return 0

def main():
    balance = 100

    print("<------------------------------------->")
    print("Welcome to the Python slot crab game!")
    print("Symbols: 💕❤️😍😘😊")
    print(">-------------------------------------<")

    while balance >0:
        print(f"Current balance: 🦀{balance}")

        bet = (input("Send the crab numbers: "))

        if not bet.isdigit():#modified -check-in the input errors
            print("Enter a valid crab number:🦀 ")
            continue


        bet = int(bet)

        if bet > balance:
            print("Insufficient funds")
            continue

        if bet <=0:
            print("Crab bet must be greater then zero")
            continue
        balance -= bet

        row = spin_row()
        print('Spinning...\n')
        print_row(row)


        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won 🦀{payout}")
            balance += payout
        else:
            print("You spend a crab, but got love!:) Win!")


        game_continue =  input("Do you want to play more? (Y/N)").upper()
        if game_continue != 'Y' and game_continue != 'N':
            print("Please, enter Y or N")
        if game_continue == 'N':
            break
    print(f"Game over! Your final balance is 🦀{balance}")
        #else:
            #print("Crabs end")
if __name__ == '__main__':
   main()