# Proyecto-1: Sistema de Registro Académico

Este proyecto simula un sistema básico de gestión académica. Permite administrar usuarios, cursos y evaluaciones mediante operaciones que reflejan procesos comunes en entornos universitarios.

## Funcionalidades actuales

**1. Crear examen**  
Permite asignar una evaluación a un curso. Se define el tipo, la fecha y el curso destino.

**2. Inscribir usuario a curso**  
Asocia un usuario a un curso existente, validando que no esté inscrito previamente.

**3. Registrar notas**  
Asigna una nota a una evaluación específica para un usuario. Verifica que el usuario esté inscrito y que la evaluación exista.

**4. Ver cursos por usuario**  
Muestra todos los cursos en los que un usuario está inscrito, incluyendo nombre, código y sección.

**5. Ver evaluaciones por curso**  
Lista todas las evaluaciones asignadas a un curso, con tipo, fecha y estado de calificación.

**6. Mostrar cursos asignados al usuario actual**  
Filtra los cursos según el usuario activo. Simula una vista personalizada del estudiante.

## Estructura del código

- `avance_1.py`: Contiene la lógica principal del sistema.
- `README.md`: Documentación del proyecto.

## Próximas funciones sugeridas

- Ver evaluaciones pendientes por usuario
- Crear nueva evaluación
- Ver historial académico del usuario
- Exportar datos a archivo `.txt` o `.csv`
- Separar funciones en módulos (`usuarios.py`, `cursos.py`, `evaluaciones.py`)

## Autor

- Luis Gerardo yo
- Otro x1
- El otro x2
Universidad Rafael Landívar  
Proyecto académico