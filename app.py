import streamlit as st
import math

# Set page configuration
st.set_page_config(
    page_title="Professional Unit Converter",
    page_icon="🔄",
    layout="wide"
)

# Add custom CSS for styling
st.markdown("""
<style>
    .stApp {
        background-color:rgb(200, 190, 210) !important;
    }
    .main-title {
        font-size: 4rem;
        font-weight: 800;
        margin-bottom: 1rem;
        color:rgb(161, 143, 249);
        text-align: center;
    }
    .category-title {
        font-size: 1.8rem;
        font-weight: 600;
        color: rgb(161, 143, 249);
        margin-top: 1rem;
    }
    .result-box {
        background-color: rgb(239, 253, 234);
        border-radius: 0.5rem;
        padding: 1rem;
        margin-top: 1rem;
        border-left: 5px solid #1E88E5;
    }
    .result-value {
        font-size: 1.8rem;
        font-weight: 700;
        color: rgb(161, 143, 249);
    }
    .formula-box {
        background-color:rgb(239, 253, 234);
        border-radius: 0.5rem;
        padding: 1rem;
        margin-top: 1rem;
        border-left: 5px solid #4CAF50;
    }
    .stButton>button {
        background-color: rgb(161, 143, 249);
        color: black;
        font-weight: 500;
    }
    .stButton>button:hover {
        background-color: rgb(129, 103, 255);
        color: black;
    }
</style>
""", unsafe_allow_html=True)

# Define conversion functions
def length_conversion(value, from_unit, to_unit):
    # Conversion factors to meters
    to_meter = {
        "Meter": 1,
        "Kilometer": 1000,
        "Centimeter": 0.01,
        "Millimeter": 0.001,
        "Mile": 1609.34,
        "Yard": 0.9144,
        "Foot": 0.3048,
        "Inch": 0.0254,
        "Nautical Mile": 1852
    }
    
    # Convert to meters first, then to target unit
    meters = value * to_meter[from_unit]
    result = meters / to_meter[to_unit]
    
    # Create formula text
    formula = f"{value} {from_unit} = {result:.6g} {to_unit}"
    if from_unit != to_unit:
        formula += f" (Conversion: {value} × {to_meter[from_unit]:.6g} ÷ {to_meter[to_unit]:.6g})"
    
    return result, formula

def weight_conversion(value, from_unit, to_unit):
    # Conversion factors to grams
    to_gram = {
        "Kilogram": 1000,
        "Gram": 1,
        "Milligram": 0.001,
        "Pound": 453.592,
        "Ounce": 28.3495,
        "Ton (Metric)": 1000000,
        "Ton (US)": 907185,
        "Stone": 6350.29
    }
    
    # Convert to grams first, then to target unit
    grams = value * to_gram[from_unit]
    result = grams / to_gram[to_unit]
    
    # Create formula text
    formula = f"{value} {from_unit} = {result:.6g} {to_unit}"
    if from_unit != to_unit:
        formula += f" (Conversion: {value} × {to_gram[from_unit]:.6g} ÷ {to_gram[to_unit]:.6g})"
    
    return result, formula

def temperature_conversion(value, from_unit, to_unit):
    result = 0
    formula = ""
    
    # Direct conversions
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        result = (value * 9/5) + 32
        formula = f"{value}°C = ({value} × 9/5) + 32 = {result:.6g}°F"
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        result = value + 273.15
        formula = f"{value}°C = {value} + 273.15 = {result:.6g}K"
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        result = (value - 32) * 5/9
        formula = f"{value}°F = ({value} - 32) × 5/9 = {result:.6g}°C"
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        result = (value - 32) * 5/9 + 273.15
        formula = f"{value}°F = ({value} - 32) × 5/9 + 273.15 = {result:.6g}K"
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        result = value - 273.15
        formula = f"{value}K = {value} - 273.15 = {result:.6g}°C"
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        result = (value - 273.15) * 9/5 + 32
        formula = f"{value}K = ({value} - 273.15) × 9/5 + 32 = {result:.6g}°F"
    else:  # Same unit
        result = value
        formula = f"{value} {from_unit} = {result} {to_unit}"
        
    return result, formula

