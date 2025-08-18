import re
import pandas as pd
import glob
import os

# Folder where your CSV files are stored
input_folder = "C:/Users/caoj/Downloads/Project"
output_file = "hospital_provider_cost_output.csv"

# Pattern to match files like CostReport_2011_Final.csv to CostReport_2022_Final.csv
file_pattern = os.path.join(input_folder, "CostReport_*_Final.csv")

# Get a list of all matching CSV files
csv_files = sorted(glob.glob(file_pattern))

# Check found files
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
merged_df.to_csv(output_file, index=False)

print(f"Merged file saved as: {output_file}")