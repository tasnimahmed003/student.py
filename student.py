import streamlit as st

# Login তথ্য
correct_username = "kawsar"
correct_password = "1234"

# Session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Login System
if not st.session_state.logged_in:
    st.title("Login System")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == correct_username and password == correct_password:
            st.success("Login Successful")
            st.session_state.logged_in = True
        else:
            st.error("Wrong Username or Password")

# Main Menu
if st.session_state.logged_in:
    st.title("Smart Student Utility System")

    menu = st.sidebar.selectbox("Choose Option", [
        "Student Info",
        "Email Parser",
        "Salary System",
        "ATM",
        "Fruits List",
        "Discount",
        "Calculator",
        "Day Finder"
    ])

    if menu == "Student Info":
        name = st.text_input("Name")
        age = st.text_input("Age")
        sid = st.text_input("ID")
        dept = st.text_input("Department")
        city = st.text_input("City")

        if st.button("Show Info"):
            st.write(name, age, sid, dept, city)

    elif menu == "Email Parser":
        email = st.text_input("Enter Email")
        if st.button("Parse"):
            if "@" in email:
                parts = email.split("@")
                st.write("Username:", parts[0])
                st.write("Domain:", parts[1])
            else:
                st.error("Invalid Email")

    elif menu == "Salary System":
        salary = st.number_input("Enter Salary", step=1000)
        if st.button("Calculate"):
            if salary > 50000:
                bonus = salary * 0.2
            else:
                bonus = salary * 0.1
            st.write("Total Salary:", salary + bonus)

    elif menu == "ATM":
        balance = 10000
        amount = st.number_input("Withdraw Amount", step=500)
        if st.button("Withdraw"):
            if amount <= balance:
                st.write("Remaining Balance:", balance - amount)
            else:
                st.error("Not enough balance")

    elif menu == "Fruits List":
        fruits = ["apple", "banana", "mango"]
        st.write(fruits)

    elif menu == "Discount":
        price = st.number_input("Enter Price", step=10)
        if st.button("Apply Discount"):
            if price > 100:
                price *= 0.9
            st.write("Final Price:", price)

    elif menu == "Calculator":
        a = st.number_input("A", step=1)
        b = st.number_input("B", step=1)
        if st.button("Add"):
            st.write("Sum:", a + b)

    elif menu == "Day Finder":
        day = st.number_input("Enter number (1-7)", min_value=1, max_value=7)
        days = ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]
        if st.button("Find Day"):
            st.write(days[day-1])
