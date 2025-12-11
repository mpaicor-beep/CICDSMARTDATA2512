-- Databricks notebook source
-- MAGIC %python
-- MAGIC dbutils.widgets.removeAll()

-- COMMAND ----------

create widget text storageName default "adlssmartdata202512";

-- COMMAND ----------

CREATE CATALOG IF NOT EXISTS catalog_dev_costos;

-- COMMAND ----------

CREATE SCHEMA IF NOT EXISTS catalog_dev_costos.bronze;
CREATE SCHEMA IF NOT EXISTS catalog_dev_costos.silver;
CREATE SCHEMA IF NOT EXISTS catalog_dev_costos.golden;


-- COMMAND ----------

CREATE EXTERNAL LOCATION IF NOT EXISTS `exlt-bronze`
URL 'abfss://bronze@${storageName}.dfs.core.windows.net/'
WITH (STORAGE CREDENTIAL credential)
COMMENT 'Ubicación externa para las tablas bronze del Data Lake';

-- COMMAND ----------

CREATE EXTERNAL LOCATION IF NOT EXISTS `exlt-silver`
URL 'abfss://silver@${storageName}.dfs.core.windows.net/'
WITH (STORAGE CREDENTIAL credential)
COMMENT 'Ubicación externa para las tablas bronze del Data Lake';

-- COMMAND ----------

CREATE EXTERNAL LOCATION IF NOT EXISTS `exlt-golden`
URL 'abfss://golden@${storageName}.dfs.core.windows.net/'
WITH (STORAGE CREDENTIAL credential)
COMMENT 'Ubicación externa para las tablas bronze del Data Lake';
