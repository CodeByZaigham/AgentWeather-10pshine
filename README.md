# AgentWeather-10pshine

## Development Milestones

| # | Phase | Focus | Status |
|---|-------|-------|--------|
| 1 | **Phase 0: Project foundation** | Environment, architecture, GitHub repository, configuration | 🟢 Start here |
| 2 | **Phase 1: Data ingestion** | OpenWeather, AQICN, API integration and raw observations | ⬜ Planned |
| 3 | **Phase 2: Data engineering and feature pipeline** | Cleaning, alignment, imputation, feature engineering and backfill | ⬜ Planned |
| 4 | **Phase 3: Hopsworks Feature Store** | Feature groups, feature views and historical training datasets | ⬜ Planned |
| 5 | **Phase 4: EDA and statistical forecasting** | Exploratory analysis, time-series analysis and naive baseline | ⬜ Planned |
| 6 | **Phase 5: Model training** | SARIMAX, Ridge/Random Forest, LSTM, evaluation and registry | ⬜ Planned |
| 7 | **Phase 6: Forecast and Alert agents** | LangGraph, forecasting, rule-based alerts and Groq reports | ⬜ Planned |
| 8 | **Phase 7: Drift detection and monitoring** | Data drift, model drift, logs and automated retraining triggers | ⬜ Planned |
| 9 | **Phase 8: CI/CD and automation** | GitHub Actions, scheduled pipelines and deployment automation | ⬜ Planned |
| 10 | **Phase 9: Dashboard and final deployment** | Streamlit, SHAP, reports, monitoring and final documentation | ⬜ Planned |

---

## AgentWeather Architecture

```mermaid
flowchart TD
    A["<b>External data sources</b><br/>OpenWeather API · AQICN API<br/>Weather, pollutants and historical observations"]
    B["<b>Data ingestion and feature engineering</b><br/>Python · Requests · Pandas · NumPy<br/>Cleaning · Alignment · Imputation · Feature generation"]
    C["<b>Hopsworks Feature Store</b><br/>Raw observations · Engineered features · Training data"]

    subgraph D["ML training and model selection"]
        direction TB
        D1["<b>SARIMAX</b><br/>Statistical"]
        D2["<b>Random Forest</b><br/>Classical ML"]
        D3["<b>LSTM</b><br/>Deep learning"]
        D4["Validation · Naive baseline · RMSE · MAE · R²"]
        D1 ~~~ D4
        D2 ~~~ D4
        D3 ~~~ D4
    end

    E["<b>Hopsworks Model Registry</b><br/>Store models, versions and validation performance"]

    subgraph F["LangGraph agentic layer"]
        direction TB
        F1["<b>Forecast Agent</b><br/>Generates forecasts"]
        F2["<b>Alert Agent</b><br/>Hazard detection"]
        F3["<b>Weather Report Agent</b><br/>News-style reports"]
        F4["<b>Drift Agent</b><br/>Data and model monitoring"]
        F1 ~~~ F2
        F3 ~~~ F4
    end

    G["<b>Forecast Ledger and monitoring</b><br/>Forecasts · Agent decisions · LLM calls · Drift events · Failures"]
    H["<b>Streamlit dashboard</b><br/>Forecasts · Reports · Alerts · EDA · SHAP · Drift · Agent activity"]
    I["<b>Automated with GitHub Actions</b><br/>Hourly ingestion · Hourly forecasting · Daily training · Drift-triggered retraining"]

    A --> B --> C --> D --> E --> F --> G --> H
    H -.-> I
```