# molsysdbs — checkpoint

## Qué queremos (objetivo del proyecto)
- Crear una librería Python llamada `molsysdbs` para recopilar información de proteínas desde bases de datos públicas (PDB, UniProt, y más en el futuro).
- Primer objetivo funcional: dado un `pdb_id`, descargar el fichero **mmCIF** correspondiente desde PDB.
- Segundo objetivo funcional (siguiente fase): dado un `uniprot_id`, descargar el **JSON** de UniProt y, más adelante, extraer información (ej. binding sites y otros campos).
- Requisitos de calidad: tests con **pytest** y documentación con **Sphinx** desde el principio, siguiendo estándares de librerías científicas open‑source.

## Dónde estamos (estado actual)
- Se creó el esqueleto de la librería con dos módulos principales: `pdb` y `uniprot`.
- Se decidió usar **mmCIF** para PDB y **JSON** para UniProt.
- Se acordó validar y normalizar los identificadores de entrada (`pdb_id`, `uniprot_id`).
- Se usó **stdlib** (urllib) en lugar de dependencias externas como `requests`.

## Qué se ha implementado (archivos clave)
- `pyproject.toml`: configuración del paquete, dependencias opcionales `dev` (pytest, sphinx).
- `molsysdbs/__init__.py`: exporta funciones y excepciones públicas.
- `molsysdbs/errors.py`: excepciones personalizadas.
- `molsysdbs/_http.py`: helper para descargar URLs con `urllib`.
- `molsysdbs/pdb.py`: validación `pdb_id` + `download_mmcif()`.
- `molsysdbs/uniprot.py`: validación `uniprot_id` + `download_uniprot_json()`.
- `tests/test_pdb.py`: tests básicos para validación y descarga simulada.
- `tests/test_uniprot.py`: tests básicos para validación y descarga simulada.
- `docs/conf.py` y `docs/index.rst`: documentación Sphinx mínima.
- `README.md`: descripción y quick start.

## Qué es lo próximo
1) Confirmar reglas de validación:
   - UniProt: decidir si usar regex oficial (más estricta) o mantener validación flexible (6 o 10 caracteres alfanuméricos).
2) Elegir 1–2 accesiones UniProt “modelo” para explorar el JSON real cuando haya permiso de red.
3) Definir el primer parser/estructura para extraer información del JSON (features, binding sites, etc.).
4) (Opcional) Añadir caché local por defecto si se desea.

## Pendiente de decidir / discutir más tarde
- Dependencias: seguir con `urllib` o permitir `requests`.
- Política de caché y ubicación por defecto para descargas.
- Definición exacta del “API público” final (funciones vs clases/cliente), aunque ya hay funciones simples.
- Alcance de datos UniProt a extraer (“todo lo que se pueda”): se aplazó hasta inspeccionar un JSON real.
- Integración futura con otras bases de datos.

## Notas operativas
- El código fuente está en el directorio `molsysdbs/` (no se usa `src/`).
- Tests: `pytest`
- Docs: `sphinx-build -b html docs docs/_build`
