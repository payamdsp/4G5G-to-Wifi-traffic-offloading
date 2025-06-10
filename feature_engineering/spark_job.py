from pyspark.sql import SparkSession

def main():
    spark = SparkSession.builder.appName("FeatureEngineering").getOrCreate()
    df = spark.read.json("s3://your-bucket/raw_data/")
    df.createOrReplaceTempView("raw_data")
    features = spark.sql("""
        SELECT
            device_id,
            AVG(biometrics.touch_pressure) AS avg_touch_pressure,
            AVG(biometrics.swipe_speed) AS avg_swipe_speed,
            FIRST(context.network_type) AS network_type
        FROM raw_data
        GROUP BY device_id, context.network_type
    """)
    features.write.parquet("s3://your-bucket/features/", mode="overwrite")
    spark.stop()

if __name__ == "__main__":
    main()