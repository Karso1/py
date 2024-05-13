import ccxt.pro


async def main()
    exchange = ccxtpro.binance(
        {
            #
        }
    )

    symbol = 'BTC/USDT'
    side = 'buy'
    amount = 1

    orde = await exchange.creat_order(symbol,'market',side,amount)

    await exchange.close()

    return order

order_result = asyncio.get_event_loop().run_until_complete(main())
print(order_result)
