# Neo4j Data Load Steps and Setup

## 1. Prepare the Data
- Download a retail transactions dataset from Kaggle (e.g., Online Retail II UCI).
- Place the CSV file in the `data/` directory and rename it to `retail_transactions.csv`.
- Use the provided Jupyter notebook (`notebooks/01_data_exploration_and_neo4j_import.ipynb`) to:
  - Explore and clean the data
  - Export the following CSVs for Neo4j import:
    - `customers.csv`
    - `products.csv`
    - `transactions.csv`
    - `transaction_products.csv`

## 2. Start Neo4j with Podman
Run the following command to start a Neo4j instance using your local Docker image:

```powershell
podman run -d --name neo4j \
  -p 7474:7474 -p 7687:7687 \
  -e NEO4J_AUTH=neo4j/testpassword \
  -v D:\neo4j\data:/data \
  docker.io/library/neo4j:5
```
- Neo4j Browser: http://localhost:7474 (user: neo4j, password: testpassword)
- Place your exported CSVs in `D:\neo4j\data\import` for Neo4j to access them.

## 3. Load Data into Neo4j
Open Neo4j Browser or Cypher Shell and run the following Cypher scripts:

---

# Cypher Scripts for Data Import

```cypher
// Create uniqueness constraints
CREATE CONSTRAINT customer_id IF NOT EXISTS FOR (c:Customer) REQUIRE c.customer_id IS UNIQUE;
CREATE CONSTRAINT product_id IF NOT EXISTS FOR (p:Product) REQUIRE p.product_id IS UNIQUE;
CREATE CONSTRAINT invoice_id IF NOT EXISTS FOR (t:Transaction) REQUIRE t.invoice_id IS UNIQUE;

// Load Customers
LOAD CSV WITH HEADERS FROM 'file:///customers.csv' AS row
MERGE (c:Customer {customer_id: row.customer_id})
SET c.country = row.country;

// Load Products
LOAD CSV WITH HEADERS FROM 'file:///products.csv' AS row
MERGE (p:Product {product_id: row.product_id})
SET p.description = row.description;

// Load Transactions
LOAD CSV WITH HEADERS FROM 'file:///transactions.csv' AS row
MERGE (t:Transaction {invoice_id: row.invoice_id})
SET t.date = row.date;

// Create PURCHASED relationships
LOAD CSV WITH HEADERS FROM 'file:///transactions.csv' AS row
MATCH (c:Customer {customer_id: row.customer_id})
MATCH (t:Transaction {invoice_id: row.invoice_id})
MERGE (c)-[:MADE]->(t);

// Create CONTAINS relationships
LOAD CSV WITH HEADERS FROM 'file:///transaction_products.csv' AS row
MATCH (t:Transaction {invoice_id: row.invoice_id})
MATCH (p:Product {product_id: row.product_id})
MERGE (t)-[r:CONTAINS]->(p)
SET r.quantity = toInteger(row.quantity), r.price = toFloat(row.price);
```

---

## 4. Validate the Graph
- Use Neo4j Browser to explore nodes and relationships.
- Example queries:
  - `MATCH (c:Customer)-[:MADE]->(t:Transaction)-[r:CONTAINS]->(p:Product) RETURN c, t, r, p LIMIT 25;`

---

## 5. Next Steps
- Build FastAPI backend and agents.
- Implement recommendation and query agents.
- Integrate with Google ADK and Gemini Flash.
