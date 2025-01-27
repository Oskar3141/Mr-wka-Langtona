import os
import time
import argparse

class Pole:
	"""
	Klasa określająca pole planszy.

	...

	Atrybuty
	----------
	zywe : bool
	    Określa czy dane pole jest "żywe" czy nie.
	mrowka : bool
	    Określa czy mrówka znajduje się na tym polu.
	"""

	def __init__(self, zywe: bool, mrowka: bool):
		"""
		Argumenty
		----------
		zywe : bool
		    Określa czy dane pole jest "żywe" czy nie.
		mrowka : bool
		    Określa czy mrówka znajduje się na tym polu.
		"""

		self.zywe = zywe;
		self.mrowka = mrowka;

class Gra:
	"""
	Klasa określająca grę (symulację).

	...

	Atrybuty
	----------
	kroki : int
		Określa to ile razy pozycja mrówki została zaktualizowana.
	czasBezAktualizacji : float
		Określa minimalny czas (w sekundach) jaki musi upłynąć między aktualizacjami mrówki.
	limitKrokow : int
		Określa liczbę kroków po której symulacja się zakończy. brak limitu przy wartościach niedodatnich.
	planszaS : int
		Szerokośc planszy.
	planszaW : int
		Wysokość planszy.
	mrowkaI : int
		Określa numer (indeks) pola na którym znajduje się mrówka, 
		zaczynając od 0 w lewym górnym rogu i kończąc na planszaW * planszaS - 1 w prawym dolnym rogu.
	mrowkaKier:
		Określa kierunek mrówki; 0 - północ; 1 - wschód: 2 - południe; 3 - zachód.
	martwePole : str
		Określa znak (ciąg znaków) prezentujący martwe pole na planszy.
	zywePole : str
		Określa znak (ciąg znaków) prezentujący żywe pole na planszy.
	mrowka : str
		Określa znak (ciąg znaków) prezentujący mrówkę na planszy.

	Metody
	----------
	wyswietlPlansze() -> None
		Rysuje planszę gry.
	zaktualizujPlansze() -> bool
		Aktualizuje pozycję mrówki. Zwraca wartość logiczną 0 w przypadku osiągnięcia limitu kroków.
	graj() -> None
		Rozpoczyna grę (symulację).
	"""

	def __init__(self, s: int, w: int, predkosc: float, limitKrokow: int, martwe: str, zywe: str, mrowka: str) -> None:
		"""
		Argumenty
		----------
		s : int
			Szerokośc planszy.
		w : int
			Wysokość planszy.
		predkosc : float 
			Określa minimalny czas (w sekundach) jaki musi upłynąć między aktualizacjami mrówki.
		limitKrokow : int 
			Określa liczbę kroków po której symulacja się zakończy. brak limitu przy wartościach niedodatnich.
		martwe : str
			Określa znak (ciąg znaków) prezentujący martwe pole na planszy.
		zywe : str
			Określa znak (ciąg znaków) prezentujący żywe pole na planszy.
		mrowka : str
			Określa znak (ciąg znaków) prezentujący mrówkę na planszy.
		"""

		self.kroki: int = 0;
		self.czasBezAktualizacji: float = predkosc;
		self.limitKrokow = limitKrokow;
		self.planszaS: int = s;
		self.planszaW: int = w;
		self.mrowkaI: int = self.planszaS // 2 + self.planszaW // 2 * self.planszaS;
		self.mrowkaKier: int = 0;
		
		self.plansza: [Pole] = [Pole(False, False) for _ in range(0, self.planszaS * self.planszaW)];
		self.plansza[self.mrowkaI].mrowka = True;

		self.martwePole = martwe;
		self.zywePole = zywe;
		self.mrowka = mrowka;

	def wyswietlPlansze(self) -> None:
		"""
		Funckja rysująca planszę gry.
		"""
		
		os.system("cls" if os.name == "nt" else "clear");
		for i in range(0, self.planszaS * self.planszaW):
			znak: str = "";
			if self.plansza[i].mrowka:
				znak = self.mrowka;
			elif self.plansza[i].zywe:
				znak = self.zywePole;
			else:
				znak = self.martwePole;

			print(znak, " ", end="");
			if i != 0 and (i+1) % self.planszaS == 0:
				print("");
		print("Kroki: ", self.kroki);

	def zaktualizujPlansze(self) -> bool:
		"""
		Funkcja aktualizująca pozycję mrówki. Zwraca wartość logiczną 0 w przypadku osiągnięcia limitu kroków.
		"""
		if self.kroki >= self.limitKrokow:
			return False;

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
		return True;

	def graj(self) -> None:
		"""
		Funckja zaczynająca grę (symulację).
		"""
		self.wyswietlPlansze();
		time.sleep(self.czasBezAktualizacji);
		while True:
			if not self.zaktualizujPlansze():
				break;
			self.wyswietlPlansze();
			time.sleep(self.czasBezAktualizacji);

parser = argparse.ArgumentParser();
parser.add_argument("szerokosc", help="Szerokość planszy, nie mniejsza niż 5.", type=int);
parser.add_argument("wysokosc", help="Wysokość planszy, nie mniejsza niż 5.", type=int);
parser.add_argument("predkosc", help="Określa czasz (w sekundach) między aktualizacjami pozycji mrówki. \
	Wartości niedodatnie są dopuszczane i określają możliwie najmniesze przerwy.", type=float);
parser.add_argument("limit", help="Określa limit kroków symulacji. Wartości niedodatnie są dopuszczalne i określają brak limitu.", type=int);

parser.add_argument("-mp", "--martwe-pole", help="Znak (albo ciąg znaków) prezentujący martwe pole na planszy.");
parser.add_argument("-zp", "--zywe-pole", help="Znak (albo ciąg znaków) prezentujący żywe pole na planszy.");
parser.add_argument("-m", "--mrowka", help="Znak (albo ciąg znaków) prezentujący mrówkę na planszy.");

arg = parser.parse_args();

if arg.wysokosc < 5 or arg.szerokosc < 5:
	raise ValueError("Minimalne wymiary planszy to 5x5.");

gra: Gra = Gra(
	arg.szerokosc, 
	arg.wysokosc, 
	arg.predkosc if arg.predkosc >= 0 else 0, 
	arg.limit,
	arg.martwe_pole or ".", 
	arg.zywe_pole or "O", 
	arg.mrowka or "@"
);
gra.graj();