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

## Task 1 - Transforming Department Data
The ' function is responsible for processing a list of dictionaries with the following format and returning a list of lists containing the **department_name**.
