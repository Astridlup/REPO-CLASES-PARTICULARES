## 🧠 Sección `<head>`

Las etiquetas en el `<head>` no se ven directamente en la página, pero contienen metadatos y configuraciones importantes para el navegador.

| Etiqueta | Descripción |
|---------|-------------|
| `<title>` | Define el título de la pestaña del navegador. |
| `<meta charset="UTF-8">` | Especifica la codificación de caracteres (UTF-8 es estándar). |
| `<meta name="viewport" content="width=device-width, initial-scale=1.0">` | Ayuda al diseño responsivo en dispositivos móviles. |
| `<meta name="description" content="Descripción de la página">` | Describe el contenido de la página para buscadores. |
| `<link rel="stylesheet" href="estilos.css">` | Vincula una hoja de estilos externa. |
| `<script src="script.js"></script>` | Vincula un archivo JavaScript externo. |
| `<style>` | Permite escribir CSS directamente en el HTML. |
| `<base>` | Define la URL base para todos los enlaces relativos de la página. |

---

## 🖼️ Sección `<body>`

Las etiquetas del `<body>` representan el contenido visible de la página web.

| Etiqueta | Descripción |
|---------|-------------|
| `<h1>` a `<h6>` | Encabezados de mayor (`h1`) a menor jerarquía (`h6`). |
| `<p>` | Párrafo de texto. |
| `<a href="url">` | Enlace a otra página o sitio. |
| `<img src="imagen.jpg" alt="Descripción">` | Imagen dentro de la página. |
| `<ul>`, `<ol>`, `<li>` | Listas desordenadas (`ul`) y ordenadas (`ol`) con ítems (`li`). |
| `<div>` | Contenedor genérico para agrupar elementos. |
| `<span>` | Contenedor en línea para aplicar estilo a una parte del texto. |
| `<br>` | Salto de línea. |
| `<strong>` y `<em>` | Resaltan texto: fuerte (negrita) o enfatizado (cursiva). |
| `<form>`, `<input>`, `<button>` | Elementos para formularios interactivos. |
| `<table>`, `<tr>`, `<td>` | Estructura para mostrar datos en tablas. |

---

## 📌 Ejemplo de Estructura Básica

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Mi primera página</title>
</head>
<body>
  <h1>Hola Mundo</h1>
  <p>Esta es mi primera página con HTML.</p>
</body>
</html>