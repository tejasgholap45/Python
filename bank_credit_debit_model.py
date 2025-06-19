class bank:
  def __init__(self,accno,name,bal):
    self.accno = accno
    self.name = name
    self.bal = bal

  def info(self):
    print(f"{self.accno},{self.name},{self.bal}")

  def credit(self,amt):
    self.bal += amt
    print(f"added amount is {amt}, total credited amount is {self.bal}")

  def debit(self,amt):
    self.bal -= amt
    print(f"added amount is {amt}, total debited amount is {self.bal}")

cust = bank(10,"tejas",2000)
cust.info()
cust.credit(50000)
cust.info()
