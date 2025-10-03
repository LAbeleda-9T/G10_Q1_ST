from pyscript import when, document, display

# for the prices of the items
prices = {
    "Matcha Latte": 119.99,
    "Glazed Donut": 39.00,
    "Spanish Latte": 149.00,
    "Iced Tea": 79.00,
    "Sparkling Water": 60.00
}

@when("click", "#submit-btn")
def show_message(event):
    name = document.querySelector("#name").value
    address = document.querySelector("#address").value
    contact = document.querySelector("#contact").value

    # te record selected items
    checked_elements = document.querySelectorAll(".item:checked")
    selected_items = [item.value for item in checked_elements]

    # calculate total
    total = sum(prices[item] for item in selected_items)
    
    # Clear the output div first
    document.querySelector("#output").innerText = ""

    # Order summary
    message = f""" 🧾 Order Summary

👤 Customer Info:
Name: {name}
Address: {address}
Contact: {contact}

🍽️ Ordered Items:
{chr(10).join(f"- {item} (₱{prices[item]:.2f})"
 for item in selected_items)}

💰 Total: ₱{total:.2f}
"""

# Display in output
    display(message, target="output")
