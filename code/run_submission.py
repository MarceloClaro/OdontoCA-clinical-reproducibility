import json
from pathlib import Path
namespace = {"__name__":"__main__"}
notebook = Path(__file__).resolve().parents[1] / "notebooks" / "OdontoCA_SUBMISSION.ipynb"
for index, cell in enumerate(json.loads(notebook.read_text())["cells"]):
    if cell["cell_type"] == "code":
        print(f"Executing cell {index}", flush=True)
        exec(compile("".join(cell["source"]), f"cell_{index}", "exec"), namespace)
