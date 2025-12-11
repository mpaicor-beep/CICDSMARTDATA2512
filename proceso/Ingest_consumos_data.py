# Databricks notebook source
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, DateType,FloatType
from pyspark.sql.functions import current_timestamp, to_timestamp, concat, col, lit

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

ruta = f"abfss://{container}@{storage_name}.dfs.core.windows.net/consumos.csv"

# COMMAND ----------

consumo_schema = StructType(fields=[StructField("Recurso", StringType(), True),
                                  StructField("IdSuscripcion", StringType(), True),
                                  StructField("Costo", FloatType(), True),
                                  StructField("Fecha", DateType(), True),
                                  StructField("Year", IntegerType(), True) 
])

# COMMAND ----------

consumo_df = spark.read \
            .option("header", True) \
            .option("sep", ";") \
            .option("dateFormat", "dd/MM/yyyy") \
            .schema(consumo_schema) \
            .csv(ruta)


# COMMAND ----------

consumo_df.display()

# COMMAND ----------

consumo_with_timestamp_df = consumo_df.withColumn("ingestion_date", current_timestamp())

# COMMAND ----------

consumo_selected_df = consumo_with_timestamp_df.select(col('Recurso').alias('recurso'), 
                                                   col('IdSuscripcion').alias('subcripcion'), 
                                                   col('Costo').alias('costo'),
                                                   col('Fecha').alias('fecha'),
                                                   col('Year').alias('year'))

# COMMAND ----------

consumo_selected_df.write.mode('overwrite').partitionBy('year').saveAsTable(f'{catalogo}.{esquema}.consumo')
