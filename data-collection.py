import requests
import pandas as pd
from tqdm import tqdm

API_KEY = "27f6ef382021fb874eeb363575c1ef5d"

def get_top_rated_ids(pages=50):
    ids = []
    for page in tqdm(range(1, pages + 1), desc="Fetching Top Rated IDs"):
        url = f"https://api.themoviedb.org/3/movie/top_rated?api_key={API_KEY}&page={page}"
        res = requests.get(url).json()

        if "results" not in res:
            continue

        for m in res["results"]:
            ids.append(m["id"])
    return ids


def get_full_details(movie_id):
    url = (
        f"https://api.themoviedb.org/3/movie/{movie_id}"
        f"?api_key={API_KEY}&append_to_response=credits,images,videos,release_dates"
    )

    res = requests.get(url)
    if res.status_code != 200:
        return None

    d = res.json()

    return {
        "id": d.get("id"),
        "title": d.get("title"),
        "original_title": d.get("original_title"),
        "overview": d.get("overview"),
        "release_date": d.get("release_date"),
        "runtime": d.get("runtime"),
        "budget": d.get("budget"),
        "revenue": d.get("revenue"),
        "status": d.get("status"),
        "vote_average": d.get("vote_average"),
        "vote_count": d.get("vote_count"),
        "popularity": d.get("popularity"),

        "genres": ", ".join([g["name"] for g in d.get("genres", [])]),
        "production_companies": ", ".join(
            [c["name"] for c in d.get("production_companies", [])]
        ),
        "production_countries": ", ".join(
            [c["name"] for c in d.get("production_countries", [])]
        ),
        "spoken_languages": ", ".join(
            [l["name"] for l in d.get("spoken_languages", [])]
        ),

        "cast": ", ".join([c["name"] for c in d.get("credits", {}).get("cast", [])[:2]]),

        "directors": ", ".join(
            [c["name"] for c in d.get("credits", {}).get("crew", []) if c["job"] == "Director"]
        )

    }



movie_ids = get_top_rated_ids(pages=50)  

all_movies = []

for mid in tqdm(movie_ids):
    details = get_full_details(mid)
    if details:
        all_movies.append(details)

df = pd.DataFrame(all_movies)
df.to_csv("top_rated_full_details1.csv", index=False, encoding="utf-8")