def area_conversion(value, from_unit, to_unit):
    # Conversion factors to square meters
    to_sq_meter = {
        "Square Meter": 1,
        "Square Kilometer": 1000000,
        "Square Mile": 2590000,
        "Hectare": 10000,
        "Acre": 4046.86,
        "Square Foot": 0.092903,
        "Square Inch": 0.00064516,
        "Square Yard": 0.836127
    }
    
    # Convert to square meters first, then to target unit
    sq_meters = value * to_sq_meter[from_unit]
    result = sq_meters / to_sq_meter[to_unit]
    
    # Create formula text
    formula = f"{value} {from_unit} = {result:.6g} {to_unit}"
    if from_unit != to_unit:
        formula += f" (Conversion: {value} × {to_sq_meter[from_unit]:.6g} ÷ {to_sq_meter[to_unit]:.6g})"
    
    return result, formula

def volume_conversion(value, from_unit, to_unit):
    # Conversion factors to milliliters
    to_ml = {
        "Cubic Meter": 1000000,
        "Liter": 1000,
        "Milliliter": 1,
        "Gallon (US)": 3785.41,
        "Gallon (UK)": 4546.09,
        "Quart (US)": 946.353,
        "Pint (US)": 473.176,
        "Cup": 236.588,
        "Fluid Ounce (US)": 29.5735,
        "Tablespoon": 14.7868,
        "Teaspoon": 4.92892,
        "Cubic Inch": 16.3871,
        "Cubic Foot": 28316.8
    }
    
    # Convert to milliliters first, then to target unit
    ml = value * to_ml[from_unit]
    result = ml / to_ml[to_unit]
    
    # Create formula text
    formula = f"{value} {from_unit} = {result:.6g} {to_unit}"
    if from_unit != to_unit:
        formula += f" (Conversion: {value} × {to_ml[from_unit]:.6g} ÷ {to_ml[to_unit]:.6g})"
    
    return result, formula

def time_conversion(value, from_unit, to_unit):
    # Conversion factors to seconds
    to_second = {
        "Second": 1,
        "Minute": 60,
        "Hour": 3600,
        "Day": 86400,
        "Week": 604800,
        "Month (30 days)": 2592000,
        "Year (365 days)": 31536000,
        "Millisecond": 0.001,
        "Microsecond": 0.000001,
        "Nanosecond": 0.000000001
    }
    
    # Convert to seconds first, then to target unit
    seconds = value * to_second[from_unit]
    result = seconds / to_second[to_unit]
    
    # Create formula text
    formula = f"{value} {from_unit} = {result:.6g} {to_unit}"
    if from_unit != to_unit:
        formula += f" (Conversion: {value} × {to_second[from_unit]:.6g} ÷ {to_second[to_unit]:.6g})"
    
    return result, formula

def speed_conversion(value, from_unit, to_unit):
    # Conversion factors to meters per second
    to_mps = {
        "Meter/Second": 1,
        "Kilometer/Hour": 0.277778,
        "Mile/Hour": 0.44704,
        "Foot/Second": 0.3048,
        "Knot": 0.514444,
        "Mach (at sea level)": 340.29
    }
    
    # Convert to meters per second first, then to target unit
    mps = value * to_mps[from_unit]
    result = mps / to_mps[to_unit]
    
    # Create formula text
    formula = f"{value} {from_unit} = {result:.6g} {to_unit}"
    if from_unit != to_unit:
        formula += f" (Conversion: {value} × {to_mps[from_unit]:.6g} ÷ {to_mps[to_unit]:.6g})"
    
    return result, formula

