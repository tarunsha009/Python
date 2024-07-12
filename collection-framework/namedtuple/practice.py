# Problem Statement:
#
# You are given a list of athletes' performance data. Each athlete has a name, country, and score. Your task is to write a function that processes this data and returns a list of the top 3 athletes based on their scores. If there are ties, sort the athletes with the same score by their name alphabetically.
#
# Details:
#
# Each athlete's performance data is represented as a tuple: (name, country, score).
# Use namedtuple to represent each athlete.
# Return the top 3 athletes in a list of namedtuple objects.

from typing import List, Tuple
from collections import namedtuple


def top_athletes(data: List[Tuple[str, str, int]]) -> List[namedtuple]:
    # Your code here
    result = sorted(data, key=lambda d: d.score, reverse=True)
    return result[:3]

data = [
        ("Alice", "USA", 95),
        ("Bob", "Canada", 90),
        ("Charlie", "UK", 95),
        ("David", "USA", 88),
        ("Eve", "Australia", 92)
    ]

Athlete = namedtuple("Athlete", ['name', 'country', 'score'])
athlete_list = [Athlete(*athlete) for athlete in data]

result = top_athletes(athlete_list)
for athlete in result:
    print(athlete.name, athlete.country, athlete.score)
    # Expected Output:
    # Alice USA 95
    # Charlie UK 95
    # Eve Australia 92



