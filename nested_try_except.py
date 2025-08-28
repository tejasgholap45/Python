try:
  us1=int(input('enter first number'))
  us2=int(input('enter second number'))
  try:
    print(us1/us2)
  except ZeroDivisionError:
    print('can not divide by zero')
except ValueError:
  print('only integer valid')
except Exception as e:
  print('unexpected error',e)
