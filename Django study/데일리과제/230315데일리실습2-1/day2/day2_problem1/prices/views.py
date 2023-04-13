from django.shortcuts import render


def price(request, product_name, quantity):
    
    product_prices = {"라면": 980, "홈런볼": 1500, "칙촉": 2300, "식빵": 1800}

    if product_name not in product_prices:
        context = {
            'product_name': product_name,
        }
    else:
        unit_price = product_prices[product_name]
        total_price = unit_price * quantity


        message = f"{product_name} {quantity}개의 가격은 {total_price}원입니다."

        context = {
            'message': message,
        }

    return render(request, 'prices/price.html', context)
