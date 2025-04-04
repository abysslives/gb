equation used to find the generational bottom
////////////                            //////////////
GB = argmin_t [ P_t - μ_P - α₁·S_t - α₂·V_t + α₃·M_t ]
////////////                            //////////////
Imputs for program:

Replace the dummy price, sentiment, valuation, and macro arrays with real historical data.

Sentiment could come from the Fear & Greed Index or Twitter sentiment analysis.

Valuation could use on-chain metrics like MVRV or NVT for crypto.

Macro can be binary flags for events like Fed pivot, inflation peak, etc.

Where:

P_t = price at time t

mu_P = long-term average price (e.g., 200-week MA)

S_t = sentiment index

V_t = valuation metric

M_t = macro signal

a1, a2, a3 = weighting factors
