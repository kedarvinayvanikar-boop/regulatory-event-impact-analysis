# Regulatory Event Study & Market Reaction Analysis
Apple Inc. — U.S. Department of Justice Antitrust Monopolization Lawsuit

Overview

This project analyzes how the U.S. Department of Justice’s antitrust monopolization lawsuit against Apple Inc. affected Apple’s stock price using a financial event study framework. The purpose of the analysis is to isolate the market’s reaction to the regulatory announcement and determine whether the effect on Apple’s stock was firm-specific rather than driven by broader market movements.

The project combines Python-based data collection with Excel-based financial modeling to mirror how analysts approach regulatory and event-driven questions in investment banking, equity research, and risk analysis. All results are presented in a structured dashboard that summarizes both quantitative outcomes and qualitative interpretation.

Background and Event Description

In March 2024, the U.S. Department of Justice filed a major antitrust lawsuit alleging that Apple unlawfully maintained monopoly power within the smartphone ecosystem. The lawsuit focused on Apple’s platform practices and raised concerns about long-term competitive restrictions, potential regulatory remedies, and increased legal risk.

Although regulatory actions do not always produce immediate financial penalties, they can significantly alter investor expectations regarding future cash flows, strategic flexibility, and risk exposure. This lawsuit therefore provides a clear real-world example for examining how equity markets incorporate regulatory and legal risk into asset prices.

Research Objective

The primary objective of this project is to evaluate how Apple’s stock performed following the announcement of the DOJ lawsuit after controlling for overall market movements. Specifically, the analysis seeks to determine whether Apple experienced a significant reaction on the event day and whether any resulting underperformance persisted in the days following the announcement.

Methodology

The analysis applies a standard financial event study framework. The event day is defined as the first trading day on which the market could react to the DOJ lawsuit announcement. When announcements occur outside market hours, the next available trading day is used, consistent with accepted finance practice.

An event window surrounding the announcement is constructed to examine stock behavior before and after the event. Apple’s performance is compared to the S&P 500, represented by the SPY exchange-traded fund, which serves as a proxy for overall market movement. This comparison allows the analysis to separate firm-specific effects from market-wide trends.

Historical price data for Apple and SPY is collected using Python. The yfinance library is used to retrieve market data, and the pandas library is used to clean, organize, and export the data. Python is intentionally limited to data collection and preparation in order to ensure reproducibility and efficiency.

All financial calculations are performed in Excel to maintain transparency and auditability. Daily returns are calculated from price data, cumulative returns are compounded over the event window, and abnormal returns are computed by subtracting market returns from Apple’s returns. This approach ensures that the analysis isolates the effect of the regulatory announcement rather than general market fluctuations.

Visualization and Dashboard Design

Results are summarized in a dashboard designed to present findings clearly and concisely. The dashboard includes headline performance metrics, written interpretation, and a cumulative return chart indexed to a base value of 100 on the event day. Indexing both Apple and the market benchmark to the same starting point allows for direct visual comparison of relative performance before and after the event.

The visualization focuses on clarity rather than complexity. It is intended to communicate the economic significance of the regulatory event in a way that is accessible to finance professionals without obscuring results behind unnecessary technical detail.

Findings and Interpretation

The analysis shows that Apple experienced a significant negative stock return on the event day, indicating that the DOJ lawsuit introduced new information that was not fully priced in by the market. Over the event window, Apple underperformed the S&P 500, resulting in a negative abnormal cumulative return. This pattern suggests that the market reaction was firm-specific and not driven by broader market conditions.

The persistence of underperformance following the announcement indicates that investors reassessed Apple’s long-term risk profile rather than treating the lawsuit as a temporary shock. The results are consistent with financial theory, which predicts that regulatory actions can materially affect valuation by altering expectations regarding future cash flows, compliance costs, and strategic constraints.

Tools and Technologies

This project uses Python for automated data collection and Excel for financial modeling and analysis. Python libraries include pandas and yfinance. Excel is used for return calculations, event-window alignment, abnormal return analysis, and dashboard creation.

Project Scope and Limitations

This project focuses specifically on market reaction rather than full valuation modeling. It does not attempt to forecast future stock prices or estimate long-term fundamental value. Potential extensions could include volatility analysis, examination of multiple regulatory events, or incorporation of valuation multiples. These extensions were intentionally excluded to keep the analysis focused, defensible, and free from unnecessary assumptions.

Conclusion

This project demonstrates how regulatory and legal developments can be translated into measurable financial outcomes using an event study framework. By combining Python-based data collection with Excel-based financial analysis, the project highlights both technical execution and financial reasoning while maintaining transparency and realism. The analysis illustrates how markets incorporate regulatory risk into asset prices and provides a practical example of event-driven analysis used in finance and investment banking contexts.
