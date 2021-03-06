# Lista 1 馃

*Zadanie rozwi膮zanie w Pythonie, ale przysi臋gam 偶e przepisze to kiedy艣 na c++, 偶eby 艣miga艂o jak tralala.*

## 馃 Zadanie 1

### 馃摎 Tre艣膰 zadania

Zapoznaj si臋 z uk艂adank膮 *logiczna pi臋tnastka*. Zaimplemetuj algorytm A* rozwi膮zuj膮cy t膮 uk艂adank臋 z dwoma r贸偶nymi funkcjami oceny heurystycznej. Jako stan pocz膮towy przyjmij losow膮 permutacj臋 elenet贸w z zawsze pustym prawym dolnym rogiem (zastan贸w si臋 czy wszystkie permutacje maj膮 rozwi膮zanie i je艣li nie to jak to 艂atwo sprawdzi膰).

### 鉁忥笍 Spos贸b rozwi膮zania

Program znajduje si臋 w pliku ```puzzle.py``` i reprezentuje rozwi膮zania zadania. Pocz膮tkow dosajemy losowa permutacj臋 (rozwi膮zywaln膮), a nast臋pnie padaby jakie ruchu s膮 dost臋pne w danej fazie. Dodajemy je na kolejke pioeytetow膮 w odpowiednim kosztem. Powtarzamy proces, a偶 do momentu kiedy nie b臋dziemy mie膰 uk艂adanki o wzorze finalnym. Kolejka gwarantuje nam, 偶e zawsze wypieramy element o najni偶szym koszcie jaki jest dost臋pny w danej chwili. 

### 馃搱 Wyniki

#### Heurystyka 1 - liczba kafelk贸w nie na swoim miejscu

Heurystyka 1 liczy ile kafelk贸w jest nie na swoim miejscu. Przeprowadzone testy jednoznacznie wskaza艂y 偶e jest to heurystyka gorsza od heurystyki 2. Heurystyka ta nie pozwoli艂a mi osi膮gn膮c zamierzonych rezulat贸w. Na losow膮 permutacje musia艂em wp艂ywa膰 wsp贸艂czynnikiem c, kt贸ry odpowiedzialny by艂, za to, jaki procent pocztku tablicy jest posortowany. Dla wsp贸艂czynnika c = 0.80, dzia艂a i ko艅czy swoje dzia艂anie w rozs膮dnym czasie. W przeciwnie艅stwie, gdy c = 0, wtedy losowoa permutacja jest faktycznie losowa, program jest bezu偶yteczny. 

#### Heurystyka 2 - Manchattan

Heurytyka ta, pozwoli艂a osi膮gna膰 lepsze wyniki od poprzedniej. Testy por贸wna艂em dla wspo艂czynnika c = 0.80. Jednak偶e ze wzgl臋du na to, 偶e jest lepsza i potrafi dla ni偶ego, wsp贸艂czynika rozwi膮zywa膰 uk艂adank臋, przeprowadzi艂em dodatkowe testy, na kt贸re heurytyka 1 by nie zadzai艂a艂a. Testy przedstawi艂em w drugeij tabeli.

Wyniki przeprowadzone dla wsp贸艂cznika c = 0.80

|   Pr贸ba	|  H1 - d艂. 艣cie偶ki 	|   H1 - l. odwiedzonych stan贸w	|   H2 - d艂. 艣cie偶ki	|   H2 - l. odwiedzonych stan贸w	|
|---	|---	|---	    |---	|---	    |
|   1 猸愶笍	|   26	|  204900 	|   26	|   28575	|
|   2	|   12	|   158	    |   12	|   72	    |
|   3	|   22	|   18436	|   22	|   1358	|
|   4 猸愶笍	|   26	|   1608834	|   26	|   4831	|
|   5	|   24	|   53374	|   24	|   2690	|
|   6	|   24	|   65217	|   24	|   3310	|
|   7	|   22	|   18436	|   22	|   1358	|
|   8	|   18	|   2552	|   18	|   597 	|
|   9	|   20	|   6056	|   20	|   447	    |
|   10	|   22	|   22097	|   22	|   1592	|
|   **AVG**	|   **21.6**	|  **55206** 	|   **21.6**	|   	**4486.5**    |

*Gwiazdami oznaczoy najlepszy wyniki (pod wzgl臋dem d艂ugo艣膰 艣cie偶ki)*

Wyniki przeprowadzone dla wsp贸艂czynnika c = 0.40 (tj. dla plaszy 4x4 -> pierwsze 5 element贸w jest na swoim miejscu)

|   Pr贸ba	|   D艂ugo艣膰 艣cie偶ki	|   l. odwiedzonych stan贸w	|
|---	|---	|---	|
|   1 猸愶笍	|   36	|   111305	|
|   2	|   34	|   33119	|
|   3	|   28	|   4910	|
|   4	|   30	|   45184	|
|   5	|   32	|   12882	|
|   6 猸愶笍	|   36	|   34109	|
|   7	|   34	|   76776	|
|   8 猸愶笍	|   36	|   98849	|
|   9	|   30	|   11711	|
|   10 猸愶笍	|   36	|   125594	|
|   **AVG**	|   **33.2**	|   **55443.9**	|

*Gwiazdami oznaczoy najlepszy wyniki (pod wzgl臋dem d艂ugo艣膰 艣cie偶ki)*

### 馃 Wnioski

Z przeprowadzonych przeze mnie bada艅, wynika, 偶e heurystyka manchatan jest znacznie lepsza od heurystyki, kt贸ra ocenia ile jest kafelk贸w na swoim miejscu. Jest wstanie bardziej eksplorowa膰 "drzewo".