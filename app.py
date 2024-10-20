from flask import Flask, request, jsonify
from ast import create_rule
from db import create_tables, connect_db

app = Flask(__name__)

# Initialize database tables
create_tables()

@app.route('/create_rule', methods=['POST'])
def create_rule_endpoint():
    data = request.json
    rule_string = data.get('rule')
    rule_node = create_rule(rule_string)
    # Store rule in the database (optional)
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO rules (rule_string) VALUES (%s)", (rule_string,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'Rule created successfully', 'ast': rule_node.value})

@app.route('/rules', methods=['GET'])
def get_rules():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM rules;")
    rules = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(rules)

@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule():
    # Placeholder for evaluation logic
    data = request.json
    return jsonify({'isEligible': True})  # Simplified response for demo

if __name__ == '__main__':
    app.run(debug=True)
