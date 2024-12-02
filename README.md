# Prueba Técnica Taurus  
**Autor:** David Cardona Duque  

En este documento se describe cómo se resolvieron los puntos propuestos en la prueba técnica y se incluye evidencia correspondiente. Además, se proporcionan instrucciones para la ejecución del proyecto.  

---

## Estructura del Proyecto  

### 1. Creación de la base de datos en MariaDB o MySQL  
Con base en los archivos CSV enviados en el archivo comprimido, se desarrolló una base de datos utilizando MariaDB.  

- **Descripción:**  
Se crearon dos scripts en Python utilizando la librería `Databases` para gestionar la base de datos:  
  1. **`database_creation.py`**: Define las tablas necesarias.  
  2. **`database_population.py`**: Realiza las conversiones de datos desde los CSV para asegurar el formato correcto y los inserta en la base de datos.  

- **Ejecución:**  
  1. Los scripts se encuentran en la carpeta `src/`.  
  2. Desde la terminal, estando en el directorio raíz del proyecto (`PruebaTaurus`), ejecute el siguiente comando:  
     ```bash
     python -m src.database_creation
     ```  
  3. Los archivos CSV se encuentran en `src/data`, mientras que las configuraciones, como variables de entorno y el logger, están en la carpeta de configuración.  

### 2. Desarrollo de un microservicio con FastAPI  
Se implementó un microservicio en **FastAPI**, utilizando **SQLAlchemy** como ORM, debido a su integración sólida con este framework.  

- **Estructura del Proyecto:**  
  La carpeta principal del backend es `src/app`, organizada de la siguiente manera:  
  - **`CRUD/`**: Contiene archivos Python responsables de la lógica de las operaciones para la API, como:  
    - Agrupamientos.  
    - Visualizaciones.  
    - Operaciones CRUD (crear, leer, actualizar y eliminar) para cada tabla.  
  - **`routers/`**: Maneja los enrutadores del proyecto.  
  - **Archivos en la raíz de `src/app/`:**  
    - `database.py`: Configuración de la conexión a la base de datos.  
    - `models.py`: Definición de los modelos de SQLAlchemy.  
    - `schemas.py`: Esquemas de Pydantic para validación, serialización y documentación.  

- **Documentación:**  
  La documentación de la API está disponible en:  
  - **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).  
  - **Redoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc).  

- **Ejecución del Proyecto:**  
  1. Asegúrese de activar el entorno virtual de Python.  
  2. En la terminal, dentro de la carpeta `src/app`, ejecute:  
     ```bash
     uvicorn app.main:app --reload
     ```  


![image](https://github.com/user-attachments/assets/efedd5fa-5eef-4d2c-aad2-365252a032c8)

![image](https://github.com/user-attachments/assets/4360fc34-0794-44fa-bbd9-d0887db23ed3)

![image](https://github.com/user-attachments/assets/1c963d7b-2e1a-4c09-ae67-18b30a06b41b)

**Determinar las siguientes columnas en un query**

Para esto se crea la ruta reports/metrics donde se devuélvelo pedido.

![image](https://github.com/user-attachments/assets/ea0e84a3-675e-4090-947f-65932da4f6aa)

**Crear agrupamiento por**

Para esto se crean las rutas:
•	groupings/by_company
•	/groupings/by_company
•	/groupings/by_state

![image](https://github.com/user-attachments/assets/b12ec54b-0dac-4dc7-b1e6-1d5b6c2b49fb)

---

## Desarrollo del Proyecto en React  

Para este proyecto, se implementó una aplicación en React que interactúa con las rutas del backend para obtener los datos necesarios para las tablas y visualizaciones.  

### Estructura del Proyecto React  
El código de la aplicación React se encuentra en una carpeta dedicada dentro del directorio principal de **PruebaTaurus**, con la siguiente estructura básica:  
- **Directorio:** `PruebaTaurus/react`.  
- **Funcionalidad principal:**  
  - Consumir las rutas del backend implementadas con FastAPI para obtener los datos necesarios.  
  - Presentar dichos datos en tablas y visualizaciones.  

### Ejecución del Proyecto  
1. **Pre-requisitos:**  
   - Asegúrese de que el backend esté ejecutándose (vea las instrucciones en el apartado anterior).  
   - Instale las dependencias del proyecto si no lo ha hecho previamente, ejecutando:  
     ```bash
     npm install
     ```  

2. **Ejecutar React:**  
   - Abra una terminal y navegue a la carpeta del proyecto React:  
     ```bash
     cd PruebaTaurus/react
     ```  
   - Inicie la aplicación con el comando:  
     ```bash
     npm run start
     ```  
![image](https://github.com/user-attachments/assets/e9eb8f94-f40f-4d7e-ba43-ddde875be187)

### Notas Importantes  
- Es imprescindible que el backend esté corriendo simultáneamente para que las rutas consumidas por la aplicación React estén disponibles.  
- La aplicación React está configurada para ejecutarse en el puerto por defecto ( `http://localhost:3000`).  
- Si se desea personalizar el consumo de las rutas o los estilos de las tablas y visualizaciones, consulte los archivos correspondientes en la carpeta `src` del proyecto React.  
