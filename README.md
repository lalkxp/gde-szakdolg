
A könyvtár tartalmazza a "Kockáztatott érték számítása Monte Carlo szimulációval" című szakdolgozatomhoz elkészített fájlokat.

Excel

MC.xlsx: Az Excel tábla tartalmazza az S&P500 valamint a Tesla Yahoo-ról letöltött értékeit 2022 január elseje és december 31.-e között. A Segéd lap tartalmazza a napi záró árfolyam változásokat a letöltött adatok alapján. A Historikus, Delta-normál és MonteCarlo lap tartalmazza a VaR és CVaR historikus számításait a megfelelő módszerekkel. A MonteCarlo_Cholesky lap a két értékpapírra vonatkozó VaR és CVaR számításokat tartalmazza.

Python

01_save_ticker_data.py: Részvény kereskedési adatok Yahoo oldaláról való letöltését és CSV formátumban való elmentését végzi el.
2.	02_plot_chart.py: Részvény záró árfolyamát jeleníti meg grafikonként.
3.	03_normalty_test.py: A megadott részvény adott időszakra vonatkozó normalitás vizsgálatát végzi el. Megjeleníti a hisztogram ábrát a hozzá tartozó normális eloszlással együtt, valamint a Q-Q ábrát. Ezenkívül elvégez 3, a normalitás vizsgálatra való statisztikai tesztet.
4.	04_mc_pi.py: Véletlen pontokat generál egy egységsugarú kör köré rajzolt négyzetben. Kiszámítja a körbe eső pontok relatív gyakoriságát az össze sponthoz viszonyítva.
5.	05_mc_pi_no_steps.py: Az előző szkript számítását végzi el háromszor a megadott lépésszámmal. Az eredményt átlagolja és kiszámítja a hibát, valamint meghatározza a futási időt.
6.	06_mc_pi_hist.py: A 4. szkript számítását ismétli meg 5, 10, 50 bés 100 ezerszer. Az eredményekről hisztogram adatokat nyomtat, valamint grafikont rajzol.
7.	07_mc_pi_var_red1.py: Variancia csökkentés antitetikus változók módszerével.
8.	08_mc_pi_var_red2.py: Variancia csökkentés fontossági mintavételezés módszerrel.
9.	09_sim_gbm.py: Geometriai Brown mozgást szimulál. A szimuláció eredményéről grafikont jelenít meg.
10.	10_sim_bootstrap.py: Az előzőhöz hasonló mozgást szimulál, de Bootstrap módszerrel és valós részvényadatok alapján.
11.	11_sim_gbm_cholesky.py: Geometriai Brown mozgást szimulál két adatsorra, amik között korreláció van. A szimuláció eredményéről grafikont jelenít meg.
12.	12_calculate_VaR.py: Kiszámolja a VaR és CVaR értékeket historikus és MC módszerrel.

A python csomagok telepítéséhez a következő parancsokat kell futtatni:

python -m pip install yfinance
python -m pip install pandas
python -m pip install matplotlib
python -m pip install scipy

