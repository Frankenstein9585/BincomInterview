from bs4 import BeautifulSoup
from collections import defaultdict
from statistics import median, variance

with open('python_class_question.html', 'r') as html:
    html_content = html.read()

soup = BeautifulSoup(html_content, 'html.parser')

rows = soup.find_all('tr')

color_counts = defaultdict(int)  # stores total number of times a particular color of shirt is worn
day_counts = defaultdict(int)  # shows the number of days a particular color of shirt is worn

for row in rows:
    day = row.find('td').text
    colors = row.find_all('td')[1].text.split(', ')

    unique_colors = set()
    for color in colors:
        color_counts[color] += 1
        if color not in unique_colors:
            day_counts[color] += 1
            unique_colors.add(color)
    # shirts[day] = colors.split(', ')

mean_color_counts = {color: color_counts[color] / day_counts[color] for color in color_counts}

mean_color = max(mean_color_counts, key=mean_color_counts.get)
most_worn_color = max(color_counts, key=mean_color_counts.get)
print(f'Mean Color = {mean_color}')
print(f'Most Worn Color = {most_worn_color}')

color_counts_list = list(color_counts.values())

sorted_counts_list = sorted(color_counts_list)  # sorted by ascending order of frequency
sorted_dict = dict(
    sorted(color_counts.items(), key=lambda item: item[1]))  # sorted dictionary by ascending order of frequency

# Find median of the colors
colors_median = median(sorted_counts_list)
current_count = 0
for color, count in sorted_dict.items():
    current_count += count
    if current_count >= colors_median:
        print(f'Median Color: {color}')
        break

colors_variance = variance(sorted_counts_list)
print(f'Variance of the Colors = {colors_variance}')

no_red = color_counts['RED']
color_count = sum(color_counts_list)
pr_red = no_red / color_count

print(f'Probability of Red = {pr_red}')
