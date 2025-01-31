# Mrówka Langtona
Symulacja mrówki Langtona w Pythonie.<br><br>

Najprostrze użycie: <code>python main.py {szerokość} {wysokość} {prędkość} {limit}</code>, gdzie <code>szerokość</code> <code>wysokość</code> <code>prędkość</code> <code>limit</code> są wymaganymi argumentami pozycyjnymi określającymi odpowiednio szerokość planszy, wysokość planszy, prędkość symulacji, limit kroków symulacji.<br><br>

Możliwość wywołania komendy <code>python main.py --help</code> po dokładnieszy opis owych parametrów oraz informacje o parametrach opcjonalnych.<br>
# Instalacja
1. Klonujemy repozytorium do wybranego folderu, ręcznie albo za pomocą komendy <code>git clone https://github.com/Oskar3141/Mrowka-Langtona</code>.<br>
2. Otwieramy folder z projektem <code>cd Mrowka-Langtona</code>.<br>
3. Tworzymy nowe środowisko wirtualne <code>python3 -m venv .venv</code>.<br>
4. Aktywujemy nowo utworzone środowisko wirtualne:<br>
  4a. Na systemie Unix albo MacOS <code>.venv\Scripts\activate</code>.<br>
  4b. Na systemie Windows <code>.venv\Scripts\activate</code>.<br>
5. Instalujemy wszystkie wymagane pakiety <code>python3 -m pip install -r wymagania.txt</code>.<br>
6. Uruchamiamy projekt, na przykład <code>python3 main.py 15 15 1 20</code>.<br>
7. Korzystamy z komendy <code>deactivate</code> aby deakywować utworze środowisko wirtualne.
