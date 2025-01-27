from enum import Enum
import os
import time

class TypPola(Enum):
	MARTWE = 0
	ZYWE = 1
	MROWKA = 2

class Gra:
	def __init__(self, x: int, y: int):
		self.x: int = x;
		self.y: int = y;
		self.plansza: [[TypPola]] = [[TypPola.MARTWE for _ in range(0, x)] for _ in range(0, y)];
		self.plansza[y // 2][x // 2] = TypPola.MROWKA;

	def wyswietlPlansze(self):
		os.system("cls" if os.name == "nt" else "clear");
		for y in self.plansza:
			for x in y:
				znak: str = "";
				if x == TypPola.MARTWE:
					znak = "."
				elif x == TypPola.ZYWE:
					znak = "o"
				else:
					znak = "@"

				print(znak, " ", end="");
			print("");

	def zaktualizujPlane(self):
		# coś...
		odwalsie = True;

	def graj(self):
		while True:
			self.zaktualizujPlane();
			self.wyswietlPlansze();
			time.sleep(0.5);

gra: Gra = Gra(20, 20);
gra.graj();