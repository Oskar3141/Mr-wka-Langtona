from enum import Enum
import os
import time

class Pole:
	def __init__(self, zywe: bool, mrowka: bool):
		self.zywe = zywe;
		self.mrowka = mrowka;

class Gra:
	def __init__(self, s: int, w: int) -> None:
		self.kroki: int = 0;
		self.czasBezAktualizacji: float = 0.1;
		self.planszaS: int = s;
		self.planszaW: int = w;
		self.mrowkaI: int = self.planszaS // 2 + self.planszaW // 2 * self.planszaS;
		self.mrowkaKier: int = 0;
		
		self.plansza: [Pole] = [Pole(False, False) for _ in range(0, self.planszaS * self.planszaW)];
		self.plansza[self.mrowkaI].mrowka = True;

	def wyswietlPlansze(self) -> None:
		os.system("cls" if os.name == "nt" else "clear");
		for i in range(0, self.planszaS * self.planszaW):
			znak: str = "";
			if self.plansza[i].mrowka:
				znak = "@"
			elif self.plansza[i].zywe:
				znak = "■"
			else:
				znak = " "

			print(znak, "", end="");
			if i != 0 and (i+1) % self.planszaS == 0:
				print("");
		print("Kroki: ", self.kroki);

	def zaktualizujPlansze(self) -> None:
		if self.plansza[self.mrowkaI].zywe:
			self.mrowkaKier += 1;
			self.mrowkaKier = 0 if self.mrowkaKier == 4 else self.mrowkaKier;
		else:
			self.mrowkaKier -= 1;
			self.mrowkaKier = 3 if self.mrowkaKier == -1 else self.mrowkaKier; 

		self.plansza[self.mrowkaI].mrowka = False;
		self.plansza[self.mrowkaI].zywe = not self.plansza[self.mrowkaI].zywe;

		if self.mrowkaKier == 0:
			if self.mrowkaI - self.planszaS < 0:
				self.mrowkaI = self.planszaS * self.planszaW - (self.planszaS - self.mrowkaI);
			else:
				self.mrowkaI -= self.planszaS;
		elif self.mrowkaKier == 1:
			if (self.mrowkaI + 1) % self.planszaS == 0:
				self.mrowkaI -= self.planszaS - 1;
			else:
				self.mrowkaI += 1;			
		elif self.mrowkaKier == 2:
			if self.mrowkaI + self.planszaS > self.planszaW * self.planszaS - 1:
				self.mrowkaI -= (self.planszaW - 1) * self.planszaS;
			else:
				self.mrowkaI += self.planszaS;
		else:
			if self.mrowkaI % self.planszaS == 0:
				self.mrowkaI += self.planszaS - 1;
			else:
				self.mrowkaI -= 1;

		self.plansza[self.mrowkaI].mrowka = True;
		self.kroki += 1;

	def graj(self) -> None:
		while True:
			self.zaktualizujPlansze();
			self.wyswietlPlansze();
			time.sleep(self.czasBezAktualizacji);

gra: Gra = Gra(41, 41);
gra.graj();