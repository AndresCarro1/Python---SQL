from git.repo import Repo

repo = Repo('https://github.com/AndresCarro1/SQL-Python')

repo.index.add(['C:\Users\user\AppData\Local\Programs\Python\Python311\SQL.py'])
repo.index.commit('commit from python')

origin = repo.remotes[0]
origin.push()
