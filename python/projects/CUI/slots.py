#slot machine
import random
class SlotMachine:
    def __init__(self, symbols, reels):
        self.symbols = symbols
        self.reels = reels

    def spin(self):
        return [random.choice(self.symbols) for _ in range(self.reels)]

    def display(self, result):
        print(" | ".join(result))

def main():
    symbols = ["🍒", "🍋", "🍊", "🍉", "⭐"]
    reels = 3
    slot_machine = SlotMachine(symbols, reels)

    print("Welcome to the Slot Machine!")
    while True:
        input("Press Enter to spin the reels...")
        result = slot_machine.spin()
        slot_machine.display(result)

        if len(set(result)) == 1:  # All symbols are the same
            print("Congratulations! You hit the jackpot!")
        else:
            print("Try again!")

        if input("Do you want to play again? (y/n): ").lower() != 'y':
            break
    print("Thanks for playing!")
if __name__ == "__main__":
    main()