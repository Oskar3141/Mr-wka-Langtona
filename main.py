from enum import Enum
import os
import time

class Pole:
	def __init__(self, zywe: bool, mrowka: bool):
		self.zywe = zywe;
		self.mrowka = mrowka;

class Gra:
	def __init__(self, s: int, w: int):
		self.planszaS: int = s;
		self.planszaW: int = w;
		
		self.plansza: [[Pole]] = [[Pole(False, False) for _ in range(0, self.planszaS)] for _ in range(0, self.planszaW)];
		self.plansza[self.planszaW // 2][self.planszaS // 2].mrowka = True;

	def wyswietlPlansze(self):
		os.system("cls" if os.name == "nt" else "clear");
		for y in self.plansza:
			for x in y:
				znak: str = "";
				if x.mrowka:
					znak = "@"
				elif x.zywe:
					znak = "o"
				else:
					znak = "."

				print(znak, " ", end="");
			print("");

	def zaktualizujPlansze(self):
		# coś...
		odwalsie = True;

	def graj(self):
		while True:
			self.zaktualizujPlane();
			self.wyswietlPlansze();
			time.sleep(0.5);

gra: Gra = Gra(20, 20);
gra.graj();