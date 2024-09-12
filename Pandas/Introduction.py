import csv

def calc_ratings_stats(data, industry = None):
    ratings = []
    for row in data:
        if row[3] != "NULL" and (not industry or row[1] == industry):
            ratings.append(float(row[3]))
    max_rating = max(ratings)
    min_rating = min(ratings)
    avg_rating = sum(ratings)/len(ratings)
    return max_rating, min_rating, avg_rating
    
with open(r"C:\Users\ADMIN\AI-ML\Pandas\movies.csv") as f:
    data = list(csv.reader(f))
    header = data[0]
    data = data[1:]
    # print(data[0]) #row0 is header
    # print(data[1:]) #row1 onwards is the actual csv data
    # print(data)
    
    max_rating, min_rating, avg_rating = calc_ratings_stats(data)
    print("All records: Min Rating => ", min_rating, " Max Rating => ", max_rating, " Avg Rating => ", avg_rating)
    
    max_rating, min_rating, avg_rating = calc_ratings_stats(data, industry = "Bollywood")
    print("Bollywood: Min Rating => ", min_rating, " Max Rating => ", max_rating, " Avg Rating => ", avg_rating)

    max_rating, min_rating, avg_rating = calc_ratings_stats(data, industry = "Hollywood")
    print("Hollywood: Min Rating => ", min_rating, " Max Rating => ", max_rating, " Avg Rating => ", avg_rating)