def pressure_conversion(value, from_unit, to_unit):
    # Conversion factors to pascals
    to_pascal = {
        "Pascal": 1,
        "Kilopascal": 1000,
        "Bar": 100000,
        "PSI": 6894.76,
        "Atmosphere": 101325,
        "Torr": 133.322,
        "Millimeter of Mercury": 133.322
    }
    
    # Convert to pascals first, then to target unit
    pascals = value * to_pascal[from_unit]
    result = pascals / to_pascal[to_unit]
    
    # Create formula text
    formula = f"{value} {from_unit} = {result:.6g} {to_unit}"
    if from_unit != to_unit:
        formula += f" (Conversion: {value} × {to_pascal[from_unit]:.6g} ÷ {to_pascal[to_unit]:.6g})"
    
    return result, formula

def energy_conversion(value, from_unit, to_unit):
    # Conversion factors to joules
    to_joule = {
        "Joule": 1,
        "Kilojoule": 1000,
        "Calorie": 4.184,
        "Kilocalorie": 4184,
        "Watt-hour": 3600,
        "Kilowatt-hour": 3600000,
        "Electronvolt": 1.602176634e-19,
        "British Thermal Unit": 1055.06,
        "Foot-pound": 1.35582
    }
    
    # Convert to joules first, then to target unit
    joules = value * to_joule[from_unit]
    result = joules / to_joule[to_unit]
    
    # Create formula text
    formula = f"{value} {from_unit} = {result:.6g} {to_unit}"
    if from_unit != to_unit:
        formula += f" (Conversion: {value} × {to_joule[from_unit]:.6g} ÷ {to_joule[to_unit]:.6g})"
    
    return result, formula

def power_conversion(value, from_unit, to_unit):
    # Conversion factors to watts
    to_watt = {
        "Watt": 1,
        "Kilowatt": 1000,
        "Megawatt": 1000000,
        "Horsepower": 745.7,
        "Foot-pound/minute": 0.0225969,
        "BTU/hour": 0.29307107
    }
    
    # Convert to watts first, then to target unit
    watts = value * to_watt[from_unit]
    result = watts / to_watt[to_unit]
    
    # Create formula text
    formula = f"{value} {from_unit} = {result:.6g} {to_unit}"
    if from_unit != to_unit:
        formula += f" (Conversion: {value} × {to_watt[from_unit]:.6g} ÷ {to_watt[to_unit]:.6g})"
    
    return result, formula

def data_conversion(value, from_unit, to_unit):
    # Conversion factors to bytes (using binary prefixes)
    to_byte = {
        "Bit": 0.125,
        "Byte": 1,
        "Kilobyte (KB)": 1024,
        "Megabyte (MB)": 1024**2,
        "Gigabyte (GB)": 1024**3,
        "Terabyte (TB)": 1024**4,
        "Petabyte (PB)": 1024**5,
        "Kibibyte (KiB)": 1024,
        "Mebibyte (MiB)": 1024**2,
        "Gibibyte (GiB)": 1024**3,
        "Tebibyte (TiB)": 1024**4,
        "Pebibyte (PiB)": 1024**5
    }
    
    # Convert to bytes first, then to target unit
    bytes_value = value * to_byte[from_unit]
    result = bytes_value / to_byte[to_unit]
    
    # Create formula text
    formula = f"{value} {from_unit} = {result:.6g} {to_unit}"
    if from_unit != to_unit:
        formula += f" (Conversion: {value} × {to_byte[from_unit]:.6g} ÷ {to_byte[to_unit]:.6g})"
    
    return result, formula

def angle_conversion(value, from_unit, to_unit):
    # Conversion factors to radians
    to_radian = {
        "Radian": 1,
        "Degree": math.pi/180,
        "Gradian": math.pi/200,
        "Minute of Arc": math.pi/(180*60),
        "Second of Arc": math.pi/(180*3600),
        "Turn/Revolution": 2*math.pi
    }
    
    # Convert to radians first, then to target unit
    radians = value * to_radian[from_unit]
    result = radians / to_radian[to_unit]
    
    # Create formula text
    formula = f"{value} {from_unit} = {result:.6g} {to_unit}"
    if from_unit != to_unit:
        formula += f" (Conversion through radians)"
    
    return result, formula

