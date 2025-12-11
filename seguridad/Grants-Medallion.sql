-- Databricks notebook source
GRANT SELECT ON TABLE catalog_dev_costos.bronze.consumo TO `DataEngineers`;
GRANT SELECT ON TABLE catalog_dev_costos.bronze.proyectos TO `DataEngineers`;
GRANT SELECT ON TABLE catalog_dev_costos.silver.costos_transformed TO `DataEngineers`;
GRANT SELECT ON TABLE catalog_dev_costos.golden.golden_costos_partitioned TO `DataEngineers`;


-- COMMAND ----------

GRANT USE CATALOG ON CATALOG catalog_dev_costos TO `DataEngineers`;

-- COMMAND ----------

GRANT USE SCHEMA ON SCHEMA catalog_dev_costos.bronze TO `DataEngineers`;
GRANT CREATE ON SCHEMA catalog_dev_costos.bronze TO `DataEngineers`;

-- COMMAND ----------

GRANT SELECT ON TABLE catalog_dev_costos.bronze.consumo TO `DataEngineers`;
GRANT SELECT ON TABLE catalog_dev_costos.bronze.proyectos TO `DataEngineers`;
GRANT SELECT ON TABLE catalog_dev_costos.silver.costos_transformed TO `DataEngineers`;
GRANT SELECT ON TABLE catalog_dev_costos.golden.golden_costos_partitioned TO `DataEngineers`;

GRANT CREATE ON CATALOG catalog_dev_costos TO `DataEngineers`;
GRANT SELECT ON CATALOG catalog_dev_costos TO `DataEngineers`;


-- COMMAND ----------

SHOW GRANTS ON TABLE catalog_dev_costos.bronze.consumo;
SHOW GRANTS ON TABLE catalog_dev_costos.bronze.proyectos;
SHOW GRANTS ON TABLE catalog_dev_costos.silver.costos_transformed;
SHOW GRANTS ON TABLE catalog_dev_costos.golden.golden_costos_partitioned;


-- COMMAND ----------

SHOW GRANTS ON SCHEMA catalog_dev_costos.bronze;

-- COMMAND ----------

SHOW GRANTS ON CATALOG catalog_dev_costos;
