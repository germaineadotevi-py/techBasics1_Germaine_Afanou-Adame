import csv
import os
from datetime import datetime
import random

DEBUG = True
FILE_NAME = "leaderboard.csv"
FIELDNAMES = ["Name", "Timestamp", "Score"]


def run_game():
    print("--- Number Guessing Game ---")

    if DEBUG:
        print("[DEBUG MODE] Game skipped.")
        return random.randint(50, 500)

    secret = random.randint(1, 10)
    guess = int(input("Guess a number between 1 and 10: "))

    return 100 if guess == secret else 0


def ensure_file_exists():
    """Creates file with header if it does not exist."""
    if not os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
                writer.writeheader()
            print("No existing data → leaderboard file created.")
        except Exception as e:
            print("Error creating file:", e)


def load_records():
    records = []

    try:
        with open(FILE_NAME, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            for row in reader:
                try:
                    row["Score"] = int(row["Score"])
                    records.append(row)
                except:
                    continue

    except Exception as e:
        print("Error loading file:", e)

    return records


def save_records(records):
    try:
        with open(FILE_NAME, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
            writer.writeheader()
            writer.writerows(records)
    except Exception as e:
        print("Error saving file:", e)


def show_leaderboard(records, top_n=5):
    print("\n--- LEADERBOARD (TOP 5) ---")

    for i, r in enumerate(records[:top_n], start=1):
        print(f"{i}. {r['Name']} | {r['Score']} | {r['Timestamp']}")


def main():
    try:
        ensure_file_exists()

        name = input("Enter your name: ").strip()
        if not name:
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

        # sort leaderboard
        records.sort(key=lambda x: x["Score"], reverse=True)

        save_records(records)

        show_leaderboard(records)

        print("\nGame saved successfully!")

    except Exception as e:
        print("Unexpected error:", e)


if __name__ == "__main__":
    main()