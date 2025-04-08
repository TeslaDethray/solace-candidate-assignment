import csv
import datetime
import random
import uuid

first_names = [
    "Alice", "Bob", "Charlie", "David", "Eve", "Jona", "Grace", "Henry", "Ivy", "Jack",
    "Kelly", "Liam", "Mia", "Noah", "Olivia", "Peter", "Quinn", "Ryan", "Sophia", "Tom",
    "Ava", "Benjamin", "Charlotte", "Daniel", "Ella", "Finn", "Hazel", "Isaac", "Jade", "Kevin",
    "Lily", "Mason", "Nora", "Owen", "Penelope", "Samuel", "Riley", "Scarlett", "Wyatt", "Zoe",
    "Adrian", "Brooke", "Caleb", "Delilah", "Ethan", "Faith", "Gabriel", "Hannah", "Isaiah", "Jasmine",
    "Leo", "Madison", "Nathan", "Stella", "Vincent", "Willow", "Xavier", "Yara", "Zachary", "Aurora",
    "Jasper", "Luna", "Milo", "Naomi", "Silas", "Ruby", "Theodore", "Violet", "Asher", "Clara",
    "Elijah", "Eleanor", "Frederick", "Genevieve", "Hugo", "Isabelle", "Julian", "Katherine", "Lucas", "Beatrice",
    "Arthur", "Cecilia", "Edward", "Florence", "George", "Harriet", "Louis", "Margaret", "Oscar", "Philippa",
    "Thea", "William", "Ada", "Charles", "Eleanor", "Felix", "Gertrude", "Harold", "Imogen", "Josephine", "Reginald",
    "Walter", "Agnes", "Bernard", "Constance", "Edmund", "Gladys", "Humphrey", "Irene", "Lionel", "Mabel", "Percival",
    "Sybil", "Victor", "Winifred", "Clarence", "Doris", "Ernest", "Hazel", "Raymond", "Ruth", "Stanley", "Ethel",
    "Clifford", "Florence", "Lloyd", "Mildred", "Russell", "Vera", "Wallace", "Gladys", "Cecil", "Olive", "Wilbur",
    "Bessie", "Chester", "Pearl", "Vernon", "Minnie", "Archie", "Hattie", "Roy", "Myrtle", "Clarence", "Ida",
    "Frank", "Lena", "Earl", "Nellie", "Harry", "Rose", "Lester", "Sadie", "Walter", "Maude", "Carl", "Grace",
    "Raymond", "Bessie", "Howard", "Ethel", "Albert", "Clara", "Ernest", "Mabel", "Clifford", "Gertrude", "Roy", "Lillian",
    "Marion", "Pauline", "Everett", "Gertrude", "Willard", "Hazel", "Clarence", "Beulah", "Virgil", "Irene", "Lester", "Bernice",
    "Floyd", "Fern", "Cecil", "Gladys", "Elmer", "Opal", "Marvin", "Velma", "Clarence", "Audrey", "Dale", "Maxine",
    "Glenn", "Doris", "Lloyd", "Norma", "Wayne", "Beverly", "Eugene", "Lois", "Dean", "Joyce", "Harold", "Joan",
    "Roger", "Carolyn", "Donald", "Shirley", "Ronald", "Brenda", "Kenneth", "Linda", "Gerald", "Sandra", "Dennis", "Nancy",
    "Raymond", "Deborah", "Stephen", "Karen", "Larry", "Susan", "Jeffrey", "Donna", "Gary", "Patricia", "Gregory", "Sharon",
    "Jose", "Michelle", "Kevin", "Lisa", "Anthony", "Laura", "Eric", "Mary", "Michael", "Jennifer", "Robert", "Elizabeth",
    "David", "Jessica", "John", "Ashley", "James", "Sarah", "Charles", "Stephanie", "George", "Nicole", "William", "Amanda"
]

last_names = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
    "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin",
    "Lee", "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson",
    "Walker", "Young", "Allen", "Torres", "King", "Wright", "Scott", "Green", "Baker", "Adams",
    "Nelson", "Hill", "Rivera", "Campbell", "Mitchell", "Roberts", "Carter", "Phillips", "Evans", "Turner",
    "Parker", "Collins", "Edwards", "Stewart", "Flores", "Morris", "Nguyen", "Murphy", "Cook", "Rogers",
    "Gutierrez", "Ortiz", "Morgan", "Cooper", "Peterson", "Bailey", "Reed", "Kelly", "Howard", "Ward",
    "Cox", "Diaz", "Richardson", "Wood", "Watson", "Brooks", "Bennett", "Gray", "James", "Reyes",
    "Cruz", "Hughes", "Price", "Myers", "Long", "Foster", "Sanders", "Ross", "Morales", "Powell",
    "Sullivan", "Russell", "Ortiz", "Jenkins", "Perry", "Butler", "Barnes", "Fisher", "Bishop", "Hayes",
    "Coleman", "Simmons", "Webb", "Ellis", "McDaniel", "Parsons", "Hamilton", "Reynolds", "O'Brien", "Underwood",
    "Vaughn", "Gregory", "Jacobs", "Kennedy", "Saunders", "Cunningham", "Walters", "Shelton", "Willis", "Weaver",
    "Barker", "Hoffman", "Henry", "Luna", "Page", "Stone", "Vega", "Winters", "Yates", "Zimmerman",
    "Blackwell", "Chambers", "Dickerson", "Ferguson", "Garrett", "Harrison", "Irwin", "Jordan", "Kramer", "Lambert",
    "Manning", "Nichols", "Oliver", "Porter", "Quinn", "Reed", "Saunders", "Stephens", "Tucker", "Upton",
    "Valdez", "Wagner", "Wheeler", "York", "Zuniga", "Atkinson", "Bradshaw", "Carlson", "Dennis", "Franklin",
    "Gilbert", "Hale", "Ingram", "Jensen", "Knight", "Larson", "Matthews", "Newman", "Osborne", "Patton",
    "Quentin", "Richards", "Sutton", "Talley", "Ullrich", "Vance", "Warren", "Xenos", "Youngblood", "Ziegler"
]

