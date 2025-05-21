# M2 Lab 1 

In this lab, we'll prepare the Avalanche data namely the Customer Reviews subset from an unstructured format to a structured format in Snowflake Notebooks.

## Setup

Follow the instructions provided in `setup.sql` to create a database, schema, stage as well as upload files for the Avalanche data.

## Using the Data

Once this is completed, the Avalanche data can be accessed from the `@avalanche_db.avalanche_schema.customer_reviews` stage directly.

For example, to list contents of the stage run this SQL query:

```SQL 
ls @avalanche_db.avalanche_schema.customer_reviews;
``` 

To read contents of a file:

```SQL 
-- Read single file
`SELECT
  SNOWFLAKE.CORTEX.PARSE_DOCUMENT(
    @avalanche_db.avalanche_schema.customer_reviews,
    'review-01.docx',
    {'mode': 'layout'}
  ) AS layout;`
```

## Data Processing

Next, we'll use the structured data to create a bar chart to visualize the daily sentiment score and the product sentiment score.

- PARSE_DOCUMENT function to extract text and data from unstructured DOCX files.
- SENTIMENT function to calculate the sentiment score of extracted customer review text
- SUMMARIZE function to return a concise summary of the customer review text
- TRANSLATE: function to translate given text from/to any supported language

## Data Visualization
Then, we'll create a bar chart to visualize the daily sentiment score and the product sentiment score.


## Running the Notebook
Download the Notebook in `IPYNB` format (`customer-reviews.ipynb`) and upload to your Snowflake Snowsight account to run the Snowflake Notebook.
