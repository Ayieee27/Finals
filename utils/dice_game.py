import random
import os
from utils.score import Score

scores = []

class DiceGame:  
    @staticmethod
    def load_scores():
        try:
            with open('utils/data/rankings.txt', 'r') as file:
                lines = file.readlines()
                if lines:
                    scores = [line.strip() for line in lines]
                    sorted_scores = sorted(scores, key=lambda x: int(x.split(": Points - ")[1].split(",")[0]), reverse=True)
                    print("Top 10 Scores:")
                    for i, score in enumerate(sorted_scores[:10], 1):
                        print(f"{i}. {score}")
                else:
                    print("No Records Yet.")
        except FileNotFoundError:
            print("No Records Yet.")

    @staticmethod
    def save_scores(username, points, stages):
        try:
            os.makedirs('utils/data', exist_ok=True)
            
            with open('utils/data/rankings.txt', 'a') as file:
                file.write(f"{username}: Points - {points}, Stages won - {stages}\n")
        except Exception as e:
            print("Error occurred while saving scores:", e)

    @staticmethod
    def play_game(username):
        bot = 0
        points = 0
        stages = 0
        choice = 0

        print("Starting Game as " + username)
        while points != 3 or bot != 3:
            playerdice = random.randint(1, 6)
            botdice = random.randint(1, 6)
            print(username + " rolled: " + str(playerdice))
            print("Bot rolled: " + str(botdice))
            if playerdice > botdice:
                print("You win this round!")
                points = points + 1
                if points == 3:
                    stages = stages + 1
                    points = points + 3
                    DiceGame.save_scores(username, points, stages)
                    print("Total points: " + str(points) + " | Stages won: " + str(stages))
                    choice = int(input(("Do you want to [1]continue or 0[Quit]? ")))
                    if choice == 1:
                        points = 0
                        bot = 0
                        stages = 0
                    elif choice == 0:
                        break
                    else:
                        print("Invalid input.")
            elif playerdice == botdice:
                continue
            else:
                print("Bot win this round!")
                bot = bot + 1
                if bot == 3:
                    print("Total points: " + str(points) + " | Stages won: " + str(stages))
                    print("You lost this stage " + username)
                    DiceGame.save_scores(username, points, stages)
                    break

    @staticmethod
    def show_top_scores():
        DiceGame.load_scores()

    @staticmethod
    def logout():
        print("Logout Successfully!")
        return False

    @staticmethod
    def menu(username):
        while True:
            choice = int(input("\nWelcome " + username + " to Dice Roll Game!\n1.Start Game\n2.Show Top Scores\n3.Logout\nEnter here: "))
            if choice == 1:
                DiceGame.play_game(username)
            elif choice == 2:
                DiceGame.show_top_scores()
            elif choice == 3:
                DiceGame.logout()
                break
            else:
                print("Invalid choice. Please try again.")
                pass