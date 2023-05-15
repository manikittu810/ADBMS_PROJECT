#starting the spark session
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

#input source data path in s3 bucket
S3_DATA_SOURCE_PATH = 's3://classnow/class1/houseRent.csv'

# creating a folder which can store the output files in the s3 bucket
S3_DATA_OUTPUT_PATH = 's3://classnow/in_class_output'


def main():

    spark = SparkSession.builder.appName('ADBMSProject').getOrCreate()

    all_data = spark.read.csv(S3_DATA_SOURCE_PATH,header=True) # reading the input file 

    print('Total number of records in the source data :%s' % all_data.count()) # prints all the records in the input file


#These are the queries and used print statements for each query to print the query output
    selected_data = all_data.where((col('beds') == 2) & (col('sqfeet')>1500))

    print('Total number of beds with 2 are :%s'%selected_data.count())



    selected_data = all_data.where((col('beds') == 1) & (col('sqfeet')>1500))

    print('Total number of beds with 1 are :%s'%selected_data.count())




    selected_data = all_data.where((col('baths')==1) & (col('type')=='apartment'))

    print('Total number of baths = 1 with type is apartment : %s', selected_data.count())



    selected_data = all_data.where((col('baths')==2) & (col('type')=='house'))

    print('Total number of baths=2 with type is apartment : %s', selected_data.count())


    selected_data = all_data.where((col('baths')==1) & (col('type')=='townhouse'))

    print('Total number of baths=2 with type is apartment : %s', selected_data.count())





    selected_data = all_data.where(col('parking_options').isin(['attached garage', 'street parking', 'off-street parking']))

    print('Total number of records with parking options of attached garage, street parking, or off-street parking: %s' % selected_data.count())



     # select data where state = 'CA' and price < 3000
    selected_data = all_data.where((col('state') == 'ca') & (col('price') < 3000))
    print('Total number of records where state = "CA" and price < 3000: %s' % selected_data.count())



    # select data where cats_allowed = true and dogs_allowed = true and smoking_allowed = false
    selected_data = all_data.where((col('cats_allowed') == 1) & (col('dogs_allowed') == 1) & (col('smoking_allowed') == 1))
    print('Total number of records where cats_allowed = 1, dogs_allowed = 1, and smoking_allowed = 1: %s' % selected_data.count())






    selected_data.write.mode('Overwrite').parquet(S3_DATA_OUTPUT_PATH) # here the data is store in the form of parquet filetype. here in place of parquet if we give .csv it will be stored as a csv file in the output bucket in the s3.
    
    print('selected data is successfully  saved to s3 : %s' % S3_DATA_OUTPUT_PATH) # this prints the output path where the data is stored.


if __name__ == '__main__' :
    main() 
