import math

def euclidean_distance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

points = []
distances = []

def turkish_casefold(input_str):
    charmap_to_lower = {
        "I": "ı",
        "İ": "i",
    }
    return ''.join(charmap_to_lower.get(char, char.lower()) for char in input_str)

def check_exit(input_str):
    if turkish_casefold(input_str) == "exit":
        print("Programdan çıkılıyor...")
        exit()

while True:
    user_input = input("Kaç nokta gireceksiniz(çıkmak için exit yazıp ENTER'e basın)? ")
    check_exit(user_input)
    try:
        number_points = int(float(user_input))
        if number_points < 2:
            print("En az iki nokta girilmelidir.")
        else:
            break
    except ValueError:
        print("Geçersiz giriş. Lütfen geçerli bir sayı girin.")

for i in range(number_points):
    while True:
        user_input = input(f"{i + 1}. noktanın (x, y) koordinatlarını girin (örneğin: 1 2): ")
        check_exit(user_input)
        try:
            x, y = map(float, user_input.split())
            points.append((x, y))
            break
        except ValueError:
            print("Geçersiz giriş. Lütfen koordinatları tekrar girin.")

print("Noktalar:")
for i, (x, y) in enumerate(points):
    print(f"Nokta {i + 1}: ({x}, {y})")

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclidean_distance(points[i], points[j])
        distances.append(distance)

if distances:
    min_distance = min(distances)
    print(f"Mesafeler: {distances}")
    print(f"Minimum Mesafe: {min_distance}")
else:
    print("En az iki nokta girilmelidir.")
