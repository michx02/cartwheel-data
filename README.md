The data source is from Kaggle : https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/michx02/cartwheel-data
cd cartwheel-data
```

### 2. Create a Virtual Environment

Using Python 3.15.2:

```bash
python3.15 -m venv .venv
```

Activate the virtual environment:

**macOS / Linux**

```bash
source .venv/bin/activate
```

**Windows (PowerShell)**

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Grant Execution Permissions

On macOS/Linux, make the Bash script executable:

```bash
chmod +x generate_orders.sh
```

### 5. Generate Order Data

Run the following command:

```bash
./generate_orders.sh
```

This generates three order data files for three consecutive days, starting from the current date.

To specify a different starting date, pass a date argument in `M/D/Y` format:

```bash
./generate_orders.sh 11/15/2026
```

If no date is provided, the script defaults to the current date.

## Requirements

- Python 3.15.2
- kagglehub 1.0.3

See `requirements.txt` for dependency specifications.
