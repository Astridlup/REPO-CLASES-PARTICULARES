# 🧠 Fundamentos Básicos de CSS

CSS (*Cascading Style Sheets*) es el lenguaje que se utiliza para definir el estilo visual de una página web. A través de **selectores**, le damos instrucciones al navegador sobre cómo deben verse los elementos de HTML.

---

## 🎯 Reset de estilos inicial

Es común comenzar un archivo CSS con una regla de "reset" para eliminar márgenes y rellenos predeterminados:

```css
* {
  margin: 0;
  padding: 0;
}
```

🧩 ¿Qué es un selector?
CSS se basa en selectores, que son formas de "llamar" o identificar elementos HTML para aplicarles estilos. Hay distintos tipos:

1. 🔹 Por etiqueta (tipo de HTML)
Aplica estilos a todos los elementos de un tipo, por ejemplo:

```
header {
  /* estilo para el header */
}

img {
  /* estilo para todas las imágenes */
}
```

2. 🔸 Por clase (className)
Las clases permiten aplicar estilos a grupos de elementos:

```
.section-1 {
  /* estilo para todos los elementos con clase "section-1" */
}
```

Se usan con un punto (.) delante del nombre.

3. 🔹 Por ID
Aplica estilos a un único elemento específico, usando el símbolo #:

```
#banner {
  /* estilo único para el elemento con id="banner" */
}
```

🧱 Estilos comunes de layout
A continuación, un ejemplo práctico aplicando estilos a un <header>:

```
header {
  /* Layout con Flexbox */
  display: flex;

  /* Alineación vertical de los hijos */
  align-items: center;

  /* Distribución horizontal de los hijos */
  justify-content: space-between;

  /* Espaciado interno (padding): arriba, derecha, abajo, izquierda */
  padding: 30px;

  /* Color de fondo con código hexadecimal */
  background: #818AA3;
}
```

🧭 Sobre Flexbox
display: flex convierte un elemento en un contenedor flexible.

Propiedades clave:

```
align-items: alinea los ítems a lo largo del eje vertical:

flex-start, center, flex-end

justify-content: distribuye los ítems en el eje horizontal:

space-between: los empuja hacia los bordes

center: los agrupa en el centro

space-evenly: distribuye el espacio equitativamente
```

📐 Margen vs Padding
padding: espacio interno del elemento, empuja su contenido hacia adentro.

margin: espacio externo, separa el elemento de otros.

El orden de dirección en CSS (cuando hay múltiples valores) sigue el sentido del reloj:
arriba → derecha → abajo → izquierda

🎨 Colores en CSS
Los colores pueden definirse de varias maneras:

Por nombre (red, blue, green)

Por código hexadecimal (#ff0000, #00ff00)

Por RGB (rgb(255, 0, 0))

Por HSL (hsl(0, 100%, 50%))

🖼️ Estilizando elementos específicos
Podés aplicar estilos a elementos particulares, como imágenes dentro del header:

```
header img {
  /* Aquí podés definir altura, ancho, borde, etc. */
}
```


