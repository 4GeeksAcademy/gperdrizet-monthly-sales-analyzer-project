# Monthly Sales Analyzer

![Project Preview](assets/preview.png)

Analyze monthly sales data for three products over 20 days using Python. This project applies loops, conditionals, and data structures to calculate totals, averages, and trends for better business insights. It also demonstrates defining functions and refactoring.

## Features

- Calculate total sales for each product
- Compute average daily sales
- Identify the day with the highest total sales
- Count days when a product exceeded a sales threshold
- Determine the top-selling product of the month

## Project Structure

```
.
├── .gitignore
├── functions.py
├── learn.json
├── monthly_sales_analyzer.py
└── assets/
    └── preview.png
```

- **`functions.py`**: Helper functions for sales analysis
- **`monthly_sales_analyzer.py`**: Example usage and function tests
- **`assets/preview.png`**: Project preview image
- **`learn.json`**: Project metadata

## Usage

### Run in GitHub Codespaces

1. Click the **Code** button on the repository page and select **"Create codespace on main"** (or your default branch).
2. Wait for the Codespace to initialize. The environment will be ready to run Python scripts out of the box.
3. In the Codespace terminal, run:

   ```sh
   python monthly_sales_analyzer.py
   ```

4. Review the output in your terminal.

---

### Run locally:

1. Clone the repository.
2. Run the analyzer script:

   ```sh
   python monthly_sales_analyzer.py
   ```

3. Review the output in your terminal.

## Example Output

```
Total sales of product_a: 3885
Average daily sales of product_b: 120.7
Day with highest total sales: 8
Days when product_c exceeded 300 sales: 7
Product with highest total sales: product_c
```

## Functions

- `total_sales_by_product`: Calculates total sales for a product.
- `average_daily_sales`: Computes average daily sales for a product.
- `best_selling_day`: Finds the day with the highest total sales.
- `days_above_threshold`: Counts days a product exceeded a sales threshold.
- `top_product`: Determines the product with the highest total sales.

## License

See [repository](https://github.com/4GeeksAcademy/monthly-sales-analyzer-project) for details.

---

*Beginner-friendly project for learning Python data analysis basics.*
