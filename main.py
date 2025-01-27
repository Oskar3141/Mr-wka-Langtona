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
		self.mrowkaI = self.planszaS * self.planszaW // 2;
		self.mrowkaI += 0 if self.planszaS * self.planszaW % 2 == 1 else self.planszaW // 2;
		
		self.plansza: [Pole] = [Pole(False, False) for _ in range(0, self.planszaS * self.planszaW)];
		self.plansza[self.mrowkaI].mrowka = True;

	def wyswietlPlansze(self):
		os.system("cls" if os.name == "nt" else "clear");
		for i in range(0, self.planszaS * self.planszaW):
			znak: str = "";
			if self.plansza[i].mrowka:
				znak = "@"
			elif self.plansza[i].zywe:
				znak = "o"
			else:
				znak = "."

			print(znak, " ", end="");
			if i != 0 and (i+1) % self.planszaW == 0:
				print("");

	def zaktualizujPlansze(self):
		doodsod = 2;

	def graj(self):
		while True:
			self.zaktualizujPlansze();
			self.wyswietlPlansze();
			time.sleep(0.5);

gra: Gra = Gra(21, 21);
gra.graj();