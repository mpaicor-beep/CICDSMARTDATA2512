# Databricks notebook source
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql import functions as F

# COMMAND ----------

dbutils.widgets.text("catalogo", "catalog_dev_costos")
dbutils.widgets.text("esquema_source", "silver")
dbutils.widgets.text("esquema_sink", "golden")

# COMMAND ----------

catalogo = dbutils.widgets.get("catalogo")
esquema_source = dbutils.widgets.get("esquema_source")
esquema_sink = dbutils.widgets.get("esquema_sink")

# COMMAND ----------

df_costos_transformed = spark.table(f"{catalogo}.{esquema_source}.costos_transformed")

# COMMAND ----------

df_transformed = df_costos_transformed.groupBy(col("continente")).agg(
                                                     sum(col("suma_costo")).alias("consumo_total_dolar")
                                                     ).orderBy(col("continente").desc())

# COMMAND ----------

df_transformed.write.mode("overwrite").saveAsTable(f"{catalogo}.{esquema_sink}.golden_costos_partitioned")
