# airline notes

- rule 1 = (older than 18 and with destinations in India) get 20% discount, but not on mondays or fridays
- rule 2 = destinations outside of India are offered 25% discount, but not if departure is on mondays or fridays
- rule 3 = those who stays >= 6 days at destination, get a 'additional' 10% discount
- rule 4 = Passengers with (2 < age < 18 ), are offered a discount of 40% for all destinations
- rule 5 = Children ( age <= 2) travel for free

<!-- | conditions            | rule 1        | rule 2        | rule 3        | rule 4        | rule 5        |
| --------------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
|dest not on M & F |T   |F              |f              |-              |              |-              |
|departure not on M & F |-              |T              |f              |              |-              |
|dest in india          |T              |F              |f              |              |-              |
|stays >= 6 days        |-              |f              |f              |              |-              |
|older than 18          |T              |f              |f              |              |F              |
| 2 < age < 18          |F              |f              |f              |              |F              |
| age < 2               |F              |F              |F              |              |T              |
| **expected action**       |               |               |               |                |              |
|                       |               |               |              |                |             |
| 20% discount         |               |           |           |           |           |              |
| 25% discount         |               |           |           |           |           |              |
| additional 10% discount|               |           |           |           |           |              |
|    40% discount                    |               |           |           |           |           |              |
|     free                   |               |           |           |           |           |              |

| conditions            | rule 1        | rule 2        | rule 3        | rule 4        | rule 5        |
| --------------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
|dest not on M & F |T   |F              |f              |-              |              |-              |
|departure not on M & F |-              |T              |f              |              |-              |
|dest in india          |T              |F              |f              |              |-              |
|stays >= 6 days        |-              |f              |f              |              |-              |
|older than 18          |T              |f              |f              |              |F              |
| 2 < age < 18          |F              |f              |f              |              |F              |
| age < 2               |F              |F              |F              |              |T              |
| **expected action**       |               |               |               |                |              |
|                       |               |               |              |                |             |
| 20% discount         |               |           |           |           |           |              |
| 25% discount         |               |           |           |           |           |              |
| additional 10% discount|               |           |           |           |           |              |
|    40% discount                    |               |           |           |           |           |              |
|     free                   |               |           |           |           |           |              |
 -->

| **Conditions**             | **Rule 1** | **Rule 2** | **Rule 3** | **Rule 4** | **Rule 5** |
| -------------------------- | ---------- | ---------- | ---------- | ---------- | ---------- |
| Dest not on Mon & Fri      | T          | F          | -          | -          | -          |
| Departure not on Mon & Fri | -          | T          | -          | -          | -          |
| Dest in India              | T          | F          | -          | -          | -          |
| Stays ≥ 6 days             | -          | (T)        | T          | (T)        | -          |
| Older than 18              | T          | F          | -          | F          | F          |
| 2 < Age < 18               | F          | F          | -          | T          | F          |
| Age <= 2                    | F          | F          | -          | F          | T          |
| **Expected Action**        |            |            |            |            |            |
| 20% discount               | ✓          |            |            |            |            |
| 25% discount               |            | ✓          |            |            |            |
| Additional 10% discount    |            | (✓)        | ✓          | (✓)        |            |
| 40% discount               |            |            |            | ✓          |            |
| Free                       |            |            |            |            | ✓          |

---
