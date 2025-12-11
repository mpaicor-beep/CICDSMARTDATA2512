# Databricks notebook source
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql import functions as F
from pyspark.sql.functions import year, current_date, col, sum as Fsum

# COMMAND ----------

dbutils.widgets.text("catalogo", "catalog_dev_costos")
dbutils.widgets.text("esquema_source", "bronze")
dbutils.widgets.text("esquema_sink", "silver")

# COMMAND ----------

catalogo = dbutils.widgets.get("catalogo")
esquema_source = dbutils.widgets.get("esquema_source")
esquema_sink = dbutils.widgets.get("esquema_sink")

# COMMAND ----------

def pais_clasifica(sede):  
    if sede == "Sede A":
        return "Peru"
    elif sede in ["Sede B", "Sede C"]:
        # Aquí puedes poner la nueva lógica que sustituya la altitud
        return "USA"  # Por ejemplo
    else:
        return "Colombia"

# COMMAND ----------

pais_udf = F.udf(pais_clasifica, StringType())

# COMMAND ----------

df_proyectos = spark.table(f"{catalogo}.{esquema_source}.proyectos")
df_consumo = spark.table(f"{catalogo}.{esquema_source}.consumo").withColumnRenamed("year","anio")

# COMMAND ----------

df_proyectos = df_proyectos.dropna(how="all")\
                        .filter((col("recurso").isNotNull()) | (col("nombre")).isNotNull())

df_consumo = df_consumo.dropna(how="all")\
                    .filter((col("costo").isNotNull()) | (col("fecha")).isNotNull())

# COMMAND ----------

df_proyectos = df_proyectos.withColumn("pais_clasifica", pais_udf("sede"))

# COMMAND ----------

df_joined = df_proyectos.alias("x").join(df_consumo.alias("y"), col("x.recurso") == col("y.recurso"), "inner")

# COMMAND ----------

df_consumo.display()

# COMMAND ----------

df_filtered_sorted = df_joined.filter(df_consumo["anio"] == 2025).orderBy("anio")

# COMMAND ----------

df_aggregated = df_filtered_sorted.groupBy("sede").agg(
    Fsum("costo").alias("suma_costo")
)

# COMMAND ----------

df_updated = df_aggregated.select("*",
                                    when(col("sede").isin("Sede A","Sede B","Sede C"), lit("America")).otherwise("Asia").alias("continente"))

# COMMAND ----------

df_updated.write.mode("overwrite").saveAsTable(f"{catalogo}.{esquema_sink}.costos_transformed")
