def apply_discount(price, discount):
    if not ininstance(price(int, float)):
        return "The price should be a number"
    if not ininstance(discount(int, float)):
        return "The discount should be a number"
    if price < 0:
        return "The price should be greater than 0"
    if discount < 0 or discount > 100:   
        return "The discount should be between 0 and 100"
    discount_price = price * (discount / 100)
    final_price = price - discount_price
    return final_price