degrees = ["MD", "PhD", "PsyD", "LCSW", "LMFT", "EdD", "DO", "MSW", "MA"]
cities = [
    "New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose",
    "Austin", "Jacksonville", "San Francisco", "Columbus", "Charlotte", "Indianapolis", "Seattle", "Denver", "Boston", "Nashville",
    "Oklahoma City", "Las Vegas", "Portland", "Milwaukee", "Albuquerque", "Tucson", "Sacramento", "Kansas City", "Omaha", "Virginia Beach",
    "Atlanta", "Miami", "Minneapolis", "Tampa", "Aurora", "Colorado Springs", "Raleigh", "Cincinnati", "Pittsburgh", "Richmond",
    "St. Louis", "Salt Lake City", "Buffalo", "Birmingham", "Knoxville", "Louisville", "Charleston", "Columbia", "Little Rock", "Providence",
    "Salt Lake City", "Honolulu", "Anchorage", "Boise", "Manchester", "New Orleans", "Cleveland", "Detroit", "Baltimore", "Memphis",
    "Fort Worth", "El Paso", "Arlington", "Mesa", "Miami Gardens", "Tulsa", "Oakland", "Minneapolis", "Wichita", "Newark",
    "Arlington", "Tampa", "Aurora", "Santa Ana", "St. Louis", "Pittsburgh", "North Las Vegas", "Orlando", "Cincinnati", "Anaheim",
    "Bridgeport", "Buffalo", "Chandler", "Chula Vista", "Detroit", "Durham", "Fort Wayne", "Fresno", "Greensboro", "Henderson",
    "Huntington Beach", "Jersey City", "Lincoln", "Madison", "New Haven", "New Orleans", "Norfolk", "Oakland", "Omaha", "Plano",
    "Raleigh", "Riverside", "Rochester", "Sacramento", "St. Petersburg", "Salt Lake City", "San Bernardino", "Santa Ana", "Scottsdale", "Seattle",
    "Spokane", "Springfield", "Stamford", "Syracuse", "Tacoma", "Toledo", "Tucson", "Tulsa", "Virginia Beach", "Washington D.C.",
    "Worcester", "Yonkers"
]
specialties_list = [
    "Bipolar", "LGBTQ", "Medication/Prescribing", "Suicide History/Attempts", "General Mental Health (anxiety depression stress grief life transitions)",
    "Men's issues", "Relationship Issues (family friends couple etc)", "Trauma & PTSD", "Personality disorders", "Personal growth",
    "Substance use/abuse", "Pediatrics", "Women's issues (post-partum infertility family planning)", "Chronic pain", "Weight loss & nutrition",
    "Eating disorders", "Diabetic Diet and nutrition", "Coaching (leadership career academic and wellness)", "Life coaching", "Obsessive-compulsive disorders",
    "Neuropsychological evaluations & testing (ADHD testing)", "Attention and Hyperactivity (ADHD)", "Sleep issues", "Schizophrenia and psychotic disorders",
    "Learning disorders", "Domestic abuse"
]

data = []
for i in range(1000):
    first_name = '"' + random.choice(first_names) + '"'
    last_name = '"' + random.choice(last_names) + '"'
    degree = '"' + random.choice(degrees) + '"'
    city = '"' + random.choice(cities) + '"'
    num_specialties = random.randint(2, 10)
    specialties = random.sample(specialties_list, num_specialties)
    years_of_experience = random.randint(2, 30)
    phone_number = '"' + "".join(random.choices("0123456789", k=10)) + '"'
    # Format the specialties for PostgreSQL TEXT[]
    random_uuid = uuid.uuid4()
    now = datetime.datetime.now(datetime.timezone.utc)
    created_at = now.isoformat()
    specialties_str = "{" + ",".join(specialties) + "}"
    data.append([first_name, last_name, degree, city, specialties_str, years_of_experience, phone_number, random_uuid, created_at])

with open("advocates.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    # The columns should be in this order for the script to work just as it is. If it isn't,rearrange line 93.
    # writer.writerow(["first_name", "last_name", "degree", "city", "specialties", "years_of_experience", "phone_number", "id", "created_at"])
    writer.writerows(data)

print("clinicians.csv file generated successfully (in a real environment).")
print("\n--- First 20 rows of the generated data: ---")
for row in data[:20]:
    print(f"{row[0]},{row[1]},{row[2]},\"{row[3]}\",\"{row[4]}\",{row[5]},{row[6]},{row[7]},{row[8]}")
