# Streamlit Session State Demo Project

## Overview
This project demonstrates the usage of Streamlit's session state mechanism and various UI components for building interactive web applications. It includes examples of data manipulation, user interface controls, and state management in Streamlit.

## Project Structure
```
├── app.py              # Main application file
├── session.py          # Session state demonstration
├── data.csv           # Sample data for table display
├── kullanici.txt      # User information storage
└── requirements.txt    # Project dependencies
```

## Features

### Session State Management (`session.py`)
- Dynamic table row manipulation
- Interactive counter implementation
- Session state variable demonstrations:
  - Basic variable storage
  - Counter management
  - Form data persistence
  - List and complex data type storage
- Table display with adjustable rows
- Callback function implementation
- UI components:
  - Buttons for increment/decrement
  - Table display
  - Dividers
  - Headers

### Data Handling
- CSV file reading with pandas
- Dynamic table display
- Row count management through session state
- Data persistence across app refreshes

## Installation

1. Create a virtual environment:
```bash
python -m venv env
```

2. Activate the virtual environment:
```bash
# On Linux/macOS:
source env/bin/activate

# On Windows:
.\env\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

### Running the Session State Demo:
```bash
streamlit run session.py
```

### Running the Main Application:
```bash
streamlit run app.py
```

## Session State Features Demonstrated

1. Basic State Management
   - Variable initialization
   - State persistence
   - Dynamic updates

2. Interactive Components
   - Buttons with callbacks
   - Table row count management
   - Dynamic data display

3. Form Data Handling
   - Text input fields
   - Password fields
   - Form submission
   - Data display

## Code Examples

### Session State Initialization
```python
if "satir_sayisi" not in st.session_state:
    st.session_state.satir_sayisi = 10
```

### Callback Functions
```python
def artir():
    st.session_state.satir_sayisi += 1

def dusur():
    st.session_state.satir_sayisi -= 1
```

### Data Display
```python
dataframe = pd.read_csv("data.csv", sep=",")
st.table(dataframe.head(st.session_state.satir_sayisi))
```

## Dependencies
- streamlit
- pandas

## Project Setup
1. Ensure Python 3.8 or higher is installed
2. Create and activate a virtual environment
3. Install dependencies from requirements.txt
4. Run the desired application file using streamlit

## Development
- The project uses Streamlit's built-in session state for managing application state
- Data is loaded from CSV files for demonstration
- User interface is built using Streamlit's components
- State management is handled through callback functions

## Contributing
1. Fork the repository
2. Create a new branch for your feature
3. Commit your changes
4. Push to your branch
5. Create a Pull Request

## Notes
- Session state is persistent across app reruns
- The application demonstrates both basic and advanced Streamlit features
- Code includes examples of form handling and data management
- Interface is built using Streamlit's native components

## Contact
Author: Sümeyra Karsavran
Repository: https://github.com/sumeyrakarsavran/streamlit
