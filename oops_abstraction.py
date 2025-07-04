import getpass
class farm:
  def __init__(self,name):
    self.owner = "durgesh"


  def change_pass(self):
    n = input("enter the new password")
    p = getpass.getpass("enter your password")
    if p == "tamaterbhai":
      return "password updated successfully...."
      self.owner = owner
    else:
      print("worng password..???")

p1 = farm("vinu vadapav")
p2 = farm("durgi misal")

p1.change_pass()
