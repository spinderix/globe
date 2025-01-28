import csv
import random

# Function to generate random latitude and longitude
def generate_lat_long():
    latitude = random.uniform(-90.0, 90.0)
    longitude = random.uniform(-180.0, 180.0)
    return latitude, longitude

# Generate random data
data = []
for _ in range(10000):
    latitude, longitude = generate_lat_long()
    num_serials = random.randint(1, 1000)  # Random number for num_serials
    data.append([latitude, longitude, num_serials])

# Write data to CSV file
with open('data/random_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['lat', 'lng', 'pop'])
    writer.writerows(data)

print("CSV file 'random_data.csv' has been created with 100 rows of random data.")
