from flask import Flask, jsonify, request

def create_app() -> Flask:
    app = Flask(__name__)

    @app.get("/health")
    def health():
        return jsonify({"status": "ok"}), 200

    # ----------------------------
    # Create short URL
    # POST /shorten
    # ----------------------------
    @app.post("/shorten")
    def create_short_url():
        return jsonify({
            "message": "Create short URL – not implemented yet"
        }), 501


    # ----------------------------
    # Retrieve original URL
    # GET /shorten/<shortCode>
    # (increments accessCount later)
    # ----------------------------
    @app.get("/shorten/<string:short_code>")
    def get_short_url(short_code: str):
        return jsonify({
            "message": f"Retrieve short URL '{short_code}' – not implemented yet"
        }), 501


    # ----------------------------
    # Update short URL
    # PUT /shorten/<shortCode>
    # ----------------------------
    @app.put("/shorten/<string:short_code>")
    def update_short_url(short_code: str):
        return jsonify({
            "message": f"Update short URL '{short_code}' – not implemented yet"
        }), 501


    # ----------------------------
    # Delete short URL
    # DELETE /shorten/<shortCode>
    # ----------------------------
    @app.delete("/shorten/<string:short_code>")
    def delete_short_url(short_code: str):
        return jsonify({
            "message": f"Delete short URL '{short_code}' – not implemented yet"
        }), 501


    # ----------------------------
    # Get statistics
    # GET /shorten/<shortCode>/stats
    # ----------------------------
    @app.get("/shorten/<string:short_code>/stats")
    def get_short_url_stats(short_code: str):
        return jsonify({
            "message": f"Stats for short URL '{short_code}' – not implemented yet"
        }), 501

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="127.0.0.1", port=5000, debug=True)
