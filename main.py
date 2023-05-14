from pyspark.sql import SparkSession
from pyspark.sql.functions import col

S3_DATA_SOURCE_PATH = 's3://adbproj1/data-input/houseRent.csv'
S3_DATA_OUTPUT_PATH = 's3://adbproj1/data-output'


def main():

    spark = SparkSession.builder.appName('ADBMSProject').getOrCreate()

    all_data = spark.read.csv(S3_DATA_SOURCE_PATH,header=True)

    print('Total number of records in the source data :%s' % all_data.count())
    
    selected_data = all_data.where((col('beds') == 2) & (col('sqfeet')>1500))
    print('Total number of beds with 2 and sqfeet > 1500 are :%s'%selected_data.count())

    selected_data = all_data.where((col('beds') == 1) & (col('sqfeet')>1500))
    print('Total number of beds with 1 and sqfeet > 1500 are  :%s',selected_data.count())

    selected_data = all_data.where((col('baths')==1) & (col('type')=='apartment'))
    print('Total number of baths = 1 with type is apartment : %s', selected_data.count())

    selected_data = all_data.where((col('baths')==2) & (col('type')=='house'))
    print('Total number of baths=2 with type is house : %s', selected_data.count())

    selected_data = all_data.where((col('baths')==1) & (col('type')=='townhouse'))
    print('Total number of baths=2 with type is townhouse : %s', selected_data.count())

    selected_data = all_data.where(col('parking_options').isin(['attached garage', 'street parking', 'off-street parking']))
    print('Total number of records with parking options of attached garage, street parking, or off-street parking: %s' % selected_data.count())

     # select data where state = 'CA' and price < 3000
    selected_data = all_data.where((col('state') == 'ca') & (col('price') < 3000))
    print('Total number of records where state = "CA" and price < 3000: %s' % selected_data.count())

     # select data where cats_allowed = true and dogs_allowed = true and smoking_allowed = false
    selected_data = all_data.where((col('cats_allowed') == 1) & (col('dogs_allowed') == 1) & (col('smoking_allowed') == 1))
    print('Total number of records where cats_allowed = 1, dogs_allowed = 1, and smoking_allowed = 1: %s' % selected_data.count())

    selected_data.write.mode('overwrite').parquet(S3_DATA_OUTPUT_PATH)
    print('selected data is successfully  saved to s3 : %s' % S3_DATA_OUTPUT_PATH)


if __name__ == '__main__' :
    main() 
