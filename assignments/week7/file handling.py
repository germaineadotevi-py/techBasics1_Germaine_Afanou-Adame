import csv
import os
from datetime import datetime
import random

DEBUG = True
FILE_NAME = "leaderboard.csv"


def run_game():
    print("--- Number Guessing Game ---")

    if DEBUG:
        print("[DEBUG MODE] Game skipped.")
        return random.randint(50, 500)

    # echtes Spiel (optional)
    secret = random.randint(1, 10)
    guess = int(input("Guess a number between 1 and 10: "))

    if guess == secret:
        return 100
    else:
        return 0


def load_records():
    records = []

    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r", newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)

                for row in reader:
                    row["Score"] = int(row["Score"])
                    records.append(row)

        except Exception as e:
            print("Error loading file:", e)

    return records


def save_records(records):
    try:
        with open(FILE_NAME, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["Name", "Timestamp", "Score"])
            writer.writeheader()
            writer.writerows(records)

    except Exception as e:
        print("Error saving file:", e)


def show_leaderboard(records):
    print("\n--- LEADERBOARD ---")

    for i, r in enumerate(records, start=1):
        print(f"{i}. {r['Name']} | {r['Score']} | {r['Timestamp']}")


def main():
    try:
        name = input("Enter your name: ").strip()
        if name == "":
            name = "Anonymous"

        score = run_game()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        new_record = {
            "Name": name,
            "Timestamp": timestamp,
            "Score": score
        }

        records = load_records()
        records.append(new_record)

        # SORTIERUNG = Leaderboard Logik
        records.sort(key=lambda x: x["Score"], reverse=True)

        save_records(records)
        show_leaderboard(records)

        print("\nGame saved successfully!")

    except Exception as e:
        print("Unexpected error:", e)


if __name__ == "__main__":
    main()