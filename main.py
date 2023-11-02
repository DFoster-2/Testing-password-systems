from linecache import getline
from tkinter import Label,Entry,Tk,Button
import json
import bcrypt

with open ("users.json", "r") as file:
  users = json.loads(file.read())

def signUp():
  global hoorayLabel
  hoorayLabel.config(text="We have signed you up because you \n didn't have an account")

root = Tk()

nameLabel = Label(root, text="Name: ")
nameLabel.grid(row=0, column=0)

nameInput = Entry(root)
nameInput.grid(row=0, column=1)

passLabel = Label(root, text="Password: ")
passLabel.grid(row=1, column=0)

passInput = Entry(root)
passInput.grid(row=1,column=1)

hoorayLabel = Label(root, text="Waiting on input...")
hoorayLabel.grid(row=4,column=0,columnspan=2)

def submit():
  global users
  global root
  global hoorayLabel
  isnew = False
  username = nameInput.get().lower()
  password = passInput.get()
  try:
    user = users[username]
  except:
    print("Creating account...")
    isnew = True
    user = {"password":bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt()).decode('ascii'),"name":username}
    users[username] = user
    data = json.dumps(users, indent=2)
    with open ("users.json", "w") as file:
      file.write(data)
  if isnew:
    signUp()
  elif bcrypt.checkpw(password.encode('utf-8'),user["password"].encode('utf-8')):
    hoorayLabel.config(text="Signed in")
  else:
    hoorayLabel.config(text="Wrong password.")
submit = Button(root, text="Submit", command=submit)
submit.grid(row=3,column=0)


root.mainloop()
