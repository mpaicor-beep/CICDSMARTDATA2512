# Databricks notebook source
from pyspark.sql.functions import *
from pyspark.sql.types import *

# COMMAND ----------

dbutils.widgets.text("storage_name", "adlssmartdata202512")
dbutils.widgets.text("container", "raw")
dbutils.widgets.text("catalogo", "catalog_dev_costos")
dbutils.widgets.text("esquema", "bronze")

# COMMAND ----------

storage_name = dbutils.widgets.get("storage_name")
container = dbutils.widgets.get("container")
catalogo = dbutils.widgets.get("catalogo")
esquema = dbutils.widgets.get("esquema")

ruta = f"abfss://{container}@{storage_name}.dfs.core.windows.net/proyectos.csv"

# COMMAND ----------

proyectos_schema = StructType(fields=[StructField("Recurso", StringType(), True),
                                     StructField("Nombre", StringType(), True),
                                     StructField("Proyecto", StringType(), True),
                                     StructField("Sede", StringType(), True),
                                     StructField("FechaRegistro", DateType(), True),
                                     StructField("Estado", IntegerType(), True)
])

# COMMAND ----------

proyectos_df = spark.read \
            .option("header", True) \
            .option("sep", ";") \
            .option("dateFormat", "dd/MM/yyyy") \
            .schema(proyectos_schema) \
            .csv(ruta)

# COMMAND ----------

# DBTITLE 1,Use user specified schema to load df with correct types
proyectos_with_timestamp_df = proyectos_df.withColumn("ingestion_date", current_timestamp())


# COMMAND ----------

# DBTITLE 1,select only specific cols
proyectos_selected_df = proyectos_with_timestamp_df.select(col('Recurso'), 
                                                   col('Nombre'), 
                                                   col('Proyecto'),
                                                   col('Sede'),
                                                   col('FechaRegistro'),
                                                   col('Estado'))



# COMMAND ----------

proyectos_selected_df.write.mode("overwrite").saveAsTable(f"{catalogo}.{esquema}.proyectos")
