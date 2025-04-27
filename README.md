# Live Analytics Dashboard for Sellers

A live analytics dashboard that allows sellers to track their product performance on an e-commerce platform. The dashboard provides insights into product views, conversions, best listing times, and pricing recommendations.

## Features

- **Product-Level Analytics**: View product performance data including views, click-through rate (CTR), and sales trends.
- **Pricing Recommendations**: Based on the product’s performance, the dashboard provides pricing suggestions to optimize sales.
- **Data Visualization**: Interactive charts (Bar, Line, Pie) using Chart.js or Plotly to visualize product performance metrics.
- **Responsive Design**: Built with Tailwind CSS to ensure a smooth experience across devices, from desktop to mobile.

## Tech Stack

- **Frontend**: React.js, Tailwind CSS
- **Backend**: Flask (Python) 
- **Charting**: Chart.js 

## Key Features

- **Views & Conversions**: Track your product views and conversion rates in real-time.
- **Sales Trends**: View product sales history and trends over time.
- **Pricing Suggestions**: Automatically get pricing recommendations based on median price and other factors.
- **Charts**: Visualize performance using bar, line, and pie charts.
- **Responsive UI**: The app is fully responsive for use on desktop, tablet, and mobile devices.

## Getting Started

To run the app locally, follow the steps below.

### Prerequisites

- **Node.js**: Ensure Node.js is installed for the frontend.
- **Python**: Install Python for the backend (Flask).

### Installation

#### Frontend

1. Clone the repository:

   ```bash
   git clone https://github.com/srishtayal/marketplace-insights.git
   cd frontend
   ```

2. Install dependencies:

   ```bash
   npm install
   ```

3. Run the React development server:

   ```bash
   npm start
   ```

#### Backend

1. Navigate to the backend folder:

   ```bash
   cd backend
   ```

2. Install dependencies (for Flask):

   ```bash
   pip3 install -r requirements.txt
   ```

3. Start the Flask server:

   ```bash
   python3 app.py
   ```

### Usage

1. Upload your product data (CSV format) via the backend API.
2. The dashboard will automatically generate pricing suggestions based on median pricing and provide insights into product performance.
3. View performance charts and adjust pricing based on the suggestions provided by the app.

### Example Data Format

Your CSV file should have the following columns:

- **Product**: Name of the product.
- **Views**: Number of product views.
- **Sales**: Number of sales.
- **Price**: Product price.

```csv
Product,Views,Sales,Price
Product A,1000,50,20.00
Product B,500,20,15.00
Product C,2000,100,25.00
```

### Screenshots
![Screenshot 2025-04-27 at 7 46 55 PM](https://github.com/user-attachments/assets/8314c9c3-a96b-486d-9343-361a3ca3c9e2)
![Screenshot 2025-04-27 at 7 47 21 PM](https://github.com/user-attachments/assets/ffe3cade-0ec8-4a05-acc8-01c869faa142)


