import pandas as pd
import numpy as np
import random

toxic_comments = [
    "You're so dumb", "This is trash", "Worst video ever", "Stop making content", "You sound horrible",
    "Clickbait title", "Can't believe people like this", "Waste of time", "Cringe content", "You're such a loser"
]

supportive_comments = [
    "This helped me a lot!", "You're amazing!", "Best tutorial I've seen", "Thanks for the content!",
    "Keep up the great work", "So clear and helpful", "Awesome explanation", "I learned a lot!", "Much appreciated!", "Legend!"
]

data = []

for i in range(50):
    data.append({"comment": random.choice(toxic_comments), "label": "toxic"})
    data.append({"comment": random.choice(supportive_comments), "label": "support"})

df = pd.DataFrame(data)
df.to_csv("youtube_comments.csv", index=False)
print("✅ Data saved successfully")