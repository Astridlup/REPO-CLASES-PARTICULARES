# Estructura básica de una página web en HTML

Este es un ejemplo **muy simple** de cómo se arma la estructura base de una página web usando solamente HTML, sin estilos (CSS) ni scripts (JavaScript).

## Estructura general

Una página web básica suele tener tres partes principales:

- `header`: la parte de arriba, donde suele ir el título, el logo o el menú.
- `main`: el contenido principal de la página.
- `footer`: la parte de abajo, donde va información extra como derechos de autor o enlaces de contacto.

## Código de ejemplo

```html
<!DOCTYPE html>
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <title>Mi página básica</title>
  </head>
  <body>
    <header>
      <h1>Bienvenidos a mi página</h1>
      <p>Este es el encabezado</p>
    </header>

    <main>
      <h2>Contenido principal</h2>
      <p>Acá va el contenido importante de la página.</p>
    </main>

    <footer>
      <p>© 2025 Mi página web</p>
    </footer>
  </body>
</html>
