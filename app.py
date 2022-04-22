class AikatauluJarjestelma:
  def __init__(self):
    self.calendar = {day + 1: {hour: "" for hour in range(8, 25)} for day in range(7)}
    self.running = True
    self.users = []

  def print_whole_calendar(self):
    """ Prints the whole week """
    for day, hours in self.calendar.items():
      print(day, hours)


  def print_day(self, day):
    """ Prints the hours of given day """
    print(self.calendar[day])


  def check_if_assigned(self, day, hour):
    """ checks if the hour in a day is already taken """
    return self.calendar[day][hour] != ""


  def add_task(self, day, starts_at, ends_at, task):
    """ Adds new task to calendar """
    myday = self.calendar[day]
    for x in range(starts_at, ends_at):
      if self.check_if_assigned(day, x):
        print(f"Klo {x} already has: {myday[x]}")
      else:
        myday[x] = task
    self.calendar[day] = myday
    

  def clear(self):
    """ clears terminal """
    for x in range(80):
      print("")


  def check_credentials(self, uname, pwd):
    for user in self.users:
      if user.username == uname and user.password == pwd:
        return True
    return False

  def run(self):
    self.clear()

    while self.running:
      print("Choose:\n\n(1) Login\n(2) Create new user\n(*) Quit\n")
      ask = input("-> ")
      if ask == "1":
        self.clear()
        print("Login:\n\n")
        ask_name = input("Username: ")
        ask_pwd = input("Password: ")
        if self.check_credentials(ask_name, ask_pwd):
          self.clear()
          print("Logged in\n")
        else:
          self.clear()
          print("User not found\n")
          continue
      elif ask == "2":
        self.clear()
        print("Create new user:\n\n")
        ask_name = input("Username: ")
        ask_pwd = input("Password: ")
        self.users.append(User(ask_name, ask_pwd))
        self.clear()
        print(f"User {ask_name} created!\n")
        continue
      else:
        self.running = False

class User:
  def __init__(self, username, password):
    self.username = username
    self.password = password

app = AikatauluJarjestelma()

app.print_day(2)
app.add_task(2, 10, 12, "Imuroi")
app.add_task(2, 11, 12, "Lenkille")
app.print_day(2)