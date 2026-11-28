# Fundamentos de Internet 

## 1. Del Cliente al Servidor

Cuando escribo "www.youtube.com" en el navegador y presiono Enter, pasa lo siguiente:

1. **El cliente (mi navegador) inicia todo.** El navegador es el que pide la página. Primero revisa si ya conoce la dirección de YouTube (en su memoria guardada). Si no, necesita averiguarla.

2. **El DNS traduce el nombre.** Las computadoras no se ubican por nombres como "youtube.com", sino por números. El DNS funciona como una agenda de contactos de internet: le pregunto por "www.youtube.com" y me responde con el número que le corresponde.

3. **La dirección IP.** Ese número es la dirección IP del servidor donde vive YouTube (algo como `142.250.x.x`). Con ella, mi solicitud sabe a qué computadora llegar a través de internet, igual que una dirección de casa le dice al repartidor adónde ir.

4. **El servidor recibe la solicitud y responde.** El servidor es una computadora potente que guarda la página y los videos de YouTube. Recibe mi pedido, busca lo que necesito (la página, los datos del video) y me los envía de vuelta.

5. **HTTP/HTTPS es el idioma de la conversación.** El navegador y el servidor se comunican con reglas llamadas HTTP: yo hago una solicitud (por ejemplo, "dame esta página") y el servidor me da una respuesta. YouTube usa HTTPS, que es lo mismo pero con una capa de seguridad que cifra la información, para que nadie pueda espiarla en el camino.

Finalmente, el navegador recibe esa respuesta, arma la página y empieza a reproducir el video. El video no llega completo de una vez, sino en pedacitos que se van enviando mientras lo veo.

## 2. Frontend y Backend en acción

Para una app web de citas médicas, dividiría el sistema así:

**Frontend (lo que el usuario ve y toca en su navegador):**
- La pantalla de inicio de sesión.
- El calendario donde el paciente elige día y hora.
- Los formularios (datos del paciente, motivo de la consulta).
- La lista de "Mis citas" y los mensajes de confirmación.

**Backend (lo que pasa "detrás", en el servidor):**
- Guardar y consultar las citas en una base de datos.
- Validar que el horario esté libre y que el doctor atienda ese día.
- Manejar usuarios, contraseñas y permisos (un paciente no puede ver las citas de otro).
- Enviar correos o recordatorios de confirmación.

**Tecnologías posibles:**

| Frontend | Backend |
|----------|---------|
| HTML, CSS y JavaScript | Node.js (con Express) |
| React | Python (con Django o Flask) |
| Vue.js | Java (con Spring Boot) |

**¿Cómo se comunican?**

El frontend y el backend se hablan a través de una **API**, que es como el mesero de un restaurante: el cliente (frontend) no entra a la cocina (backend), sino que le hace el pedido al mesero y este le trae la respuesta.

Esa conversación usa el protocolo **HTTP** y funciona con el esquema **request/response** (solicitud y respuesta). Por ejemplo, cuando un paciente agenda una cita:

1. El frontend envía una **request**: un `POST` a `/api/citas` con los datos (fecha, hora, doctor).
2. El backend la recibe, revisa que el horario esté disponible y guarda la cita en la base de datos.
3. El backend devuelve una **response**: un código `201` (creada) junto con los datos de la cita, normalmente en formato JSON.
4. El frontend lee esa respuesta y le muestra al paciente: "¡Cita confirmada!".

## 3. REST vs SOAP vs GraphQL

| Tipo de API | Formato de datos usado | Nivel de flexibilidad | Dificultad de implementación | Uso actual (Alta / Media / Baja) |
|-------------|------------------------|------------------------|-------------------------------|-----------------------------------|
| REST        | JSON (también XML)     | Media: el servidor define qué devuelve cada endpoint | Baja: fácil de aprender y con muchas herramientas | Alta |
| SOAP        | XML                    | Baja: reglas estrictas y contrato fijo (WSDL) | Alta: más complejo y con mucha configuración | Baja |
| GraphQL     | JSON                   | Alta: el cliente pide exactamente los datos que necesita | Media: requiere definir un esquema y más curva de aprendizaje | Media |

**¿Cuál es más apropiada para una startup moderna? ¿Por qué?**

Para un sistema de reservas en línea, creo que la más apropiada es **REST**. Es sencilla de aprender y de implementar, tiene muchísimas herramientas y documentación, y funciona bien con HTTP y JSON, lo que permite avanzar rápido, algo clave en una startup. Además, las operaciones de un sistema de reservas (consultar disponibilidad, crear, modificar o cancelar una reserva) encajan de forma natural con los endpoints y métodos de REST (`GET`, `POST`, `PUT`, `DELETE`).

GraphQL sería una buena opción más adelante, si la app crece y necesita pedir datos muy variados desde distintas pantallas. SOAP lo descartaría porque es más pesado y rígido, y hoy se usa sobre todo en sistemas antiguos o bancarios.

## 4. Explorando APIs con Postman