def fuel_economy_conversion(value, from_unit, to_unit):
    # First convert everything to kilometers per liter
    if from_unit == "Miles per Gallon (US)":
        kpl = value * 0.425144
    elif from_unit == "Miles per Gallon (UK)":
        kpl = value * 0.354006
    elif from_unit == "Kilometers per Liter":
        kpl = value
    elif from_unit == "Liters per 100 Kilometers":
        kpl = 100 / value if value != 0 else float('inf')
    
    # Then convert to the target unit
    if to_unit == "Miles per Gallon (US)":
        result = kpl / 0.425144
    elif to_unit == "Miles per Gallon (UK)":
        result = kpl / 0.354006
    elif to_unit == "Kilometers per Liter":
        result = kpl
    elif to_unit == "Liters per 100 Kilometers":
        result = 100 / kpl if kpl != 0 else float('inf')
    
    # Create formula text
    formula = f"{value} {from_unit} = {result:.6g} {to_unit}"
    
    return result, formula

def currency_conversion(value, from_unit, to_unit):
    # Exchange rates (as of a recent date)
    # In a real app, you would use an API to get current rates
    exchange_rates = {
        "USD": 1.0,
        "EUR": 0.92,
        "GBP": 0.79,
        "JPY": 149.5,
        "CAD": 1.35,
        "AUD": 1.52,
        "INR": 83.1,
        "CNY": 7.2,
        "PKR": 278.5,  # Pakistani Rupee
        "SAR": 3.75,    # Saudi Riyal
        "AED": 3.67     # UAE Dirham
    }
    
    # Convert to USD first, then to target currency
    usd_amount = value / exchange_rates[from_unit]
    result = usd_amount * exchange_rates[to_unit]
    
    # Create formula text
    formula = f"{value} {from_unit} = {result:.6g} {to_unit}"
    if from_unit != to_unit:
        formula += f" (Via USD: {value}/{exchange_rates[from_unit]} × {exchange_rates[to_unit]})"
    
    return result, formula

