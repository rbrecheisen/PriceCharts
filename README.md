# PriceCharts
Web application that calculates and tracks price chart indicators with notifications about interesting combinations.

Idea is to make an HTML page where you can retrieve candle stick information and provide parameters like:
- CandleStickGranularity: e.g., S15, M15, H1, D, W, M
- PricingComponent: e.g., M (midpoint), B (bid) and A (ask) or a combination of these (e.g., BM)
- InstrumentName: EUR_USD

When the candle stick information has been retrieved, the price chart is displayed.