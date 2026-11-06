import os
import json
from pydantic import BaseModel, ValidationError
from .models import OutputResult


def load_json_array(filepath: str,
                    model: type[BaseModel]) -> list[BaseModel]:
    """Read a JSON array from the file given and validate each element
    as the model type given.

    Raises:
        ValueError: if the file cannot be read, the JSON cannot be
        decoded, or if the validation fails.
    """
    print(f"Reading from {filepath}...")
    try:
        with open(filepath, encoding="utf-8") as file:
            data = json.load(file)
            if not isinstance(data, list) or not data:
                raise ValueError(f"{filepath} contains an empty JSON array")
            result = [model.model_validate(entry) for entry in data]
    except OSError as e:
        raise ValueError(f"could not read {filepath}: {e}")
    except json.JSONDecodeError as e:
        raise ValueError(f"invalid JSON in {filepath}: {e}")
    except ValidationError as exc:
        raise ValueError(f"invalid entry in {filepath}: {exc}")
    print(f"Loaded {len(result)} functions.")
    return result


def write_results(filepath: str, results: list[OutputResult]) -> None:
    """Write the results as one JSON array to output."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    payload = [result.model_dump() for result in results]
    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(payload, file, indent=2, ensure_ascii=False)
