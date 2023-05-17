# python-sql-review
## Overview

The purpose of these exercises is to provide you with an opportunity to practice problem solving using Python and Test-Driven Development (TDD). Although there is a component related to SQL, it is not the main focus. In assessing your work, the following aspects will be considered:

- Demonstrating the ability to break down problems effectively.
- Exhibiting strong problem-solving skills.
- Employing a logical project structure.
- Implementing Test-Driven Development practices.
- Demonstrating proficiency in using Git effectively.
- Adhering to excellent code standards, including compliance with PEP8 guidelines and thorough documentation.
The tasks for today are divided into sections, and it is not necessary to complete all of them. Instead, it is encouraged to focus on the first section

** However, please note that some of the later tasks will require the completion of previous tasks. This information will be provided in the README document.

## The Objective

We have embarked on a venture to establish a department store offering a wide range of unique items. However, our initial attempt at designing a database has not been as effective as desired, particularly when it comes to analyzing our sales—a crucial aspect for maximizing profits.

To address this challenge, we have enlisted the expertise of a professional to design a new database. This new database will enable us to identify the best-selling products and determine which items are not worth stocking.

Your task involves manipulating the data extracted from the first database to align with the schema specified in the second database. You can find the schemas for both databases at the following directory:

> First database: ./EDR/EDR-1

> New database: ./EDR/EDR-2

## Section 1: Data Transformation

Your initial task is to develop six utility functions that will format the raw data, preparing it for insertion into the new database tables using the pg8000 module.

It is essential to have a clear understanding of the expected arguments for each function and the structure of the data to be returned.

### Task 1 - Transforming Department Data
The ' function is responsible for processing a list of dictionaries with the following format and returning a list of lists containing the **department_name**.

# EXAMPLE INPUT
[
    {
        'staff_id': 1,
        'first_name': 'Will',
        'last_name': 'Crawley',
        'department': 'Beauty'
    },
    {
        'staff_id': 2,
        'first_name': 'Cat',
        'last_name': 'Hoang',
        'department': 'Footwear'
    }
]

# OUTPUT
[['Beauty'], ['Footwear']]

### Task 2 - Transforming Stock Data
The format_stock function is responsible for processing a list of dictionaries with the following format and returning a list containing the **item_name** and the **amount**.

# EXAMPLE INPUT
[
    {
        'item_id': 1,
        'item_name': 'Louboutin Flip Flops',
        'features': ['Designer', 'Faux-Faux-Leather'],
        'department': 'Footwear',
        'amount': 5
    }, {
        'item_id': 2,
        'item_name': 'Eau de Fromage',
        'features': ['Fragrance', 'Designer'],
        'department': 'Beauty',
        'amount': 10
    }
]

# OUTPUT
[['Louboutin Flip Flops', 5], ['Eau de Fromage', 10]]

### Task 3 - Transforming Feature Data
The format_features function is responsible for processing a list of dictionaries with the following format and returning a list of lists containing the unique feature_name.

# EXAMPLE INPUT
[
    {
        'item_id': 1,
        'item_name': 'Louboutin Flip Flops',
        'features': ['Designer', 'Faux-Faux-Leather'],
        'department': 'Footwear',
        'amount': 5
    }, {
        'item_id': 2,
        'item_name': 'Eau de Fromage',
        'features': ['Fragrance', 'Designer'],
        'department': 'Beauty',
        'amount': 10
    }
]

# OUTPUT
[['Designer'], ['Faux-Faux-Leather'], ['Fragrance']]

### Task 4 - Transforming Staff Data
The format_staff function should accept a list of dictionaries representing staff data and a list of dictionaries representing the new department data. It should return a list of lists containing the first_name, last_name, and the correct department_id.

# EXAMPLE INPUT
# Staff list
[
    {
        'staff_id': 1,
        'first_name': 'Duncan',
        'last_name': 'Crawley',
        'department': 'Beauty'
    }, {
        'staff_id': 2,
        'first_name': 'Cat',
        'last_name': 'Hoang',
        'department': 'Footwear'
    }
]
# Department list
[
    {
        'department_id': 1,
        'department_name': 'Beauty'
    }, {
        'department_id': 2,
        'department_name': 'Footwear'
    }
]

# OUTPUT
[['Duncan', 'Crawley', 1], ['Cat', 'Hoang', 2]]


