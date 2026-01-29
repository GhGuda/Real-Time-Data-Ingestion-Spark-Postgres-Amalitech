def write_to_postgres(df, url, table, user, password):
    (
        df.write
        .format("jdbc")
        .option("url", url)
        .option("dbtable", table)
        .option("user", user)
        .option("password", password)
        .mode("append")
        .save()
    )
