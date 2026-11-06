import argparse
from time import time
from .json_processing import load_json_array
from .models import FunctionDef, Prompt


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--functions_definition",
                        default="data/input/functions_definition.json")
    parser.add_argument("--input",
                        default="data/input/function_calling_tests.json")
    parser.add_argument("--output",
                        default="data/output/function_calling_results.json")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    start_time = time()
    try:
        functions = load_json_array(args.functions_definition, FunctionDef)
        prompts = load_json_array(args.input, Prompt)
    except ValueError as e:
        print(f"An error occured: {e}.\nProgram terminated")
    elapsed = int(time() - start_time)
    minutes, seconds = divmod(elapsed, 60)
    print(f"Total time: {minutes} minutes and {seconds} seconds")


if __name__ == "__main__":
    main()
