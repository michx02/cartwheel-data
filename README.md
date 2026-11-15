# Order Data Generator

A Python-based project that generates order data files for three consecutive days using a single Bash command.

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

### 4. Download the Olist Dataset

Run the main Python program:

```bash
python3 main.py
```

This initializes the project by downloading the Olist dataset using KaggleHub.

### 5. Grant Execution Permissions

On macOS/Linux, make the Bash script executable:

```bash
chmod +x generate_orders.sh
```

### 6. Generate Order Data

Run:

```bash
./generate_orders.sh
```

This generates three order data files for three consecutive days, working backwards from the specified date.

By default, the script uses the current date.

To specify a custom starting date, provide an argument in `M/D/Y` format:

```bash
./generate_orders.sh 11/15/2026
```

## Requirements

- Python 3.15.2
- kagglehub 1.0.3

See `requirements.txt` for dependency specifications.
