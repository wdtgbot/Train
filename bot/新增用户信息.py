from json import load

with open("./user.json", "r", encoding="utf-8") as f1:
    user = load(f1)
new_user = {"id": "333", "token": "333", "time": "333"}
user['auth'].append(new_user)
with open("./user.json", "w", encoding="utf-8") as f2:
    f2.write(str(user).replace("'", '"'))
