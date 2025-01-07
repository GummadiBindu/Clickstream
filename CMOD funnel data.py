# Databricks notebook source

df=spark.read.table('development.consumer_online_behavior_ebi.experience_funnel_daily_ebi_viz_qa_v1')
display(df)



# COMMAND ----------

df = spark.read.table("published_analytics.consumer_online_behavior.experience_funnel_daily_v")
df.show()
