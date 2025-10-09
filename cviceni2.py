def vrat_treti(seznam):
 if len(seznam) <= 3:
  return seznam[2]
 else:
    return None


def prumer(cisla):
  cisla1 = (sum(cisla)/len(cisla))
  return cisla1

def naformatuj_text(student):
  znamky = prumer(student["znamka"])
  return f"Student: {student['jmeno']} {student['prijmeni']} ve veku {student['vek']} ma prumer {round(znamky,2)}"



if __name__ == "__main__":
 # vytvorime novy seznam(list)
 seznam = [12, 50, 1, 3, 5]
# vezmeme 3. prvek a vynasobim tremi
 seznam[3] *= 3
# na konec seznamu pripojime hodnotu 100
 seznam.append(100)
# seznam setridime a oticime poradi prvku
 seznam.sort()
 seznam.reverse()

 seznam2 = [1,2,3]

 student = {"jmeno": "Jan",
   "prijmeni": "Novak",
   "vek": 22,
   "znamka": [1,2,1,3,1,2,1]
   }
student["vek"] += 1
print(student["znamka"][4])
print(naformatuj_text(student))