# backend/app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    df = pd.read_csv(file)

    df["CTR"] = df["Clicks"] / df["Views"]
    summary = {
        "total_views": int(df["Views"].sum()),
        "total_sales": int(df["Sales"].sum()),
        "avg_ctr": round(df["CTR"].mean(), 2),
        "top_product": df.loc[df["Sales"].idxmax(), "Product"]
    }

    pricing_suggestions = []
    median_price = df["Price"].median()
    for _, row in df.iterrows():
        if row["Price"] > median_price * 1.1:
            pricing_suggestions.append({
                "product": row["Product"],
                "suggestion": f"Consider lowering price to around ${median_price:.2f}"
            })

    charts = {
        "line": df[["Product", "Views", "Sales"]].to_dict(orient="records"),
        "bar": df[["Product", "CTR"]].to_dict(orient="records"),
        "pie": df[["Product", "Sales"]].to_dict(orient="records"),
    }

    return jsonify({"summary": summary, "pricing": pricing_suggestions, "charts": charts})

if __name__ == "__main__":
    app.run(debug=True)
