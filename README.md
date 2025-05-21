# mtcars Flask API

This is a simple Flask-based API that serves a linear regression model trained on the `mtcars` dataset. The model predicts a car's miles per gallon using six features:`cyl`, `disp`, `hp`, `drat`, `wt`, and `qsec`.

The API is containerized with Docker and deployed on Google Cloud Run.

---
## How to use

Example `curl` command:

```bash
curl -X POST https://mtcars-api-691844217421.us-west2.run.app/model \
     -H "Content-Type: application/json" \
     -d '{"cyl": 6, "disp": 160, "hp": 110, "drat": 3.9, "wt": 2.62, "qsec": 16.46}'
```

Expected response:
```bash
{"predicted mpg": 22.314140557947972}
```
