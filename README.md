# Rule Engine with AST

## Overview

This project implements a simple 3-tier rule engine that determines user eligibility based on attributes such as age, department, income, and spending. The engine uses an Abstract Syntax Tree (AST) to represent conditional rules, allowing for dynamic creation, combination, and modification of these rules.

## Problem Statement

We aim to create a rule engine that can evaluate complex eligibility rules defined by the user. The engine should support:
- Dynamic creation of rules using logical operators (AND, OR).
- Evaluation of rules against user attributes.
- Storage of rules and user metadata in a relational database.

## Solution Outline

### 1. Data Structure

The core of the rule engine is the Abstract Syntax Tree (AST). Each node in the tree represents either an operator (AND/OR) or an operand (conditions). The structure is defined as follows:

```python
class Node:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.type = node_type
        self.left = left
        self.right = right
        self.value = value
2. Database Schema
We use PostgreSQL to store rules and user metadata. The schema includes:

Rules Table:

sql

CREATE TABLE rules (
    id SERIAL PRIMARY KEY,
    rule_string TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
Metadata Table:

sql

CREATE TABLE metadata (
    id SERIAL PRIMARY KEY,
    attribute_name VARCHAR(255) NOT NULL,
    attribute_type VARCHAR(50) NOT NULL
);
3. Core Functions
Rule Creation: Parse a rule string and create the corresponding AST.
Rule Combination: Combine multiple ASTs into a single AST.
Rule Evaluation: Evaluate the combined AST against provided user attributes.
4. Example Rule
Here’s an example of a rule that combines multiple conditions:

((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)
5. Testing
You can test the application using cURL commands or Postman.

Create a Rule:

curl -X POST http://localhost:3000/create_rule -H "Content-Type: application/json" -d "{\"rule\":\"age > 30 AND salary > 50000\"}"
Retrieve All Rules:

curl http://localhost:3000/rules
Evaluate a Rule:

curl -X POST http://localhost:3000/evaluate_rule -H "Content-Type: application/json" -d "{\"ruleId\":1, \"userData\":{\"age\":35, \"salary\":60000}}"
Setup Instructions
Prerequisites
Python 3.x
PostgreSQL installed and running
psycopg2 library for PostgreSQL connectivity
Flask or a similar framework for creating the API
Installation
Clone the Repository:

git clone https://github.com/yourusername/rule-engine-ast.git
cd rule-engine-ast
Install Dependencies: Create a virtual environment and install required packages.

python -m venv venv
venv\Scripts\activate 
pip install psycopg2 flask
Set Up the Database: Create a PostgreSQL database named rule_engine and set up the schema as defined above.

Update Database Credentials: Update the connect_db() function in your code with the appropriate PostgreSQL username and password.

Run the Application:

python app.py
Usage
Once the application is running, you can interact with it using the provided API endpoints to create rules, retrieve existing rules, and evaluate rules against user attributes.

Future Improvements
Implement error handling for invalid rules.
Support for user-defined functions in the rule language.
Enhancement of the rule parser for more complex expressions.