from bs4 import BeautifulSoup


with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')
print(soup.title)
print(soup.title.name)

all_anchor_tags = soup.findAll(name="a")

heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading.getText())
