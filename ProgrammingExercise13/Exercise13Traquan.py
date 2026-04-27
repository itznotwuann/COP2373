import sqlite3
import random
import matplotlib.pyplot as plt

# ---------------------------------------------------
# 1. YOUR 2025 POPULATION DATA
# ---------------------------------------------------
CITIES_2025 = {
    "Bradenton": 56289,
    "Sarasota": 59211,
    "Ruskin": 30074,
    "Daytona Beach": 89000,
    "Parrish": 67560,
    "Venice": 30800,
    "Miami": 464655,
    "Tampa": 414547,
    "Orlando": 343000,
    "Jacksonville": 1360000
}

DB_NAME = "population_TP.db"


# ---------------------------------------------------
# 2. CREATE DATABASE + TABLE
# ---------------------------------------------------
def create_database():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS population (
            city TEXT,
            year INTEGER,
            population INTEGER
        )
    """)

    conn.commit()
    conn.close()


# ---------------------------------------------------
# 3. INSERT 2025 BASE DATA
# ---------------------------------------------------
def insert_initial_data():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    # Clear old data so it doesn't duplicate if you rerun
    cur.execute("DELETE FROM population")

    for city, pop in CITIES_2025.items():
        cur.execute(
            "INSERT INTO population VALUES (?, ?, ?)",
            (city, 2025, pop)
        )

    conn.commit()
    conn.close()


# ---------------------------------------------------
# 4. SIMULATE 20 YEARS OF GROWTH/DECLINE
# ---------------------------------------------------
def simulate_population():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    for city, base_pop in CITIES_2025.items():
        current_pop = base_pop

        for year in range(2026, 2046):  # 20 years
            growth_rate = random.uniform(-0.02, 0.035)  # -2% to +3.5%
            current_pop = int(current_pop * (1 + growth_rate))

            cur.execute(
                "INSERT INTO population VALUES (?, ?, ?)",
                (city, year, current_pop)
            )

    conn.commit()
    conn.close()


# ---------------------------------------------------
# 5. PLOT CITY POPULATION
# ---------------------------------------------------
def plot_city_population(city_name):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute(
        "SELECT year, population FROM population WHERE city=?",
        (city_name,)
    )

    data = cur.fetchall()
    conn.close()

    years = [row[0] for row in data]
    populations = [row[1] for row in data]

    plt.plot(years, populations, marker="o")
    plt.title(f"Population Growth/Decline: {city_name}")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.grid(True)
    plt.show()


# ---------------------------------------------------
# 6. MAIN PROGRAM
# ---------------------------------------------------
def main():
    create_database()
    insert_initial_data()
    simulate_population()

    cities = list(CITIES_2025.keys())

    print("\nChoose a city to view population growth:\n")

    for i, city in enumerate(cities, 1):
        print(f"{i}. {city}")

    choice = int(input("\nEnter a number (1-10): "))
    selected_city = cities[choice - 1]

    plot_city_population(selected_city)


# Run program
main()