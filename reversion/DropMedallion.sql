-- Databricks notebook source
-- MAGIC %python
-- MAGIC dbutils.widgets.removeAll()

-- COMMAND ----------

-- MAGIC %python
-- MAGIC dbutils.widgets.text("storageName","adlssmartdata202512")
-- MAGIC dbutils.widgets.text("containerName","raw")
-- MAGIC dbutils.widgets.text("catalogo","catalog_dev_costos")

-- COMMAND ----------

-- MAGIC %python
-- MAGIC
-- MAGIC storageName = dbutils.widgets.get("storageName")
-- MAGIC containerName = dbutils.widgets.get("containerName")
-- MAGIC catalogo = dbutils.widgets.get("catalogo")
-- MAGIC
-- MAGIC ruta = f"abfss://{containerName}@{storageName}.dfs.core.windows.net"

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### Eliminacion tablas Bronze

-- COMMAND ----------

-- DROP TABLES
DROP TABLE IF EXISTS catalog_dev_costos.bronze.consumo;
DROP TABLE IF EXISTS catalog_dev_costos.bronze.proyectos;

-- COMMAND ----------

-- MAGIC %python
-- MAGIC ## REMOVE DATA (Bronze)
-- MAGIC dbutils.fs.rm(f"{ruta}/consumo", True)
-- MAGIC dbutils.fs.rm(f"{ruta}/proyectos", True)

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### Eliminacion tablas Silver

-- COMMAND ----------

-- DROP TABLES
DROP TABLE IF EXISTS catalog_dev_costos.silver.costos_transformed;

-- COMMAND ----------

-- MAGIC %python
-- MAGIC # REMOVE DATA (Silver)
-- MAGIC dbutils.fs.rm(f"{ruta}/costos_transformed", True)

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### Eliminacion tablas Golden

-- COMMAND ----------

-- DROP TABLES
DROP TABLE IF EXISTS catalog_dev_costos.golden.golden_costos_partitioned;

-- COMMAND ----------

-- MAGIC %python
-- MAGIC # REMOVE DATA (Golden)
-- MAGIC dbutils.fs.rm(f"{ruta}/golden_costos_partitioned", True)
-- MAGIC
