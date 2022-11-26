# HTTP:
Pasos regulares para agregar una nueva tarea:
- HTTP Request /add
- [SERVER] se recibe la solicitud y se inserta la tarea en la DB. Se retorna una redireccion.
- [CLIENTE] recibe la respuesta (redireccion)
- HTTP Request /
- [SERVER] se recibe la solicitud. Se extraen todas las tareas de la DB.
- [SERVER] se renderiza un HTML con todas las tareas.
- [SERVER] se le responde al cliente, con el HTML completo.
- [CLIENTE] recibe la respuesta y lo pinta.

# XHTTP:
```
XML HTTP Request (XHR)
(El servidor va a usar el mismo HTTP Respone)
```
- XHR /add
- [SERVER] recibe e inserta. Responde con un OK.
- [CLIENTE] recibe la respuesta y pinta la última tarea enviada.


