# UniProt JSON fields for P52789

Source file: `data/P52789.json`

## Top-level fields

| Campo | Descripción breve | Relevancia para MolSysSuite |
| --- | --- | --- |
| `primaryAccession` | Accesión principal de UniProt. | Alta (ID canónico para enlazar datos). |
| `uniProtkbId` | Identificador legible de UniProtKB. | Media (útil para UI/ETL, no siempre estable). |
| `entryType` | Tipo de entrada (Swiss‑Prot/TrEMBL). | Alta (calidad de anotación). |
| `secondaryAccessions` | Accesiones secundarias. | Media (trazabilidad/alias). |
| `entryAudit` | Metadatos de curación/actualización. | Media (proveniencia). |
| `annotationScore` | Puntaje global de anotación. | Media (priorización de calidad). |
| `proteinExistence` | Evidencia de existencia de proteína. | Media (confianza). |
| `proteinDescription` | Nombres recomendados/alternativos. | Alta (nomenclatura para reportes). |
| `genes` | Genes asociados (nombres, sinónimos). | Alta (mapeo gen‑proteína). |
| `organism` | Especie, taxonomía y linaje. | Alta (contexto biológico). |
| `sequence` | Secuencia y metadatos (longitud, MD5, peso). | Muy alta (núcleo para modelado/estructura). |
| `features` | Anotaciones por región/residuo (e.g. binding sites). | Muy alta (sitios funcionales). |
| `comments` | Anotaciones curadas (función, actividad, pathway, etc.). | Muy alta (interpretación biológica). |
| `keywords` | Términos controlados de UniProt. | Media (indexación/filtrado). |
| `references` | Bibliografía y evidencias. | Media (proveniencia). |
| `uniProtKBCrossReferences` | Links a otras bases (PDB, Pfam, Reactome, etc.). | Muy alta (integración multi‑DB). |
| `extraAttributes` | Atributos adicionales (según entry). | Baja‑Media (caso a caso). |

## Subcampos relevantes (observados en P52789)

- `sequence`: `value`, `length`, `molWeight`, `crc64`, `md5`.
- `organism`: `scientificName`, `commonName`, `taxonId`, `lineage`.
- `proteinDescription`: `recommendedName`, `alternativeNames`.
- `comments` contiene tipos: FUNCTION, CATALYTIC ACTIVITY, PATHWAY, SUBUNIT, SUBCELLULAR LOCATION, DOMAIN, INTERACTION, TISSUE SPECIFICITY, etc.
- `features` contiene tipos y conteos (P52789):
  - Helix (40), Binding site (30), Beta strand (28), Natural variant (13), Turn (10), Region (5), Mutagenesis (3), Domain (2), Sequence conflict (2), Chain (1), Modified residue (1).

## Notas para próximos pasos

- Priorizar parseo de `features` para extraer binding sites, dominios, variantes y modificaciones post‑traduccionales.
- En `comments`, priorizar FUNCTION, CATALYTIC ACTIVITY, PATHWAY, SUBCELLULAR LOCATION y INTERACTION.
- En `uniProtKBCrossReferences`, localizar enlaces a PDB, AlphaFold, Pfam, InterPro, Reactome, etc.