### 4.1 Selección de la API
- **Nombre de la API:** JSONPlaceholder
- **Descripción:** API pública y gratuita, sin autenticación, que ofrece datos de prueba falsos (publicaciones, comentarios, usuarios, tareas, álbumes y fotos). Permite practicar solicitudes GET, POST, PUT, PATCH y DELETE. Los cambios se simulan, no se guardan de verdad, por lo que es ideal para aprender.

### 4.2 Configuración en Postman
- **Nombre de la colección:** JSONPlaceholder
- **Solicitudes agregadas:**
  - GET - Obtener publicaciones
  - POST - Crear publicación
  - PUT/PATCH/DELETE - PUT - Actualizar publicación

### 4.3 Ejecución y análisis

| Solicitud | Método | Endpoint | Código de estado | Notas |
|-----------|--------|----------|-------------------|-------|
| Obtener publicaciones | GET | https://jsonplaceholder.typicode.com/posts | 200 OK | Devuelve una lista de 100 publicaciones en JSON. |
| Crear publicación | POST | https://jsonplaceholder.typicode.com/posts | 201 Created | Devuelve lo enviado más un `id` nuevo (101). El dato no se guarda realmente. |
| Actualizar publicación | PUT | https://jsonplaceholder.typicode.com/posts/1 | 200 OK | Devuelve la publicación 1 con los datos modificados. El cambio es simulado. |

### 4.4 Explicación técnica

#### GET - Obtener publicaciones
- **Método HTTP:** GET
- **Endpoint:** `https://jsonplaceholder.typicode.com/posts`
- **Parámetros / body:** No lleva body ni parámetros. Solo se pide la lista de recursos.
- **Descripción de la respuesta:** Devuelve el código 200 OK y un arreglo JSON con 100 publicaciones. Cada una trae `userId`, `id`, `title` y `body`.

#### POST - Crear publicación
- **Método HTTP:** POST
- **Endpoint:** `https://jsonplaceholder.typicode.com/posts`
- **Parámetros / body:** Body en formato JSON (raw) con los datos de la nueva publicación:
  ```json
  {
    "title": "Mi primera publicación. PS",
    "body": "Probando la API con Postman",
    "userId": 1
  }
 - **Descripción de la respuesta:** Devuelve el código 201 Created y el mismo contenido enviado, con un id nuevo (101) asignado por el servidor. Como JSONPlaceholder es una API de prueba, la publicación no se guarda realmente.

#### PUT - Actualizar publicación
 - **Método HTTP:** PUT
- **Endpoint:** `https://jsonplaceholder.typicode.com/posts/1` (El 1 es el id de la publicación a modificar)
- **Parámetros / body:** El id va en la URL, y el body en JSON lleva los datos con la publicación nueva.
  ```json
  {
    "id": 1,
    "title": "Publicación actualizada",
    "body": "Cambiando el contenido con PUT",
    "userId": 1
  }
- **Descripción de la respuesta:** Devuelve el código 200 OK y la publicación 1 con los datos modificados. El cambio es simulado y no queda guardado.

**¿Qué aprendiste del proceso?**

Aprendí cómo se ve en la práctica lo que antes solo había visto en la lección con Alek y leído por mi cuenta: una API recibe una solicitud con un método (GET para pedir, POST para crear, PUT para actualizar) y responde con un código de estado y datos en JSON. Los códigos me ayudaron a entender qué pasó: 200 significa que todo salió bien y 201 que se creó algo nuevo. También vi la diferencia entre un endpoint de lista (/posts) y uno de un solo recurso (/posts/1), y que cuando uso POST o PUT tengo que mandar un body. Por último, Postman me sirvió para probar todo sin escribir código y para guardar las respuestas como examples.

### 4.5 Reflexión final

Con este ejercicio entendí que una API es la forma en que dos programas se comunican: un cliente hace una solicitud a una dirección (endpoint) usando un método HTTP, y el servidor responde con un código de estado y los datos, normalmente en JSON. Antes veía las APIs como algo más abstracto, como que era simplemente acceder a recursos de otro sistema, pero al hacer las pruebas vi que cada método tiene un propósito: GET para pedir información, POST para crear y PUT para actualizar. También entendí que los códigos de estado, como 200 o 201, son la forma que tiene el servidor de decirme si la solicitud salió bien.

Lo que me costó principalmente fue entender la UI de Postman, donde encontrar las herramientas para exportar archivos, cambiar mi workspace a que no fuera uno local o cómo crear las collections para así ejecutar los
request. Espero mejorar en la navegación.

Postman me ayudó a ver esa comunicación de forma práctica. Pude armar cada solicitud, enviarla y ver al instante la respuesta con su código, sus encabezados y su cuerpo sin tener que programar directamente. Eso me permitió entender qué envía el cliente y qué devuelve el servidor, y comparar cómo cambian la solicitud y la respuesta entre un GET, un POST y un PUT. Además, guardar las respuestas como examples me dejó documentar lo que ocurre en cada caso.

Creo que me podría funcionar en el trabajo para revisar endpoints de páginas
y qué me devuelve cada una.