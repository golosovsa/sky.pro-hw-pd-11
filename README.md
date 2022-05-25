# Homework №11
[link to the source](https://skyengpublic.notion.site/11-8d13de21a29f4467a5dd3c07217042fc)
### Task:
In the last homework, we created a simple web application using the flask framework. Do you like it? let's do something else and the first part is to create an html file about yourself. In the next and last part you have to create a simple web app using html templates.
## Part 1. What should you do:  
### Step 0 :  

!(pic)[https://skyengpublic.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fd82ac4ae-31a1-4082-a134-b73e9d0ca886%2F%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2022-02-14_%D0%B2_22.29.33.png?table=block&id=c17cd724-5bce-417c-968a-a24d6675cf0f&spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&width=2000&userId=&cache=v2]

Creat an HTML file about yourself

## Part 2. What should you do:
### Step 1:  
Save data to candidates.json file
```json
[
  {
    "id": 1,
    "name": "Adela Hendricks",
    "picture": "https://picsum.photos/200",
    "position": "Go разработчик",
    "gender": "female",
    "age": 40,
    "skills": "go, python"
  },
  {
    "id": 2,
    "name": "Sheri Torres",
    "picture": "https://picsum.photos/200",
    "position": "Delphi developer",
    "gender": "female",
    "age": 26,
    "skills": "Delphi, pascal, fortran, basic"
  },
  {
    "id": 3,
    "name": "Burt Stein",
    "picture": "https://picsum.photos/200",
    "position": "Team lead",
    "gender": "male",
    "age": 33,
    "skills": "делегирование, пользоваться календарем, обсуждать важные вопросы"
  },
  {
    "id": 4,
    "name": "Bauer Adkins",
    "picture": "https://picsum.photos/200",
    "position": "CTO",
    "gender": "male",
    "age": 37,
    "skills": "very important face"
  },
  {
    "id": 5,
    "name": "Day Holloway",
    "picture": "https://picsum.photos/200",
    "position": "HR manager",
    "gender": "male",
    "age": 35,
    "skills": "LinkedIn, telegram, spam, spam, spam"
  },
  {
    "id": 6,
    "name": "Austin Cochran",
    "picture": "https://picsum.photos/200",
    "position": "python-develop",
    "gender": "male",
    "age": 26,
    "skills": "python, html"
  },
  {
    "id": 7,
    "name": "Sheree Love",
    "picture": "https://picsum.photos/200",
    "position": "Django developer",
    "gender": "female",
    "age": 33,
    "skills": "Python, Django, flask"
  }
]
```

### Step 2:  
Create file, such as utils.py, and implement the functions that will receive the data. You can change the names of the functions.

- `load_candidates_from_json(path)` – return list of candidates
- `get_candidate(candidate_id)` – return candidate by id
- `get_candidates_by_name(candidate_name)` – return candidate by name
- `get_candidates_by_skill(skill_name)` – return list of candidates by skill

Test each function, after that import the functions into the main application file.

### Step 3:  
* Install Flask, write a minimal app code 
* Create a view for   `/`.
* Print list of candidates in next format:
```html
<h1>All Candidates</h1>
<p><a href="/candidate/<x>">Candidate name</a></p>
<p><a href="/candidate/<x>">Candidate name</a></p>
...
```
Create a template `list.html`
All links must open the candidate's page
### Step 4:
* Create a view for 'candidate/<x>' which should be printed as:

```html
<h1>Candidate name</h1>
<p>Candidate position</p>
<img src="(picture)" width=200/>
<p>Candidate skills</p>
```
Create a template `single.html` or `card.html`
### Step 5:
* Create a view for `/search/<candidate_name>` to search by name

print a list of candidates whose names contain the searched `candidate_name`
```html
<h1>Found 2 candidates</h2>
<p><a href="/candidate/<x>">Leo Black</a></p>
<p><a href="/candidate/<x>">Leo Brown</a></p>
```
Create a template `search.html`

### Step 6:
* Create a view for `/skill/<skill_name>` to search by skill.

print a list of candidates whose skills contain the searched `skill_name`

```html
<h1>Found 2 candidates with skill X</h2>
<p><a href="/candidate/<x>">Candidate name</a></p>
<p><a href="/candidate/<x>">Candidate name</a></p>
```
Create a template `skill.html`
## How it should be implemented  
### What will be checked in the homework:
- [ ] Routers without options are implemented correctly
- [ ] Routers with options are implemented correctly
- [ ] Flask is installed and works
- [ ] HTML is correct.
- [ ] The HTML layout is correct.
- [ ] Your name in a header tag (`<hx>`)
- [ ] There must be a link to your social media page (`<a>`)
- [ ] There must be a avatar picture (`<img>`)
- [ ] There are several paragraphs with text tags `<p>`, `<br>`, `<div>`. 
- [ ] There are must contains tags `<strong>`, `<em>`, `<del>`, `<mark>`.
 
 [## Project status]::
 [### Tag v1.0]::
 [- Create MVP]::