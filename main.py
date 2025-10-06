from api import alerts
app.include_router(alerts.router, prefix="/alerts", tags=["Alerts"])