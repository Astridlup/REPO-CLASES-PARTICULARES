🐍 Estructuras de Control y Colecciones en Python

Python nos ofrece estructuras de control de flujo como while y for, y colecciones como listas y diccionarios para trabajar con datos de manera flexible y dinámica.

🔁 Bucle while

Se repite mientras una condición sea verdadera.

```
contador = 0

while contador < 5:
    print(f"El contador es: {contador}")
    contador += 1
```

📌 Ideal cuando no sabés cuántas veces se va a repetir el ciclo.

🔁 Bucle for

Se usa para recorrer elementos de una colección (lista, string, etc.).

```
nombres = ["Ana", "Luis", "Juan"]

for nombre in nombres:
    print(f"Hola, {nombre}")
```

📌 Ideal cuando ya tenés una secuencia para recorrer.

También se puede usar con range() para repetir un número fijo de veces:

```
for i in range(3):
    print(f"Repetición {i}")
```

📚 Listas
Son colecciones ordenadas y modificables de elementos.

```
frutas = ["manzana", "banana", "pera"]
print(frutas[0])  # manzana
```

Métodos comunes de listas

| Método      | Descripción                              |
| ----------- | ---------------------------------------- |
| `append()`  | Agrega un elemento al final              |
| `insert()`  | Inserta en una posición específica       |
| `remove()`  | Elimina el primer elemento con ese valor |
| `pop()`     | Elimina el último (o índice específico)  |
| `sort()`    | Ordena la lista                          |
| `reverse()` | Invierte el orden                        |
| `len()`     | Devuelve la cantidad de elementos        |

📌 Ejemplo:

```
frutas.append("uva")
frutas.remove("banana")
print(frutas)
```


🧾 Diccionarios
Estructuras de datos que almacenan pares clave:valor.

```
persona = {
    "nombre": "Cristian",
    "edad": 30,
    "ciudad": "Córdoba"
}

print(persona["nombre"])  # Cristian
```

Métodos comunes de diccionarios

| Método       | Descripción                             |
| ------------ | --------------------------------------- |
| `get(clave)` | Devuelve el valor de la clave (o None)  |
| `keys()`     | Devuelve todas las claves               |
| `values()`   | Devuelve todos los valores              |
| `items()`    | Devuelve lista de tuplas (clave, valor) |
| `update()`   | Actualiza valores con otro diccionario  |
| `pop(clave)` | Elimina un par clave\:valor             |

📌 Ejemplo:
```
persona["edad"] = 31
persona.update({"ciudad": "Rosario"})
print(persona.get("nombre"))
```

✅ Ejemplo combinado
```
alumnos = [
    {"nombre": "Ana", "nota": 8},
    {"nombre": "Luis", "nota": 6},
    {"nombre": "Juan", "nota": 9}
]

for alumno in alumnos:
    if alumno["nota"] >= 7:
        print(f"{alumno['nombre']} aprobó con {alumno['nota']}")
```