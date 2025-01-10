# Office window electricity price forecast

Concept: Can I build a simple model, to give me a decent forecast of the spot electricity prices, just using the weather. 

Background: staring out the office window in Aarhus often, and noticing the wind speed and cloud cover, can I use these two simple factors to get a non crappy prediction of the spot price for the West Denmark zone?

Methodology:
- load Aarhus hourly weather data from OpenMeteo for 2024
- load Elspot Spot Prices for DK1 (hourly) for 2024
- Feature engineering:
    - Pearson's correlation
    - Spearman's rank
    - Target normality
- Build model
    - Linear regression model
- Finetune/Update/Compare
    - Add consumption power as an input variable
    - Test difference