# Define conversion categories and their units
categories = {
    "Length": {
        "units": ["Meter", "Kilometer", "Centimeter", "Millimeter", "Mile", "Yard", "Foot", "Inch", "Nautical Mile"],
        "conversion_function": length_conversion,
        "icon": "📏"
    },
    "Weight/Mass": {
        "units": ["Kilogram", "Gram", "Milligram", "Pound", "Ounce", "Ton (Metric)", "Ton (US)", "Stone"],
        "conversion_function": weight_conversion,
        "icon": "⚖️"
    },
    "Temperature": {
        "units": ["Celsius", "Fahrenheit", "Kelvin"],
        "conversion_function": temperature_conversion,
        "icon": "🌡️"
    },
    "Area": {
        "units": ["Square Meter", "Square Kilometer", "Square Mile", "Hectare", "Acre", "Square Foot", "Square Inch", "Square Yard"],
        "conversion_function": area_conversion,
        "icon": "📐"
    },
    "Volume": {
        "units": ["Cubic Meter", "Liter", "Milliliter", "Gallon (US)", "Gallon (UK)", "Quart (US)", "Pint (US)", 
                 "Cup", "Fluid Ounce (US)", "Tablespoon", "Teaspoon", "Cubic Inch", "Cubic Foot"],
        "conversion_function": volume_conversion,
        "icon": "🧪"
    },
    "Time": {
        "units": ["Second", "Minute", "Hour", "Day", "Week", "Month (30 days)", "Year (365 days)", 
                 "Millisecond", "Microsecond", "Nanosecond"],
        "conversion_function": time_conversion,
        "icon": "⏱️"
    },
    "Speed": {
        "units": ["Meter/Second", "Kilometer/Hour", "Mile/Hour", "Foot/Second", "Knot", "Mach (at sea level)"],
        "conversion_function": speed_conversion,
        "icon": "🚀"
    },
    "Pressure": {
        "units": ["Pascal", "Kilopascal", "Bar", "PSI", "Atmosphere", "Torr", "Millimeter of Mercury"],
        "conversion_function": pressure_conversion,
        "icon": "🔄"
    },
    "Energy": {
        "units": ["Joule", "Kilojoule", "Calorie", "Kilocalorie", "Watt-hour", "Kilowatt-hour", 
                 "Electronvolt", "British Thermal Unit", "Foot-pound"],
        "conversion_function": energy_conversion,
        "icon": "⚡"
    },
    "Power": {
        "units": ["Watt", "Kilowatt", "Megawatt", "Horsepower", "Foot-pound/minute", "BTU/hour"],
        "conversion_function": power_conversion,
        "icon": "💪"
    },
    "Data": {
        "units": ["Bit", "Byte", "Kilobyte (KB)", "Megabyte (MB)", "Gigabyte (GB)", "Terabyte (TB)", "Petabyte (PB)",
                 "Kibibyte (KiB)", "Mebibyte (MiB)", "Gibibyte (GiB)", "Tebibyte (TiB)", "Pebibyte (PiB)"],
        "conversion_function": data_conversion,
        "icon": "💾"
    },
    "Angle": {
        "units": ["Degree", "Radian", "Gradian", "Minute of Arc", "Second of Arc", "Turn/Revolution"],
        "conversion_function": angle_conversion,
        "icon": "📐"
    },
    "Fuel Economy": {
        "units": ["Miles per Gallon (US)", "Miles per Gallon (UK)", "Kilometers per Liter", "Liters per 100 Kilometers"],
        "conversion_function": fuel_economy_conversion,
        "icon": "⛽"
    },
    "Currency": {
        "units": ["USD", "EUR", "GBP", "JPY", "CAD", "AUD", "INR", "CNY", "PKR", "SAR", "AED"],
        "conversion_function": currency_conversion,
        "icon": "💰"
    }
}

# Initialize session state for swap functionality
if 'from_unit' not in st.session_state:
    st.session_state['from_unit'] = {}
if 'to_unit' not in st.session_state:
    st.session_state['to_unit'] = {}

