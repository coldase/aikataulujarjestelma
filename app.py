import pickle

class AikatauluJarjestelma:
  def __init__(self):
    self.running = True
    self.calendar = self.load_calendar() if self.load_calendar() else self.make_empty_calendar()
    self.users = self.load_users() if self.load_users() else []
    self.loggedin = False

  def make_empty_calendar(self):
    """ Makes and empty calendar template """
    return {day + 1: {hour: {} for hour in range(8, 25)} for day in range(7)}

  def print_whole_calendar(self):
    """ Prints the whole week """
    for day, hours in self.calendar.items():
      print(day, hours)


  def print_day(self, day):
    """ Prints the hours of given day """
    print(f"\nDay: {day}\n")
    for hour, task in self.calendar[day].items():
      print(f"Klo: {hour} - {task}")


  def check_if_assigned(self, day, hour):
    """ checks if the hour in a day is already taken """
    return self.calendar[day][hour] != {}


  def add_task(self, day, starts_at, ends_at, user, task):
    """ 
          Adds new task to calendar 
          *************************
          day: 1-7
          starts_at: 8-24
          ends_at: 8-24
          user: Name of the user whos going to complete the task
          task: Name of task
    
    """
    myday = self.calendar[day]
    for x in range(starts_at, ends_at):
      if self.check_if_assigned(day, x):
        print(f"Klo {x} already has: {myday[x]}")
      else:
        myday[x] = {user: task}
    self.calendar[day] = myday
    self.save_calendar()
    

  def clear(self):
    """ clears terminal """
    for _ in range(80):
      print("")


  def check_credentials(self, uname, pwd):
    """ Checks if username and passoword found in users """
    for user in self.users:
      if user.username == uname and user.password == pwd:
        return True
    return False

  def save_calendar(self):
    """ Saves calendar data to ./data.pickle """
    with open("data.pickle", "wb") as f:
      pickle.dump(self.calendar, f)

  def load_calendar(self):
    """ Loads calendar data from ./data.pickle """
    try:
      with open("data.pickle", "rb") as f:
        return pickle.load(f)
    except:
      return False

  def save_users(self):
    """ Saves user data to ./users.pickle """
    with open("users.pickle", "wb") as f:
      pickle.dump(self.users, f)

  def load_users(self):
    """ Loads user data from ./users.pickle """
    try:
      with open("users.pickle", "rb") as f:
        return pickle.load(f)
    except:
      return False

  def run(self):
    """ Main loop for the application """
    self.clear()
    self.save_calendar()
    while self.running:
      if not self.loggedin:
        print("Aikataulujarjestelma 1.0\n")
        print("Choose:\n(1) Login\n(2) Create new user\n(*) Quit\n")
        ask = input("-> ")
        if ask == "1":
          self.clear()
          print("Login:\n")
          ask_name = input("Username: ")
          ask_pwd = input("Password: ")
          if self.check_credentials(ask_name, ask_pwd):
            self.clear()
            print(f"Logged in as {ask_name}\n")
            self.loggedin = True
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
          self.save_users()
          continue
        else:
          self.running = False
          
      else:
          print("\nChoose:\n(1) Print Week\n(2) Print Day\n(3) Add tasks\n(4) Remove task\n(5) Reset calendar\n(*) Logout\n")
          ask = input("-> ")
          if ask == "1":
            self.clear()
            self.print_whole_calendar()
          elif ask == "2":
            self.clear()
            print("Give a day number (1-7):\n")
            ask = input("->  ")
            try:
              self.clear()
              self.print_day(int(ask))
            except:
              self.clear()
              print("Invalid input")
          elif ask == "3":
            self.clear()
            print("Add new task (day, starttime, endtime, user, task)\n")
            d = input("Day: ")
            s = input("Start time: ")
            e = input("End time: ")
            u = input("User: ")
            t = input("Task: ")
            self.clear()
            self.add_task(int(d), int(s), int(e), u, t)
            print("Task created!")

          elif ask == "4":
            self.clear()
            print("removing task in progress\n")
          elif ask == "5":
            self.clear()
            self.calendar = self.make_empty_calendar()
            print("Calendar reseted!")
            self.save_calendar()
          else:
            self.clear()
            self.loggedin = False
            continue

class User:
  def __init__(self, username, password):
    self.username = username
    self.password = password

app = AikatauluJarjestelma()

if __name__ == "__main__":
  app.run()
  