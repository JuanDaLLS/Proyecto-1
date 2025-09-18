# Proyecto-1: Sistema de Registro Académico

Este proyecto simula un sistema básico de gestión académica. Permite administrar usuarios, cursos y evaluaciones mediante operaciones que reflejan procesos comunes en entornos universitarios

## Funcionalidades actuales

**1. Agregar nuevo usuario**  
Se agrega un nuevo usuario al sistema, se solicita carne, nombre, edad, correo, tipo (profesor /estudiante).

**2. Ver todos los usuarios**  
Se muestra una lista de usuarios registrados en el sistema. 
**3. Agregar curso**  
Se agrega un curso a la lista añadiendo nombre de curso, cupo y carnet del docente. 

**4. Listar cursos**  
Muestra los cursos existentes. 

**5. Inscribir usuario a curso**  
Asocia un usuario a un curso existente, validando que no esté inscrito previamente.

**6. Crear evaluacion**  
Permite asignar una evaluación a un curso. Se define el tipo, la fecha y el curso destino.

**7. Registrar notas**  
Asigna una nota a una evaluación específica para un usuario. Verifica que el usuario esté inscrito y que la evaluación exista.

**8. Mostrar cursos asignados al usuario actual**  
Filtra los cursos según el usuario activo. Simula una vista personalizada del estudiante.

**9. Mostrar promedios bajos**  
Muestra a los docentes los alumnos con un promedio bajo. 

**10. salir**  
Se finaliza la ejecucion del programa. 

## Estructura del código

- `avance_1.py`: Contiene la lógica principal del sistema.
- `README.md`: Documentación del proyecto.


## Autor

- Luis Gerardo
- Fernando Mendez
- Juan Ulin
Universidad Rafael Landívar  
Proyecto académico

## Requisitos

Este sistema requiere de la librería `colorama` para mostrar el menú con colores en consola.

### Instalación de dependencias

Ejecutar en terminal:

```bash
pip install colorama
