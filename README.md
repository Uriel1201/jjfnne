```
sql-data-warehouse-project/
│
├── datasets/                           # Datos en crudo usados en el proyecto (datos del ERP y del CRM)
│   ├── source_crm/                     # cust_info.csv, prd_info.csv, sales_details.csv
│   └── source_erp/                     # CUST_AZ12.csv, LOC_A101.csv, PX_CAT_G1V2.csv
│
├── docs/                               # Documentación del proyecto
│   ├── data_catalog.md                 # Catálogo de la capa gold: tablas, columnas y descripciones
│   ├── diagrams.md                     # Arquitectura, flujo de datos, integración y modelo de datos
│   └── naming_conventions.md           # Reglas de nombres para tablas, columnas y archivos
│
├── scripts/                            # Scripts SQL de ETL y transformaciones
│   ├── init_database.sql               # Crea la base de datos DataWarehouse y sus esquemas
│   ├── bronze/                         # DDL y procedimiento de carga de la capa bronze
│   ├── silver/                         # DDL y procedimiento de carga de la capa silver
│   └── gold/                           # Vistas de la capa gold (esquema estrella)
│
├── tests/                              # Pruebas de calidad de datos para silver y gold
│
├── README.md
├── LICENSE
└── .gitignore
```
