def get_current_price_as_KRW(coin_list):

    # get current price as KRW by coin-type

    import pyupbit as pb
    results = {}
    for coin in coin_list:
        price = pb.get_current_price(f"KRW-{coin}")
        results[f"KRW-{coin}"] = format(price, ",")

    return results
