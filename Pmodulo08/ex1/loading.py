def fetch_matrix_data():
    print("\nAnalyzing Matrix data...")

    # we generate dates simulate with numpy
    data_size = 50
    names = [f"number_{i}" for i in range(data_size)]
    weights = np.random.randint(10, 100, size=data_size)

    df = pd.DataFrame({
        "name": names,
        "weight": weights
    })

    print(f"Processing {data_size} data points...")
    return df


def generate_visualization(df):
    print("Generating visualization...")
    pyplot.figure(figsize=(20, 8))

    pyplot.bar(df["name"], df["weight"])
    pyplot.xlabel("Analyzing Matrix data")
    pyplot.ylabel("Weight")
    pyplot.title("randomly generated numbers to generate an analytical graph")

    pyplot.xticks(rotation=60, fontsize=6)
    pyplot.tight_layout()

    output_file = "matrix_analysis.png"
    pyplot.savefig(output_file)
    pyplot.close()

    print("Analysis complete!")
    print(f"Results saved to: {output_file}")


print("\nLOADING STATUS: Loading programs...")
print("\nChecking dependencies:")

if __name__ == '__main__':

    try:
        import pandas as pd
        print(f"[OK] {pd.__name__} ({pd.__version__})"
              " - Data manipulation ready")
    except ModuleNotFoundError as e:
        pd = None
        print("[ERROR]", e)

    try:
        import numpy as np
        print(f"[OK] {np.__name__} ({np.__version__}) "
              "- Numerical computation ready")
    except ModuleNotFoundError as e:
        np = None
        print("[ERROR]", e)

    try:
        import matplotlib
        import matplotlib.pyplot as pyplot
        print(f"[OK] {matplotlib.__name__} ({matplotlib.__version__})"
              " - Visualization ready")
    except ModuleNotFoundError as e:
        pyplot = None
        print("[ERROR]", e)

    if pd and np and pyplot:
        df = fetch_matrix_data()
        generate_visualization(df)
    else:
        print("\nMissing dependencies!")
        print("\n-- With poetry --")
        print("try pip install poetry")
        print("python3 -m poetry install")
        print("python3 -m poetry run python loading.py")
        print("\n-- With pip --")
        print("pip install -r requirements.txt")
        print("python3 loading.py")
