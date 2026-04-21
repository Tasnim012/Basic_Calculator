import streamlit as st

st.title("Saimun Calculator", anchor=False)
st.subheader("You can calculate only basic calculation", anchor=False)
st.divider()

with st.sidebar:
    st.text("Controls")
    number1 = st.text_input("Enter first number", placeholder="Enter a number")
    number2 = st.text_input("Enter second number", placeholder="Enter a number")
    
    select = st.selectbox("Choose an action",
                 ("+", "-", "*", "/"), index=None)
    st.write("You selected:", select)
    
    pressed = st.button("Click button", type="primary")
    
if not number1 or not number2:
    st.error("Please enter two number")
    
elif number1 and number2:
    if pressed:
        if select == "+":
            sum = int(number1) + int(number2)
            st.text(f"{number1} + {number2}")
            st.text(f"Addition: {sum}")
        elif select == "-":
            sub = int(number1) - int(number2)
            st.text(f"{number1} - {number2}")
            st.text(f"Subtraction: {sub}")
        elif select == "*":
            mul = int(number1) * int(number2)
            st.text(f"{number1} * {number2}")
            st.text(f"Multiplication: {mul}")
        elif select == "/":
            div = int(number1) / int(number2)
            st.text(f"{number1} / {number2}")
            st.text(f"Division: {div}")
    else:
        st.error("Please select action")
        
        
    
