from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample services offered by the digital marketing company
SERVICES = {
    "seo": "Search Engine Optimization",
    "content_marketing": "Content Marketing",
    "ppc": "Pay-Per-Click Advertising",
    "social_media_management": "Social Media Management"
}

# Sample pricing information
PRICING = {
    "seo": "Starting at $500/month",
    "content_marketing": "Starting at $800/month",
    "ppc": "Starting at $300/month",
    "social_media_management": "Starting at $600/month"
}

# Sample timelines
TIMELINES = {
    "seo": "3-6 months for noticeable results",
    "content_marketing": "2-4 weeks for content creation",
    "ppc": "1-2 weeks to set up campaigns",
    "social_media_management": "Ongoing management"
}

def handle_query(query):
    query_lower = query.lower()
    if "services" in query_lower:
        return f"We offer the following services: {', '.join(SERVICES.values())}."
    elif any(service in query_lower for service in SERVICES):
        for service_key, service_name in SERVICES.items():
            if service_key in query_lower:
                return f"{service_name} is available. Pricing: {PRICING[service_key]}, Timeline: {TIMELINES[service_key]}."
    elif "pricing" in query_lower or "cost" in query_lower:
        return f"Our pricing is as follows: {', '.join([f'{service}: {price}' for service, price in PRICING.items()])}."
    elif "escalate" in query_lower or "human" in query_lower:
        return "I am transferring you to a human agent. Please wait..."
    else:
        return "I'm sorry, I don't understand your request. Can you please clarify?"

@app.route('/')
def home():
    return "Welcome to the Customer Support Chatbot. Use the /chat endpoint to interact."

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    if not user_message:
        return jsonify({"error": "No message provided"}), 400
    response = handle_query(user_message)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
