import re
import pandas as pd
import glob
import os
import argparse

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(
        description="Merge Hospital Provider Cost Report CSV files into one file."
    )
    parser.add_argument(
        "--input_folder",
        required=True,
        help="Path to folder with raw CSV files (e.g. Data/raw)"
    )
    parser.add_argument(
        "--output_file",
        default="hospital_provider_cost_output.csv",
        help="Output CSV filename (default: hospital_provider_cost_output.csv)"
    )

    args = parser.parse_args()

    # Pattern to match files like CostReport_2011_Final.csv to CostReport_2022_Final.csv
    file_pattern = os.path.join(args.input_folder, "CostReport_*_Final.csv")
    csv_files = sorted(glob.glob(file_pattern))

    print(f"Found {len(csv_files)} files:")
    for f in csv_files:
        print(os.path.basename(f))

    df_list = []
    for file in csv_files:
        # Extract year from file name using regex
        match = re.search(r"CostReport_(\d{4})_Final\.csv", os.path.basename(file), re.IGNORECASE)
        if match:
            year = int(match.group(1))
        else:
            raise ValueError(f"Could not extract year from file name: {file}")

        # Read file
        df = pd.read_csv(file)

        # Add new column for the year
        df["Cost Report Year"] = year

        df_list.append(df)

    # Merge all into one DataFrame
    merged_df = pd.concat(df_list, ignore_index=True)

    # Save merged file
    merged_df.to_csv(args.output_file, index=False)

    print(f"Merged file saved as: {args.output_file}")

if __name__ == "__main__":
    main()
