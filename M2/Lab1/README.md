# M2 Lab 1 

In this lab, we'll prepare the Avalanche data namely the Customer Reviews subset from an unstructured format to a structured format in Snowflake Notebooks.

## Setup

Follow the instructions provided in `setup.sql` to create a database, schema, stage as well as upload files for the Avalanche data.

## Using the Data

Once this is completed, the Avalanche data can be accessed from the `@avalanche_db.avalanche_schema.customer_reviews` stage directly.

For example, to list contents of the stage run this SQL query:

``` 
ls @avalanche_db.avalanche_schema.customer_reviews;
``` 

To read contents of a file:

```ruby 
-- Read single file
`SELECT
  SNOWFLAKE.CORTEX.PARSE_DOCUMENT(
    @avalanche_db.avalanche_schema.customer_reviews,
    'review-01.docx',
    {'mode': 'layout'}
  ) AS layout;`
```

## Downloading the Lab Notebook
To follow along with the lab video:
1. From the Github Repo, browse to the folder M2/Lab1 and download the customer-reviews.ipynb file.
2. In your Snowflake Snowsight account, from the left sidebar menu, select “Projects/Notebooks”
3. To the right of the bright blue “+Notebook” button on the top-right of your screen, click on the down arrow to bring up a drop-down menu
4. Select “Import .ipynb file”
5. Browse to the location where you downloaded the customer-reviews.ipynb file and click on “Open”
6. Select the avalanche database, schema and stage that you created in the steps above
7. Leave all other options at default
8. Click on Create
This will open a notebook that will allow you to follow along with the Module 2 Lab 1 video for more information on how to process the data and perform sentiment analysis and visualization. 

## Setup

Before we begin ingesting our dataset, we’ll first need to create a database, schema and stage to upload them into. 

### Create a Database
1. Start by logging into your Snowflake account
2. From the left sidebar, click on “Data”
3. Click on the bright blue “+ Database” button at the top right of your screen
4. Name your database "avalanche_db" and click on “Create”

### Create a Schema
1.  Double click on the avalanche_db you just created.
2.  A bright blue button called “+ Schema” will appear at the top of your screen, click on it.
3.  Name this new schema “avalanche_schema”

### Create a Stage
1. From the left sidebar, click on Data and then Add Data
2. Click on the box on the top-right of your screen that says “Snowflake Stage”
3. Name the stage “customer_reviews”
4. From the dropdown menu called “Select or create a database and schema”
    - Select the database avalanche_db
    - Select the schema avalanche_schema
5. From the Encryption section, select Server-side encryption
6. Click on Create

## Adding Data to the Stage
1. If you have not already, download the Avalanche dataset from https://github.com/https-deeplearning-ai/rapid-prototyping-with-streamlit/tree/master/Avalanche/files/customer_reviews/ 
    - Note that we want to grab the unstructured Docx files, not the pre-compiled csv we used previously
2. On Snowflake, navigate back to the menu page at Data/Add Data
3. Click on the block that says “Load files into a Stage”
4. Browse to the location where you stored the Avalanche dataset and select all the files that end with docx
5. Select the avalanche_db and avalanche_schema from the drop down menu
6. Select the “customer_reviews” stage
7. Click on Upload and give it a minute or so to upload all the files

## Parsing the data
Now that we have the data on Snowflake, we can easily parse the data using a SQL workbook so that we have access to Snowflake Cortex functions.
1. From your Snowflake account, on the left sidebar menu, open a new Snowflake Workbook by clicking on Projects/Notebooks
2. Click on the bright-blue “+ Notebook” button on the top-right corner of your screen
3. Select the Avalanche database and schema you created in the steps above
4. Leave all other options and default and click on “Create”
5. Every new notebook opens with sample code blocks, go ahead and delete those by clicking on the three dots at the top-right of each code block and selecting “Delete”
6. On the top middle of your workbook screen, you’ll see three buttons that allow you to add new codeblocks in either python, sql or markdown. Click on “+ SQL”
7. In the SQL cell called “cell1”, copy and paste the following code: 
`WITH files AS (
   SELECT 
     REPLACE(REGEXP_SUBSTR(file_url, '[^/]+$'), '%2e', '.') as filename
   FROM DIRECTORY('@avalanche_db.avalanche_schema.customer_reviews')
   WHERE filename LIKE '%.docx'
 )
 SELECT 
   filename,
   SNOWFLAKE.CORTEX.PARSE_DOCUMENT(
     @avalanche_db.avalanche_schema.customer_reviews,
     filename,
     {'mode': 'layout'}
   ):content AS layout
 FROM files;`
8. Make sure the database, schema and stage names match the names you created in the steps above (you’ll notice mine are different because I’ve done this so many times)
9. Click on the play button at the top of the code block
10. After a few moments you’ll see a list of the ingested and parsed files in a window under the code block

## Using the Data
Now, the Avalanche customer reviews can always be accessed from the location @avalanche_db.avalanche_schema.customer_reviews; directly.

For example, to list contents of the stage run this SQL query in a SQL codeblock:
ls @avalanche_db.avalanche_schema.customer_reviews;

To read contents of a file:
-- Read single file
`SELECT
  SNOWFLAKE.CORTEX.PARSE_DOCUMENT(
    @avalanche_db.avalanche_schema.customer_reviews,
    'review-01.docx',
    {'mode': 'layout'}
  ) AS layout;`
## Data Processing and Sentiment Score
In this lab, we’ll be using the  following Cortex functions to prepare and analyze your Customer Review dataset: 


PARSE_DOCUMENT function to extract text and data from unstructured DOCX files.
- SENTIMENT function to calculate the sentiment score of extracted customer review text
- SUMMARIZE function to return a concise summary of the customer review text
- TRANSLATE: function to translate given text from/to any supported language

## Data Visualization
Then, we'll create a bar chart to visualize the daily sentiment score and the product sentiment score.