# Main app
def main():
    # Header
    st.markdown('## <p class="main-title">Professional Unit Converter</p>', unsafe_allow_html=True)
    st.markdown("Convert between different units of measurement with ease and precision.")
    
    # Category selection
    category_icons = {cat: data["icon"] for cat, data in categories.items()}
    category_options = [f"{category_icons[cat]} {cat}" for cat in categories.keys()]
    
    selected_category_with_icon = st.selectbox("Select Category", category_options)
    selected_category = selected_category_with_icon.split(" ", 1)[1]  # Remove the icon
    
    # Get the selected category data
    category_data = categories[selected_category]
    
    # Display category title
    st.markdown(f'<p class="category-title">{category_data["icon"]} {selected_category} Conversion</p>', unsafe_allow_html=True)
    
    # Create two columns for input and output
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("From")
        from_value = st.number_input(
            "Enter value",
            value=1.0,
            format="%.6g",
            key=f"from_value_{selected_category}"
        )
        
        # Initialize default from_unit if not set for this category
        if selected_category not in st.session_state['from_unit']:
            st.session_state['from_unit'][selected_category] = category_data["units"][0]
        
        from_unit = st.selectbox(
            "From unit",
            options=category_data["units"],
            index=category_data["units"].index(st.session_state['from_unit'][selected_category]),
            key=f"from_unit_select_{selected_category}"
        )
        # Update session state
        st.session_state['from_unit'][selected_category] = from_unit
    
    with col2:
        st.subheader("To")
        
        # Initialize default to_unit if not set for this category
        if selected_category not in st.session_state['to_unit']:
            to_unit_index = 1 if len(category_data["units"]) > 1 else 0
            st.session_state['to_unit'][selected_category] = category_data["units"][to_unit_index]
        
        to_unit = st.selectbox(
            "To unit",
            options=category_data["units"],
            index=category_data["units"].index(st.session_state['to_unit'][selected_category]),
            key=f"to_unit_select_{selected_category}"
        )
        # Update session state
        st.session_state['to_unit'][selected_category] = to_unit
        
        # Calculate conversion
        try:
            result, formula = category_data["conversion_function"](from_value, from_unit, to_unit)
            
            # Display result
            st.markdown('<div class="result-box">' + 
                       f'<span class="result-value">{result:.6g}</span>' +
                       '</div>', 
                       unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Error in conversion: {str(e)}")
            result, formula = 0, "Error in conversion"
    
    # Swap button
    if st.button("↔️ Swap Units", key=f"swap_{selected_category}"):
        # Swap the units in session state
        temp_from = st.session_state['from_unit'][selected_category]
        temp_to = st.session_state['to_unit'][selected_category]
        
        st.session_state['from_unit'][selected_category] = temp_to
        st.session_state['to_unit'][selected_category] = temp_from
        
        # Use st.rerun() instead of experimental_rerun
        st.rerun()
    
    # Display formula
    st.markdown('<div class="formula-box">' + 
               f"<b>Formula:</b> {formula}" + 
               '</div>', 
               unsafe_allow_html=True)
    
    # Add information about the category
    st.subheader("About this conversion")
    if selected_category == "Length":
        st.write("Length is a measure of distance. In this converter, all length units are converted through meters as the base unit.")
    elif selected_category == "Weight/Mass":
        st.write("Weight (or mass) is a measure of how heavy an object is. All weight units are converted through grams as the base unit.")
    elif selected_category == "Temperature":
        st.write("Temperature is a measure of how hot or cold something is. Temperature conversions use specific formulas rather than simple multiplication.")
    elif selected_category == "Area":
        st.write("Area is a measure of the size of a surface. All area units are converted through square meters as the base unit.")
    elif selected_category == "Volume":
        st.write("Volume is a measure of the three-dimensional space occupied by a substance. All volume units are converted through milliliters as the base unit.")
    elif selected_category == "Time":
        st.write("Time is a measure of duration. All time units are converted through seconds as the base unit.")
    elif selected_category == "Speed":
        st.write("Speed is a measure of how quickly something moves. All speed units are converted through meters per second as the base unit.")
    elif selected_category == "Pressure":
        st.write("Pressure is force per unit area. All pressure units are converted through pascals as the base unit.")
    elif selected_category == "Energy":
        st.write("Energy is the capacity to do work. All energy units are converted through joules as the base unit.")
    elif selected_category == "Power":
        st.write("Power is the rate at which energy is transferred. All power units are converted through watts as the base unit.")
    elif selected_category == "Data":
        st.write("Data storage units measure digital information. All data units are converted through bytes as the base unit.")
    elif selected_category == "Angle":
        st.write("Angle measures rotation or orientation. All angle units are converted through radians as the base unit.")
    elif selected_category == "Fuel Economy":
        st.write("Fuel economy measures the efficiency of fuel consumption. Units are converted through kilometers per liter as an intermediate step.")
    elif selected_category == "Currency":
        st.write("Currency conversion is based on exchange rates. Note: These rates are approximations and may not reflect current market values.")

    # Footer
    st.markdown("---")
    st.markdown("### How to use this converter")
    st.write("1. Select a category from the dropdown menu")
    st.write("2. Enter a value in the 'From' section")
    st.write("3. Select the units you want to convert from and to")
    st.write("4. The result will be displayed automatically")
    st.write("5. Use the 'Swap Units' button to quickly reverse the conversion")

# Run the app
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        st.error(f"An unexpected error occurred: {str(e)}")
        st.info("Please report this error to the developer.")
