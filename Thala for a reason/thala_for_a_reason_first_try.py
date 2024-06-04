import streamlit as st
import itertools
from PIL import Image

def calculate_to_seven(numbers):
    for ops in itertools.product('+-*/', repeat=len(numbers) - 1):
        expression = ''.join(str(n) + op for n, op in zip(numbers, ops)) + str(numbers[-1])
        try:
            result = eval(expression)
            if result == 7 and result % 1 == 0:
                return expression
        except (ZeroDivisionError, OverflowError, ValueError):
            pass

    return "Thala ko pasand nahi aya"

def main():
    st.title("Calculate to Seven")

    # Load MS Dhoni image
    ms_dhoni_image = Image.open("ms_dhoni.jpg")
    st.image(ms_dhoni_image, caption="MS Dhoni", use_column_width=True)

    num_count = st.number_input("Enter the number of values:", min_value=1, value=1, step=1)

    user_numbers = []
    for i in range(1, num_count + 1):
        user_numbers.append(st.number_input(f"Enter number {i}:", step=1))

    if st.button("Calculate"):
        result_expression = calculate_to_seven(user_numbers)
        st.write(f"Result: {result_expression}")

if __name__ == '__main__':
    main()
