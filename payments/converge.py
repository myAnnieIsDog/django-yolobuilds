import requests


def converge(
        ssl_pin="123",
        ssl_transaction_type="ccsale",
        ssl_amount="0.10", 
        merchant_id="000062",
        merchant_user_id="sdoolittle",
        merchant_pin="tbd",
        demo="", 
        **kwargs
    ):
    params = {
        "ssl_pin": ssl_pin,
        "ssl_transaction_type": ssl_transaction_type,
        "ssl_amount": ssl_amount, 
        "merchant_id": merchant_id,
        "merchant_user_id": merchant_user_id,
        "merchant_pin": merchant_pin,
    }
    demo = "demo." # comment-out for production url's to use the default empty string.
    token_url = (f"https://api.{demo}convergepay.com/hosted-payments/transaction_token")
    response = requests.post(token_url, params)  
    print(response)
    response.raise_for_status()
    if response.status_code == 200:
        header = (f"Location: https://api.{demo}convergepay.com/hosted-payments?ssl_txn_auth_token=$sessiontoken")
        return requests.post(header)
    else:
        return f"HTTP Status: {response.status_code}. {response}"

print(converge(ssl_amount = 0.50))