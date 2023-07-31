# This query creates or replaces a new table named tbl_analytics in the dataset 'data-with-soham.uber_data_engineering_yt'.
CREATE OR REPLACE TABLE `data-with-soham.uber_data_engineering_yt.tbl_analytics` AS (

# This is the SELECT statement that retrieves data from multiple tables and joins them together.
SELECT 
    f.trip_id,
    f.VendorID,
    d.tpep_pickup_datetime,
    d.tpep_dropoff_datetime,
    p.passenger_count,
    t.trip_distance,
    r.rate_code_name,
    pick.pickup_latitude,
    pick.pickup_longitude,
    drop.dropoff_latitude,
    drop.dropoff_longitude,
    pay.payment_type_name,
    f.fare_amount,
    f.extra,
    f.mta_tax,
    f.tip_amount,
    f.tolls_amount,
    f.improvement_surcharge,
    f.total_amount
FROM 

# The main table 'fact_table' is aliased as 'f'.
`data-with-soham.uber_data_engineering_yt.fact_table` f

# The fact table 'f' is joined with the 'datetime_dim' table using the 'datetime_id' key to get pickup and dropoff timestamps.
JOIN `data-with-soham.uber_data_engineering_yt.datetime_dim` d  ON f.datetime_id=d.datetime_id

# The fact table 'f' is joined with the 'passenger_count_dim' table using the 'passenger_count_id' key to get passenger count information.
JOIN `data-with-soham.uber_data_engineering_yt.passenger_count_dim` p  ON p.passenger_count_id=f.passenger_count_id

# The fact table 'f' is joined with the 'trip_distance_dim' table using the 'trip_distance_id' key to get trip distance information.
JOIN `data-with-soham.uber_data_engineering_yt.trip_distance_dim` t  ON t.trip_distance_id=f.trip_distance_id

# The fact table 'f' is joined with the 'rate_code_dim' table using the 'rate_code_id' key to get rate code information.
JOIN `data-with-soham.uber_data_engineering_yt.rate_code_dim` r ON r.rate_code_id=f.rate_code_id

# The fact table 'f' is joined with the 'pickup_location_dim' table using the 'pickup_location_id' key to get pickup location information.
JOIN `data-with-soham.uber_data_engineering_yt.pickup_location_dim` pick ON pick.pickup_location_id=f.pickup_location_id

# The fact table 'f' is joined with the 'dropoff_location_dim' table using the 'dropoff_location_id' key to get dropoff location information.
JOIN `data-with-soham.uber_data_engineering_yt.dropoff_location_dim` drop ON drop.dropoff_location_id=f.dropoff_location_id

# The fact table 'f' is joined with the 'payment_type_dim' table using the 'payment_type_id' key to get payment type information.
JOIN `data-with-soham.uber_data_engineering_yt.payment_type_dim` pay ON pay.payment_type_id=f.payment_type_id
)
;
