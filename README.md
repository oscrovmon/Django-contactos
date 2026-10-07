# 📇 Agenda de Contactos — Guía de Evaluación y Funcionalidades

Este proyecto es una aplicación web de **Agenda de Contactos** desarrollada con **Python y Django 6.1.1**, utilizando **SQLite** como base de datos y **Bootstrap 5** para la interfaz de usuario. A continuación se detallan las instrucciones para acceder al panel de administración y el resumen de funcionalidades implementadas.

## 🔑 1. Acceso al Panel de Administración

1. **Iniciar el servidor local**:
   
   ```bash
   python manage.py runserver```

2. Abre el navegador y ves a la siguiente URL: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## 🚀 2. Funcionalidades de la Aplicación Web

    Credenciales de acceso (para acceder a todas las funcionalidades como administrador):

        Usuario: Oscar

        Contraseña: (admin123)

👤 **Gestión de Contactos** (CRUD)

    Listado General: Vista principal con tabla limpia e intuitiva que muestra todos los contactos registrados junto con su provincia e imagen (si esta insertada) asociada.

    Creación de Contactos (/contacto/nuevo/): Formulario para añadir nuevos contactos incluyendo campos como Nombre, Teléfono, Email, Provincia (desplegable) e Imagen de perfil.

    Edición de Contactos: Permite modificar la información existente de cualquier contacto registrado.

    Ficha de Detalle: Vista individual con la información completa de cada contacto y su foto.

    Eliminación Segura: Confirmación previa antes de eliminar un registro para evitar borrados accidentales.

🔍 **Buscador y Filtros**

    Búsqueda por texto: Permite buscar contactos en tiempo real por Nombre, Email o Teléfono.

    Filtrado por Provincia: Desplegable interactivo para filtrar el listado según la provincia asociada (Castellón, Valencia, Alicante).

📁 **Gestión de Archivos e Imágenes**

    Manejo dinámico de archivos mediante MEDIA_ROOT y MEDIA_URL con Pillow, permitiendo la subida y visualización directa de las imágenes de perfil de cada contacto.

🛡️ **Autenticación y Seguridad**

    Sistema de Autenticación Integrado: Control de acceso que muestra el estado de sesión activo ("Hola, Oscar").

    Cerrar Sesión Seguro (POST): Botón de Logout adaptado a las especificaciones de seguridad de Django que procesa la desconexión mediante peticiones POST cifradas con CSRF token.

   **Conversación con la IA**

   Este es el link para revisar la conversación que tuve con la IA para crear la página web:

   https://share.gemini.google/Xr9VBay8EQVQ

   **Óscar Rovira Montes**
