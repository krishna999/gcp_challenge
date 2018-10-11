# gcp_challenge

1. Pull current data for all cryptocurrencies using the CoinMarketCap API
2. Save this data as a CSV file

   import_coin_data.py imports data from the coinmarketcap via API and saves as csv.
   
3. Upload the CSV to a Google Cloud Storage Bucket

  upload_coinmarketcap_gcs.py moves the csv to the bucket gs://coinmarketcap-2018/crypto.csv
  
4. Move cryptocurrency data from GCS bucket to BigQuery
   
   dags/upload_coinmarketcap_bq.py is a composer dag that imports the csv to BigQuery Table using bq load bash operation.
   
   * gcloud composer create is used to create a new composer environment with the appropriate flags.
   
5. coinmarketbase.ipynb contains the notebook with all bq queries.


Rationale for using composer:
Eventhough it is easy to write another script to pull the csv to bq, composer can make this task repeatable and schedule this based on time intervals and has a nice visual interface of data pipeline.

