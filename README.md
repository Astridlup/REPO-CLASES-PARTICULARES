## 📘 Teoría: Condicionales en Python

Los **condicionales** nos permiten ejecutar diferentes bloques de código dependiendo de si una condición es verdadera (`True`) o falsa (`False`).

### 🔹 Sintaxis básica

```
if condición:
    # bloque si la condición es verdadera

```

🔸 Ejemplo:


```
edad = 20

if edad >= 18:
    print("Sos mayor de edad.")

```


🔹 if...else
Cuando queremos hacer algo si la condición es verdadera y otra cosa si es falsa:

```
if condición:
    # si la condición es verdadera
else:
    # si la condición es falsa
```


🔸 Ejemplo:

```
edad = 16

if edad >= 18:
    print("Podés votar.")
else:
    print("Todavía no podés votar.")
```

🔹 if...elif...else
Usamos elif (abreviatura de else if) cuando tenemos múltiples condiciones posibles.

```
if condición1:
    # bloque 1
elif condición2:
    # bloque 2
else:
    # bloque si ninguna se cumple
```

🔸 Ejemplo:

```
nota = 7

if nota >= 9:
    print("Excelente")
elif nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")
```

🧪 Operadores de comparación más usados:
| Operador | Significado       | Ejemplo          |
| -------- | ----------------- | ---------------- |
| `==`     | Igual a           | `x == 10`        |
| `!=`     | Distinto de       | `x != 5`         |
| `>`      | Mayor que         | `edad > 18`      |
| `<`      | Menor que         | `nota < 4`       |
| `>=`     | Mayor o igual que | `peso >= 50`     |
| `<=`     | Menor o igual que | `altura <= 1.80` |


🧠 Tips útiles:
El bloque indentado (tabulado) debe ir debajo del if, elif o else, si no, da error.

Se pueden anidar condicionales (if dentro de otro if), pero hay que tener cuidado con la indentación.
