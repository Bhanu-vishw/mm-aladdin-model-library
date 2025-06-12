# Contributing

Thanks for helping build the MM Aladdin Model Library! To add a new model:

1. Copy `model_template.py` and create a new script, e.g., `03_my_model.py`.
2. Add a clear docstring at the top describing:
   - Model name
   - Required columns
   - Input/output format
   - Short description
3. Update `models.json` with your model’s metadata.
4. Submit a pull request!

**All scripts must:**
- Take input CSV path as the first argument, output file path as the second argument.
- Print or save results as instructed.
- Not use unsafe or unapproved libraries.
