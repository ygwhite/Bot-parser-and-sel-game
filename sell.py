from convert import currency_exchange

def selling(game_sell):
    print(game_sell)
    curren = currency_exchange()
    sel = game_sell.replace('2.', '2')
    sell = sel.replace('1.', '1')
    sell1 = sell.replace(',', '.')
    print(sell1)
    sell_clear = sell1.replace('TL', '')
    print(sell_clear)
    procent = round(float(sell_clear) * curren / 2)
    finish_sell_ps5 = round(float(sell_clear) * curren + procent)
    print(finish_sell_ps5)
    return finish_sell_ps5