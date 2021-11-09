# Lista 1 🧠

*Zadanie rozwiązanie w Pythonie, ale przysięgam że przepisze to kiedyś na c++, żeby śmigało jak tralala.*

## 🦾 Zadanie 1

### 📚 Treść zadania

Zapoznaj się z układanką *logiczna piętnastka*. Zaimplemetuj algorytm A* rozwiązujący tą układankę z dwoma różnymi funkcjami oceny heurystycznej. Jako stan początowy przyjmij losową permutację elenetów z zawsze pustym prawym dolnym rogiem (zastanów się czy wszystkie permutacje mają rozwiązanie i jeśli nie to jak to łatwo sprawdzić).

### ✏️ Sposób rozwiązania

Program znajduje się w pliku ```puzzle.py``` i reprezentuje rozwiązania zadania. Początkow dosajemy losowa permutację (rozwiązywalną), a następnie padaby jakie ruchu są dostępne w danej fazie. Dodajemy je na kolejke pioeytetową w odpowiednim kosztem. Powtarzamy proces, aż do momentu kiedy nie będziemy mieć układanki o wzorze finalnym. Kolejka gwarantuje nam, że zawsze wypieramy element o najniższym koszcie jaki jest dostępny w danej chwili. 

### 📈 Wyniki

#### Heurystyka 1 - liczba kafelków nie na swoim miejscu

Heurystyka 1 liczy ile kafelków jest nie na swoim miejscu. Przeprowadzone testy jednoznacznie wskazały że jest to heurystyka gorsza od heurystyki 2. Heurystyka ta nie pozwoliła mi osiągnąc zamierzonych rezulatów. Na losową permutacje musiałem wpływać współczynnikiem c, który odpowiedzialny był, za to, jaki procent pocztku tablicy jest posortowany. Dla współczynnika c = 0.80, działa i kończy swoje działanie w rozsądnym czasie. W przeciwnieństwie, gdy c = 0, wtedy losowoa permutacja jest faktycznie losowa, program jest bezużyteczny. 

#### Heurystyka 2 - Manchattan

Heurytyka ta, pozwoliła osiągnać lepsze wyniki od poprzedniej. Testy porównałem dla wspołczynnika c = 0.80. Jednakże ze względu na to, że jest lepsza i potrafi dla niżego, współczynika rozwiązywać układankę, przeprowadziłem dodatkowe testy, na które heurytyka 1 by nie zadzaiłała. Testy przedstawiłem w drugeij tabeli.

Wyniki przeprowadzone dla współcznika c = 0.80

|   Próba	|  H1 - dł. ścieżki 	|   H1 - l. odwiedzonych stanów	|   H2 - dł. ścieżki	|   H2 - l. odwiedzonych stanów	|
|---	|---	|---	    |---	|---	    |
|   1 ⭐️	|   26	|  204900 	|   26	|   28575	|
|   2	|   12	|   158	    |   12	|   72	    |
|   3	|   22	|   18436	|   22	|   1358	|
|   4 ⭐️	|   26	|   1608834	|   26	|   4831	|
|   5	|   24	|   53374	|   24	|   2690	|
|   6	|   24	|   65217	|   24	|   3310	|
|   7	|   22	|   18436	|   22	|   1358	|
|   8	|   18	|   2552	|   18	|   597 	|
|   9	|   20	|   6056	|   20	|   447	    |
|   10	|   22	|   22097	|   22	|   1592	|
|   **AVG**	|   **21.6**	|  **55206** 	|   **21.6**	|   	**4486.5**    |

*Gwiazdami oznaczoy najlepszy wyniki (pod względem długość ścieżki)*

Wyniki przeprowadzone dla współczynnika c = 0.40 (tj. dla plaszy 4x4 -> pierwsze 5 elementów jest na swoim miejscu)

|   Próba	|   Długość ścieżki	|   l. odwiedzonych stanów	|
|---	|---	|---	|
|   1 ⭐️	|   36	|   111305	|
|   2	|   34	|   33119	|
|   3	|   28	|   4910	|
|   4	|   30	|   45184	|
|   5	|   32	|   12882	|
|   6 ⭐️	|   36	|   34109	|
|   7	|   34	|   76776	|
|   8 ⭐️	|   36	|   98849	|
|   9	|   30	|   11711	|
|   10 ⭐️	|   36	|   125594	|
|   **AVG**	|   **33.2**	|   **55443.9**	|

*Gwiazdami oznaczoy najlepszy wyniki (pod względem długość ścieżki)*

### 🤔 Wnioski

Z przeprowadzonych przeze mnie badań, wynika, że heurystyka manchatan jest znacznie lepsza od heurystyki, która ocenia ile jest kafelków na swoim miejscu. Jest wstanie bardziej eksplorować "drzewo".