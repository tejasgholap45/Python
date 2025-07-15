income = int(input( "सर, तुमचा income टाका"))
bill = float(input("आपले बिल किती झाले..?"))

if 0 <= income <= 15000:
  print(f"sorry, तुम्हाला डिस्काउंट उपलब्ध नाही, तुमचा बिल घ्या. {bill}")

elif 15000 < income <= 50000:
  print(f"तुमचा बिल एवढे आहे {bill}, तुम्हाला 10% discount मिळाला, तुम्ही एवढे द्या. {bill*0.9}")

elif 50000 < income <= 70000:
  print(f"तुमचा बिल एवढे आहे {bill}, तुम्हाला 20% discount मिळाला, तुम्ही एवढे द्या. {bill*0.8}")

elif 70000 < income <= 100000:
  print(f"तुमचा बिल एवढे आहे {bill}, तुम्हाला 30% discount मिळाला, तुम्ही एवढे द्या. {bill*0.7}")

elif  income > 100000:
  print(f"तुमचा बिल एवढे आहे {bill}, तुम्हाला 40% discount मिळाला, तुम्ही एवढे द्या. {bill*0.6}")

else:
  print("तुम्ही कोणत्याच Criteria मध्ये बसत नाही!!")