### Task 5 - Transforming Stock_Feature Data
The format_stock_feature function requires data from the following data structures:

- A list representing the newly inserted stock data
- A list representing the newly inserted feature data
- A list representing the original stock data
**Hint: It may be beneficial to break down this problem into multiple functions.**

The function should return a list of lists containing the stock_id and feature_id.

**Please note that each product can have multiple features, and as a result, there may be multiple instances of the same stock_id with different feature_id values.**
# New stock data:
[
    {
        'item_id': 1,
        'item_name': 'Louboutin Flip Flops',
        'amount_in_stock': 5
    }, {
        'item_id': 2,
        'item_name': 'Eau de Fromage',
        'amount_in_stock': 10
    }
]
# New feature data:
[
    {
        'feature_id': 1,
        'feature_name': 'Designer'
    }, {
        'feature_id': 2,
        'feature_name': 'Faux-Faux-Leather'
    }
]
# Original stock data
[
    {
        'item_id': 1,
        'item_name': 'Louboutin Flip Flops',
        'features': ['Designer', 'Faux-Faux-Leather'],
        'department': 'Footwear',
        'amount': 5
    }, {
        'item_id': 2,
        'item_name': 'Eau de Fromage',
        'features': ['Designer'],
        'department': 'Beauty',
        'amount': 10
    }
]

# OUTPUT
[[1, 1], [1, 2], [2, 1]]

### Task 6 - Manipulate Sales Data
The format_sales function is the final function in this task. It has the following signature:

def format_sales(new_stock_data, new_staff_data, original_sales_data):

- new_stock_data is a list representing the newly inserted stock data.
- new_staff_data is a list representing the newly inserted staff data.
- original_sales_data is a list representing the original sales data.
_hint: You may want to break this problem down into multiple functions._

The function should return a list of lists that contains the following information for each sale:

- item_id: The correct ID based on the item's name in the new_stock_data.
- salesperson: The correct ID based on the name of the staff member in the new_staff_data.
- price
- quantity
- created_at
Here's an example of the provided data:

# New stock data:
[
    {
        'item_id': 1,
        'item_name': 'Louboutin Flip Flops',
        'amount_in_stock': 5
    },
    {
        'item_id': 2,
        'item_name': 'Eau de Fromage',
        'amount_in_stock': 10
    }
]

# New staff data:
[
    {
        'staff_id': 1,
        'first_name': 'Duncan',
        'last_name': 'Crawley',
        'department_id': 1
    },
    {
        'staff_id': 2,
        'first_name': 'Cat',
        'last_name': 'Hoang',
        'department_id': 2
    }
]

# Original sales data:
[
    {
        'sale_code': 'guiiljnevn',
        'item_name': 'Louboutin Flip Flops',
        'salesperson': 'Duncan Crawley',
        'price': 22.49,
        'quantity': 1,
        'created_at': '2023-01-03 10:34:56'
    }
]

# OUTPUT
[[1, 1, 22.49, 1, '2023-01-03 10:34:56']]

Please note that the price, quantity, and created_at values should be replaced with the actual values from your sales data.


## Section 2: Retrieve Postgres Data

To begin this section, please execute the setup-db.sql file using the following command:
psql -f setup-db.sql

This command will create both databases and insert data into the first database, preparing it for the subsequent tasks.

### Task 1: Retrieve Initial Data
> You need a way to access all the initial data from each of the three tables.

> You should write a function (or functions) specifically for this purpose. The function should return the data as a list of dictionaries, where the keys align with the column titles (refer to the input examples in Section 1).

> You might consider using a data manipulation utility function. If you choose to do so, ensure that it has unit tests. However, testing the functionality of the pg8000 module is not necessary.

_THE NEXT SECTION RELIES ON SOME DATA BEING INSERTED FIRST. MOVE ON TO THE NEXT SECTION AND RETURN HERE WHEN YOU HAVE THE REQUIRED DATA INSERTED._

### Task 2: Retrieve Newly Inserted Data for the Following Tables:
- 'dim_feature'
- 'dim_stock'
- 'dim_department'
- 'dim_staff'

## Section 3: Insert Formatted Data

Congratulations on making it this far! 🎉

The final step is to combine everything you have accomplished thus far and populate the new database.

Consider what needs to be done and the order in which those tasks should be performed.

_Remember, you may need to execute part of the data insertion and then return to Task 2 of Section 2 to utilize the newly inserted data._
